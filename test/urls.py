from django.urls import path
from test import views


urlpatterns = [
    path('',views.index_view,name="home"),
    path('task',views.Tasklist,name="tasklist"),
    path('taskview/<str:pk>/',views.TaskView,name="taskview"),
    path('taskcreate',views.Taskcreate,name="taskcreate"),
    path('taskupdate/<str:pk>/',views.Taskupdate,name="taskupdate"),
    path('taskdelete/<str:pk>/',views.Taskdelete,name="taskdelete"),



]
