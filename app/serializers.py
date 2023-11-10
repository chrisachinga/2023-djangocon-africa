from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    is_verified = serializers.BooleanField(default=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    gender = serializers.ChoiceField(choices=User.GENDER_CHOICES, required=False)
    year_of_birth = serializers.IntegerField(required=False)
    
    class Meta:
        model = User
        fields = (
          'id', 'username', 'first_name', 'last_name', 'phone_number', 'is_verified',
          'gender', 'email', 'year_of_birth', 'password'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }
    

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

  
