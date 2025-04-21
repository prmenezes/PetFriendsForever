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
   
# Roadmap (If I had all the time in the world to work on PFF)

1.	 - [ ] Display All Adoptable Pets
•	 - [ ] List only available Pets 
•	 - [ ] Detail Information of the Pets
•	 - [ ] Display one or more photos of the pets
•	 - [ ] Admin support to manage pets i.e. add/delete/edit pet details
2.	 - [ ] Filter Available Pets by Type
•	 - [ ] List only pets type user is interested in 
•	 - [ ] List pets by breed
•	 - [ ] List pets by age 
•	 - [ ] Sort pets by name
•	 - [ ] Sort pets by age
3.	 - [ ] Book an Appointment
•	 - [ ] Create a user information form 
i.	 - [ ] First Name, Last Name
ii.	 - [ ] Phone Number
iii.	 - [ ] Email Address
iv.	 - [ ] Address
v.	 - [ ] Interested species
vi.	 - [ ] Interested pets (Select upto 3 pets)
vii.	 - [ ] First time owner radio button 
viii.	 - [ ] Select appointment slot
ix.	 - [ ] Select appointment reason
x.	 - [ ] ID Proof number
xi.	 - [ ] ID Proof upload
xii.	 - [ ] Submit form
•	 - [ ] Reschedule an appointment (Needs #10 for implementation)
•	 - [ ] Delete an appointment (Needs #10 for implementation)
 - [ ] 
4.	 - [ ] Validate user forms
•	 - [ ] Strict validation for each of the above fields
5.	 - [ ] Walk-In information
6.	 - [ ] Adoption process information
•	 - [ ] Info on the process
•	 - [ ] Fees for each category
•	 - [ ] Additional procedure fees
7.	 - [ ] About us
•	 - [ ] Info about the organization
•	 - [ ] Contact information
•	 - [ ] Hours of operation
8.	 - [ ] Search functionality
•	 - [ ] Search by name
•	 - [ ] Search by breed
9.	 - [ ] Templates – Styling pages using bootstrap
•	 - [ ] Theme – Bright colors
•	 - [ ] Home page – Welcome
•	 - [ ] Navigation bar
•	 - [ ] Links to Adoptable animals and filters
•	 - [ ] Make pages responsive
•	 - [ ] Paginate listings
10.	 - [ ] User authentication and Authorization
11.	 - [ ] Create Staff User and Permissions
12.	 - [ ] Pet shop
13.	 - [ ] Per services
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


  
