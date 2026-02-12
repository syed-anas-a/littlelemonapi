from django.urls import path, include
from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #User registration and token generation endpoints 
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),

    # group management
    path('groups/<str:group_name>/users/', views.GroupManagementView.as_view()),
    path('groups/<str:group_name>/users/<int:userId>/', views.GroupManagementView.as_view()),

    #MenuItemview
    path('menu-items/', views.MenuItemListCreate.as_view()),
    path('menu-items/<int:pk>', views.MenuItemRUD.as_view())
]