from django.urls import path, include
from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    #User registration and token generation endpoints 
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),

    #MenuItemview
    path('menu-items/', views.MenuItemListCreate.as_view()),
    path('menu-items/<str:item>', views.MenuItemRUD.as_view())
]