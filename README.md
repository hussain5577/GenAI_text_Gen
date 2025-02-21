# Building a Generative AI API with Django Rest Framework
## This tutorial will guide you through creating a RESTful API that serves AI-generated text using Django Rest Framework (DRF) and a pre-trained language model.
### Prerequisites

#### Python 3.8+
#### Basic understanding of Python and Django
#### Familiarity with REST APIs
#### pip (Python package manager)

# Project Setup
## First, let's create a new Django project and install the required dependencies.
#### Create a new virtual environment
#### python -m venv env
#### source env/bin/activate  # On Windows, use: env\Scripts\activate
When we install a virtual environment, the activation script sometimes fails to work, and we encounter an error. 
We can activate it either through the Command Prompt (CMD) or by setting the command in the terminal of Visual Studio. 
Visual Studio has its own terminal where this can be done
######  " Set-ExecutionPolicy RemoteSigned -Scope Process "

# Install required packages
##### pip install django djangorestframework transformers torch
##### Create a new Django project and app:
##### bashCopydjango-admin startproject ai_api_project
##### cd ai_api_project
##### python manage.py startapp text_generator
