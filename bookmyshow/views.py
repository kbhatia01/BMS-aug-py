from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from bookmyshow.serializer import *


class BookingViewSet(viewsets.ViewSet):

    def __init__(self, service, **kwargs):
        self.service = service
        super().__init__(**kwargs)

    def create_booking(self, request):
        #req.data: { user_id 1: show_id: 3, show_seat_id: [2,4]}
        try:
            req = CreateBookingRequestDto(request.data)
            # req.is_valid(raise_exception=True)

            booking = self.service.create_booking(
                user_id=req.data.get("user_id"),
                show_seat_ids=req.data.get("show_seat_ids"),
                show_id=req.data.get("show_id")
            )

            data = {
                'booking_id': booking.booking_id,
                'status': booking.status,
            }
            return CreateBookingResponseDto(data)
        except Exception as e:
            print(e)
            return CreateBookingResponseDto({"status": "ERROR"})
