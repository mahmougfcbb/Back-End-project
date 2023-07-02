from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant2 import views

router = DefaultRouter()
router.register(r'booking', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant2/', include('restaurant2.urls')),
    path('restaurant2/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('restaurant2/menu/', include('restaurant2.urls')),

]
