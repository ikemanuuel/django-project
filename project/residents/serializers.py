from .models import Residents
from rest_framework import serializers


class ResidentsSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField()
    middlename = serializers.CharField()
    lastname = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.CharField()
    birthdate = serializers.DateField()
    birthplace = serializers.CharField()
    civilstatus = serializers.CharField()
    bloodtype = serializers.CharField()
    religion = serializers.CharField()
    totalhouseholdmember = serializers.IntegerField()
    occupation = serializers.CharField()
    nationality = serializers.CharField()
    educationalattainment = serializers.CharField()
    householdno = serializers.IntegerField()

    class Meta:
        model = Residents
        fields = '__all__'

    def create(self, validated_data):
        return Residents.objects.create(**validated_data)