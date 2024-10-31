from django.urls import path
from .views import  ProductMixinsViews
#DetailProductView, CreateProductView, UpdateProductView, DeleteProductView, ListProductView

urlpatterns = [
# # path('', api_view, name='api_view'),
#     path('detail-product/<int:pk>/', DetailProductView.as_view(), name='detail'),
#     path('create-product/', CreateProductView.as_view(), name='Create'),
#     path('list-product/', ListProductView.as_view(), name='list'),
#     path('update-product/<int:pk>/', UpdateProductView.as_view(), name='update'),
#     path('delete-product/<int:pk>/', DeleteProductView.as_view(), name='delete'),

    path('detail-product/<int:pk>/', ProductMixinsViews.as_view(), name='detail'),
    path('create-product/', ProductMixinsViews.as_view(), name='Create'),
    path('list-product/', ProductMixinsViews.as_view(), name='list'),
    path('update-product/<int:pk>/', ProductMixinsViews.as_view(), name='update'),
    path('delete-product/<int:pk>/', ProductMixinsViews.as_view(), name='delete'),
]
