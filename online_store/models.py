from django.db import models


class Brand(models.Model):
    class Meta:
        db_table = "brands"
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
    title = models.CharField(verbose_name="Title", max_length=200, blank=False, null=False)

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"
    title = models.CharField(verbose_name="Title", max_length=200, blank=False, null=False)
    price = models.DecimalField(verbose_name="Price", blank=False, null=False, default=0, decimal_places=2,
                                max_digits=100000000)
    old_price = models.DecimalField(verbose_name="Old Price", blank=False, null=False, default=0, decimal_places=2,
                                    max_digits=100000000)
    description = models.TextField(verbose_name="Product", max_length=50000, blank=False, null=False)
    quantity = models.IntegerField(verbose_name="Quantity", blank=False, null=False)
    photo = models.ImageField(verbose_name="Image", upload_to="", blank=True, null=True)
    brand = models.ForeignKey(Brand, verbose_name="Brand", on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    title = models.CharField(verbose_name="Title", max_length=200, blank=False, null=False)
    # Как использовать BooleanField()?
    is_active = models.BooleanField(verbose_name="Is Active", blank=False, null=False)

    def __str__(self):
        return f"{self.title}"


class ProductCategory(models.Model):
    class Meta:
        db_table = "product_categories"
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE, blank=False, null=False)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.product} is in {self.category}"


class ProductReview(models.Model):
    class Meta:
        db_table = "product_reviews"
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"
    review = models.TextField(verbose_name="Review", max_length=10000, blank=False, null=False)
    fullname = models.CharField(verbose_name="Full Name", max_length=200, blank=False, null=False)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.fullname}'s review"


class Customer(models.Model):
    class Meta:
        db_table = "customers"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
    first_name = models.CharField(verbose_name="First Name", max_length=200, blank=False, null=False)
    last_name = models.CharField(verbose_name="Last Name", max_length=200, blank=False, null=False)
    phone = models.IntegerField(verbose_name="Is Active", blank=False, null=False)
    email = models.CharField(verbose_name="Email", max_length=100, blank=False, null=False)
    time_created = models.DateTimeField(verbose_name="Created Time", auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CustomersAddress(models.Model):
    class Meta:
        db_table = "customers_address"
        verbose_name = "Customers Address"
        verbose_name_plural = "Customers Addresses"
    customer = models.ForeignKey(Customer, verbose_name="Customer", on_delete=models.CASCADE, blank=False, null=False)
    country = models.CharField(verbose_name="Country", max_length=100, blank=False, null=False)
    city = models.CharField(verbose_name="City", max_length=100, blank=False, null=False)
    post_code = models.IntegerField(verbose_name="Is Active", blank=False, null=False)
    address = models.CharField(verbose_name="Address", max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{self.customer}'s address"


class Order(models.Model):
    class Meta:
        db_table = "orders"
        verbose_name = "Order"
        verbose_name_plural = "Orders"
    customer = models.ForeignKey(Customer, verbose_name="Customer", on_delete=models.CASCADE, blank=False, null=False)
    customer_shipping_address = models.ForeignKey(CustomersAddress, verbose_name="Shipping Address", on_delete=models.CASCADE, blank=False, null=False)
    time_created = models.DateTimeField(verbose_name="Created Time", auto_now_add=True)
    time_checkout = models.DateTimeField(verbose_name="Checkout Time", auto_now_add=True)
    time_delivery = models.DateTimeField(verbose_name="Delivery Time", auto_now_add=True)
    is_ordered = models.BooleanField(verbose_name="Is Ordered", blank=False, null=False)

    def __str__(self):
        return f"{self.customer}'s order"



