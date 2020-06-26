from django.contrib import admin

# Register your models here.
from .models import FacultyInfo, GroupInfo, Project, HeadOfDepartment, ClassCoordinator

admin.site.register(FacultyInfo)
admin.site.register(GroupInfo)
admin.site.register(Project)
admin.site.register(HeadOfDepartment)
admin.site.register(ClassCoordinator)
