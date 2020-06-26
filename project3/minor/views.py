from django.shortcuts import render, get_object_or_404 ,redirect, reverse
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FacultyInfo,GroupInfo, Project, HeadOfDepartment, ClassCoordinator
from .forms import UserInfoForm, FacultyInfoForm, GroupInfoForm, ProjectForm, ProjectApprovalByMentorForm, ProjectApprovalByHODForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import datetime
class HomeView(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        my_project = []
        hod = ''
        faculty = ''
        group = ''
        if FacultyInfo.objects.filter(user = self.request.user):
            faculty = FacultyInfo.objects.filter(user = self.request.user)[0]
            group = GroupInfo.objects.filter(mentor = faculty)
            for i in group:
                if Project.objects.filter(group = i):
                    project =  Project.objects.get(group = i)
                    my_project.append(project)
        if HeadOfDepartment.objects.filter(user = self.request.user):
            hod = HeadOfDepartment.objects.filter(user = self.request.user)[0]
            group = GroupInfo.objects.filter(department = hod.department)
            for i in group:
                project = Project.objects.get(group = i)
                my_project.append(project)
        if GroupInfo.objects.filter(user = self.request.user):
            group = GroupInfo.objects.get(user = self.request.user)
            if Project.objects.filter(group = group):
                project = Project.objects.filter(group = group)[0]
                my_project.append(project)

        d = dict()
        if faculty:
            d['faculty'] = faculty
        if hod:
            d['hod'] = hod
        if group:
            d['group'] = group
        d['my_project'] = my_project
        return render(self.request,'new_home.html',d)

class ProjectDetailView(LoginRequiredMixin,DetailView):
    model = Project
    hod = ''
    faculty = ''
    template_name = 'project_detail.html'
    def get_context_data(self, **kwargs):
        hod = ''
        faculty = ''
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        if HeadOfDepartment.objects.filter(user = self.request.user):
            hod = HeadOfDepartment.objects.filter(user = self.request.user)[0]
        elif FacultyInfo.objects.filter(user = self.request.user):
            faculty = FacultyInfo.objects.filter(user = self.request.user)[0]
        if faculty:
            context['faculty'] = faculty
        if hod:
            context['hod'] = hod
        # context['hod'] = self.

        return context

    def post(self,*args,**kwargs):
        hod = ''
        faculty = ''
        # context = super(ProjectDetailView, self).get_context_data(**kwargs)
        if HeadOfDepartment.objects.filter(user = self.request.user):
            hod = HeadOfDepartment.objects.filter(user = self.request.user)[0]
        elif FacultyInfo.objects.filter(user = self.request.user):
            faculty = FacultyInfo.objects.filter(user = self.request.user)[0]
        if self.request.method == 'POST':
            # context = super(ProjectDetailView, self).get_context_data(**kwargs)
            if faculty:
                print("Faculty ")
                user = faculty
                # print("Pk : ",pk)
                project_title = self.request.GET.get('title')
                title = project_title
                pk = kwargs.get('pk')
                project = Project.objects.get(pk = pk)
                mentor_feedback = self.request.POST.get('mentor_feedback')
                mentor_message = self.request.POST.get('mentor_message')
                project.mentor_feedback = mentor_feedback
                time = datetime.datetime.now()
                day = str(time.day)
                month = str(time.month)
                year = str(time.year)
                project.mentor_message += mentor_message +" \nSent on :  "+ day+"/" +month+"/"+year   + "\n\n\n"+"\n"
                project.save()
                return redirect("/")

            elif hod:
                print("HOD")
                # print("Pk : ",pk)
                user = hod
                pk = kwargs.get('pk')
                # project_title = self.request.GET.get('title')
                # project = Project.objects.get(self.pk = pk)
                # title = project_title
                project = Project.objects.get(pk =pk)
                hod_feedback = self.request.POST.get('hod_feedback')
                project.hod_feedback = hod_feedback
                project.save()
                return redirect("/")

            else:
                print("Student")
                # print("Pk : ",pk)
                user = self.request.user
                project_status = self.request.POST.get('project_status')
                # mentor_feedback = self.request.POST.get('mentor_feedback')
                # hod_feedback = self.request.POST.get('hod_feedback')
                project_title = self.request.GET.get('title')
                # group = GroupInfo.objects.get(self.pk = pk)
                # project = Project.objects.get(self.pk = pk)
                pk = kwargs.get('pk')
                project = Project.objects.get(pk = pk)
                synopsis = self.request.FILES['synopsis']
                wbs = self.request.FILES['wbs']
                srs = self.request.FILES['srs']
                project.status = project_status
                project.synopsis = synopsis
                project.srs = srs
                project.wbs = wbs
                time = datetime.datetime.now()
                day = str(time.day)
                month = str(time.month)
                year = str(time.year)
                project.group_message += self.request.POST.get('group_message') + " Sent on :  "+ day+"/" +month+"/"+year   + "\n\n\n"+"\n"
                # project.mentor_feedback = mentor_feedback
                # project.hod_feedback = hod_feedback
                project.save()

                return redirect("/")


@login_required
def mentor_approval(request,pk):
    project = Project.objects.get(pk = pk)
    print(project)
    if project:
        project.is_approved_by_mentor = True
    project.save()
    return redirect("/")

@login_required
def hod_approval(request,pk):
    project = Project.objects.get(pk = pk)
    print(project)
    if project:
        project.is_approved_by_HOD = True
    project.save()
    return redirect("/")

@login_required
def coordinator_home(request):
    faculty = FacultyInfo.objects.get(user = request.user)
    coordinator = ''
    group = ''
    if ClassCoordinator.objects.filter(faculty = faculty):
        coordinator = ClassCoordinator.objects.filter(faculty = faculty)[0]
    print(faculty, coordinator)
    if coordinator:
        if GroupInfo.objects.filter(department = faculty.department, section = coordinator.section, year = coordinator.year):
            group = GroupInfo.objects.filter(department = faculty.department, section = coordinator.section, year = coordinator.year)
    my_project = []
    if group:
        for i in group:
            project = Project.objects.filter(group = i)[0]
            my_project.append(project)
    return render(request,'coordinator.html',{'my_project':my_project})

def faculty_registration(request):
    registered = False
    if request.method == "POST":
        user_form = UserInfoForm(request.POST)
        faculty_form = FacultyInfoForm(request.POST)

        if user_form.is_valid() and faculty_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            faculty = faculty_form.save(commit = False)
            faculty.user = user
            faculty.save()
            registered = True
            return redirect("/")
        else:
            print(user_form.errors, faculty_form.errors)

    else:
        user_form = UserInfoForm()
        faculty_form = FacultyInfoForm()

    return render(request,'faculty_registration.html',{
                                'user_form':user_form,
                                'faculty_form':faculty_form,
                                'registered':registered
    })


def group_registration(request):
    registered = False
    if request.method == "POST":
        user_form = UserInfoForm(request.POST)
        group_form = GroupInfoForm(request.POST)
        # group_detail_form = GroupDetailForm(request.POST)
        if user_form.is_valid() and group_form.is_valid():




            # group_detail = group_detail_form.save()
            group = group_form.save(commit=False)
            # group.department = group.mentor.department
            # group.department = group.mentor.department
            if group.department == group.mentor.department:
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                group.user = user
                group.save()
                registered = True
                return redirect("/")
            else:
                return render(request,'error.html')
        else:
            print(user_form.errors, group_form.errors)

    else:
        user_form = UserInfoForm()
        group_form = GroupInfoForm()
        # group_detail_form = GroupDetailForm()
    return render(request,'group_registration.html',{
                                'user_form':user_form,
                                'group_form':group_form,
                                'registered':registered
    })

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username,password= password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,'greet.html',{'username':username})
            else:
                return HttpResponse("<h1 class= 'jumbotron' >Your account is not active</h1>")
        else:
                print("Invalid credentials : ",username,password)
                return render(request,'Invalid_login.html')
    else:
        return render(request,'login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return redirect("/")

@login_required
def project_form_view(request):
        registered = False
        if request.method == "POST":
            # user = get_object_or_404(User)username
            project_form = ProjectForm(request.POST)
            group = GroupInfo.objects.get(user = request.user)
            if project_form.is_valid():
                project = project_form.save(commit = False)
                project.user = request.user
                project.group = group
                project.save()
                registered = True
                return redirect("/")
            else:
                print(project_form.errors)
        else:
            project_form = ProjectForm()
            return render(request,'project_form.html',{'project_form':project_form,'registered':registered})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    login_url = '/login/'
    redirect_field_name = 'project_detail.html'
