Full Stack Frameworks with Django Milestone Project 4 - Code Institute

{PIC OF IAM RESPONSIVE}

# **_Mountain Gear_**

This project is my fourth Milestone Project for the [Code Institute](https://codeinstitute.net/) Full Stack Software Developer Diploma. This project is designed to demostrate my capabilities to create a Full Stack web application with the use of [Python3](https://www.python.org/download/releases/3.0/) and 
[Django](https://www.djangoproject.com/). The project is an e-commerce application which will be using a Sql type database to store product informations. Also in the database will be stored user informations to allow users to login, logout and store delivery informations.


## **_UX_**  
### **_Strategy / Site Owner story_**

I have designed this website to allow the User to be able to check and buy climbing equipment. The main users will be climbers and mountain lovers. The User can come to the website and be able to purchase goods without the need of registering. If the User register an account within the website the user will be able to store delivery information to quickly checkout for the next purchases and be able to check an order history. For Admin and maintenance purposes an admin account will be created.

#### **_Data schema_**

The database for this project is Sql. Sql works with tables instead of documents like in MongoDb databases. For the products of the website I have created 2 tables. One containing the categories of products and the second table containing the products. The products have all the related fields that descibe the product. Every product in the products table has a Primary Key and also a Category id which refer to the Primary key of each category in the catergories table.
There is also a table for the Users, reviews and wishlist.

#### **_Security_**
ADD SECURITY FEATURES OF Django

### **_Scope_**

Features that I want to implement are:

* Ability for the User to browse climbing products in different categories.
* Ability for the not registered User to browse climbing products in different categories.
* Ability for the not registered User to buy climbing products.
* Ability for the User to register an account. 
* Ability for the registered User to receive confirmation emails for registration and order confirmation.
* Ability for the registered User to retrive lost password for login.
* Ability for the registered User to browse climbing products in different categories.
* Ability for the registered User to buy climbing products.
* Ability for the registered User to save items in the wishlist.
* Ability for the registered User to delete items from the wishlist.
* Ability for the registered User to delete the wishlist.
* Ability for the registered User to view the order history.
* Ability for the registered User to login / logout from the website.
* Ability for any User to search products.
* Ability for any User to modify the cart by removing unwanted products.
* Ability for the Admin to add, edit and update products and category.
* Ability for any User to contact the Admin/Developer via the Contact Us page.
* Easy design and navigation.
* Mobile first design.


### **_Structure_**

* The products are divided in 4 categories: Equipment, Clothing, Camping and Climbing shoes.  
* The Equipment category is composed by 3 type of products: Ropes, Helmets and Harnesses.
* The Clothing category is composed by 2 type of products: Shoes and Trousers.
* The Camping category is composed by 2 type of products: Tents and Sleeping bags.
* The Climbing shoes category is composed by 2 type of products: Mens and Womens.
* A search function will allow Users to search products.  
* The Categories are accessible from the main page under the search box if clicked a sub menu will open showing the types of products.  
* The Users will be able to access registration, login/logout functionality from the navigation menu.  
* The Users will be able to access the cart from the navigation bar.
* The User will be able to access delivery information, purchase history.
* The registered User to view the order history via the navigation bar under the Account menu.
* Any user will be able to access a contact us page via the footer.


### **_Skeleton_**

* The website will be easy to navigate by having displayed the different pages and sub menus via the navigation bar.
* The User will be able to search the products by using the search bar present throughout the website.
* When browsing the products, the products will be shown in a card like style with pictures and minimum information.
* When clicking on the product's card the product with full information will be shown.
* To register, login and to add delivery informations, forms will be implemented with validations features.
* On the footer a link for directing the Users to the contact page will always be present.
* The contact page will hold a form to contact the developer.
* The logo and "Home" link in the Navigation bar will redirect the Users to the main page and will always be present.
* The shopping cart will display the products added in a card style format.
* The checkout page will show the list of product and the form to add delievery and payment information with validation functionality.

### **_Surface_**

The website uses [Bootstrap](https://getbootstrap.com/) as a framework. Mobile first approch will be use. For the dign and look of the website I have taken ideas and styles from Boutique Ado Code Institute tutorial and [Gooutdoors](https://www.gooutdoors.co.uk/) e-commerce.
The color use is mainly grey.
* The color #545659 is used for the main navigation and footer.
* The product bar uses color #9c9c9c.
* When in mobile view main navigation the color #9c9c9c is used. I have decided to change color due to the size of the screen and by having a lighter grey the page is easier to read then using dark grey color #545659.
* The buttons also use color #545659.
* The text inside banners uses 2 colors. Black with in banners with color #9c9c9c and color #fafafa with banner color #545659 to help with contrast.
* The fonts choosen are from [Google Fonts](https://fonts.google.com/) 'Oxygen' and as a back up 'sans-serif'.
* The icons used throughout the web site are from [Fontawesome](https://fontawesome.com/).


## **_Wireframes_**

Link to Wireframes folder: [Wireframes]()

## **_User Story_**

## **_Features_**

### **_Existing Features_**


### **_Features to be implemented_**

* Login functionality with one click with Google, Facebook, Twitter accounts.
* Add card to show disocunts and sales of certain products.

## **_Technology Used_** 

* [HTML](https://en.wikipedia.org/wiki/HTML) has been used in this project because is the standard markup language for documents designed to be displayed in a web browser.

* [CSS](https://en.wikipedia.org/wiki/CSS)
is a style sheet language. It is used to style markup language such as HTML.

* [Gitpod](https://gitpod.io) has been used as an on-line IDE followed by [Heroku](https://www.heroku.com/) for deployment. IDE is a software application used by computer programmers for software development.
* [Github](https://github.com/) has been used to store the code.


## **_Testing_**


## **_Bugs and fixes_*



## **_Credits_**

* This project is inspired by [GoOutdoors](https://www.gooutdoors.co.uk/). The code is taken by following the Boutique Ado project from Code Institite.




color main #545659
color 2nd  #92a396
color 2nd  #9c9c9c
