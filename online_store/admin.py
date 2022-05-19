from django.contrib import admin
from .models import Brand, Category, Product, ProductCategory, ProductReview, Customer, CustomersAddress, Order


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    list_display = [
        "title"
    ]


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = [
        "title",
        "price",
        "old_price",
        "description",
        "quantity",
        "photo",
        "brand"
    ]


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = [
        "title",
        "is_active"
    ]


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    list_display = [
        "product",
        "category"
    ]


@admin.register(ProductReview)
class AdminProductReview(admin.ModelAdmin):
    list_display = [
        "review",
        "fullname",
        "product"
    ]


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "phone",
        "email",
        "time_created"
    ]


@admin.register(CustomersAddress)
class AdminCustomerAddress(admin.ModelAdmin):
    list_display = [
        "customer",
        "country",
        "city",
        "post_code",
        "address"
    ]


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = [
        "customer",
        "customer_shipping_address",
        "time_created",
        "time_checkout",
        "time_delivery",
        "is_ordered"
    ]