from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
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

# class ItemSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Item
        # fields = (
            
        # )

# class AuctionSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Auction
        # fields = (
            
        # )
        
# class BidSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Bid
        # fields = (
            
        # )
