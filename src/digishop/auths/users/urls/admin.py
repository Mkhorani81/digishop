from django.urls import path
from rest_framework.routers import SimpleRouter

from digishop.auths.users.views.admin import AdminLoginView

router = SimpleRouter()

urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='login')
              ] + router.urls