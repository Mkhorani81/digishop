from rest_framework.routers import SimpleRouter

from digishop.apps.catalog.views.front import CategoryViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet)
urlpatterns = [] + router.urls