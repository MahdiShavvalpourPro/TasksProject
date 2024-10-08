from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from task_module import views

router = DefaultRouter()
router_2 = DefaultRouter()
router.register('', views.Test)
router_2.register('', views.TaskViewSetApiView)

urlpatterns = [
    # path('', include(router_2.urls)),
    path('tasks/', include(router.urls)),

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # for authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
