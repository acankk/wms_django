from django.urls import path

from .views.product import ProductDetailView, ProductListCreateView

from .views.category import CategoryListCreateView, CategoryDetailView

from .views.supplier import SupplierListCreateView, SupplierDetailView


urlpatterns = [
    # Category
    path(
        "categories/",
        CategoryListCreateView.as_view(),
        name="category-list",
    ),
    path(
        "categories/<int:pk>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),

    # Supplier

    path(
        "suppliers/",
        SupplierListCreateView.as_view(),
        name="supplier-list",
    ),

    path(
        "suppliers/<int:pk>/",
        SupplierDetailView.as_view(),
        name="supplier-detail",
    ),

    # Product

    path(
        "products/",
        ProductListCreateView.as_view(),
        name="product-list",
    ),


    path(
        "products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail",
    ),
]