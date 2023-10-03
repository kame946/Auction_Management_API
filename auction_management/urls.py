from django.urls import path
from .views import list_active_auctions, AuctionCreateView, AuctionDetailView, place_bid

urlpatterns = [
    path('create/', AuctionCreateView.as_view(), name='auction-create'),
    path('detail/<int:pk>/', AuctionDetailView.as_view(), name='auction-detail'),
    path('active/', list_active_auctions, name='active-auctions'),
    path('bid/<int:id>', place_bid, name='place-bid'),
]
