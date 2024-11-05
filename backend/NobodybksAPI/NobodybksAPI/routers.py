from rest_framework.routers import DefaultRouter
from product.viewset import ProductViewsets, ProductListRetrieveDestroyViewset

router = DefaultRouter()
router.register('product-a', ProductListRetrieveDestroyViewset, basename='product-b')

urlpatterns = router.urls

print(router.urls)