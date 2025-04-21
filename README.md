# Pet Friends Forever**

A pet adoption web app where the user can see details of adorable adoptable pet animals and book an appointment to see them in person.

The website will have a list of adoptable pets with pictures. Users can go through all animal listings or by type, for eg. only dogs or only cats.
The user can click on the listing to see detailed information. On the details page, there will be an option to book at appointment or walk in. Book an appointment will require the user to fill a form with user information, the pet(s) they would like to see and select a date and time. The walk in option will display the contact information and address of the adoption facility.

One or more staff users should be able to create, update, delete the pet listings when a new pet arrives, its details have changed or when the animal has been adopted.

# Framework Used**
The application will use 
1. Django(Python) framework for backend
2. Bootstrap to style the HTML/CSS components for the front end
3. SQLite for database

# How to run the application**
1. Install the virtual enviroment
      python -m env .venv
      source venv/bin/activate
2. Install Django, Pillow
      python -m pip install django
      python -m pip install Pillow
3. Fork the project?
4. Rename .env.example to .env and define your own secret_key
5. Run migrations
      python manage.py makemigrations
      python manage.py migrate
6. Run the app 
      python manage.py runserver
   
# Roadmap (If I had all the time in the world to work on PFF)

1.	 - [x] Display All Adoptable Pets
•	 - [x] List only available Pets 
•	 - [x] Detail Information of the Pets
•	 - [x] Display one or more photos of the pets
•	 - [x] Admin support to manage pets i.e. add/delete/edit pet details
2.	 - [x] Filter Available Pets by Type
•	 - [x] List only pets type user is interested in 
•	 - [ ] List pets by breed
•	 - [ ] List pets by age 
•	 - [ ] Sort pets by name
•	 - [ ] Sort pets by age
3.	 - [x] Book an Appointment
•	 - [x] Create a user information form 
i.	 - [x] First Name, Last Name
ii.	 - [x] Phone Number
iii.- [x] Email Address
iv.	 - [ ] Address
v.	 - [x] Interested species
vi.	 - [ ] Interested pets (Select upto 3 pets)
vii.	 - [x] First time owner radio button 
viii.	 - [x] Select appointment slot
ix.	 - [ ] Select appointment reason
x.	 - [ ] ID Proof number
xi.	 - [ ] ID Proof upload
xii.	 - [x] Submit form
•	 - [ ] Reschedule an appointment (Needs #10 for implementation)
•	 - [ ] Delete an appointment (Needs #10 for implementation
4.	 - [ ] Validate user forms
•	 - [ ] Strict validation for each of the above fields
5.	 - [x] Walk-In information
6.	 - [x] Adoption process information
•	 - [x] Info on the process
•	 - [x] Fees for each category
•	 - [x] Additional procedure fees
7.	 - [] About us
•	 - [ ] Info about the organization
•	 - [x] Contact information
•	 - [x] Hours of operation
8.	 - [x] Search functionality
•	 - [x] Search by name
•	 - [ ] Search by breed
9.	 - [x] Templates – Styling pages using bootstrap
•	 - [x] Theme – Bright colors
•	 - [x] Home page – Welcome
•	 - [x] Navigation bar
•	 - [x] Links to Adoptable animals and filters
•	 - [x] Make pages responsive
•	 - [ ] Paginate listings
10.	 - [ ] User authentication and Authorization
11.	 - [ ] Create Staff User and Permissions
12.	 - [ ] Pet shop
13.	 - [ ] Pet services
14.	 - [ ] Fees calculator – for Staff
•	 - [ ] Add category to each pet to calculate fees easily
15.	 - [ ] User verification 
•	 - [ ] Check box if uploaded ID is verified in person – for Staff
16.	 - [ ]  Wishlist a pet
•	 - [ ] Logged in user should be able to wishlist pets
•	 - [ ] Relogin should show the wishlist
•	 - [ ] Share the list via social media
17.	 - [ ] A custom staff dashboard
18.	 - [ ] Pet age	
•	 - [ ] Have birthday field to calculate age
19.	 - [ ] Favicon for webpages


  
