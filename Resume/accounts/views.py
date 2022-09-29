from email import message
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpFrom
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.contrib.staticfiles import finders
from django.conf import settings
import os
# Create your views here.

class valuess:
    d={}
v=valuess()

def home(request):
    return render(request, 'home.html')


@login_required
def login_home(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpFrom()
    return render(request, 'registration/signup.html', {'form': form})


def TermsAndCondition(request):
    return render(request, 'termsAndCondition.html')


def password_change(request):
    return render(request, 'password_change_form.html')


def aboutUs(request):
    return render(request, 'aboutUs.html')


def ContactUs(request):
    return render(request, 'ContactUs.html')


def render_pdf_view(request,data,temp):
    template_path = temp
    context = data
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response,link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def link_callback(uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path



def edu_form(request):
    return render(request,"edu_form.html")


def work_form(request):

    cc=request.GET["bk"]
    if cc=='':
        cc=0
    c=int(cc)+1
  
    Edu_dic={}

    for i in range(1,c):
        dic={}
        s="school"
        i=i.__str__()
        s=s+i
        d=request.GET[s]
        dic["school"]=d

        p="course"
        i=i.__str__()
        p=p+i
        vp=request.GET[p]
        dic["cource"]=vp

        sd="start"
        i=i.__str__()
        sd=sd+i
        sdv=request.GET[sd]
        dic["start"]=sdv

        ed="end"
        i=i.__str__()
        ed=ed+i
        ev=request.GET[ed]
        dic["end"]=ev

        pr="pr"
        i=i.__str__()
        pr=pr+i
        prv=request.GET[pr]
        dic["pr"]=prv

        Edu_dic[i]=dic

    v.d["edu"]=Edu_dic

    return render(request,'Workexp.html')
    
def awards_form(request):

    cc=request.GET["bk"]
    if cc=='':
        cc=0
    c=int(cc)+1
  
    Edu_dic={}

    for i in range(1,c):
        dic={}
        s="compny"
        i=i.__str__()
        s=s+i
        d=request.GET[s]
        dic["compny"]=d

    
        sd="start"
        i=i.__str__()
        sd=sd+i
        sdv=request.GET[sd]
        dic["start"]=sdv

        ed="end"
        i=i.__str__()
        ed=ed+i
        ev=request.GET[ed]
        dic["end"]=ev

        pr="about"
        i=i.__str__()
        pr=pr+i
        prv=request.GET[pr]
        dic["about"]=prv

        Edu_dic[i]=dic
    
    v.d["work"]=Edu_dic

    return render(request,'awards_form.html')




def skill_form(request):

    cc=request.GET["bk"]
    if cc=='':
        cc=0
    c=int(cc)+1
  
    Edu_dic={}

    for i in range(1,c):
        dic={}
        s="award"
        i=i.__str__()
        s=s+i
        d=request.GET[s]
        dic["award"]=d

        Edu_dic[i]=dic
    
    v.d["awards"]=Edu_dic

    return render(request,'skill_form.html')


def personal_form(request):

    cc=request.GET["bk"]
    if cc=='':
        cc=0

    c=int(cc)+1
  
    Edu_dic={}

    for i in range(1,c):
        dic={}
        s="skill"
        i=i.__str__()
        s=s+i
        d=request.GET[s]
        dic["skill"]=d
        Edu_dic[i]=dic
    v.d["skills"]=Edu_dic

    return render(request,'personal_form.html')


def temp_Result1(request):
    dic=v.d
    return render(request,'Temp1Result.html', dic)


def choose_templete(request):

    Fname=request.GET['Fname']
    Lname=request.GET['Lname']
    intre=request.GET['intrest']
    mo=request.GET['mono']
    email=request.GET['email']
    contry=request.GET['contry']    
    english=request.GET["lang"]
    about=request.GET["about"]

    lang=english.split(",")

    v.d["Fname"]=Fname
    v.d["Lname"]=Lname
    v.d["intrest"]=intre
    v.d["mo"]=mo
    v.d["email"]=email
    v.d["contry"]=contry
    v.d["lang"]=lang
    v.d["about"]=about

    return render(request, 'choose.html')


def choose_templete_aftervalue(request):

    return render(request,'choose.html')


def temp_Result1(request):
    dic=v.d
    return render(request,'Temp1Result.html', dic)

def temp_Result2(request):
    dic=v.d
    return render(request,'Temp2Result.html', dic)
    
def temp_Result3(request):
    dic=v.d
    return render(request,'Temp3Result.html', dic)


def conformForFirst(request):
    return render_pdf_view(request,v.d,'r1.html')

def conformForSecond(request):
    return render_pdf_view(request,v.d,'r4.html')

def conformForThird(request):
    return render_pdf_view(request,v.d,'r3.html')

