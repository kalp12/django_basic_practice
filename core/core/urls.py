"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home.views import *

from vege.views import *

urlpatterns = [
    path('', home , name='home'),
    path('success-page/', success_page , name='success'),
    path('contact/', contact , name='contact'),
    path('about/', about , name='about'),

    path('send-email/',send_email, name="send_email" ),

    path('recipe/', recipe , name='recipe'),
    path('delete-recipe/<idx>/', delete_recipe , name='delete_recipe'),
    path('update-recipe/<idx>/', update_recipe , name='update_recipe'),

    path('login-page/', login_page , name='login_page'),
    path('register-page/', register_page , name='register_page'),
    path('logout-page/', logout_page , name='logout_page'),

    path('students/', get_students , name='student'),
    path('get-student-marks/<student_id>', get_student_marks , name='get_student_marks'),


    path('admin/', admin.site.urls),
]


from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  
# // import in header


# // import in footer
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()