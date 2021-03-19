from django.contrib.auth.models import User
from rest_framework import serializers

from drones.models import DroneCategory, Drone, Competition, Pilot


class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='drone-detail'
    )

    class Meta:
        model = DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            "drones"
        )


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Drone
        fields = (
            'url',
            'drone_category',
            'name',
            'owner',
            'manufacturing_date',
            'has_it_completed',
            'inserted_timestamp',
        )


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer()

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'drone',
            'distance_in_feet',
            'distance_achievement_day'
        )


class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(
        choices=Pilot.GENDER_CHOICES
    )
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True
    )

    class Meta:
        model = Pilot
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'races_count',
            'competitions',
            'inserted_timestamp'
        )


class PilotCompetitionSerializer(serializers.ModelSerializer):
    drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='name')
    pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'pilot',
            'drone',
            'distance_in_feet',
            'distance_achievement_day'
        )


class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        fields = (
            'url',
            'name'
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    drones = UserDroneSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'username',
            'drone'
        )