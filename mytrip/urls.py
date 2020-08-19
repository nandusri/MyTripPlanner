from mytrip import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'cities', views.CityViewSet, basename='cities'),
router.register(r'trips', views.TripViewSet, basename='trips'),
router.register(r'photos', views.PhotoViewSet, basename='photos')

urlpatterns = router.urls