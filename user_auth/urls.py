from django.urls import path
from .views import *

urlpatterns = [
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout_user', logout_user, name='logout_user'),
]
