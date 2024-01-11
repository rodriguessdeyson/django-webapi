from django.urls import path
from .views.manufacturerView import ManufacturerViewList, ManufacturerViewDetail
from .views.componentView import ComponentViewList, ComponentViewDetail

urlpatterns = [
    path('manufacturers', ManufacturerViewList.as_view()),
    path('manufacturers/<int:id>', ManufacturerViewDetail.as_view()),
    path('components', ComponentViewList.as_view()),
    path('components/<int:id>', ComponentViewDetail.as_view()),
]