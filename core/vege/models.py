from django.db import models

from django.contrib.auth.models import User
#for customize User 
# from django.contrib.auth import get_user_model
# User = get_user_model()

from .utils import generate_slugify


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipe')

    def save(self, *args, **kwargs):
        self.slug = generate_slugify(self.recipe_name)
        super(Recipe, self).save(*args, **kwargs)

    
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:   
        ordering = ['department']    # it store in alphabetical order


class StudentID(models.Model):
    student_id = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.student_id  
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name
    
class StudentManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)    
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    is_deleted = models.BooleanField(default=False)

    objects = StudentManger()
    admin_objects = models.Manager()
    
    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ['student_name']   #  it store in alphabetical order
        verbose_name = "student"     # it means Student class can also known as student 

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name}'
    
    class Meta:
        unique_together = ['student','subject']    # both student and subject will not be repeat

class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name="studentreportcard", on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date_of_report_card_generated = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student_rank','date_of_report_card_generated']    # both student and subject will not be repeat
    