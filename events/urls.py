from django.urls import path
from . import views
from .views import EventListView

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), name='list'),
    path('<int:pk>/', views.event_detail, name='detail'),
    path('create/', views.event_create, name='create'),
    path('<int:pk>/update/', views.event_update, name='update'),
    path('<int:pk>/delete/', views.event_delete, name='delete'),
    path('<int:pk>/register/', views.event_register, name='register'),
    path('<int:pk>/unregister/', views.event_unregister, name='unregister'),
]