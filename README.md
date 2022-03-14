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

## Scope

**What a user may expect**

 - Easy and intuitive website navigation.
 - That all links within the site work.
 - Site is understandable and viewable regardless of screen size.
 - Site looks professional and relevant to the businesses operating processes.
 
 



## Structure

**The site will consist of:**

 - A Home page displaying an overview of products and services offered
   by the business to current and potential customers.
 - A Hire products page displaying images and descriptions of the types
   of hire equipment available for hire.
 - A Contact page containing a form for users to contact and make
   enquiries with PLS.

**Design**

I have used the company logo and branding colour scheme throughout the site and utilised Google’s “Eye Dropper” extension to pick out the colours from the company logo.

Where appropriate transparent background effects were used while still using the branding colours.

**Colour list:**
rgba(51, 45, 108, .7);
`#562680``#528``darkslateblue``hsl(272,54%,32%)``rgb(86,38,128)`

`#f8f9fa``#fff``ghostwhite``hsl(210,16%,97%)``rgb(248,249,250)`
**Typography**

Although I imported Google Fonts I have mainly used Arial and increased the letter spacing on white text and purple backgrounds in the Hero images. *ref Code Institute “Love Running” tutorial site*

@import url("https://fonts.googleapis.com/css?family=Merienda+One|Open+Sans&display=swap");

**Call to Action**


### Images

 -No images are utilised on this system

## Site Framework

**Responsive layout**

 - The sites responsive design retains the style and branding of the
   site as screen size change.
 - I used the Bootstrap Branded Navbar for the site navigation in the
   header and a Bootstrap Grid for hire equipment images.

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




## Future Features

 - Sales page for product information and on-line sales.
 - Inspection page – information on what is required by law, what is
   best practice and detail on the services that PLS can provide.
   provide Popup information on all hire and sales equipment images.
 - Technical Support page with FAQ’s and possible chat facility.
 - Add Captcha "I'm not a Robot" Turing test to the Contact form to stop automated phishing.

## Technology Used

 - **HTML5** – Markup Langauge for structure and functionality.
 - **CSS3** – Cascading Stylsheets for responsiveness and consistant style
   throughout the site.
 - **Materialize** – for responsive navigation.
 - **Javascript and Jquery** - utilised for Popup
 - **Google Fonts** – for Typography.
 - **GitPod** for code editing, saving commits and pushing versions to
   GitHub.
 - **Git** – version control.
 - **Microsoft Paintbrush** – resize images.
 - **Chrome Developer Tools** – testing page responsiveness.

## Testing

**Navigaation**

 - All links have been tested.
 - The PLS logo returns the user back to the Home page.
 - To aid navigation the text for the links in the Navbar are coloured
   black when on target, with all other links in the Navbar coloured
   red.

**Responsiveness**

The responsive ranges targeted were:

 - For Desktops @media screen max-width 5000px  
 - For Handheld Touchscreens with screen max-width: 1280px
 - Mobile phones with screen max-width: 414px
 - 
**Responsiveness Testing**

Testing was initially carried using the Chrome Developer Tools using the responsive ranges listed above. Further developer tool testing was carried out using the Firefox and Microsoft Edge developer tools.

The Firefox tools did find an issue with the iPhone 6/7/8 Plus iOS11 screen size which was resolved by increasing the max width to414px.

Hardware tested ranged from a Motorola G5s, Samsung Galaxy S5, 10" Amazon Kindle Fire Tablet and a widescreen desktop PC.

**Browser Testing**
Browsers used for testing were:

 - Google Chrome - Desktop and Mobile
 - Firefox - Desktop and Mobile
 - Microsoft Edge
 - Amazon Silk

**Performance Testing**
Performance tested against Google Lighthouse Developer Tools which were very useful for testing and as an aid to increase performance with it suggested improvements.
An initial example of poor performance was the Contact page with the following stats:


By altering background contrasts, font colours and improving the Metafile content the following was achieved:



The final tests for the Home and Hire pages are:
Home Page





**The Companies Current WordPress Site**


## User Testing
### Testing - What a user may expect

 
 **Easy and intuitive website navigation.**

 - On entering the site the user immediately see's the navigation bar
   and the easily readable links at the top of the page

 **That all links within the site work.**
 

 - All  links have been tested and selecting the logo links directly
   back to the Home page.

 **Site is understandable and viewable regardless of screen size.**
 

 - The navigation bar automatically converts to a drop down menu when a
   screen reaches tablet size and all pages are accessible and viewable
   in the common mobile formats.

 **Site looks professional and relevant to the product and nature of the
   business.**
 

 - On entering the site the user is greeted with the company logo and
   the Hero image which shows one of the liveried company vehicles
   outside the company premises. This shows that the company is
   established.    
  

 - The Hero image slowly zooms in drawing the users eye    to the text 
   over the image, the company name and below that    "Supplying
   Everything Below The Hook" which quickly establishes the    purpose
   of the company to any one familiar with the Lifting Industry.

 
### What a user may want

**As the majority of trade currently comes from the locality the user    would need to know how to physically locate the business.**
All Footers on the display:

 - The company address
 - A Google map showing the location of the company
 - Company opening times

 **To quickly be able to gain a good understanding of the products and
   services offered by the business.**
   
 - Just below the hero image on the home page the four main
   products/services of the company listed and described.

 - The Hire Equipment section also provides a **popup** text option
   which explains the companies hire terms.

 **To gain a sense of confidence in the business from the design,
   statements and any affiliations with trade associations.**
   
 - From the design of the logo to the images used there is a clear
   message to the user of the services provided.

 - There is also a logo and link (which opens in a separate browser tab)
   to the Hire Association of Europe (HAE) in all Footers, displaying
   companies affiliation.

**To find a direct method of contact on the site.**
 - The Contact page  provide a clear contact and enquiry method, giving
   the user a choice of how they wish to be contacted.

### The business would expect the site to provide:

**The business would expect the site to provide improved SEO  capabilities to encourage the relevant traffic to the site.**

 - The Home page scored 100 on the Google Lighthouse Developer Tools
   compared to a score of 82 for the current site.

 **An overview of products and services offered by the business to
   current and potential customers.**

 - The home page lists and describes the four main products/services of
   the company, just below the hero image.
 - A **popup** explains the companies hire terms in the Hire box.
 - The Hire page displays an overview of equipment available for hire.
 
 **To provide an easy method of contact for customers and suppliers**

 - The Contact page form is clear and attractive with the Hero image of
   the liveried company van as background.

 - The current WordPress site also has a contact form but does attract
   some unwanted enquiries. To reduce this issue and to ensures capture
   of all information all fields are set as "Required".

## HTML and CSS Validation

**HTML Testing**
Initially some errors were picked up by the Validator, these ranged from Elements with no closing tags, elements such as iframe which required a title to double ups on alt attributes. However, as the Validator tells you what thee error is and on what line code is easily resolved.
The following images are the pass results for all three pages:

**Home Page**


**Hire Page**



**Contact Page**


**CSS Validation**
Although a few parsing errors were picked up initially these were resolved and the CSS code has now passed W3C validation with permission to embed their logo's if required.



## Deployment

**Add Commit and Push files**
With the current project open in **GitPod** and all files saved navigate to the command line:

 1. At the command prompt type git add . and press the Enter key – this
    selects all files in the project.
 2. At the next command prompt type git commit –m “add a relative
    comment” and press the Enter key – this action adds the files to the
    commit.
 3. At the next command prompt type git push and press the Enter key –
    this action commits this version of your project to your GitHub
    repository with the comment from the commit as it the label for any
    files that were updated compared to the previous version.

**Deploying via GitHub Pages**




## Credits

**Acknowledgements**
The Inspiration for this project was based on the Code Institute  "Data Centric Design mini-project" by Tim Nelson.
 - Brian Macharia- Mentor support, for the advice, tips and guidance.
 - Nicola Tarran for site testing and proof reading.
  










> Written with [StackEdit](https://stackedit.io/).
