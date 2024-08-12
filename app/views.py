# # from rest_framework import viewsets
# # from .models import Employee
# # from .serializers import EmployeeSerializers
# #
# # class EmployeeViewSet(viewsets.ModelViewSet):
# #     queryset = Employee.objects.all()
# #     serializer_class = EmployeeSerializers
#
#
# from rest_framework import viewsets
# from .models import *
# from .serializers import *
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#
# class NotificationViewSet(viewsets.ModelViewSet):
#     queryset = Notification.objects.all()
#     serializer_class = NotificationSerializer
#
# class TrainingsViewSet(viewsets.ModelViewSet):
#     queryset = Trainings.objects.all()
#     serializer_class = TrainingsSerializer
#
# class DepartmentViewSet(viewsets.ModelViewSet):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer
#
# class UserSecondDepartmentViewSet(viewsets.ModelViewSet):
#     queryset = UserSecondDepartment.objects.all()
#     serializer_class = UserSecondDepartmentSerializer
#
# class DivisionViewSet(viewsets.ModelViewSet):
#     queryset = Division.objects.all()
#     serializer_class = DivisionSerializer
#
# class EmployeePositionViewSet(viewsets.ModelViewSet):
#     queryset = EmployeePosition.objects.all()
#     serializer_class = EmployeePositionSerializer
#
# class PositionViewSet(viewsets.ModelViewSet):
#     queryset = Position.objects.all()
#     serializer_class = PositionSerializer
#
# class TeamViewSet(viewsets.ModelViewSet):
#     queryset = Team.objects.all()
#     serializer_class = TeamSerializer
#
# class TeamMembersViewSet(viewsets.ModelViewSet):
#     queryset = TeamMembers.objects.all()
#     serializer_class = TeamMembersSerializer
#
# class DocumentViewSet(viewsets.ModelViewSet):
#     queryset = Document.objects.all()
#     serializer_class = DocumentSerializer
#
# class EmployeeDocumentViewSet(viewsets.ModelViewSet):
#     queryset = EmployeeDocument.objects.all()
#     serializer_class = EmployeeDocumentSerializer
#
# class UserRoleViewSet(viewsets.ModelViewSet):
#     queryset = UserRole.objects.all()
#     serializer_class = UserRoleSerializer
#
# class RoleViewSet(viewsets.ModelViewSet):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer
#
# class AnnouncementViewSet(viewsets.ModelViewSet):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer
#
# class LeaveTripViewSet(viewsets.ModelViewSet):
#     queryset = Leaves.objects.all()
#     serializer_class = LeaveSerializer
#
# class TokenViewSet(viewsets.ModelViewSet):
#     queryset = Token.objects.all()
#     serializer_class = TokenSerializer



from rest_framework import viewsets
from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class EmployeePositionHistoryViewSet(viewsets.ModelViewSet):
    queryset = EmployeePositionHistory.objects.all()
    serializer_class = EmployeePositionHistorySerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class EmployeeDocumentViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDocument.objects.all()
    serializer_class = EmployeeDocumentSerializer

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class EmployeeTrainingViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTraining.objects.all()
    serializer_class = EmployeeTrainingSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
