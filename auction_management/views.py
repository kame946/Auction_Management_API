from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Auction
#from user_management.models import UserBalance
from .serializers import AuctionSerializer
from django.utils import timezone

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_active_auctions(request):
    print(request.data)
    """
    List all active auctions that are currently ongoing.
    """
    active_auctions = Auction.objects.filter(end_time__gt=timezone.now())
    serializer = AuctionSerializer(active_auctions, many=True)
    return Response(serializer.data)

class AuctionCreateView(generics.CreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [permissions.IsAdminUser]

class AuctionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [permissions.IsAdminUser]


# Handling the bid functionality
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def place_bid(request, id):
    """
    Place a bid on a specific auction using user token authentication.
    """
    try:
        auction = Auction.objects.get(pk=id)
        print(auction)
    except Auction.DoesNotExist:
        return Response({'error': 'Auction does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    
    if not auction.is_active():
        return Response({'error': 'Auction has ended.'}, status=status.HTTP_400_BAD_REQUEST)
    
    bid_amount = request.data.get('bid_amount')
    if bid_amount is None:
        return Response({'error': 'Bid amount is required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = request.user
    
    if bid_amount <= auction.start_price:
        return Response({'error': 'Bid amount must be greater than the start price.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if bid_amount > user.wallet_balance:
        return Response({'error': 'Insufficient balance.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Update the user's wallet balance and save the bid
    user.wallet_balance -= bid_amount
    user.save()
    
    auction.start_price = bid_amount
    auction.winner = user
    auction.save()
    
    return Response({'message': 'Bid placed successfully.'}, status=status.HTTP_200_OK)
