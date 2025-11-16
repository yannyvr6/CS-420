from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WebUserViewSet, AddressTypeViewSet, AddressViewSet, PhoneTypeViewSet, PhoneViewSet, UserInfoViewSet, PageViewSet

router = DefaultRouter()
router.register(r'users', WebUserViewSet)
router.register(r'address-types', AddressTypeViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'phone-types', PhoneTypeViewSet)
router.register(r'phones', PhoneViewSet)
router.register(r'user-infos', UserInfoViewSet)
router.register(r'pages', PageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]