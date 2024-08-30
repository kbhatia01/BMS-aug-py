from django.utils import timezone

from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)


class Region(BaseModel):
    name = models.CharField(max_length=50)


class Theatre(BaseModel):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Feature(BaseModel):
    name = models.CharField(max_length=50)


class Screen(BaseModel):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)


class ScreenFeature:
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('screen', 'feature'),)


class Movie(BaseModel):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    runtime = models.IntegerField()


class Show(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    features = models.ForeignKey(Feature, on_delete=models.CASCADE)


class ShowFeature:
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)


class SeatType(models.TextChoices):
    GOLD = 'GOLD', 'Gold'
    SILVER = 'SILVER', 'Silver'
    PLATINUM = 'PLATINUM', 'Platinum'


class Seat(BaseModel):
    row_number = models.IntegerField()
    col_number = models.IntegerField()
    number = models.CharField(max_length=50)
    seat_type = models.TextField(choices=SeatType.choices)


class showSeatStatus(models.TextChoices):
    AVAILABLE = 'AVAILABLE', 'Available'
    MAINTENANCE = 'MAINTENANCE', 'Maintenance'
    RESERVED = 'RESERVED', 'Reserved'
    LOCKED = 'LOCKED', 'Locked'


class ShowSeat(BaseModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show_seat_status = models.TextField(choices=showSeatStatus.choices)


class ShowSeatType(BaseModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_type = models.ForeignKey(SeatType, on_delete=models.CASCADE)
    price = models.IntegerField()


class Ticket(BaseModel):
    ticket_number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    show_seats = models.ManyToManyField(ShowSeat)
    amount = models.IntegerField()
    booking_status = models.CharField(max_length=50)
    booking_time = models.DateTimeField(default=timezone.now)


class Payment(BaseModel):
    ref_number = models.IntegerField()
    amount = models.IntegerField()
    mode = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
