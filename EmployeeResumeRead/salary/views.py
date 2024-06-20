 
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
# from .pdfread import extract_salary_data,extract_text_from_docx
import pandas as pd
import re
import time

#****************************
import re
import tempfile
import pdfplumber
from . import docx_custom
import pandas as pd
import asyncio

def extract_phone(data):
    pattern = r"(?:\+\d{1,3}\s?)?\d{10}"
    if not isinstance(data, list):
        data = data.split('\n')
    for line in data:
        match = re.findall(pattern, line)
        if match:
            return match[0]
    return None

def extract_email(data):
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if not isinstance(data, list):
        data = data.split("\n")
    for line in data:
        match = re.findall(email_pattern, line)
        if match:
            return match[0]
    return None

def name_from_email(data):
    email = extract_email(data)
    if email:
        ls = email.split("@")
        namee = re.sub(r'\d', "", ls[0])
        return namee
    return None

def name_line1(data):
    if not isinstance(data, list):
        data = data.split("\n")
    return data[0][:20] if len(data) > 0 else "NA"

def name_line2(data):
    if not isinstance(data, list):
        data = data.split("\n")
    return data[1][:20] if len(data) > 1 else "NA"

async def extract_salary_data(uploaded_file):
    salary_data = []
    
    # Create a temporary file and write the uploaded file content to it
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
    
    # Use pdfplumber to open and process the temporary file
    with pdfplumber.open(temp_file_path) as pdf:
        page = pdf.pages[0]  # Assuming data is on the first page
        text = page.extract_text()
        phone = extract_phone(text)
        email = extract_email(text)
        nameemail = name_from_email(text)
        nameline1 = name_line1(text)
        nameline2 = name_line2(text)

        salary_data.append({
            "Name_from_Email": nameemail,
            "Name_Line1": nameline1,
            "Name_Line2": nameline2,
            'Phone_Number': phone,
            'Email_id': email
        })
    
    return salary_data

async def extract_text_from_docx(file):
    doc = docx_custom.opendocx(file)
    data = docx_custom.getdocumenttext(doc)
    phone = extract_phone(data)
    email = extract_email(data)
    nameemail = name_from_email(data)
    nameline1 = name_line1(data)
    nameline2 = name_line2(data)

    salary_data = [{
        "Name_from_Email": nameemail,
        "Name_Line1": nameline1,
        "Name_Line2": nameline2,
        'Phone_Number': phone,
        'Email_id': email
    }]
    return salary_data
#*******************************














def NameFile(file):
    match = re.search(r'_(.*?)\[\d+y_\d+m\]', file)
    if match:
        return match.group(1)
    else:
        return file
duplicates_count = 0
def findunique(ls,op,file):
    global duplicates_count
    op[0].setdefault("NamefromFile",NameFile(file))
    if ls is not None:
        for i in ls:
            if i['Email_id'] == op[0]['Email_id']:
               duplicates_count +=1
               return []
    return op
'''
def process_salary(request):
    if request.method == 'POST':
        uploaded_files =  request.FILES.getlist('files')
        data = []
        dfs = []
        count= 1

        # subrecords = None
        # cont = len(uploaded_files)
        # parts = cont//50
        # start = 0
        # end = 50
        # for i in range(parts):
        #     subrecords =uploaded_files[start:end]
        for uploaded_file in uploaded_files:   
            # import pdb; pdb.set_trace()
            print(count)
            count+=1
            fileName = uploaded_file.name
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
            #     subrecords.remove(uploaded_file)
            #     # filesList.append(fileName)
            # while subrecords:
            #     print("sleep")
            #     print(len(subr))
            #     time.sleep(2)
            # start = end
            # end += 50
            # if end > parts:
            #     end = parts
'''
import asyncio
import pandas as pd

async def process_file(uploaded_file, data, dfs):
    fileName = uploaded_file.name
    if fileName.endswith(".pdf"):
        op = await extract_salary_data(uploaded_file)
        data.extend(findunique(data, op, fileName))

    elif fileName.endswith(".docx"):
        op = await extract_text_from_docx(uploaded_file)
        data.extend(findunique(data, op, fileName))

    elif fileName.endswith(".xlsx"):
        df = await read_excel(uploaded_file)
        dfs.append(df)

async def read_excel(file):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, pd.read_excel, file)

async def process_salary(request):
    if request.method == 'POST':
        uploaded_files =  request.FILES.getlist('files')
        data = []
        dfs = []
        tasks = []
        count = 0

        for uploaded_file in uploaded_files:
            print(count)
            count += 1
            tasks.append(process_file(uploaded_file, data, dfs))

        await asyncio.gather(*tasks)
        # return data, dfs


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
            with open(excel_file,'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename='+excel_file
                global duplicates_count
                print('duplicates',duplicates_count)
                duplicates_count = 0
                return response   
        except FileNotFoundError as fe:
            return HttpResponse("Please choose atleast one file......!!")
        except Exception as e:
            print(f"An error occurred: {e}")
    return render(request, 'temp2.html')
 