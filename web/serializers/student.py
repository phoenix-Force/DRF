from dataclasses import fields
from wsgiref.validate import validator
from rest_framework import serializers
from ..models import Student

def requiredssss( value):
    if value is None:
        raise serializers.ValidationError('field is requiredss')
    return 
        
        

class StudentSerializer1(serializers.Serializer):
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
    
    #field lavel validation
    # def validate_roll(self, value):
    #     if value > 1000:
    #         raise serializers.ValidationError('Roll cannot be gretter then 1000')
    #     return value
    
    # # $object lavel validation
    
    # def validate(self, data):
    #     roll = data.get('roll')
    
    
    
    
    
    # MODEL SEREALIZER
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'city', 'roll', 'id']
        
        # read only mode
        # read_only_fields = ['roll']
        extra_kwargs = { 'name': { 'read_only': True}}
        
        
        
    # def validate_roll(self, value):
    #     if value > 1000:
    #         raise serializers.ValidationError('Roll cannot be gretter then 1000')
    #     return value
    
    # def validate(self, data):
    #     roll = data.get('roll')
        
            
    
    