from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import ( 
    ProductViewSet, CategoryViewSet,
    InventoryViewSet, OrderViewSet, 
    RegisterView, DeleteAccountView, 
    ProfileView, LogoutView, UserViewSet,
    OrderItemViewSet,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register (r'products', ProductViewSet)
router.register (r'categories', CategoryViewSet)
router.register (r'inventory', InventoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'users', UserViewSet)

orders_router = routers.NestedDefaultRouter(router, r'orders', lookup='order')
orders_router.register(r'items', OrderItemViewSet, basename='order-items')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
    path('auth/delete/', DeleteAccountView.as_view(), name='delete-account'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
urlpatterns = router.urls + orders_router.urls
