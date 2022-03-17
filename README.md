[Link to the live site](https://flask-worklists.herokuapp.com/)

**About**

# Internal Call Logging System 
**Scenario**
Below the Hook Ltd (BTH) is a small family run company  with 30 years of experience in the Lifting Industry. The company hires, sells, services and inspects equipment involved in all types of commercial lifting.

**The business goals of this website are:**

Improve the management of day to day business processes by providing an internal web based system to:

 - centrally record and share day to day business information.
 - allocate jobs to members of the team.
 - provide a global company worklist that displays an overview of the current work load.

This project is designed to provide a proof of concept for an Internal Call/Job Logging System that provides colleagues with a tool for recording jobs, creating jobs and allocating them to colleagues who can access them via the global worklist.

***This system will be internal only and will have no SEO considerations.***

**Potential Customers**

 - Construction industry contractors, Steel Fabrication Companies, Lift
   Manufacture and Maintenance Companies.

 - Any companies needing to hire or purchase Lifting or height safety
   equipment in the South Wales area.

 - Companies wishing to improve their businesses workflow.

## Scope

**What a user may expect**

 - Easy and intuitive website navigation.
 - That all links within the site work.
 - Site is understandable and viewable regardless of screen size.
 - Site looks professional and relevant to the businesses operating processes.
 
 **What a user may want**


**The business would expect the site to provide:**

## Structure

The code for the site sits on the **Github** repository hosting service and is deployed through **Heroku**, a cloud platform that allows developers to deploy apps in the cloud. Heroku also links to the **MongoDB** Non relational database, a non SQL document-oriented database that holds the data in collections.
**Mongo DB System Data Model**

![Mongo DB System Data Model](https://starranuk.github.io/dice-game/assets/readme_worklist/MongoDB_data_model.png)



**User Instructions**
There are two types user accounts:
**Normal staff accounts that can:**
 - Create new jobs. 
 - Only edit the jobs they are allocated. 
 - Allocate jobs to colleagues. 
 - View all jobs for all users.
 - View all staff profiles but only see the details of their own.

**The sysadmin account can:**
 - Create user accounts.
 - Edit user accounts.
 - Delete user accounts.
 - Create and delete Job Types and Job Status's.
 - Create and edit all jobs in the Worklist

**Instructions for normal user**

 - Once logged in select the "Worklist" link.
 - This displays the current open jobs.
 - You will be able to view the details of all the current jobs but only edit those allocated to your username.
 - To create a new job select the "New Job" .
 - Enter the relevant information into the fields and set the priority/urgency of the task by selecting the switch at the bottom of the page.
 - The call will automatically be allocated to your username if you don not add the username of a colleague.
 - When editing you can update all fields apart from:
	 - Job Creation Date
	 - Job Created By
	 - Job Type

 **Design**

**Colour list:**
Background #f8f9fa
Font colours:  Black rgb 0, 0, 0
						Blue rgb 0, 0, 255
**Typography**

Although I imported Google Fonts I have mainly used Arial. 

**Call to Action**


### Images

 -No images are utilised on this system

## Site Framework

**Responsive layout**

**Materialize Framework** – for responsive mobile navigation, grid system, date picker and dropdown pickers.

### Wire Frame

**Worklist - All Jobs**
This is the page displayed with the sysadmin account logged in and looking at the All Jobs Worklist
![enter image description here](https://starranuk.github.io/dice-game/assets/readme_worklist/all_jobs_desktop.PNG)

![enter image description here](https://starranuk.github.io/dice-game/assets/readme_worklist/all_jobs_desktop_normal_user.PNG)

![enter image description here](https://starranuk.github.io/dice-game/assets/readme_worklist/add_job_desktop_normal_user.PNG)

![enter image description here](https://starranuk.github.io/dice-game/assets/readme_worklist/all_staff_desktop_normal_user.PNG)

![enter image description here](https://starranuk.github.io/dice-game/assets/readme_worklist/all_jobs_mobile_normal_user.PNG)

![enter image description here](https://starranuk.github.io/dice-game/assets/readme_worklist/add_job_mobile_normal_user.PNG)

## Common Features

**Header**

 - Colours and style match current company branding.
 - A responsive Materialize Navbar  provides standard navigation
   at the top of each page, with the link in the logo linking the user
   back to the home page from all pages.
 - On mobile devices the Navigation dropdown is located in the top right
   hand corner of the screen, when
   selected the text links are appropriately sized.


## Technology Used

 -   **Python**
 -  **Flask** Python web framework.

 - **MongoDB** Non relational database, non SQL document-oriented database

-   **Git** Version control.
-   **Github** Git repository hosting service that Heroku links to.
-   **Heroku**  Cloud Platform that allows developers to deploy apps in the cloud. Important for this project as GitHub can not host Python.
 - **HTML5** – Markup Langauge for structure and functionality.
 - **CSS3** – Cascading Stylsheets for responsiveness and consistant style
   throughout the site.
 - **Materialize Framework** – for responsive navigation, grid system, datepicker, collapsible-body and dropdown.
 - **Javascript and Jquery** - utilised for Materialize
 - **Google Fonts** – for Typography.
 - **GitPod** for code editing, saving commits and pushing versions to
   GitHub.
 - **Git** – version control.
 - **Chrome Developer Tools** – testing page responsiveness.

## Testing

 - Testing uncovered issues with the Job Status dropdown on the Job Edit
   page deleting the selection from the database. Even with support from
   my Mentor and Student Support I was not able to resolve this in time.
   My temporary work around is that they can be updated manually.

**Navigation**

 - All links have been tested.
 

**Responsiveness**

The responsive ranges targeted were:
 - For Desktops 
 - Mobile phones with screen max-width: 414px
 
**Responsiveness Testing**

Testing was initially carried using the Chrome Developer Tools using the responsive ranges listed above. 

Hardware tested ranged from a Motorola G5s, Samsung Galaxy S5, 10" Amazon Kindle Fire Tablet and a widescreen desktop PC.

**Browser Testing**
Browsers used for testing were:

 - Google Chrome - Desktop and Mobile
 - Firefox - Desktop and Mobile
 - Microsoft Edge
 - Amazon Silk

**Performance Testing**
Performance tested against Google Lighthouse Developer Tools which were very useful but only seemed to see the Login Page even when alternative pages were open for the report to be run against.

## Future Features

 - Increase the use of dropdown's and codes
 - Automate some of the call allocation
 - Provide reporting functionality for business information/data
 - Improve support status functionality so that 
 - Technical Support page with FAQ’s and possible chat facility.
 - Add Captcha "I'm not a Robot" Turing test to the Contact form to stop automated phishing.



## User Testing
### Testing - What a user may expect

 
 **Easy and intuitive navigation.**

 - Once the user has logged in they are welcomed on the landing page and will immediately see the the links that they have access to

 **That all links within the site work.**

 - All  links have been tested 

 **Site is understandable and viewable regardless of screen size.**
 
 - The navigation bar automatically converts to a drop down menu when a
   screen reaches tablet size and all pages are accessible and viewable
   in the common mobile formats.

 **Site looks professional and relevant to the product and nature of the
   business.**
 
 - The site will only be used by staff for the purposes of the company and so therefore is not customer/public facing.   

 
### What a user may want

 - To have a good overall view of the workload on the company through
   the Worklist.  This would in turn help with allocating resources.
 - To be able to see at a glance what is urgent.
 - To view individuals workloads. Especially useful if they are out of the office.
 - For colleagues to be able to pass jobs    backwards and forwards
   between each other until they're completion.




#### Code Validation
    
 -   Python code checked and corrected using PEP8 online checker.
 - http://pep8online.com/
    
## Deployment

**Add Commit and Push files**
### DEPLOYMENT

 Follow this link to the current Worklist Repository (https://github.com/starranuk/worklist)

 - Follow the link above to the Worklist repository. 
 - Select the "Code" button and select "Download Zip".
 - Once downloaded extract and upload to your fresh GitHub repository.
 - In your repository terminal  type: pip3 install Flask
 - Create your variable folder in your repository type: touch env.py
 - Type: touch .gitignore this will hold information on what not to copy upto GitHub, i.e. the variables folder.
 - Open .gitignore and add env.py __pycache__/ - this stops these files from being copied upto GitHub.
 - Go to MongoDB.com and open an account.
 - Create a new Cluster (Database) and name it job_worklist
 - Open the env.py file and add the following 
 
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", ">create this secret key yourself")
os.environ.setdefault("MONGO_URI", "mongodb+srv://accountthatyoucreateforthecluster:OUDQSw0BP5oX2Xw3@clustername.extqj.mongodb.net/yourrepositoryname?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "job_worklist")
 
 - Within the database create the collections so that they match the database model illustrated below:

 ![Mongo DB System Data Model](https://starranuk.github.io/dice-game/assets/readme_worklist/MongoDB_data_model.png)


 - Go to Heroku.com and create an account.
 - Create your App and use the Automatic Deployment link to your GitHub repository.
 - Once your GitHub profile is displayed add your repository name and
   click search.
 - Once it finds your repository, click to connect to this app.
 - Select the "Settings" tab for your app, and then click on "Reveal Config Vars"
 - As HeroKu won't be able to see the variables in the env.py file this is where you add them:
 "IP", "0.0.0.0"
"PORT", "5000"
"SECRET_KEY", ">create this secret key yourself"
"MONGO_URI", "mongodb+srv://accountthatyoucreateforthecluster:OUDQSw0BP5oX2Xw3@clustername.extqj.mongodb.net/yourrepositoryname?retryWrites=true&w=majority"
"MONGO_DBNAME", "job_worklist"

 - Run a commit to your repository and then return to HeroKu.
 - Heroku should now be able to see the files in your repository so select 'Enable Automatic Deployment'

## Credits

**Acknowledgements**
The Inspiration for this project was based on the Code Institute  "Data Centric Design mini-project" by Tim Nelson.
 - Brian Macharia- Mentor support, for the advice, tips and guidance.
 - Student Support - Sean and Rebecca
 
  










> Written with [StackEdit](https://stackedit.io/).



