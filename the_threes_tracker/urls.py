
''' Defines URL patterns for the_threes_tracker '''

from django.urls import path

from . import views

app_name = 'the_threes_tracker'

urlpatterns = [
    # Home Page
    path('', views.index, name = 'index'),

    # Shows all 'threes'
    path('topics/', views.topics, name='topics'),

    # Detail page for each 'three'
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for a user to add a new 'three'
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for user to add new entries
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing a previous entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
