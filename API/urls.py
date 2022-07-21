from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    PropertyList,PropertyDetail,AddProperty,LocationList,
    LocationDetail,ImagesList,UploadImageView
)

urlpatterns = [
    
    path('properties/',PropertyList.as_view()),
    path('add_property/',AddProperty.as_view()),
    path('property/<property_id>/',PropertyDetail.as_view()),
    path('locations/',LocationList.as_view()),
    path('location/<int:pk>/',LocationDetail.as_view()),
    path('properties_images/',ImagesList.as_view()),
    path('upload_property_images/',UploadImageView.as_view()),
    path('AuthToken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('AuthToken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
