from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),       # existing tasks endpoints
    path('api/', include('users.urls')),       # new users endpoints
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
