from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from bookmyshow.serializer import *
class BookingViewSet(viewsets.ViewSet):

    def create_booking(self, request):
        #req.data: { user_id 1: show_id: 3, show_seat_id: [2,4]}
        req = CreateBookingRequestDto(request.data)
        req.is_valid(raise_exception=True)
        try:


        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


