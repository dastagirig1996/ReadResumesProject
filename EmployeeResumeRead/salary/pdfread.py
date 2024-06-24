import pdfplumber
import re
from . import docx_custom
import tempfile
from . import docx_custom
import pandas as pd
import asyncio
technologies = ['ui-ux','jira','.net', 'arcore', 'arkit', 'asp.net', 'aws', 'activemq', 'actix', 'adapter', 'agile', 'amazon web services', 'android', 'angular', 'angular.js', 'ansible', 'apache camel', 'apache kafka', 'archimate', 'arduino', 'azure', 'bamboo', 'bash', 'beego', 'big data analytics', 'bitbucket', 'blazor', 'bootstrap', 'c', 'c#', 'c++', 'cobol', 'css', 'cassandra', 'chef', 'circleci', 'cocos2d', 'codeigniter', 'couchdbdjango', 'dapp development', 'dns', 'datadog', 'deep learning', 'devops', 'django', 'docker', 'drupal', 'dynamodb', 'elk stack', 'esb', 'eslint', 'echo', 'eclipse', 'elasticsearch', 'elixirmysql', 'embedded c', 'encryption', 'enterprise service bus', 'ethereum', 'express.js', 'factory', 'fastapi', 'firebase', 'flask', 'flutter', 'fortran', 'gin', 'git', 'github', 'gitlab', 'gitlab ci/cd', 'google cloud', 'google cloud platformgcp', 'grafana', 'graphql', 'html', 'html/css', 'http/https', 'hadoop','helm', 'hibernate', 'hive', 'hubspot', 'hyper-v', 'hyperledger', 'ipfs', 'integration testing', 'intellij idea', 'interplanetary', 'file system', 'iot platforms', 'jsf', 'jshint', 'json', 'junit', 'java', 'javascript', 'javaserver faces', 'jenkins', 'joomla', 'kanban', 'kitura', 'kotlin', 'ktor', 'kubernetes', 'laravel', 'linux', 'load balancing', 'matlab', 'machine learning', 'mariadb', 'meteor', 'microservices', 'microsoft dynamics', 'microsoft q#', 'mongodb', 'mysql', 'nunit', 'nagios', 'nestjs', 'network security', 'new relic', 'next.js', 'nosql', 'node.js', 'nuxt.js', 'owasp', 'observer', 'oculus sdk', 'openshift', 'oracle', 'oracle database', 'oracle erp', 'php', 'pl/sql', 'penetration testing', 'perl', 'phoenix', 'pig', 'postgresql', 'postman', 'power bi', 'powershell', 'prometheus', 'puppet', 'pytorch', 'pyramid', 'python', 'qiskit', 'r', 'restful apis', 'ros', 'rabbitmq', 'raspberry pi', 'react', 'react native', 'react.js', 'redis', 'robot operating system', 'rocket', 'ruby', 'ruby on rails', 'rust', 'sap', 'soap', 'sql', 'sql server', 'sqlite', 'sails.js', 'salesforce', 'saltstack', 'scala', 'scikit-learn', 'scrum', 'selenium', 'sinatra', 'singleton', 'smart contracts', 'solidity', 'sonarqube', 'spark', 'splunk', 'spring', 'strategy', 'struts', 'stylelint', 'svelte', 'swift', 'symfony', 'tcp/ip', 'tdd', 'togaf', 'tableau', 'tailwind css', 'tensorflow', 'terraform', 'test-driven development', 'tornadoexpress.js', 'travis ci', 'typescript', 'unit testing', 'unity', 'unreal engine', 'usability testing', 'user experience (ux) design', 'user interface (ui) design', 'vmware', 'vagrant', 'vapor', 'virtualbox', 'visual studio code', 'vue.js', 'waterfall', 'web services', 'windows', 'wordpress', 'xml', 'xcode', 'zend', 'zoho crm', 'gogo', 'ios', 'jquery', 'jquerypython', 'macos']


#****************************

def extract_info(data):
    dic = {}
    dic["Phone_Number"]=None
    dic["Email_id"]=None
    dic["Name_from_Email"]=None

    phone_pattern = r"(?:\+\d{1,3}\s?)?\d{10}"
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    designation_pattern = r"(designation|role|position|title)\s*:\s*(\w+)"
    experience_pattern =r'\b(\d+(?:\.\d+)?\+?)\s+years'
    clients_pattern = r"(organization|company|employer|clients|client|projects|worked for)\s*:\s*(.+)"
    skills_pattern = r'\b(?:' + '|'.join(map(re.escape, technologies)) + r')\b'


    phone_flag = False
    email_flag = False
    design_flag = False
    exp_flag = False
    
    clients = []
    skills = set()
    if not isinstance(data, list):
        data = data.split('\n')
        name_line1 = data[0][:20] if len(data) > 0 else "NA"
        name_line2 = data[1][:20] if len(data) > 1 else "NA"
        dic["Name_Line1"] = name_line1
        dic["Name_Line2"] = name_line2

    for line in data:
        if not phone_flag:
           phone_match = re.findall(phone_pattern, line)
           if phone_match:
                dic["Phone_Number"]=phone_match[0]  
                phone_flag = True

        if not email_flag:
            email_match = re.findall(email_pattern, line)
            if email_match:
                email = email_match[0]
                dic["Email_id"] = email
                ls = email.split("@")
                name = re.sub(r'\d', "", ls[0])
                dic["Name_from_Email"] = name
                email_flag = True

        if not design_flag:
            design_match = re.search(designation_pattern, line, re.IGNORECASE)
            if design_match:
                dic["Designation"]=design_match[0] 
                design_flag = True

        if not exp_flag:
           exp_match = re.search(experience_pattern, line, re.IGNORECASE)
           if exp_match:
                dic["Experience"]=exp_match[0]  
                exp_flag = True

        
        client_match = re.findall(clients_pattern, line, re.IGNORECASE)
        if client_match:
            clients.append(client_match[0])
            # exp_flag = True
        
        # if not exp_flag:
        skills_match = re.findall(skills_pattern, line, re.IGNORECASE)
        if skills_match:
            skills.add(skills_match[0])
    if clients:
        dic["Clients"] = clients
    else:
        dic["Clients"] = None
    dic["skills"] = list(skills)
    return dic
 
 
'''

def extract_desig(data):
    designation_pattern = r"(designation|role|position|title)\s*:\s*(\w+)"
    if not isinstance(data, list):
        data = data.split('\n')
    for line in data:
        match = re.search(designation_pattern, line, re.IGNORECASE)
        if match:
            return match.group(2)
    return None
 
def extract_years_of_experience(data):
    experience_pattern = r"(\d+(?:\.\d+)?)\s*(years|yrs|year|yr)"
    if not isinstance(data, list):
        data = data.split('\n')
    for line in data:
        match = re.search(experience_pattern, line.lower())
        if match:
            return match.group(1)
    return None
 
def extract_previous_clients(data):
    clients_pattern = r"(organization|company|employer|clients|client|projects|worked for)\s*:\s*(.+)"
    if not isinstance(data, list):
        data = data.split('\n')
    for line in data:
        match = re.search(clients_pattern, line.lower(), re.IGNORECASE)
        if match:
            return match.group(2)
    return None
 
    return 
   
'''





async def extract_pdf_data(uploaded_file):
    salary_data = []
    # Create a temporary file and write the uploaded file content to it
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
    # Use pdfplumber to open and process the temporary file
    with pdfplumber.open(temp_file_path) as pdf:
        page = pdf.pages[0]  # Assuming data is on the first page
        text = page.extract_text()
        extract_dic = extract_info(text)
        salary_data.append(extract_dic)
    return salary_data

async def extract_text_from_docx(file):
    doc = docx_custom.opendocx(file)
    data = docx_custom.getdocumenttext(doc)
    extract_dic = extract_info(data)
    salary_data = [extract_dic]
    return salary_data


#****************************
