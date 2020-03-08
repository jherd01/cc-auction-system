from rest_framework import serializers
from .models import User, Item, Auction, Bid

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name',
            'address_1',
            'address_2',
            'city',
            'postcode',
            'email',
            'dob'
        )

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'seller_id',
            'title',
            'description',
            'condition',
            'created'
        )

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = (
            'item_id',
            'start',
            'end',
            'duration'
        )
        
class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = (
            'auction_id',
            'user_id',
            'bid_amount',
            'timestamp'
        )
