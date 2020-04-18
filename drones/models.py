from django.db import models


class DroneCategory(models.Model):
    name = models.CharField(max_length=250, blank=False, default='', unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Drone(models.Model):
    name = models.CharField(max_length=250, blank=False, default='', unique=True)
    drone_category = models.ForeignKey(
        DroneCategory,
        related_name='drones',
        on_delete=models.CASCADE
    )
    manufacturing_date = models.DateTimeField()
    has_it_completed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='drones',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Pilot(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    name = models.CharField(max_length=250, blank=False, default='', unique=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE
    )
    races_count = models.IntegerField()
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Competition(models.Model):
    pilot = models.ForeignKey(
        Pilot,
        related_name='competitions',
        on_delete=models.CASCADE
    )
    drone = models.ForeignKey(
        Drone,
        on_delete=models.CASCADE
    )
    distance_in_feet = models.IntegerField()
    distance_achievement_day = models.DateTimeField()

    class Meta:
        ordering = ('-distance_in_feet',)
