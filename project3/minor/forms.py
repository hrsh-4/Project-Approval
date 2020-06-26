from django import forms
from .models import FacultyInfo, GroupInfo, Project
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
CHOICES=[('Yes','Approved'),
         ('No','Not Approved')]

class UserInfoForm(forms.ModelForm):
    min_length = 8
    password = forms.CharField(widget = forms.PasswordInput(),validators=[MinLengthValidator(int(min_length))])

    class Meta:
        model = User
        fields = ['username','email','password']
        REQUIRED_FIELDS = ['username','email','password']

class FacultyInfoForm(forms.ModelForm):
    class Meta:
        model = FacultyInfo
        fields = ['name','department','contact']


class GroupInfoForm(forms.ModelForm):
    class Meta:
        model = GroupInfo

        fields = [
            'department','year','section',
            'mentor','group_name','member_1_name','member_1_enrollment',
            'member_2_name','member_2_enrollment',
            'member_3_name','member_3_enrollment','contact'
        ]
        REQUIRED_FIELDS = ['user','member_1_name','member_1_enrollment','mentor','department',
                            'year','section','group_name','contact'
        ]
        # REQUIRED_FIELDS = ['user','department','year','section','mentor','group_name',
        #                     'member_1_name','member_1_enrollment','contact']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description']

class ProjectApprovalByMentorForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['is_approved_by_mentor']

class ProjectApprovalByHODForm(forms.Form):
        is_approved_by_HOD = forms.ChoiceField(label = 'Approve Project ?'  ,choices = CHOICES, widget = forms.RadioSelect)

# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ('srs', 'synopsis','wbs')
