import random
from django.shortcuts import render,redirect

from django.http import HttpResponse

from vege.seed import seed_db 
from .utils import send_email_to_client
from django.conf import settings

from home.models import Car

def send_email(request):
    # send_email_to_client()
    file_path = f"{settings.BASE_DIR}/public/static/recipe/GuviCertification_-_911d26p5r31f5e45OJ.png"
    send_email_to_client(file_path)
    return redirect('/')

def home(request):

    Car.objects.create(car_name= f"Nexon-{random.randint(0,100)}")

    # seed_db(100)
    peoples = [
        {'name':'Abhi', 'age':24},
        {'name':'Kap', 'age':20},
        {'name':'Ajink', 'age':49},
        {'name':'Dora', 'age':16}
    ]
    text = """Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nostrum nobis a repudiandae illo distinctio molestias temporibus? Laudantium, quae ullam, molestiae veniam doloremque error, debitis sit hic consectetur delectus dignissimos praesentium!
    Reiciendis voluptatum temporibus quidem itaque non cum nemo eum esse placeat aliquid exercitationem aperiam eligendi, accusamus neque numquam excepturi voluptatibus aspernatur vel nesciunt quia nulla illum beatae debitis! Iste, quia?
    ur ratione quaerat iure itaque doloremque? Vitae ipsa obcaecati distinctio autem repellendus unde atque facere quia repudiandae laudantium deleniti at, itaque tempora consectetur veniam repellat veritatis quidem voluptatum eius?"""
    return render(request,"home/index.html",context={'peoples':peoples,'text':text, 'title':'Django tutorial 2024'})

def contact(request):
    return render(request,"home/contact.html", context={'title':'Contact'})

def about(request):
    return render(request,"home/about.html", context={'title':'About'})

def success_page(request):
    print("*" * 100)
    return HttpResponse("You have successfully signed in")