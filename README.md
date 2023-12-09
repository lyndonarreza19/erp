# erp
This repository houses the source code for our comprehensive Enterprise Resource Planning (ERP) system. Our ERP system aims to streamline and integrate key business processes, including finance, human resources, inventory management, and more. Developed collaboratively using GitHub, this repository serves as the central hub for our team's efforts.
# Django ERP Project

Welcome to the Django ERP project! This web application leverages the Django framework to provide a comprehensive Enterprise Resource Planning (ERP) system.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Django Web Framework:** The project is built on the Django web framework, providing a robust foundation for building ERP applications.
- **Django REST Framework:** Utilizes Django REST framework for developing Web APIs to support your ERP functionalities.
- **Django Packages:**
  - `django-crispy-forms`: Simplifies form rendering in Django.
  - `django-filter`: Adds easy-to-use filtering capabilities to Django.
  - `django-guardian`: Implements per-object permissions in Django.
  - `django-widget-tweaks`: Enhances form widget rendering in Django.
- **Other Dependencies:**
  - `asgiref`: ASGI reference implementation.
  - `Pillow`: Imaging library for Python.
  - `pytz`: Python library for handling time zones.
  - `sqlparse`: SQL parsing library for Python.
  - `typing_extensions`: Backport of the standard library typing module.
  - `tzdata`: Time zone data for Python.

## Installation
1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/lyndonarreza19/erp.git


##activate virtualenv
python -m venv env
.\env\Scripts\activate   # On Windows
source env/bin/activate  # On macOS/Linux

pip install -r requirements.txt

python manage.py migrate

Visit http://localhost:8000/ in your web browser.

Dependencies
asgiref==3.7.2
Django==4.2.3
django-crispy-forms==2.0
django-filter==23.2
django-guardian==2.4.0
django-widget-tweaks==1.4.12
djangorestframework==3.14.0
Pillow==10.0.0
pytz==2023.3
sqlparse==0.4.4
typing_extensions==4.7.1
tzdata==2023.3

