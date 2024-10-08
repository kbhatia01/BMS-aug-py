from rest_framework import serializers


class CreateBookingRequestDto(serializers.Serializer):
    user_id = serializers.IntegerField()
    show_id = serializers.IntegerField()
    show_seat_ids = serializers.ListField(child=serializers.IntegerField())


class CreateBookingResponseDto(serializers.Serializer):
    booking_id = serializers.IntegerField(required=False)
    response_status = serializers.CharField(max_length=10)
