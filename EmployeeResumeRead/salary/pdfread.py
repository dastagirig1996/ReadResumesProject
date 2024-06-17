import pdfplumber
import re
import docx

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

    doc = docx.opendocx(file)
    data = docx.getdocumenttext(doc)
     
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
