
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from .pdfread import extract_salary_data,extract_text_from_docx
import pandas as pd
import re

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
        dfs = []
        for uploaded_file in uploaded_files:    
            # import pdb; pdb.set_trace()
            fileName = uploaded_file.name
            print(fileName)
            if fileName.endswith(".pdf"):
                op = extract_salary_data(uploaded_file)
                data.extend(findunique(data,op,fileName))

            elif fileName.endswith(".docx"):
                op = extract_text_from_docx(uploaded_file)
                data.extend(findunique(data,op,fileName))
    
            elif fileName.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
                # import pdb; pdb.set_trace()
                dfs.append(df)
            # filesList.append(fileName)
        excel_file = 'empty.xlsx'
        try:
            if data:
                df = pd.DataFrame(data)
                excel_file = 'employee_resumes_data.xlsx'
                df.to_excel(excel_file,index=False)
            elif dfs:
                merged_df = pd.concat(dfs,ignore_index=True)
                merged_df = merged_df.drop_duplicates(subset = ['Email_id'])
                excel_file = 'merged_excels.xlsx'
                merged_df.to_excel(excel_file,index=False)
            fh = open(excel_file,'rb')
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename='+excel_file
            fh.close()
            return response   
        except FileNotFoundError as fe:
            return HttpResponse("Please choose atleast one file......!!")
    return render(request, 'temp2.html')
