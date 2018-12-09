from .models import UserData

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	def __init__(self, *args, **kwargs):
		many = kwargs.pop('many', True)
		super(UserSerializer, self).__init__(many=many, *args, **kwargs)
	class Meta:
		model = UserData
		fields = '__all__'