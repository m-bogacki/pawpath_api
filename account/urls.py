from django.urls import path
from .views import UserListView, UserCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
       path('', UserListView.as_view(), name="user_list"),
       path('<id>', UserRetrieveUpdateDestroyView.as_view(), name="user_retrieve_update_delete"),
       path('create/', UserCreateView.as_view(), name="user_create")
]
