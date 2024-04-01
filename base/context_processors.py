from .models import *
from django.template.context_processors import request

def blog_data(request):
    blogs = Blog.objects.all()
    return {'blogdata': blogs}

def calendar_data(request):
    calendars = Calendar.objects.all().order_by('-is_default')
    return {'calendardata': calendars}

def custom_data(request):
    if SchoolSetup.objects.all().exists():
        setup = SchoolSetup.objects.all().order_by('-created_at')
        data = setup[0]
        return {'data': data}
    else:
        data=None
        return {'data': data}
    
def social_data(request):
    if Socials.objects.all().exists():
        social = Socials.objects.all().order_by('-created_at')
        sodata = social[0]
        return {'sodata': sodata}
    else:
        sodata=None
        return {'sodata': sodata}
    
def message_data(request):
    msgdata = MessageFrom.objects.all()
    return {'message_data': msgdata}
      
def team_data(request):
    team = TeamMember.objects.all()
    return {'tdata': team}
 
def faq(request):
    faq = Faqs.objects.all()
    return {'fdata': faq}

def courses(request):
    courses = Courses.objects.all()
    return {'cdata': courses}

def testimonial(request):
    tmsg = Testimonial.objects.all()
    return {'tedata': tmsg}

def popup(request):
    modal = PopupMessage.objects.all()
    return {'pdata': modal}
