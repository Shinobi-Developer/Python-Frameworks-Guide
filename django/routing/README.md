# Django Routing

This repository contains a Django project with a basic setup for routing. It demonstrates how to define routes and corresponding views in Django.

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine using the following command:

   ```
   git clone https://github.com/Shinobi-Developer/Python-Frameworks-Guide.git
   ```

2. Navigate to the project directory:

   ```
   cd Python-Frameworks-Guide/django/routing
   ```

3. Create a virtual environment to isolate the project's dependencies:

   ```
   python -m venv .venv
   ```
   It will be better to run this command in VS Code terminal.

4. Activate the virtual environment:

   - On macOS and Linux:
     ```
     source env/bin/activate
     ```

   - On Windows:
     ```
     .venv\Scripts\activate
     ```

5. Install Django framework and confirm the version:

   ```
   pip install django  
   ```
   ```
   django-admin --version  
   ```
   
6. Create your project:
   ```
   django-admin startproject yourprojectname
   ```
   
7. Navigate to the project directory and run the server:
   ```
   cd yourprojectname
   ```
   ```
   py manage.py runserver
   ```

## Usage

This Django project demonstrates how to define routes using the `urls.py` file. Here is an example of the defined routes:

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('overview/', views.overview, name='overview'),
]
```

- The root URL (`''`) maps to the `home` view function.
- The `/about/` URL maps to the `about` view function.
- The `/contact/` URL maps to the `contact` view function.

Each view function simply renders a corresponding HTML template.

Feel free to explore the project's code and modify it according to your needs.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions, feel free to contact us at [iris.minami0307@gmail.com](iris.minami0307@gmail.com). We appreciate your feedback!

Happy coding!
