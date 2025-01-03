from django.urls import path
from . import views
urlpatterns = [
    path('owner_home/', views.owner_home, name='owner_home'),
    path('add_employee/', views.add_employee, name='add_employee'),

]