from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from login.views import LoginViewset

router = DefaultRouter()
router.register(r'login', LoginViewset)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]
