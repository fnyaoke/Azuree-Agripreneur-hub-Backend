from django.urls import path, re_path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()


urlpatterns=[
  path('registeruser/', views.Registration.as_view(), name="registeruser"),
  path('getuser/', views.Registration.as_view(), name="getusers"),
  path('loginuser/', views.LoginUser.as_view(), name="loginuser"),
  path('authlogin/', ObtainAuthToken.as_view(), name="authlogin"),
  path('api/users/',views.UserList.as_view(),name='user'),
  path('api/info/',views.AgriInfo.as_view(),name='info'),
  path('api/update/users/<int:pk>/',views.UserDetails.as_view(),name='update_users'),
  path('api/delete/users/<int:pk>/',views.UserList.as_view(),name='delete_users'),
#   re_path('api/update/business/(?P<pk>[0-9]+)/',views.BusinessList.as_view(),name='update_business'),
#   path('api/delete/business/<int:pk>/',views.BusinessList.as_view(),name='delete_business'),
#   path('api/update/neighbors/<int:pk>/',views.NeighborhoodList.as_view(),name='update_neighbors'),
#   re_path('api/delete/(?P<pk>[0-9]+)/',views.NeighborhoodList.as_view(),name='delete_neighbors')
]