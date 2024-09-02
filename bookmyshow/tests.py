from unittest.mock import Mock

from django.utils import timezone

from django.test import TestCase

# Create your tests here.
from django.test import TransactionTestCase

from bookmyshow.models import User, Movie, Screen, Region, Theatre, Seat, SeatType, Show, Feature, ShowSeat, \
    showSeatStatus, ShowSeatType
from bookmyshow.service import BookShowService
from bookmyshow.views import BookingViewSet


class BookShowTestCase(TransactionTestCase):

    def setUp(self):
        self.user, val = User.objects.get_or_create(
            id=1,
            email="abc@gmail.com",
            password="password"
        )
        self.movie, val = Movie.objects.get_or_create(
            title="abc",
            release_date="2020-01-20",
            runtime=200
        )
        self.region, val = Region.objects.get_or_create(
            id=2,
            name="DELHI"
        )
        self.theatre, val = Theatre.objects.get_or_create(
            name="inox",
            region=self.region
        )
        self.screen, val = Screen.objects.get_or_create(
            region=self.region,
            name="AUDI1",
            theatre=self.theatre
        )

        self.seat1, val = Seat.objects.get_or_create(
            row_number=1,
            col_number=1,
            number="A1",
            seat_type=SeatType.SILVER,
            screen=self.screen
        )
        self.seat2, val = Seat.objects.get_or_create(
            row_number=2,
            col_number=1,
            number="B1",
            seat_type=SeatType.SILVER,
            screen=self.screen
        )

        self.feature, val = Feature.objects.get_or_create(
            name="2D"
        )
        self.show, val = Show.objects.get_or_create(
            movie=self.movie,
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=2),
            screen=self.screen,
            features=self.feature
        )

        self.showSeat, val = ShowSeat.objects.get_or_create(
            show=self.show,
            seat=self.seat1,
            show_seat_status=showSeatStatus.AVAILABLE
        )

        self.showSeat, val = ShowSeat.objects.get_or_create(
            show=self.show,
            seat=self.seat2,
            show_seat_status=showSeatStatus.AVAILABLE
        )

        self.ShowSeatType, val = ShowSeatType.objects.get_or_create(
            show=self.show,
            seat_type=SeatType.SILVER,
            price=500
        )


    def test_create_booking(self):
        self.service = BookShowService()
        self.view = BookingViewSet(service=self.service)

        request_data = {
            'user_id': 1,
            'show_id' : 1,
            'show_seat_ids': [1,2]
        }

        request = Mock()
        request.data = request_data
        booking = self.view.create_booking(request)

        print(booking.data)






