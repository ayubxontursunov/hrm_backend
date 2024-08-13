from rest_framework import serializers
from .models import *

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#
#     def create(self, validated_data):
#         user = User.objects.create(**validated_data)
#         return user

from rest_framework import serializers
from .models import User

from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
import random
import string

from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
import random
import string

from django.contrib.auth import authenticate
from .models import User  # Adjust import if using a custom user model

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from .models import User  # Adjust this if using a custom user model

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Retrieve the user by username
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        # Check password
        if not check_password(password, user.password_hash):
            raise serializers.ValidationError("Invalid credentials")

        # Add user instance to validated data
        data['user'] = user
        return data

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)  # Optional on creation

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_active']

    def create(self, validated_data):
        # Extract the password and remove it from validated_data
        password = validated_data.pop('password', None)
        # Generate a random password if none is provided
        if not password:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        # Create the user instance
        user = super().create(validated_data)
        # Set the password hash and save the user
        user.password_hash = make_password(password)
        user.save()
        # Return the user instance and the generated password
        return user, password

    def update(self, instance, validated_data):
        # Extract the password and remove it from validated_data
        password = validated_data.pop('password', None)
        # Update the user instance
        user = super().update(instance, validated_data)
        # Set the new password hash if provided
        if password:
            user.password_hash = make_password(password)
            user.save()
        return user






class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class EmployeePositionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePositionHistory
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class EmployeeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDocument
        fields = '__all__'

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class EmployeeTrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTraining
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'
