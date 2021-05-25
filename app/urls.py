from django.urls import path
from . import views
app_name='api'
urlpatterns=[
    
    path('todolist',views.todo_view,name='todolist'),
    path('task/<str:id>',views.todo_task,name='taskview'),
    path('create',views.taskcreate,name='createtask'),
    path('update/<str:id>',views.update_task,name='updatetask'),
    path('delete/<str:id>',views.delete_task,name="deletetask")
]