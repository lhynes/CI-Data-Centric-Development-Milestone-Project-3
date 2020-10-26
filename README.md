# Data-Centric-Development-Milestone-Project-3

<h1 align="center">
  <a href="https://galway-charity-projects.herokuapp.com/" target="_blank"><img src="https://res.cloudinary.com/daqyuuzq9/image/upload/v1603642648/Galway_Charity_Projects_youzgg.png" alt="Galway Charity Projects"/></a>
</h1>
<div align="center"> 
<img src="https://res.cloudinary.com/daqyuuzq9/image/upload/v1603730801/favicon-32x32_owefug.png" alt="Galway Charity Projects"/>
</div>
<h2 align="center">
Galway Charity Prjects(GCP) - A home for Galway's volunteering community to come together to support local charities. 
</h2>
<div > 
Before Covid-19 people, interested in volunteering, would often look beyond their own county and even country for volunteering oppotunities.  The recent times have taught us all how powerful the impact can be when we support local. 
Today, some charities are struggling because they cannot get access to volunteers to support their projects and some volunteers are lost as they don't know what projects they can support in their area. 
[Galway Charity Projects](https://galway-charity-projects.herokuapp.com/) is a place to encourage local volunteers and charities to engage more and work together to strengthen our community
<br>
<br>
Features of the site include easy to view project list and detail page and simple registration process for charities which I hope will allow users to achieve the following: 

* Allow *charities* to register their project
* Enable *volunteers* to search live projects in their area and get in touch with the charity to find out more. 
* *Project Detail Page - Select a project,* they should see the instructions, any downloadable files, and a contact for the charity.
<br>
In Phase one we are focusing on the city of Galway with the intention to build on this for all the cities and towns in Ireland to encourage people to learn more about the volunteering opportunities close to home. 
<br>

[Click here to view the page now!](https://galway-charity-projects.herokuapp.com/)

</div>

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**Charity goals**](#charity-goals)
    - [**Volunteer goals**](#volunteer-goals)
    - [**Developer and Business Goals**](#developer-and-Business-Goals)
    - [**User Stories**](#user-stories)
    - [**Design choices**](#design-choices)
    - [**Wireframes**](#wireframes)
    - [**Database**](#database)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)
    - [**How to run this project locally**](#how-to-run-this-project-locally)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

7. [**Disclaimer**](#disclaimer)

## UX

### Project Goals

The primary goal of Galway Charity Projects (GCP) is to provide a clean, intuitive and engaging site to help people find out more about the ongoing charity projects close to them. 

GCP has two target audiences: Local charities and the local community/volunteers looking to support. 

#### Charity Goals

Local charities want and need project support: 
- They want to get their message out there about the projects they have live and need support on. 
- They want to make sure the community is aware of they different initiatives
- They want an easy way to register their projects online

GCP can help local charities owners because:
- It provides a platform for local charities to share their projects. 
- It ensures their listing is live and active on the site.
- Charities can easily submit their projects for the site using a simple form
- GCP also offers them the feature to update their projects when details change or remove them one complete. 
- Charities can also indicate projects that need urgent support



#### Volunteer goals

People want to make the extra effort to support local where they can and give back to the community and volunteering is a great way to do this but 
sometimes they might not always be aware of the different opportunities and projects in their area. 

Volunteers and members of the local community can:
- Learn about new charity projects in Galway
- Find out more information on different projects via a detail page
- Discover which projects might need urgent support
- Have a one stop location where they can find out all about the local charity 

GCP can help meet the needs of the community because: 
- It can offer a list view of all live projects. 
- Provide a search feature on the projects page to filter to the volunteers interest. 
- It displays in an engaging and simple way.
- It has been designed with user experience as a priority to easily guide them through the site 

#### Developer and Business Goals

- A well designed directory of charity projects that strives to have a positive imact on the community. 
- Good and clean programming that is robust and scaleable with the increase of cities and charities joining. 
- A professional looking first attempt of using python, flask, materialize which the developer is excited to make a part of her portfolio and continue to develop in the future

#### User Stories

As a charity owner, I want:
1. To register my charity
2. Create new charity project listing and share details. 
3. Edit, update and delete a project when necessary. 

As a volunteer and member of the community, I want:
1. Discover more about the volunteering opportunities in my area based on my catagories of interest
2. A visually and operationally appealing site that makes if simple to learn more about local charitiy projects. 
3. Easily view the details of a specific project.

As an admin user, I want:
1. To view all projects
2. Create, edit, update and dleete project categories when needed



#### Design Choices

The overall feel of the site is one that is visually appealing and simple to follow. The following design choices were made with this in mind:

**Fonts**

- The primary font **Roboto** was chosen because it is a crisp, sharp and easy to read font. It was inspired by the logo created on Canva.com. 

**Colours**

- The primary colour choices for this site is purple and blue.  This has been inspired by the county colours of Galway and also the blue as an uplifting balance. 
A basic pallet was chosen to ensure the infomration on the page was the main focus.

**Styling**

- On the listing page cards have a minimalist design and rounded edges and a drop shadow to highlight these areas on the page more.  
- Design and styting consistency was important on this site to help linking and combining the related areas together. 



**Home Tile Images**

- At present these have been kept simple and will be considered again int the future. 



**Header and home Banner images**

- A strong header was chosen to make the logo and heading memorable 
- The homepage image was chosen for its friendliness and warmness of complimentry colour palette. 



#### Wireframes

During the early part of the project wireframes were created using pen and paper and on [Pages](https://www.apple.com/pages/). 

- [Link](https://drive.google.com/drive/folders/14ucGfk0wU4zXHGPPJoB9GMs4_lIcOa28?usp=sharing)


### Database
Database

This website has a MongoDB database called: galway_charity_projects_manager
The database consists of 3 collections(tables)
- Users
- Projects
- Project Categories
<div align="center">
<img src="https://res.cloudinary.com/daqyuuzq9/image/upload/v1603730576/Screenshot_2020-10-26_at_16.41.55_hnoews.png" alt="Screenshot: Homepage" >
</div>
*This database was a good fit for the complexity level of this project - in the future I would review the options available*



## Features
 
### Existing Features

#### *Visible to all users*

1. **Home - Site Overview**
    - On arriving at the homepage page the user is presented with the option to select one of two options 
        - Volunteer - Find Projects 
        - Charity - Register Project
    - They can select Galway and be directed to the Galway Catagory Page
    - 




2. **Buiness Owner**
    - Business owner can add their business by following the navigation link "Submit a business" or the Call To Action Link under the catagory tiles. 

<div align="center">
<img src="https://user-images.githubusercontent.com/17083566/89499911-b5118500-d7b8-11ea-8fb1-014890c50430.png" alt="Screenshot: Navigation"><br>
<img src="https://user-images.githubusercontent.com/17083566/89499916-b773df00-d7b8-11ea-8f99-34abf1372f60.png" alt="Screenshot: CTA"><br>
</div>

3. **Newsletter Sign Up**
    - Both business owners and Community members can sign up to the We Support Local Newletter

<div align="center">
<img src="hhttps://user-images.githubusercontent.com/17083566/89500101-06ba0f80-d7b9-11ea-99f5-7f23eb361369.png" alt="Screenshot: Galway Catagory Page"><br>
</div>

4. **Galway Catagory Page**
    - On the city homepage a user can review all the different related business catagories in an easy and visually appealing phot grid. 
    - On select of any catagory thwy will be directed to that catagories page. 

<div align="center">
<img src="https://user-images.githubusercontent.com/17083566/89500142-19ccdf80-d7b9-11ea-8591-0d0958c3d969.png" alt="Screenshot: Galway Catagory Page"><br>
</div>

5. **Catagory Page - Map & Listing**
    - On any single catagory page the user can see all the listings of the businesses on the google map located at the top center of the page
    - Below the map the user can view the listings on styled cards


6. **View on Google Maps button**
    - On each card there is a button "View on Google Maps" - This redirects the user to the google maps url for that place opening in a new window allowing the user to explore further. 

7. **Back to top button**
    - To enhance the UX on pages with long listings a "Back to top" button scrolls the user back to the top of the page. 


#### *Visible to all registered users*


#### *Visible to admin*

- Username: admin
- Password:123123123

1. **Categories**
    - Full CRUD funtionality  arriving at the homepage page the user is presented with the option to select their city of preference - at present only Galway is active 
    - They can select Galway and be directed to the Galway Catagory Page
At this time there are three main Categories, however, the page assumes that the Administrator might want to expand on it in the future. Therefore there are three options available here:

Add Category
Edit Category
Delete Category


### Features Left to Implement

1. **Increased City Coverage**

In the future I would like to add more cities and towns to be featured on the site. 
    - I would like to give ht suer more freedom to review what's availabilie based on their location


2. **Additional Catagories**
    - Allow the user to carry out more flexible searches via free text seaches

3. **More Filtering options**
    - Allow the user to freely select how they would like to filter and order the search output - by rating or locations. 

4. **Automated content creation**
    - Once a user submits their listing it would be great to dynalically generate this content on the listing page. 

   

## Technologies Used

- This project uses HTML, CSS and JavaScript programming languages.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [GitPod](https://www.gitpod.io/) 
    - Developer used **GitPod** for their IDE while building the website.
- [Bootstrap](https://www.bootstrapcdn.com/)
    - The project uses **Bootstrap** to simplify the structure of the website and make the website responsive easily.
- [Google Fonts](https://fonts.google.com/)
    - The project uses **Google fonts** to style the website fonts.
- [GitHub](https://github.com/)
    - This project uses **GitHub** to store and share all project code remotely. 
    - The new GitHub Projects planner was utilised to plan and keep track of this project. This project plan can be viewed [here](https://github.com/AJGreaves/picflip/projects/1).
    - The **Issues** feature in GitHub was used to generate links for all external images for this project. 
    - This project used tools in **Canva** to edit, crop and save images. 
    - **Canva** was also used to source all imagery and design of banner, logo and tile elements. 
    - Colour picker was also used to ensure color consistency over the entire project. 

## Testing 

Manual testing was carried out on this site by the developers family memebers to review the UX and responsivness 

## Deployment

This project was developed using the [GitHub IDE- GitPod](https://www.gitpod.io/) , committed to git and pushed to GitHub via the terminal in GitPod

To deploy We Support Local to GitHub Pages from its [GitHub repository](https://github.com/lhynes/Interactive-Frontend-Development-milestone-Project), the following steps were taken: 
1. Log into GitHub. 
2. From the list of repositories on the screen, select **Interactive-Frontend-Development-milestone-Project**.
3. From the menu items near the top of the page, select **Settings**.
4. Scroll down to the **GitHub Pages** section.
5. Under **Source** click the drop-down menu labelled **None** and select **Master Branch**
6. On selecting Master Branch the page is automatically refreshed, PicFlip! is now deployed. 
7. Scroll back down to the **GitHub Pages** section to retrieve the link to the deployed website.

The Master Branch is up to date containing the most recent version of the project. 

### How to run this project locally

You can follow this [link](https://lhynes.github.io/Interactive-Frontend-Development-milestone-Project/index.html) to view the site. 

To clone this project from GitHub:
1. Follow this link to the [GitHub repository](https://github.com/lhynes/Interactive-Frontend-Development-milestone-Project).
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.
```console
git clone https://github.com/USERNAME/REPOSITORY
```
7. Press Enter. Your local clone will be created.


## Credits

### Content

- All text in this project was written by the developer.

### Media

#### Images
- The We Support Local logo was created using [Canva](https://www.canva.com/).
- All imagery for the site was sourced from [Canva](https://www.canva.com/).


### Code
- Code for the photo grid was taken from this [W3Schools](https://www.w3schools.com/howto/howto_css_image_grid_responsive.asp) post.
- Google maps impmelentation was supported but the [Goole Maps Places API Documentation](https://developers.google.com/places/web-service/overview)
- Code for the radio buttons input for the goodle maps type was from [StactOverflow](https://stackoverflow.com/questions/41970336/update-marker-and-place-types-using-radio-button-google-place);
- Elements and layout for the site was taken from [Bootstrap](https://startbootstrap.com/snippets/)

### Acknowledgements

I would like to extend a special thanks to my Code Institute Mentor Anthony Ngene for kind support and time throughout this project.
He inpsired me to try new things, helped to explain and show ways to imporve my code when struggling. 


#### Disclaimer
The content of this website, including the images used, are for educational purposes only.