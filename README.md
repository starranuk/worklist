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

 **Design**

The design

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

**Navigaation**

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
Performance tested against Google Lighthouse Developer Tools which were very useful but only seemed to see the Login Page even alternative pages were open for the report to be run against.

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

1.  Follow this link to my  [Repository on Github] and open it.
2.  Click  `Clone or Download`.
3.  In the Clone with HTTPs section, click the  `copy`  icon.
4.  In your local IDE open Git Bash.
5.  Change the current working directory to where you want the cloned directory to be made.
6.  Type  `git clone`, and then paste the URL you copied earlier.
7.  Press enter and your local clone will be ready.

#### [](https://github.com/taikatta/Milestone3-Konyvkucko/blob/master/README.md#deploy-to-heroku)DEPLOY TO HEROKU

1.  On Heroku create an account and log in.
2.  Click  `new`  and  `create new app`.
3.  Choose a unique name for your app, select region and click on  `Create App`
4.  Under the  `Settings`  click  `Reveal Config Vars`  and set IP to 0.0.0.0 and the PORT to 5000
5.  Go to the CLI and type  `$ sudo snap install --classic heroku`
6.  Type  `$ heroku login`  command into the terminal
7.  Create  `requirements.txt`  ($ sudo pip3 freeze --local > requirements.txt)
8.  Create a  `Procfile`  (`$ echo web: python app.py > Procfile`)
9.  Go back to Heroku, under  `Deploy`  find  `Existing Git repository`  and copy the command:`$ heroku git:remote -a <app_name>`  Paste this into the terminal.
10.  (If repository was not created already, type:
11.  `$ cd my-project/`
12.  `$ git init`
13.  `$ heroku git:remote -a <app_name>`)
14.  Type  `$ heroku ps:scale web=1`  into the terminal.
15.  Go back to Heroku, and at  `Settings`  copy  `https://<app_name>.herokuapp.com/`
16.  In the terminal type  `git remote add http://<app_name>.herokuapp.com/`
17.  Type  `git push -u heroku master`
18.  In the app dashboard, under  `Settings`  click on  `Reveal Config Vars`
19.  Set "MONGO_URI" and "MONGO_DBNAME" and "SECRET_KEY"
20.  Once the build is complete, go back to Heroku and click on  `Open App`



## Credits

**Acknowledgements**
The Inspiration for this project was based on the Code Institute  "Data Centric Design mini-project" by Tim Nelson.
 - Brian Macharia- Mentor support, for the advice, tips and guidance.
 - Nicola Tarran for site testing and proof reading.
  










> Written with [StackEdit](https://stackedit.io/).


