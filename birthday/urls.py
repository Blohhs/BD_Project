from django.urls import path
from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.birthday, name='create'),
    path('list/', views.birthday_list, name='list'),
    path('<int:pk>/edit/', views.birthday, name='edit'),
    
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),
    
    path('<int:pk>/detail/', views.BirthdayDetailView.as_view(), name='detail'),
]