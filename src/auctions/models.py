from django.db import models

# Create your models here.
class User(models.Model):
    auth_id = models.IntegerField(unique=True, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    dob = models.DateField()

class Item(models.Model):
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    NEW = 'new'
    USED = 'used'
    CONDITION_CHOICES = [
        (NEW, 'New'),
        (USED, 'Used'),
    ]
    condition = models.CharField(
        max_length=10,
        choices=CONDITION_CHOICES,
        default=NEW,
    )
    created = models.DateField(auto_now_add=True)
    
class Auction(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    start = models.DateField(auto_now_add=True)
    end = models.DateField()
    D1 = 'd1'
    D3 = 'd3'
    D5 = 'd5'
    D7 = 'd7'
    D10 = 'd10'
    DURATION_CHOICES = [
        (D1, '1 Day'),
        (D3, '3 Days'),
        (D5, '5 Days'),
        (D7, '7 Days'),
        (D10, '10 Days'),
    ]
    duration = models.CharField(
        max_length=3,
        choices=DURATION_CHOICES,
        default=D3,
    )
    
class Bid(models.Model):
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateField(auto_now_add=True)
