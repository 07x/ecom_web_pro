from django.db import models
from userapp.models import CustomUserModel


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# CATEGORY 
class Category(BaseModel):
    name        = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    picture     = models.ImageField(null=True,blank=True)
    def __str__(self):
        return str(self.name) + '|' + str(self.id)

# OFFER
class Offer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    offer_type_choices = (
        ('percentage', 'Percentage'),
        ('fixed_amount', 'Fixed Amount'),
        ('bogo', 'Buy One Get One'),
        ('quantity_based', 'Quantity Based'),
        ('time_limited', 'Time Limited'),
        ('conditional', 'Conditional'),
        ('tiered', 'Tiered'),
        ('coupon_code', 'Coupon Code'),
        ('membership', 'Membership'),
        ('bundle', 'Bundle'),
    )
    offer_type = models.CharField(max_length=20, choices=offer_type_choices)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text='Only for Percentage offer type')
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='For Fixed Amount offer type')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    min_quantity = models.PositiveIntegerField(default=1, blank=True, null=True)
    min_purchase_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    coupon_code = models.CharField(max_length=20, blank=True)
    membership_required = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
# PRODUCT 
class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    picture = models.ImageField(null=True, blank=True)
    in_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.name) +'|'+ str(self.price) + '|' + str(self.in_stock)

# PRODUCT VARIENT
class ProductVariant(BaseModel):
    SIZE = (
        ('SMALL','SMALL'),
        ('LARGE','LARGGE'),
        ('MEDIUM','MEDIUM'))

    product = models.ForeignKey('Product',on_delete=models.CASCADE,related_name='product_variant')
    sku           = models.CharField(max_length=20)
    size          = models.CharField(max_length=100,choices=SIZE,null=True,blank=True)
    def __str__(self):
        return str(self.product) +'|'+ str(self.sku)

# DISCOUNTED _ PRODUCT 
class ProductOffer(BaseModel):
    product = models.ForeignKey('Product',on_delete=models.CASCADE,related_name='product_offer')
    offer   = models.ForeignKey('Offer',on_delete=models.CASCADE,related_name='product_offer')

    def __str__(self):
        return str(self.product) +'|'+ str(self.offer)

# CART 
class Cart(BaseModel):
    user            = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)

# CART ITEM
class CartItem(BaseModel):
    cart            = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity        = models.PositiveIntegerField(default=1)
    price           = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.cart) +'|'+ str(self.product) +'|'+ str(self.price)

# ORDER
class Order(BaseModel):
    ORDER_METHOD_CHOICES = (
        ("COD", "COD"),
        ("ONLINE", "ONLINE")
    )
    ORDER_STATUS_CHOICES = (
        ("PENDING", "PENDING"),
        ("DELIVERED", "DELIVERED"),
        ("CANCELED", "CANCELED")
    )
    PAYMENT_STATUS_CHOICES = (
        ("SUCCESS", "Success"),
        ("FAILURE", "Failure"),
        ("PENDING", "Pending")
    )

    user            = models.ForeignKey(CustomUserModel,on_delete=models.CASCADE) 
    order_id        = models.AutoField(primary_key=True)
    order_date      = models.DateTimeField(auto_now_add=True)
    order_mode      = models.CharField(choices=ORDER_METHOD_CHOICES, default='COD', max_length=10)
    order_status    = models.CharField(choices=ORDER_STATUS_CHOICES, default='PENDING', max_length=20)
    payment_status  = models.CharField(choices=PAYMENT_STATUS_CHOICES, default='PENDING', max_length=20)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

# ORDER ITEMS
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order: {self.order.order_id})"


