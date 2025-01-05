from django.urls import path
from . import views
urlpatterns = [
    path('add_item_to_cart', views.add_item_to_cart, name='add_item_to_cart'),
    path('add_to_edit_cart', views.add_to_edit_cart, name='add_to_edit_cart'),
    path('cut_to_edit_cart', views.cut_to_edit_cart, name='cut_to_edit_cart'),
    path('cut_item_to_cart', views.cut_item_to_cart, name='cut_item_to_cart'),
    path('search_item', views.search_item, name='search_item'),
    path('search_item_by_category', views.search_item_by_category, name='search_item_by_category'),
    path('select_category_item', views.select_category_item, name='select_category_item'),
    path('search_item_by_category_edit', views.search_item_by_category_edit, name='search_item_by_category_edit'),
    path('search_item_edit', views.search_item_edit, name='search_item_edit'),
    ]