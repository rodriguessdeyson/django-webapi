from django.urls import path
from .views import manufacturerView, componentView, homeView

urlpatterns = [
    path('home', homeView.APIOverview),
    path('components', componentView.ComponentList.as_view()),
    path('components/<int:pk>', componentView.ComponentDetail.as_view()),
    path('manufacturers', manufacturerView.ManufacturerList.as_view()),
    path('manufacturers/<int:pk>', manufacturerView.ManufacturerDetail.as_view()),
]