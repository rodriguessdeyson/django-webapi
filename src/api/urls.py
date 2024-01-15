from django.urls import path
from .views.homeView import APIOverview
from .views.manufacturerView import ManufacturerViewList, ManufacturerViewDetail
from .views.componentView import ComponentViewList, ComponentViewDetail
from .views.accountView import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('home', APIOverview),
    path('manufacturers', ManufacturerViewList.as_view()),
    path('manufacturers/<int:id>', ManufacturerViewDetail.as_view()),
    path('components', ComponentViewList.as_view()),
    path('components/<int:id>', ComponentViewDetail.as_view()),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]