# # from django.urls import path, include
# # from rest_framework.routers import DefaultRouter
# # from .views import EmployeeViewSet
# #
# # router = DefaultRouter()
# # router.register(r'employees', EmployeeViewSet)
# #
# # urlpatterns = [
# #     path('', include(router.urls)),
# # ]
#
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     UserViewSet, EmployeeViewSet, CompanyViewSet, NotificationViewSet,
#     TrainingsViewSet, DepartmentViewSet, UserSecondDepartmentViewSet,
#     DivisionViewSet, EmployeePositionViewSet, PositionViewSet, TeamViewSet,
#     TeamMembersViewSet, DocumentViewSet, EmployeeDocumentViewSet,
#     UserRoleViewSet, RoleViewSet, AnnouncementViewSet, LeaveTripViewSet,
#     TokenViewSet
# )
#
# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'employees', EmployeeViewSet)
# router.register(r'companies', CompanyViewSet)
# router.register(r'notifications', NotificationViewSet)
# router.register(r'trainings', TrainingsViewSet)
# router.register(r'departments', DepartmentViewSet)
# router.register(r'user-second-departments', UserSecondDepartmentViewSet)
# router.register(r'divisions', DivisionViewSet)
# router.register(r'employee-positions', EmployeePositionViewSet)
# router.register(r'positions', PositionViewSet)
# router.register(r'teams', TeamViewSet)
# router.register(r'team-members', TeamMembersViewSet)
# router.register(r'documents', DocumentViewSet)
# router.register(r'employee-documents', EmployeeDocumentViewSet)
# router.register(r'user-roles', UserRoleViewSet)
# router.register(r'roles', RoleViewSet)
# router.register(r'announcements', AnnouncementViewSet)
# router.register(r'leaves', LeaveTripViewSet)
# router.register(r'tokens', TokenViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'divisions', views.DivisionViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'positions', views.PositionViewSet)
router.register(r'employee-position-history', views.EmployeePositionHistoryViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'user-roles', views.UserRoleViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'employee-documents', views.EmployeeDocumentViewSet)
router.register(r'trainings', views.TrainingViewSet)
router.register(r'employee-trainings', views.EmployeeTrainingViewSet)
router.register(r'announcements', views.AnnouncementViewSet)
router.register(r'leaves', views.LeaveViewSet)
router.register(r'notifications', views.NotificationViewSet)
router.register(r'tokens', views.TokenViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
