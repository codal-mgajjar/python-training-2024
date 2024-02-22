from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

# Normal serializer.Serializer 
class ItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    category = serializers.CharField()

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
    
#Model serializer example
class ItemSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'category']
        #exclude = ['price']
        # depth = 1
        read_only_fields = ['name']

#Hyperlinked model serializer
class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['url', 'id', 'name', 'price', 'category']