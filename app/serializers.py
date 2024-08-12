# # from rest_framework import serializers
# # from .models import Employee
# # from rest_framework.serializers import Serializer, FileField
# #
# # class EmployeeSerializers(serializers.ModelSerializer):
# #     class Meta:
# #         model = Employee
# #         fields ="__all__"
# #
#
# from rest_framework import serializers
# from .models import (
#     User, Employee, Company, Notification, Trainings, Department,
#     UserSecondDepartment, Division, EmployeePosition, Position, Team,
#     TeamMembers, Document, EmployeeDocument, UserRole, Role, Announcement,
#     Leaves, Token
# )
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#
# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = '__all__'
#
# class CompanySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = '__all__'
#
# class NotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Notification
#         fields = '__all__'
#
# class TrainingsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Trainings
#         fields = '__all__'
#
# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = '__all__'
#
# class UserSecondDepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserSecondDepartment
#         fields = '__all__'
#
# class DivisionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Division
#         fields = '__all__'
#
# class EmployeePositionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeePosition
#         fields = '__all__'
#
# class PositionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Position
#         fields = '__all__'
#
# class TeamSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Team
#         fields = '__all__'
#
# class TeamMembersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TeamMembers
#         fields = '__all__'
#
# class DocumentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Document
#         fields = '__all__'
#
# class EmployeeDocumentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeDocument
#         fields = '__all__'
#
# class UserRoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserRole
#         fields = '__all__'
#
# class RoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Role
#         fields = '__all__'
#
# class AnnouncementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Announcement
#         fields = '__all__'
#
# class LeaveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Leaves
#         fields = '__all__'
#
# class TokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Token
#         fields = '__all__'


from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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
