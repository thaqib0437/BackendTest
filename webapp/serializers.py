from rest_framework import serializers
from .models import User, activity_periods


class activity_periodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = activity_periods
        fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):
    activity_periods = activity_periodsSerializer(many = True)

    class Meta:
        model = User
        fields = ['user_id', 'real_name', 'tz', 'activity_periods']
    