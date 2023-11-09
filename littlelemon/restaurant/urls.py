from .views import *
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
	path('menu/', MenuItemsView.as_view()),
	path('menu/<int:pk>', SingleMenuItemView.as_view()),
	path('api-token-auth/', obtain_auth_token),
	path('users/', UserList.as_view())
]


