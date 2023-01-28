from django.urls import path

from image_parroter.thumbnailer.views import HomeView, TaskView

urlpatterns = (
    path('', HomeView.as_view(), name='home view'),
    path('task/<str:task_id>/', TaskView.as_view(), name='task view'),
)
