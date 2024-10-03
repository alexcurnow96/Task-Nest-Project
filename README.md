# TASK NEST

### Deployed Link
https://task-nest-442b155992ec.herokuapp.com/

![Overview](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/amiresponsive.png)

## Project description

"Welcome to the place where productivity meets simplicity. Here you can, quite simply, "get it done, one task at a time". All tasks can be organised and achieved through projects, tasks and subtasks. Useable as a one person show or as a member of the team, we want to make your planning simple."

Task Nest is a todo application, focused on offering a simple way to track your tasks. Users can, once authorised, add a task, view the task in on it's own page, edit the task form, and delete the task. Users can also add comments to each task from the task view page.

### User demographics

This app can be used by anyone for any type of task list. It is easy to use and simple to understand, the only exception being that you need to be signed up and logged in.
The first demographic was professionals completing a project, but I quickly understood that the site would be useable by anyone in any walk of life.

# Planning

## User Interface Design (UI)

### Inspiration

I started by using a mindmap to establish an idea. I knew I wanted to create a site based on project management as I would like to get into that field after this course. I have also recieved feedback on my previous projects to indicate that my planning and project management skills were my best aspect.

My overall thinking was to create a simple to use, easy to look at site to help those wanting to organise their projects. This would feature:

- user creation and profiles to have individual lists and team boards
- kanban board to visualise tasks and enhance workflow
- ability to collaborate to optimise teamwork
- todo list to organise tasks further
- ability to prioritise tasks for an individual
- site to enhance productivity

I then created an MVP from these ideas which included a simple to-do list with user registration and log in. This would fulfill the CRUD functionality needed for the project.

I then began looking into competitors sites/apps to see what as already on the market and what appeared to be popular.

![Project Ideas](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/ideas-for-project.png)

These included:

- [A simple to do list for you and your team (any.do)](https://www.any.do/)
- [Todoist | A To-Do List to Organize Your Work & Life](https://todoist.com/)
- [Manage Your Team’s Projects From Anywhere | Trello](https://trello.com/)
- [KanbanFlow - Lean project management. Simplified.](https://kanbanflow.com/)
- [Kanban Tool - Kanban Boards for Business | Kanban Software](https://kanbantool.com/)
- [Home (taskworld.com)](https://taskworld.com/)
- [MeisterTask | Work Management Software | Task Management](https://www.meistertask.com/)

I chose these sites as inspiration for my board because I liked their simplicity. It also seemed as though I could \_\_\_\_ achieve my goals and create my own project site.

### Wireframes

I began my wireframing journey by sketching with pen and paper. This was a very simple and early idea, made using a template.
![sketched wireframe](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/sketched-wireframe.png)

I then began wireframing using my Miro board, using shapes and lines. These were able to give me a better idea of what I wanted the site to look like. In this iteration I included both desktop and mobile versions of each page, including all pages I could possibly make for this project.
![wireframe board on Miro](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/wireframes.png)

I then tried using Figma.com to create more complex wireframes/prototypes. I made one prototype, but could not get on with this tool.
![Figma prototype](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/prototype.png)

My finished wireframes were made using the Balsamiq application and featured every page I wanted to create in desktop and mobile view. This became my best planning tool when it came to development as I knew exactly what I wanted to create.
![Desktop Homepage](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/Desktop-homepage.png)
![Phone Homepage](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/Phone-Homepage.png)
![Desktop Projects](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/Desktop-Project-Page.png)
![Phone Projects](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/Phone-Projects-page.png)
![Desktop Kanban](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/Desktop-kanban-board.png)
![Phone Kanban](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/Phone-Kanban-board.png)
![Profile wireframes](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/profile-page.png)
![Sign in/up wireframes](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/Sign-in_Sign-up.png)

### Brand Identity

A big part of User Interface Design is the brand identity. This is how users recognise the site and build trust. I established this identity by first creating a brand name. I used the generative powers of AI by asking Perplexity.com to create names for a task management website. The responses from Perplexity were varied and most included alliterative names. Both of my previous projects with CI have featured alliterative names so I wanted to steer clear of that this time. The name Task Nest was featured and this became the name I started referring to my project as.
![Design Miro Board](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/design-ideas.png)

The brand colours are also a big part of the brand identity of Task Nest. My market research had led to me being pulled to a monochrome colour scheme. The different shades of one colour being used throughout the site made it look more professional for the use of development teams and individuals.

Upon looking into brand colours, I found that blue is a "harmonious colour that is stress relieving and does not disturb the focus of the brain, resulting in more efficient work being delivered." (https://www.haiken.com/insights/the-top-colours-for-your-office-to-increase-productivity) For this reason I chose an all blue colour scheme.
"[Colour Scheme](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/colour-scheme.jpeg)

I then used Adobe Firefly to create a logo for the website that would feature on the nav bar. This would provide an added layer of trust to the site and become a recognisable part of the brand. I used the checkpoints from the to-do list inside of a birds nest to make it clear that this logo belongs to the brand.
![Logo](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/logo.jpg)

The typography came at the end of the design process as I wanted it to follow the professionalism of the rest of the branding design. I started by looking at www.fontpair.co, and choosing a series of font pairings that I thought could work for Task Nest. When looking at the final choices, I noticed that they all featured "Karla" as a heading font. This became the natural heading font, and the pairing of "Inconsolata" went well for the paragraph elements. These fonts were then procured from Google Fonts (fonts.google.com).
![Font Pairing](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/font-pairing.png)

### Interaction Design

The interactivity of a website is also incredibly important. This includes the basic interaction, use of buttons, drag and drop, user creation, but also more complex interactions within a site. For this reason, I researched the 10 Usability Heuristics and how to assess where a design is falling short and where it is excelling. This also looks into what aspects of design can be sacrificed and what needs to be prioritised.

The most important heuristics for my project are user control and freedom, consistency and standards, and recognition rather than recall. These are all prioritising the users ability to move throughout the site with clearly marked actions. The CRUD functionality should be clearly marked and, if a user makes a mistake by clicking on an action when they do not want to, there should be clear signposts to return. This should be the same on every page throughout the site.

![Userflow Diagram](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/userflow-diagram.png)

### Accessibility

Throughout this course, the accessibility of users has been highlighted. For this reason, I wanted to plan for accessibility issues before I had begun coding my site. This would make sure my site was useable by everyone who had need to use it. This was a relatively easy portion of the design as I didn't want to complicate accessibility. This should be at the forefront of my design and should not be thought of as extra complications to the design.

The accessibility designs I made were to use large buttons and large font throughout the site, to implement a light/dark toggle mode for those who wish to use the site on either setting, and an overall simple app functionality with an easy to follow user flow for all users.

These would all be planned for and tested at the end of my project to ensure the site is functional for all users.

## User Experience (UX)

### Database Planning

I began my database design by sketching out my models and an entity relationship diagram. Because of my previous experience in SQL, I began by following the principles of MySQL and used integer, varchar, and set. This helped me understand what I was going to create in the backend of this site.
![Sketched ERD](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/sketched-erd.png)

I then began using LucidChart (www.lucidchart.com) to create an actual ERD to be used in my project. This included Users, Tasks and Subtasks with primary keys and foreign keys. This allowed me to create simple models with simple connections.
![Lucidchart diagram](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/tasknest.png)

I then discovered that you could import the user model from Django AllAuth, and decided to use that functionality for the Users model.

### The Purpose and Target Audience

My target audience are individuals within teams in a project. There is also a secondary audience of just individuals who want to achieve tasks generally.

The purpose of this website is related to project management. I wanted to create something that would enable productivity and streamline working practices. I am also aware that this site can be used by anyone who would like to log their tasks and be more productive though.

### User Journeys

All users journey through a website, and I needed to keep in mind the path users would take on mine. I wanted to keep the site as simple as possible for the user to navigate. This reduced the amount of pages I had, and reduced the amount of decisions for the user to make.

The CRUD functionality was the main focus of the site. This included the ability to create tasks, read the tasks, update the tasks, and delete the tasks when completed.
![User Flow Diagram](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/users-model.png)

### User stories

| User Story                                                                                                                           | MoSCoW Prioritisation |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------: |
| As a user I want to sign up for an account so that I can access the project management features.                                     |       Must Have       |
| As a user I want to log in to my account so that I can view and manage my projects.                                                  |       Must Have       |
| As a user I want to log our of my account to ensure my information remains secure.                                                   |       Must Have       |
| As a team member I want to create a new project so that I can start organising tasks and collaborating with others.                  |       Must Have       |
| As a project manager I want to add team members to a project so that they can contribute and view project details.                   |      Could Have       |
| As a team member I want to create tasks on a Kanban board so that I can visualise and manage the workflow.                           |      Won't Have       |
| As a user I want to drag and drop tasks between columns on the Kanban board so that I can update their status easily.                |      Won't Have       |
| As a team member I want to create and manage to-do lists within a project so that I can track smaller action items.                  |       Must Have       |
| As a team member I want to upload PDF files to a project so that I can share important documents within the team.                    |      Should Have      |
| As a user I want to comment on tasks so that I can collaborate and communicate with team members.                                    |       Must Have       |
| As a user I want to share links within a project so that team members can access relevant external resources.                        |      Should Have      |
| As a project mananager I want to assign roles and permissions to team members so that I can manage access levels within the project. |      Won't Have       |
| As a user I want to toggle between light and dark modes so that I can adjust the interface to my preference.                         |      Should Have      |
| As a team member I want to recieve notifications for project updates so that I can stay informed of changes and new assignments.     |       Must Have       |
| As a user I want a logo so that I can recognise the site and build trust.                                                            |       Must Have       |
| As a user I want a vertical navbar that is visible on every page.                                                                    |       Must Have       |
| As a user I want clear links on the nav bar so I can go to any page.                                                                 |       Must Have       |
| As a user I want a log in page that is easy to use so that I can log in every time.                                                  |       Must Have       |
| As a user I want a sign up page so that I can sign up for the service easily.                                                        |       Must Have       |
| As a team leader I want roles on the sign up page so that my colleagues can sign up with their permissions.                          |      Should Have      |
| As a user I want my username to be visible on the nav bar to promote familiarity.                                                    |       Must Have       |
| As a user I want to create a project from the projects page so that I can create multiple projects.                                  |      Could Have       |
| As a user I want to be able to name a project and give a brief description.                                                          |      Could Have       |
| As a user I want an add task button so that I can add tasks to my project easily.                                                    |       Must Have       |
| As a user I want an edit task button so that I can edit tasks in my project.                                                         |       Must Have       |
| As a user I want a delete task button so that I can delete tasks in my project.                                                      |       Must Have       |
| As a user I want a backlog column so that I can see all the tasks that need to be done in the future.                                |      Won't Have       |
| As a user I want a to-do column so that I can see what tasks need to be done.                                                        |      Won't Have       |
| As a user I want an in progress column so that I can see what task I am currently doing.                                             |      Won't Have       |
| As a user I want a done column so that I can see what task I have done.                                                              |      Won't Have       |
| As a developer I want to use fonticons for each column for user experience.                                                          |       Must Have       |
| As an admin I want to see how many users I have and what projects they have so that I can organise my team.                          |      Won't Have       |
| As a team leader I want to see what my colleagues are working on within their projects so that I can organise my team.               |      Won't Have       |

![Miro Board Screenshot with User Stories](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/userstories1.png)
![Miro Board Screenshot with User Stories](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/planning/userstories2.png)

### Agile

I took an agile approach to this project, focusing on the user and iterating my work to better create my project.

I started my agile approach by creating my user stories, justifying all choices from the perspective of users and developers. I tried to create users stories from a range of perspectives, not limited to just end users but also developers, team leaders and project managers. Although this proved to be ambitious given the time frame and my own abilities, I felt these perspectives gave me confidence to complete my project.

I used a github projects kanban board to organise my user stories. I used it as a visual guide to my progress throught the project, moving tasks from one column to another based on where I was in my sprints. There were four columns on my board:

1. Backlog: This section housed all of the user stories at the beginning of the project. It was then used for the tasks that would not be completed in this iteration, due to time constraints or my own ability with the technologies. Therefore, the backlog almost became a future features section too.
2. Todo: This column was used for items that hadn't been started but needed to be worked on in one of my upcoming sprints. This section served to help when planning my tasks per day.
3. In Progress: This section was for items currently being worked on. I could keep on task when stories were placed into this column, and had a visual guide as to how far along in my sprint I was. If a task was not completed in a given sprint, it was placed back into the todo column for the next day.
4. Done: This column was for all completed tasks. Tasks only made it to the done column once they had been fully completed. This was a great motivator to see what stories I had already completed.

Each user story had a MoSCoW prioritisation label attached to it. These labels were added in the middle of the project as I felt this helped me understand where I was within the project better. At the beginning I was hopeful (and naive) enough to think that I could fulfill all user stories. But during the project I realised that my MVP was the most important aspect of the project and so used the prioritisation labels to reflect that. This helped me in my planning towards the second half of the project because I focused on only the must have features.

My MVP became a very simple task app rather than a full project management app. I felt that the Kanban board and team organisation aspects were better suited to a future iteration of my project. The site would fulfill the criteria for the project, and work well for users as just a simple to-do list task app.

The biggest aspect of Agile I used in this project was my sprints. I took each day as a seperate sprint to achieve an aspect of my plan. This was only possible because of the daily scrum meetings led by my facilitator, Amy. The scheduled meetings at 9am and 4pm helped keep my sprints contained and the ability to talk about that days work kept me focused. I seldom ran into problems because of our daily meetings and this also helped boost my confidence going into the next days sprints.

# Features

### Navbar

I decided to create a sidebar with my navigation links to make better use of the space. I wanted a clean and simple site with very few distractions outside of the basic functionality, so using a portion of the page for the navbar helped to highlight the links throughout the site for the user.
The main features of the navbar are the sites logo and the username of the logged in user. The links to other pages change depending on if the user is logged in or not. An unauthorized user sees Sign Up, Log in, and Task List links, whereas an authorized user sees the Tast List and Log Out links.
This site does not feature a footer. There are instead social media links at the bottom of the sidebar. These link to Facebook, Instagram, and Twitter.

![Navbar 1](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/navbar-logout.png)
![Navbar 2](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/navbar-login.png)

### Buttons or links

There are a number of buttons on the site. The two buttons on the home page link to the Task List page and the Sign Up page. When an unauthorized user clicks on the first they are sent to the Log In page instead because unauthorized users cannot access the Task List.

![Home Page button](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/homepagebutton.png)

The Task List page features many buttons. There is one button for adding a task which leads you to the Task Form Page. Every added task then generates three more buttons. These are “view”, “edit”, and “delete”. Each of these buttons has a hoverable popup that tells the user what to do on that page. This is to ensure user flow is seamless and there is reduced confusion.
Every form on the website has a submit button which posts the content back to the server and sends the user to the chosen page.

![Task List Buttons](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/tasklistbuttons.png)

### Forms

Forms are the main way of inputting information into this site. They provide a user-friendly, easy way to send and get information from the database in the backend of this project. I used Django’s built-in forms as well as creating my own to populate the site.
The forms featured on Task Nest are the Sign Up, Log In, and Log Out pages, as well as the form to create a task, and create a comment. The Task Form is also used on the edit task page.

![Form](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/taskform.png)

# Manual Testing

### HTML VALIDATION

I have used HTML W3C Validator (https://validator.w3.org/) to validate all of my HTML files.

Due to my pages being developed with Jinja syntax, owing to Python/Django, I had to change the way I validated my templates. This included:

- Deploying my site to Heroku and navigating to each individual page.
- Right clicking to access the page’s source code.
- Ctrl + A to select all the page’s HTML code from this screen.
- Pasting this code into the direct input on the HTML W3C Validator.

I could then check for any errors and warnings to be able to fix them. If there were any errors that needed to be fixed, I then redeployed to Heroku and followed the steps to revalidate the code.

![HTML Validator](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/html-checker.png)

|           |           |             |
| --------- | :-------: | ----------: |
| Task Form | No errors | No warnings |
| Index     | No errors | No warnings |
| Task List | No errors |   1 warning |
| Task      | No errors | No warnings |
| Delete    | No errors | No warnings |
| Logout    | No errors | No warnings |
| Sign In   | No errors |   1 warning |
| Sign Up   | No errors | No warnings |

![Task List Warning](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/tasklisthtml.png)
![Sign In Warning](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/signin-warning.png)

### JAVASCRIPT VALIDATION

JSHint (https://jshint.com/) was used to validate the small amount of JavaScript code added to the project. Below are the findings.

![JShint 1](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/javascript1.png)
![JShint 2](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/javascript2.png)
![JShint 3](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/javascript3.png)

### PYTHON VALIDATION

CI Python Linter (https://pep8ci.herokuapp.com/) was used to validate the Python files that were created or edited by myself.


| |admin.py| forms.py| models.py| urls.py |views.py|
| :---:| --- | --- | --- | --- | --- |
|todoapp| No errors| No errors| No errors| No errors| No errors|
|tasknest| n/a| n/a| n/a| No errors| n/a|

### CSS VALIDATION
W3C CSS Validator (https://jigsaw.w3.org/css-validator/) was used to validate my CSS file. No errors were present for my CSS file. Below are the findings.

![CSS Validator](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/css-checker.png)

### LIGHTHOUSE SCORES
Lighthouse testing was carried out in Incognito mode to achieve the best result. Performance was lower than preferred on mobile due to the site being image heavy because of the logo. I changed the format of the logo image to help this score. This report will be reviewed for future developments to raise this score. Desktop and mobile scores are listed below.

![Lighthouse Desktop](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/lighthouse-desktop.png)
![Lighthouse Mobile](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/lighthouse-mobile.png)

### WAVE ACCESSIBILITY EVALUATION

![WAVE test](https://github.com/alexcurnow96/portfolio-project/blob/main/documentation/testing/wavetest.png)

## Deployment steps

The site was deployed to Heroku. The steps to deploy are as follows:
- Install the gunicorn python package and create a file called 'Procfile' in the repo's root directory
- In the Procfile write 'web: gunicorn lunar_lists.wsgi'
- In settings.py add ".herokuapp.com" to the ALLOWED_HOSTS list
- In settings.py add 'https://*.herokuapp.com' to CSRF_TRUSTED_ORIGINS list
- git add, commit and push to github
- Navigate to the Heroku dashboard
- Create a new Heroku app
- Give it a name and select the region 'Europe'
- Navigate to settings tab and scroll down to Config Vars
- Click 'Reveal Config Vars'
- Add the following keys:
    - key = DATABASE_URL | value = (my secret database url)
    - key = SECRET_KEY | value = (my secret key)
- Navigate to Deploy tab
- Connect to GitHub and select the repo 'lunar-lists'
- Scroll down to 'Manual deploy' and select the 'main' branch
- Click 'Deploy Branch'


## Credits

### Tutorials
- Dennis Ivy: Django To Do List App with User Registration & Login.
    - To Do list app with User Registration, Login, Search and full Create Read Update and DELETE functionality. (https://www.youtube.com/watch?v=llbtoQTt4qw)
- Code With Stein: Django Project Management System | Django project with source code
    - Learn how to build a simple project management system from scratch using Django and Tailwind. Plus, you will learn how to deploy this project to a cloud based service called Acorn.(https://www.youtube.com/watch?v=m3nYd_IFZuU&t=33s)
- Code Institute: Learning Management System
    - Developing with Django, Love Running - Essentials Project, Love Rosie - Bootstrap Project (https://learn.codeinstitute.net/dashboard)
- rajeshdn: Side Navigation bar Using HTML and CSS
    - For CSS styling (https://codepen.io/RajRajeshDn/pen/LKzZNe)
- Tyler Potts: Build a Responsive Sidebar in 10 minutes | HTML, CSS & JavaScript
    - Learn how to build a simple and easy responsive animated sidebar in under 10 minutes using HTML, CSS & JavaScript! (https://www.youtube.com/watch?v=neb7WcDixoY)
- amylour: FreeFido_v2
    - A social-community and booking system for a private dog park. Built for Code Institute's Full Stack Software Development Diploma using Django, ElephantSQL and Bootstrap. (https://github.com/amylour/FreeFido_v2)
- MarkChips: lunar-lists
    - Lunar lists allows users to create to-do lists for any task with the addition of a fun and friendly space theme. Whether you are a busy person, or a forgetful one, you can use lunar lists to log all your tasks, set their due date, and mark them as completed when they're done. Your lunar lists are only available to you, so don't worry about people tampering with your lists. (https://github.com/MarkChips/lunar-lists)
### Other
- Google Fonts
- Font Awesome
- Adobe Firefly
- Figma
- Balsamiq
- Fontpair
- Adobe Colour
- Lucid Chart
- Perplexity
- Claude
- Django Documentation
- Amy Richardson's worksheets and files that were made to help us with this project.
- Mark Briscoe's SME sessions
- Martin and Roo MacArthur and John Rearden from the Coding Coach Sessions