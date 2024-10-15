from django.shortcuts import render,redirect

from .models import *

from django.db.models import Q, Sum
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

#for customize User 
# from django.contrib.auth import get_user_model
# User = get_user_model()

@login_required(login_url='/login-page')
def recipe(request):
    if request.method == "POST":
        data = request.POST
        file = request.FILES
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = file.get('recipe_image')
        # print(recipe_name)
        # print(recipe_description)
        # print(recipe_image)

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image= recipe_image
        )

        return redirect('/recipe')
    
    queryset = Recipe.objects.all()
    
    search_key = request.GET.get('search_key')
    if search_key:
        queryset = queryset.filter(
        Q(recipe_name__icontains=search_key) | Q(recipe_description__icontains=search_key)
    )

    context = {'recipes': queryset}

    return render(request,'recipe.html', context)

@login_required(login_url='/login-page')
def update_recipe(request,idx):
    queryset = Recipe.objects.get(slug=idx)

    if request.method == "POST":
        data = request.POST
        file = request.FILES

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = file.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipe')

    context = {'recipe': queryset}
    return render(request, 'update_recipe.html', context)

def login_page(request):
    if request.method == "POST":
        data = request.POST

        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login-page')
        
        user_authenticate = authenticate(username = username, password = password)
        if user_authenticate is None:
            messages.error(request, "Invalid Password")
            return redirect('/login-page')
        else:
            login(request,user_authenticate)
            return redirect('/recipe')

    return render(request, 'login_page.html')

def register_page(request):
    if request.method == "POST":
        data = request.POST

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        user_detail_name = User.objects.filter(username=username)
        if user_detail_name.exists():
            messages.error(request, "Username already taken")
            return redirect('/register-page/')
        
        user_detail = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user_detail.set_password(password)
        user_detail.save()
        messages.success(request, "Account created sucessfully!")
        return redirect('/register-page/')
    
    return render(request, 'register_page.html')

@login_required(login_url='/login-page')
def logout_page(request):
    logout(request)
    return redirect('/login-page')

@login_required(login_url='/login-page')
def delete_recipe(request,idx):
    queryset = Recipe.objects.get(id=idx)
    queryset.delete()
    return redirect('/recipe')

def get_students(request):
    queryset = Student.objects.all()

    search = request.GET.get("search_key")
    if search:
        queryset = queryset.filter(
            Q(student_name__icontains = search)|
            Q(student_id__student_id__icontains = search)|
            Q(student_age__icontains = search)|
            Q(student_address__icontains = search)|
            Q(student_email__icontains = search)|
            Q(department__department__icontains = search)
        )

    paginator = Paginator(queryset, 25)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'report/student.html', context={'queryset':page_obj})

def get_student_marks(request, student_id):
    # from .seed import generate_report_card
    # generate_report_card()
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    # First method - lengthy method
    # ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-student_age')
    # i = 1
    # for rank in ranks:
    #     # print(rank.student_name)
    #     # print(rank.marks)
    #     # print(rank.student_id)
    #     if student_id == rank.student_id.student_id:
    #         current_rank = i
    #         break
    #     i+=1
    # return render(request, 'report/get_student_marks.html', context={'queryset':queryset, 'total_marks':total_marks, 'current_rank':current_rank})

    # second method
    return render(request, 'report/get_student_marks.html', context={'queryset':queryset, 'total_marks':total_marks})