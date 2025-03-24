from rest_framework import serializers

from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password # validate_password: Validates whether the password meets the required criteria.

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'imageprofile')

       # extra_kwargs (dict): Additional keyword arguments for specific fields.
                # - 'first_name': {'required': True}  Indicates that the first_name field is required.
                # - 'last_name': {'required': True}  Indicates that the last_name field is required.
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            imageprofile=validated_data.get('imageprofile', None)
        )
        
        user.set_password(validated_data['password'])
        user.save()
        
        return user