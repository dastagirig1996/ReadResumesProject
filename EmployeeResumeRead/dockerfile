FROM python:3.10-bullseye
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "EmployeeSalary.wsgi:application"]