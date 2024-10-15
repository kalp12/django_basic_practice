from faker import Faker
fake = Faker()
import  random
from .models import *
from django.db.models import Sum

def create_subject_marks():
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subject_objs = Subject.objects.all()
            for subject in subject_objs:
                SubjectMarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(20,100)
                )
    except Exception as e:
        print(e)

def seed_db(n=100)->None:   # it execute 10 times and will be returne None
    try:
        for _ in range(0,n):

            departments_objs = Department.objects.all()
            random_index =  random.randint(0, len(departments_objs)-1)

            student_id = f'STU-0{random.randint(100, 999)}'
            department = departments_objs[random_index]
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address  = fake.address()
            
            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
        )
    except Exception as e:
        print(e)

def generate_report_card():
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-student_age')
    i = 1
    for rank in ranks:
        ReportCard.objects.create(
            student = rank,
            student_rank = i
        )
        i+=1