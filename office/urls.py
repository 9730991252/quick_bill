from django.urls import path
from . import views
urlpatterns = [
    path('office_home/', views.office_home , name='office_home'),
    path('item/', views.item, name='item'),
    path('completed_bill/', views.completed_bill, name='completed_bill'),
    path('completed_view_bill/<int:order_filter>', views.completed_view_bill, name='completed_view_bill'),
    path('profile/', views.profile, name='profile'),
    path('report/', views.report, name='report'),
    path('category/', views.category, name='category'),
    path('select_category_items/<int:category_id>', views.select_category_items, name='select_category_items'),
    path('edit_bill/<int:id>', views.edit_bill, name='edit_bill'),
]