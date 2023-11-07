from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    model = Booking
    fields = '__all__'