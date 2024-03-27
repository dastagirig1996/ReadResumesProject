
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import os
from .pdfread import extract_salary_data,extract_text_from_docx
import pandas as pd
from django.contrib.auth.decorators import login_required
import re
def sign(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()   
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


def logins(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                
                    return HttpResponseRedirect('/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/sign/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def NameFile(file):
    match = re.search(r'_(.*?)\[\d+y_\d+m\]', file)
    if match:
        return match.group(1)
    else:
        return file

def findunique(ls,op,file):
    op[0].setdefault("NamefromFile",NameFile(file))
    if ls is not None:
        for i in ls:
            if i['Email_id'] == op[0]['Email_id']:
               return []
    return op

# @login_required(login_url='login')
def process_salary(request):
    if request.method == 'POST':
        uploaded_files =  request.FILES.getlist('files')
        print(uploaded_files)
        data = []
        # filesList = []
        for uploaded_file in uploaded_files:    
            # import pdb; pdb.set_trace()
            fileName = uploaded_file.name
            if fileName.endswith(".pdf"):
                op = extract_salary_data(uploaded_file)
                data.extend(findunique(data,op,fileName))

            elif fileName.endswith(".docx"):
                op = extract_text_from_docx(uploaded_file)
                data.extend(findunique(data,op,fileName))
            # filesList.append(fileName)
        df = pd.DataFrame(data)
        excel_file = 'employee_info.xlsx'
        df.to_excel(excel_file,index=False)
        fh = open(excel_file,'rb')
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename='+excel_file
        fh.close()
        return response   
    return render(request, 'process_salary_slip.html')

def process_excel