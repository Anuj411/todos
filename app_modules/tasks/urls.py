from django.urls import path
from app_modules.tasks import views

app_name = "tasks"

urlpatterns = [
    path('', views.ListTaskView.as_view(), name="list_task"),
    path('create/', views.CreateTaskView.as_view(), name="create_task"),
    path('update/<int:pk>/', views.UpdateTaskView.as_view(), name="update_task"),
    path('delete/<int:pk>/', views.DeleteTaskView.as_view(), name="delete_task"),
]