**#Pet Friends Forever**

A pet adoption web app where the user can see details of adorable adoptable pet animals and book an appointment to see them in person.

The website will have a list of adoptable pets with pictures. Users can go through all animal listings or by type, for eg. only dogs or only cats.
The user can click on the listing to see detailed information. On the details page, there will be an option to book at appointment or walk in. Book an appointment will require the user to fill a form with user information, the pet(s) they would like to see and select a date and time. The walk in option will display the contact information and address of the adoption facility.

One or more staff users should be able to create, update, delete the pet listings when a new pet arrives, its details have changed or when the animal has been adopted.

**#Framework Used**
The application will use 
1. Django(Python) framework for backend
2. Bootstrap to style the HTML/CSS components for the front end
3. SQLite for database

**#How to run the application**
1. Install the virtual enviroment
   python -m env .venv
2. Install Django, Pillow
   python -m pip install django
   python -m pip install Pillow
3. Fork the project?
4. Rename .env.example to .env and define your own secret_key
4. Run migrations
   python manage.py makemigrations
   python manage.py migrate
5. Run the app 
   python manage.py runserver
   
