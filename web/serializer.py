from rest_framework import serializers
from .models import client
from .models import Student
class clientSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    # email = serializers.EmailField()
    def create(self, validate_data):
        return client.objects.create(**validate_data)

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    # id = serializers.IntegerField()

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.city = validate_data.get('city', instance.city)
        instance.roll = validate_data.get('roll', instance.roll)
        instance.save()
        return instance