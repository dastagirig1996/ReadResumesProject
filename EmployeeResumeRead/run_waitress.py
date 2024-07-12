from waitress import serve
from EmployeeSalary.wsgi import application  # Replace 'myproject' with your actual project name

if __name__ == '__main__':
    serve(application, host='0.0.0.0', port=8888, channel_timeout=3600)  # Timeout in seconds
