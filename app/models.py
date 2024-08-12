#
# from django.db import models
#
# class Employee(models.Model):
#     profile_photo = models.BinaryField(blank=True, null=True)
#     full_name = models.CharField(max_length=255)
#     status = models.BooleanField(default=True)
#     user_role = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     phonenumber = models.CharField(max_length=15)
#     email = models.EmailField()
#     birthdate = models.DateField()
#     wages = models.CharField(max_length=255)
#     work_exp_company = models.CharField(max_length=255)
#     education = models.TextField()
#     marital_status = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class User(models.Model):
#     username = models.CharField(max_length=255)
#     employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#
#
# class Division(models.Model):
#     division_id = models.AutoField(primary_key=True)
#     division_name = models.CharField(max_length=255)
#     team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='divisions')
#
# class Team(models.Model):
#     team_name = models.CharField(max_length=255)
#     team_lead = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='lead_teams')
#
# 1
#
# class Department(models.Model):
#     department_id = models.AutoField(primary_key=True)
#     department_name = models.CharField(max_length=255)
#     division = models.ForeignKey(Division, on_delete=models.CASCADE)
#
#
# class Company(models.Model):
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     division = models.ForeignKey(Division, on_delete=models.CASCADE)
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     user = models.ForeignKey(Employee, on_delete=models.CASCADE)
#
# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)
#
# class Trainings(models.Model):
#     training_name = models.CharField(max_length=255)
#     coordinator = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='coordinated_trainings')
#     department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='trainings')
#     division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, related_name='trainings')
#     start_date = models.DateField()
#     end_date = models.DateField()
#     created_by = models.ForeignKey(Employee, related_name='created_trainings', on_delete=models.SET_NULL, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
# class TeamMembers(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
#     user = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='team_memberships')
#
# class UserSecondDepartment(models.Model):
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     user = models.ForeignKey(Employee, on_delete=models.CASCADE)
#
# class EmployeePosition(models.Model):
#     duty = models.CharField(max_length=255)
#     position = models.ForeignKey('Position', on_delete=models.CASCADE)
#     rank = models.CharField(max_length=255)
#     user = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     is_current = models.BooleanField(default=True)
#     start_date = models.DateField()
#     end_date = models.DateField(blank=True, null=True)
#
# class Position(models.Model):
#     position_name = models.CharField(max_length=255)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     job_description = models.TextField()
#
# class Document(models.Model):
#     document_name = models.CharField(max_length=255)
#     document_type = models.CharField(max_length=255)
#     details = models.TextField()
#     document_data = models.BinaryField()
#
# class EmployeeDocument(models.Model):
#     document = models.ForeignKey(Document, on_delete=models.CASCADE)
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     access_type = models.CharField(max_length=255)
#     upload_date = models.DateTimeField(auto_now_add=True)
#
# class UserRole(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     role = models.ForeignKey('Role', on_delete=models.CASCADE)
#
# class Role(models.Model):
#     role_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Announcement(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     user = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
# class Leaves(models.Model):
#     leave_type = models.CharField(max_length=255)
#     description = models.TextField()
#     start_date = models.DateField()
#     end_date = models.DateField()
#     duration = models.CharField(max_length=255)
#     approval_status = models.CharField(max_length=255)
#     user = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
# class Token(models.Model):
#     user = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     token = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     blacklisted = models.BooleanField(default=False)


from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password_hash = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Department(models.Model):
    department_name = models.CharField(max_length=100, null=False)
    parent_department = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child_departments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name

class Division(models.Model):
    division_name = models.CharField(max_length=100, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='divisions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.division_name

class Team(models.Model):
    team_name = models.CharField(max_length=100, null=False)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='teams')
    team_lead = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='lead_teams')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name

class Position(models.Model):
    position_name = models.CharField(max_length=100, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='positions')
    job_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position_name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    profile_photo = models.BinaryField(blank=True, null=True)
    status = models.BooleanField(default=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, related_name='employees')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='employees')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name='employees')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EmployeePositionHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='position_history')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_date = models.DateField(null=False)
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Role(models.Model):
    role_name = models.CharField(max_length=50, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role_name

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'role')

class Document(models.Model):
    document_name = models.CharField(max_length=255, null=False)
    document_type = models.CharField(max_length=50, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    document_data = models.BinaryField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EmployeeDocument(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='documents')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='employee_documents')
    access_type = models.CharField(max_length=20, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

class Training(models.Model):
    training_name = models.CharField(max_length=255, null=False)
    coordinator = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='coordinated_trainings')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='trainings')
    start_date = models.DateField(null=False)
    end_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='created_trainings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EmployeeTraining(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='trainings')
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='employees')
    status = models.CharField(max_length=20, blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('employee', 'training')

class Announcement(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='created_announcements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leaves')
    leave_type = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    duration = models.IntegerField(blank=True, null=True)
    approval_status = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField(null=False)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tokens')
    token = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    is_blacklisted = models.BooleanField(default=False)
