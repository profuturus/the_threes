from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def check_topic_owner(request, topic):
    ''' make sure the topic belongs to the current user '''
    if topic.owner != request.user:
        raise Http404

def index(request):
    ''' The Home Page for 'The Threes' app '''

    return render(request, 'the_threes_tracker/index.html')

@login_required
def topics(request):
    ''' show all 'threes' '''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'the_threes_tracker/topics.html', context)

@login_required
def topic(request, topic_id):
    ''' Show a single 'three' and all its entries '''
    topic = get_object_or_404(Topic, id=topic_id)
    # Make sure the topic belongs to the current user
    check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'the_threes_tracker/topic.html', context)

@login_required
def new_topic(request):
    ''' user add new topic '''
    if request.method != 'POST':
        # No data submitted. Create a blank form
        form = TopicForm()
    else:
        #POST data submitted. Process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('the_threes_tracker:topics'))

    context = {'form': form}
    return render(request, 'the_threes_tracker/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    ''' user add new entry for a particular topic '''
    topic = get_object_or_404(Topic, id=topic_id)
    check_topic_owner(request, topic)
    if request.method != 'POST':
        # No data submitted. Create a blank form
        form = EntryForm()
    else:
        #POST data submitted. Process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('the_threes_tracker:topic',
                                                args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'the_threes_tracker/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    ''' Edit an existing entry '''
    entry = get_object_or_404(Entry, id=topic_id)
    topic = entry.topic
    check_topic_owner(request, topic)
    if request.method != 'POST':
        # Initial request. pre-fill form with current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted. Process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('the_threes_tracker:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'the_threes_tracker/edit_entry.html', context)
