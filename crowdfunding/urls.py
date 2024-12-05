from django.urls import path
from .views import ProjectList, ProjectDetail, DonationList


app_name = 'crowdfunding'

urlpatterns = [
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('donations/', DonationList.as_view(), name='donation-list')
]