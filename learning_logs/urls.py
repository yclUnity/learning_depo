from django.urls import path
from.import views

app_name='learning_logs'
urlpatterns = [
    #Home Page
    path('',views.index, name='index.html'),
    path('topics/',views.topics,name="topics.html"),
    path('topics/<int:topic_id>/', views.topic,name='topic.html'),
    #path('new_topic/', views.new_topic, name='new_topic')
]
