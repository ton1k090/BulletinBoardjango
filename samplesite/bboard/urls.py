from django.contrib import admin
from django.urls import path
from .views import index, by_rubric, BbCreateView, CookingAPI, CookingAPIDetail, CookingCategoryAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('rubric/api/', CookingAPI.as_view(), name='CookingAPI'),
    path('rubric/api/<int:pk>', CookingAPIDetail.as_view(), name='CookingAPIDetail'),
    path('categories/api/', CookingCategoryAPI.as_view(), name='CookingCategoryAPI'),
]