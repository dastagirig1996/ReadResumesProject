
'''
import pdfplumber
import re
from . import docx_custom

def extract_phone(data):
    pattern = r"(?:\+\d{1,3}\s?)?\d{10}"
    if not isinstance(data,list):
        data = data.split('\n')
    for line in data:
        match = re.findall(pattern, line)
        if match:
            phone = match[0]
            break
        else:
            phone = None
    return phone

def extract_email(data):
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if not isinstance(data,list):
        data = data.split("\n")
    for line in data:
        match = re.findall(email_pattern, line)
        if match:
            email = match[0]
            break
        else:
            email = None 
    return email
def nameFromEmail(data):
    email = extract_email(data)
    try:
        ls = email.split("@")
        namee = re.sub(r'\d',"",ls[0])
        return namee
    except:
        return None
def nameLine1(data):
        try:
            if not isinstance(data,list):
                data = data.split("\n")
            names = data[0][:20]
            return names
        except:
            return "NA"

def nameLine2(data):
        try:
            if not isinstance(data,list):
                data = data.split("\n")
            names = data[1][:20]
            return names
        except:
            return "NA"




def extract_salary_data(pdf_path):
    salary_data = []
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]  # Assuming data is on the first page
        text = page.extract_text()
        phone = extract_phone(text)
        email = extract_email(text)
        nameemail = nameFromEmail(text)
        nameline1 = nameLine1(text)
        nameline2 = nameLine2(text)

        salary_data.append({
        "Name_from_Email":nameemail,
        "Name_Line1":nameline1,
        "Name_Line2":nameline2,
        'Phone_Number' : phone,
        'Email_id': email
        
           })
    return salary_data

def extract_text_from_docx(file):
    salary_data = []
    
    doc = docx_custom.opendocx(file)
    data = docx_custom.getdocumenttext(doc)
     
    phone = extract_phone(data)
    email = extract_email(data)
    nameemail = nameFromEmail(data)
    nameline1 = nameLine1(data)
    nameline2 = nameLine2(data)

    salary_data.append({
    "Name_from_Email":nameemail,
    "Name_Line1":nameline1,
    "Name_Line2":nameline2,
    'Phone_Number' : phone,
    'Email_id': email
    
    
        })

    return salary_data
'''


import asyncio
import aiofiles
import re
import pdfplumber
from . import docx_custom

async def extract_phone(data):
    pattern = r"(?:\+\d{1,3}\s?)?\d{10}"
    if not isinstance(data, list):
        data = data.split('\n')
    for line in data:
        match = re.findall(pattern, line)
        if match:
            return match[0]
    return None

async def extract_email(data):
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    if not isinstance(data, list):
        data = data.split("\n")
    for line in data:
        match = re.findall(email_pattern, line)
        if match:
            return match[0]
    return None

async def name_from_email(data):
    email = await extract_email(data)
    if email:
        ls = email.split("@")
        namee = re.sub(r'\d', "", ls[0])
        return namee
    return None

async def name_line1(data):
    if not isinstance(data, list):
        data = data.split("\n")
    return data[0][:20] if len(data) > 0 else "NA"

async def name_line2(data):
    if not isinstance(data, list):
        data = data.split("\n")
    return data[1][:20] if len(data) > 1 else "NA"

async def extract_salary_data(pdf_path):
    async with aiofiles.open(pdf_path, 'rb') as f:
        async with pdfplumber.open(f) as pdf:
            page = pdf.pages[0]  # Assuming data is on the first page
            text = page.extract_text()
            phone = await extract_phone(text)
            email = await extract_email(text)
            nameemail = await name_from_email(text)
            nameline1 = await name_line1(text)
            nameline2 = await name_line2(text)

            salary_data = [{
                "Name_from_Email": nameemail,
                "Name_Line1": nameline1,
                "Name_Line2": nameline2,
                'Phone_Number': phone,
                'Email_id': email
            }]
    return salary_data

async def extract_text_from_docx(file):
    doc = docx_custom.opendocx(file)
    data = docx_custom.getdocumenttext(doc)
    phone = await extract_phone(data)
    email = await extract_email(data)
    nameemail = await name_from_email(data)
    nameline1 = await name_line1(data)
    nameline2 = await name_line2(data)

    salary_data = [{
        "Name_from_Email": nameemail,
        "Name_Line1": nameline1,
        "Name_Line2": nameline2,
        'Phone_Number': phone,
        'Email_id': email
    }]
    return salary_data
