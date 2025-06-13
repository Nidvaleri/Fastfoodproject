from django.urls import path
from . import views

urlpatterns = [
    path('couriers/', views.courier_list, name='courier-list'),
    path('couriers/<int:pk>/', views.courier_detail, name='courier-detail'),
]


