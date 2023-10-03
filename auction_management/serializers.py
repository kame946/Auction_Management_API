from rest_framework import serializers
from .models import Auction

class AuctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auction
        fields = ('id', 'item_name', 'start_time', 'end_time', 'start_price', 'winner')