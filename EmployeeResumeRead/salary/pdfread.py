# import pdfplumber
# import re
# from . import docx_custom
# import tempfile
# from . import docx_custom
# import pandas as pd
# import asyncio
# technologies = ['databricks', 'JUnit', 'cucumber', 'vue', 'nunit', 'windows', 'cocoa touch', 'Prometheus', 'user experience (ux) design', 'Postman', 'zend', 'azure data services', 'restful apis', 'jasmine', 'rollup', 'microsoft dynamics', 'github actions', 'nuget', 'arcore', 'hyperledger', 'tensorflow', 'Ansible', 'TestRail', 'boto3', 'Burp Suite', 'Gatling', 'parcel', 'Git', 'adobe xd', 'php', 'ant', 
# 'shiny', 'jenkins', 'teamcity', 'caret', 'dapp development', 'jakarta ee', 'salesforce', 'MongoDB', 'user interface (ui) design', 
# 'scrapy', 'cypress', 'symfony', 'terraform', 'tdd', 'github', 'embedded c', 'httpx', 'gitlab ci', 'owasp', 'codeception', 'JSON', 
# 'vue-router', 'minitest', 'Metasploit', 'dask', 'solidity', 'apache kafka', 'vmware', 'Bitbucket', 'sklearn', 'next.js', 'MITRE ATT&CK', 'struts', 'cassandra', 'r', 'google cloud platformgcp', 'twisted', 'prometheus', 'sqlalchemy', 'stylelint', 'puppet', 'angular', 'Tableau Bridge', 'scrum', 'Babel', 'postman', 'Jenkins', 'aws', 'identitynow', 'gitlab ci/cd', 'Puppet', 'beego', 'asyncio', 'macos', 'cakephp', 'tornado', 'dns', 'rust', 'vue.js', 'virtualbox', 'grunt', 'hiveql', 'sails.js', 'mongodb', 'seaborn','iot' 
# , 'jquery', 'react.js', 'power bi desktop', 'apex', 'file system', 'selenium', 'VMware', 'Azure', 'Cucumber', 'salesforce dx', 'xctest', 'tox', 'dash', 'jquerypython', 'svelte', 'quick', 'figma', 'kitura', 'nimble', 'salesforce service cloud', 'OSINT', 'oculus sdk', 'ios', 'travis ci', 'flutter', 'tornadoexpress.js', 'togaf', 'click', 'devops', 'eslint', 'react', 'kotlin', 'jest', 'dplyr', 'powershell', 'Tableau Online', 'elasticsearch', 'perl', 'dynamodb', 'phpunit', 'observer', 'GitLab', 'fabric', 'VirtualBox', 'intellij idea', 'LoadRunner', 'sonarqube', 'airflow', 'gradle', 'mariadb', 'pydantic', 'new relic', 'mstest', 'fastapi', 'rabbitmq', 'sinatra', 'nagios', 'drupal', 'typescript', 'catboost', 'archimate', 'zoho crm', 'Chef', 'visual studio code', 'hive', 'java', 'html/css', 'graphql', 'sap', 'penetration testing', 'hibernate', 'eclipse', 'swift', 'angular.js', 'arduino', 'machine learning', 'phoenix', 'c', 'usability testing', 'gin', 'Nagios', 'gensim', 'bootstrap', 'scipy', 'oracle enterprise manager', 'kafka', 'lxml', 'NIST Cybersecurity Framework', 'tableau', 'raspberry pi', 'Nmap', 'requests', 'enterprise service bus', 'test-driven development', 'vapor', 'scikit-learn', 'actix', 'msbuild', 'json', 'Windows Server', 'nosql', 'mocha', 'strategy', 'android sdk', 'hubspot', 'Linux', 'redux', 'spring', 'behat', 'hadoop', 'power bi', 'helm', 'matlab', 'waterfall', 'entity framework', 'unreal engine', 'oracle sql developer', 'big data analytics', 'html', 'log4net', 'echo', 'AWS Security', 'elixirmysql', 'SQL databases', 'Node.js', 'ansible', 'REST Assured', 'apache commons', 'amazon web services', 'git', 'JIRA', 'Zabbix', 'CircleCI', 'log4j', 'gcp', 'testng', 'heroku', 'objective-c', 'qiskit', 'deep learning', 'sql', 'Selenium', 'spark', 'Excel', 'luigi', 'pyspark', 'pytz', 
# 'load balancing', 'meteor', 'numpy', 'firebase', 'datadog', 'javascript', 'Mocha', 'urllib3', 'rails', 'nhibernate', 'GCP', 'storm', 'yii', 'jupyter', 'textblob', 'joomla', 'TestNG', 'maven', 'soap', 'flask', 'React.js', 'gitlab', 'nestjs', 'unity', 'jsf', 'Cypress', 'argparse', 'ruby on rails', 'linux', 'azure', 'salesforce crm', 'asp.net', 'adapter', 'GitHub Actions', 'espresso', 'PowerShell', 'couchdbdjango', 'ktor', 'bitbucket', 'node.js', 'azure devops', 'unit testing', '.net', 'bamboo', 'Express.js', 'unittest', 'pandas', 'ui-ux', 'android studio', 'junit', 'cobol', 'gogo', 'encryption', 'power automate', 'openshift', 'randomforest', 'vuex', 'FI/CO', 'SAP ERP', 'factory', 'azure logic apps', 'esb', 'SAP BW/4HANA', 'asp.net core', 'postgresql', 'redis', 'apache camel', 'Tableau Server', 'identityiq', 'lightgbm', 'python', 'xgboost', 'ggplot2', 'vue-cli', 'android', 'pillow', 'peewee', 'hyper-v', 'interplanetary', 'hbase', 'pyramid', 'sketch', 'swiftui', 'codeigniter', 'AWS', 'network security', 'oracle erp', 'xcode', 'proto.io', 'GCP Security', 'axure', 'Wireshark', 'Tableau Desktop', 'GitHub', 'specflow', 'web services', 'gulp', 'rocket', 'ethereum', 'bokeh', 'guava', 'CSV', 'sql server', 'slf4j', 'visualforce', 'microsoft q#', 'ros', 'sqlite', 'JMeter', 'HANA', 'Azure Security', 'Travis CI', 'keras', 'Enzyme', 'Shell scripting', 'oracle database', 'Kali Linux', 'circleci', 'SAP Fiori', 'karma', 'pytest', 'padrino', 'plotly', 'docker', 'mockito', 'web2py', 'Webpack', 'agile', 'blazor', 'mysql', 'spring boot', 'saltstack', 'flink', 'kanban', 'activemq', 'react native', 'micronaut', 'elk stack', 'Hyper-V', 'Chai', 'css', 'integration testing', 'tcp/ip', 'ruby', 'Tableau Prep', 'hanami', 'bash', 'xunit', 'nuxt.js', 'webpack', 'aiohttp', 'c#', 'jshint', 'Google Sheets', 'jira', 'ABAP', 'statsmodels', 'pl/sql', 'wordpress', 'arkit', 'pony orm', 'pytorch', 'scala', 'beautifulsoup', 'c++', 'http/https', 'vaadin', 'fortran', 'javaserver faces', 'microservices', 'robot operating system', 'singleton', 'spacy', 'opencv', 'kubeflow', 'tailwind css', 
# 'salesforce cloud', 'kubernetes', 'SAP S/4HANA', 'serilog', 'smart contracts', 'dapper', 'chef', 'celery', 'nose', 'grafana', 'mlflow', 'power bi service', 'Jest', 'hypothesis', 'invision', 'google cloud', 'ipfs', 'bottle', 'laravel', 'express.js', 'vagrant', 
# 'excel', 'pig', 'xml', 'cocos2d', 'mobx', 'splunk', 'django', 'nltk', 'oracle', 'matplotlib', 'django orm', 'play', 'salesforce lightning', 'rspec']


# #****************************

# def extract_info(data):
#     dic = {}
#     dic["Phone_Number"]=None
#     dic["Email_id"]=None
#     dic["Name_from_Email"]=None

#     phone_pattern = r"(?:\+\d{1,3}\s?)?\d{10}"
#     email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
#     designation_pattern = r"(designation|role|position|title)\s*:\s*(\w+)"
#     experience_pattern =r'\b(\d+(?:\.\d+)?\+?)\s+years'
#     clients_pattern = r"(organization|company|employer|clients|client|projects|worked for)\s*:\s*(.+)"
#     skills_pattern = r'\b(?:' + '|'.join(map(re.escape, technologies)) + r')\b'


#     phone_flag = False
#     email_flag = False
#     design_flag = False
#     exp_flag = False
    
#     clients = []
#     skills = set()
#     if not isinstance(data, list):
#         data = data.split('\n')
#         name_line1 = data[0][:20] if len(data) > 0 else "NA"
#         name_line2 = data[1][:20] if len(data) > 1 else "NA"
#         dic["Name_Line1"] = name_line1
#         dic["Name_Line2"] = name_line2

#     for line in data:
#         if not phone_flag:
#            phone_match = re.findall(phone_pattern, line)
#            if phone_match:
#                 dic["Phone_Number"]=phone_match[0]  
#                 phone_flag = True

#         if not email_flag:
#             email_match = re.findall(email_pattern, line)
#             if email_match:
#                 email = email_match[0]
#                 dic["Email_id"] = email
#                 ls = email.split("@")
#                 name = re.sub(r'\d', "", ls[0])
#                 dic["Name_from_Email"] = name
#                 email_flag = True

#         if not design_flag:
#             design_match = re.search(designation_pattern, line, re.IGNORECASE)
#             if design_match:
#                 dic["Designation"]=design_match[0] 
#                 design_flag = True

#         if not exp_flag:
#            exp_match = re.search(experience_pattern, line, re.IGNORECASE)
#            if exp_match:
#                 dic["Experience"]=exp_match[0]  
#                 exp_flag = True

        
#         client_match = re.findall(clients_pattern, line, re.IGNORECASE)
#         if client_match:
#             clients.append(client_match[0])
#             # exp_flag = True
        
#         # if not exp_flag:
#         skills_match = re.findall(skills_pattern, line, re.IGNORECASE)
#         if skills_match:
#             skills.add(skills_match[0])
#     if clients:
#         dic["Clients"] = clients
#     else:
#         dic["Clients"] = None
#     dic["skills"] = list(skills)
#     return dic
 
 
# '''

# def extract_desig(data):
#     designation_pattern = r"(designation|role|position|title)\s*:\s*(\w+)"
#     if not isinstance(data, list):
#         data = data.split('\n')
#     for line in data:
#         match = re.search(designation_pattern, line, re.IGNORECASE)
#         if match:
#             return match.group(2)
#     return None
 
# def extract_years_of_experience(data):
#     experience_pattern = r"(\d+(?:\.\d+)?)\s*(years|yrs|year|yr)"
#     if not isinstance(data, list):
#         data = data.split('\n')
#     for line in data:
#         match = re.search(experience_pattern, line.lower())
#         if match:
#             return match.group(1)
#     return None
 
# def extract_previous_clients(data):
#     clients_pattern = r"(organization|company|employer|clients|client|projects|worked for)\s*:\s*(.+)"
#     if not isinstance(data, list):
#         data = data.split('\n')
#     for line in data:
#         match = re.search(clients_pattern, line.lower(), re.IGNORECASE)
#         if match:
#             return match.group(2)
#     return None
 
#     return 
   
# '''





# async def extract_pdf_data(uploaded_file):
#     salary_data = []
#     # Create a temporary file and write the uploaded file content to it
#     with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#         temp_file.write(uploaded_file.read())
#         temp_file_path = temp_file.name
#     # Use pdfplumber to open and process the temporary file
#     with pdfplumber.open(temp_file_path) as pdf:
#         page = pdf.pages[0]  # Assuming data is on the first page
#         text = page.extract_text()
#         extract_dic = extract_info(text)
#         salary_data.append(extract_dic)
#     return salary_data

# async def extract_text_from_docx(file):
#     doc = docx_custom.opendocx(file)
#     data = docx_custom.getdocumenttext(doc)
#     extract_dic = extract_info(data)
#     salary_data = [extract_dic]
#     return salary_data


# #****************************




import pdfplumber
import re
from . import docx_custom
import tempfile
from . import docx_custom
import win32com.client
import pythoncom

technologies = ['databricks', 'JUnit', 'cucumber', 'vue', 'nunit', 'windows', 'cocoa touch', 'Prometheus', 'user experience (ux) design', 'Postman', 'zend', 'azure data services', 'restful apis', 'jasmine', 'rollup', 'microsoft dynamics', 'github actions', 'nuget', 'arcore', 'hyperledger', 'tensorflow', 'Ansible', 'TestRail', 'boto3', 'Burp Suite', 'Gatling', 'parcel', 'Git', 'adobe xd', 'php', 'ant', 
'shiny', 'jenkins', 'teamcity', 'caret', 'dapp development', 'jakarta ee', 'salesforce', 'MongoDB', 'user interface (ui) design', 
'scrapy', 'cypress', 'symfony', 'terraform', 'tdd', 'github', 'embedded c', 'httpx', 'gitlab ci', 'owasp', 'codeception', 'JSON', 
'vue-router', 'minitest', 'Metasploit', 'dask', 'solidity', 'apache kafka', 'vmware', 'Bitbucket', 'sklearn', 'next.js', 'MITRE ATT&CK', 'struts', 'cassandra', 'r', 'google cloud platformgcp', 'twisted', 'prometheus', 'sqlalchemy', 'stylelint', 'puppet', 'angular', 'Tableau Bridge', 'scrum', 'Babel', 'postman', 'Jenkins', 'aws', 'identitynow', 'gitlab ci/cd', 'Puppet', 'beego', 'asyncio', 'macos', 'cakephp', 'tornado', 'dns', 'rust', 'vue.js', 'virtualbox', 'grunt', 'hiveql', 'sails.js', 'mongodb', 'seaborn','iot' 
, 'jquery', 'react.js', 'power bi desktop', 'apex', 'file system', 'selenium', 'VMware', 'Azure', 'Cucumber', 'salesforce dx', 'xctest', 'tox', 'dash', 'jquerypython', 'svelte', 'quick', 'figma', 'kitura', 'nimble', 'salesforce service cloud', 'OSINT', 'oculus sdk', 'ios', 'travis ci', 'flutter', 'tornadoexpress.js', 'togaf', 'click', 'devops', 'eslint', 'react', 'kotlin', 'jest', 'dplyr', 'powershell', 'Tableau Online', 'elasticsearch', 'perl', 'dynamodb', 'phpunit', 'observer', 'GitLab', 'fabric', 'VirtualBox', 'intellij idea', 'LoadRunner', 'sonarqube', 'airflow', 'gradle', 'mariadb', 'pydantic', 'new relic', 'mstest', 'fastapi', 'rabbitmq', 'sinatra', 'nagios', 'drupal', 'typescript', 'catboost', 'archimate', 'zoho crm', 'Chef', 'visual studio code', 'hive', 'java', 'html/css', 'graphql', 'sap', 'penetration testing', 'hibernate', 'eclipse', 'swift', 'angular.js', 'arduino', 'machine learning', 'phoenix', 'c', 'usability testing', 'gin', 'Nagios', 'gensim', 'bootstrap', 'scipy', 'oracle enterprise manager', 'kafka', 'lxml', 'NIST Cybersecurity Framework', 'tableau', 'raspberry pi', 'Nmap', 'requests', 'enterprise service bus', 'test-driven development', 'vapor', 'scikit-learn', 'actix', 'msbuild', 'json', 'Windows Server', 'nosql', 'mocha', 'strategy', 'android sdk', 'hubspot', 'Linux', 'redux', 'spring', 'behat', 'hadoop', 'power bi', 'helm', 'matlab', 'waterfall', 'entity framework', 'unreal engine', 'oracle sql developer', 'big data analytics', 'html', 'log4net', 'echo', 'AWS Security', 'elixirmysql', 'SQL databases', 'Node.js', 'ansible', 'REST Assured', 'apache commons', 'amazon web services', 'git', 'JIRA', 'Zabbix', 'CircleCI', 'log4j', 'gcp', 'testng', 'heroku', 'objective-c', 'qiskit', 'deep learning', 'sql', 'Selenium', 'spark', 'Excel', 'luigi', 'pyspark', 'pytz', 
'load balancing', 'meteor', 'numpy', 'firebase', 'datadog', 'javascript', 'Mocha', 'urllib3', 'rails', 'nhibernate', 'GCP', 'storm', 'yii', 'jupyter', 'textblob', 'joomla', 'TestNG', 'maven', 'soap', 'flask', 'React.js', 'gitlab', 'nestjs', 'unity', 'jsf', 'Cypress', 'argparse', 'ruby on rails', 'linux', 'azure', 'salesforce crm', 'asp.net', 'adapter', 'GitHub Actions', 'espresso', 'PowerShell', 'couchdbdjango', 'ktor', 'bitbucket', 'node.js', 'azure devops', 'unit testing', '.net', 'bamboo', 'Express.js', 'unittest', 'pandas', 'ui-ux', 'android studio', 'junit', 'cobol', 'gogo', 'encryption', 'power automate', 'openshift', 'randomforest', 'vuex', 'FI/CO', 'SAP ERP', 'factory', 'azure logic apps', 'esb', 'SAP BW/4HANA', 'asp.net core', 'postgresql', 'redis', 'apache camel', 'Tableau Server', 'identityiq', 'lightgbm', 'python', 'xgboost', 'ggplot2', 'vue-cli', 'android', 'pillow', 'peewee', 'hyper-v', 'interplanetary', 'hbase', 'pyramid', 'sketch', 'swiftui', 'codeigniter', 'AWS', 'network security', 'oracle erp', 'xcode', 'proto.io', 'GCP Security', 'axure', 'Wireshark', 'Tableau Desktop', 'GitHub', 'specflow', 'web services', 'gulp', 'rocket', 'ethereum', 'bokeh', 'guava', 'CSV', 'sql server', 'slf4j', 'visualforce', 'microsoft q#', 'ros', 'sqlite', 'JMeter', 'HANA', 'Azure Security', 'Travis CI', 'keras', 'Enzyme', 'Shell scripting', 'oracle database', 'Kali Linux', 'circleci', 'SAP Fiori', 'karma', 'pytest', 'padrino', 'plotly', 'docker', 'mockito', 'web2py', 'Webpack', 'agile', 'blazor', 'mysql', 'spring boot', 'saltstack', 'flink', 'kanban', 'activemq', 'react native', 'micronaut', 'elk stack', 'Hyper-V', 'Chai', 'css', 'integration testing', 'tcp/ip', 'ruby', 'Tableau Prep', 'hanami', 'bash', 'xunit', 'nuxt.js', 'webpack', 'aiohttp', 'c#', 'jshint', 'Google Sheets', 'jira', 'ABAP', 'statsmodels', 'pl/sql', 'wordpress', 'arkit', 'pony orm', 'pytorch', 'scala', 'beautifulsoup', 'c++', 'http/https', 'vaadin', 'fortran', 'javaserver faces', 'microservices', 'robot operating system', 'singleton', 'spacy', 'opencv', 'kubeflow', 'tailwind css', 
'salesforce cloud', 'kubernetes', 'SAP S/4HANA', 'serilog', 'smart contracts', 'dapper', 'chef', 'celery', 'nose', 'grafana', 'mlflow', 'power bi service', 'Jest', 'hypothesis', 'invision', 'google cloud', 'ipfs', 'bottle', 'laravel', 'express.js', 'vagrant', 
'excel', 'pig', 'xml', 'cocos2d', 'mobx', 'splunk', 'django', 'nltk', 'oracle', 'matplotlib', 'django orm', 'play', 'salesforce lightning', 'rspec']


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
    docx = docx_custom.opendocx(file)
    data = docx_custom.getdocumenttext(docx)
    extract_dic = extract_info(data)
    salary_data = [extract_dic]
    return salary_data

async def extract_text_from_docfile(filedata):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(filedata.read())
        temp_file_path = temp_file.name
    filepath = repr(temp_file_path)[1:-1]
    pythoncom.CoInitialize()
    try:
        word = win32com.client.Dispatch("Word.Application")
        doc = word.Documents.Open(filepath)
        content = []
        for paragraph in doc.Paragraphs:
            content.append(paragraph.Range.Text)
        doc.Close()
        word.Quit()
    finally:
        pythoncom.CoUninitialize()
    extract_dic = extract_info(content)
    salary_data = [extract_dic]
    return salary_data






    # extract_dic = extract_info(doc)
    # salary_data = [extract_dic]
    # return salary_data



#****************************