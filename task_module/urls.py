from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from task_module import views

# for graphql
from graphene_django.views import GraphQLView
# from django.views.decorators.csrf import csrf_exempt
from task_module.schema import schema

router = DefaultRouter()
router.register(r'', views.TaskViewSetApiView, basename='task_api')
router.register(r'tasks/', views.TasksMixinsFilterApiView, basename='task_filter')

urlpatterns = [
    path('test/', views.get_all_tasks),
    # YOUR PATTERNS
    # UI for Graphql
    path("graphql/", (GraphQLView.as_view(graphiql=True, schema=schema))),

    # UI for Tasks
    path('', include(router.urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # for authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
