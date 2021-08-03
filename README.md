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
ADD SCREEN SHOT OF PRODUCT AND CAT ADMIN.
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

1. As an unregister / register User I want to be able to view climbing products.
2. As an unregister / register User I want to be able to buy a product.
4. As an unregister / register User I want to be able to contact the website via contact us page. 
3. As an unregister User I want to be able to register to the website.
5. As a register User I want to be able to login to the website.
6. As a register User I want to be able to recover my password.
7. As a register User I want to be able to logout to the website.
8. As a register User I want to be able to view my profile.
9. As a register User I want to be able to receive email confirmation after registration.
10. As a register User I want to be able to view total purchase in every page.
11. As a register User I want to be able to view purchase history.
12. As a register User I want to be able to save my delivery information.
13. As a register User I want to be able to receive email confirmation after check out.
14. As a unregister / register I want to be able to search products.
15. As a unregister / register  I want to be able to view a specific category of products.
16. As a unregister / register I want to be able to view products added to shopping cart.
17. As a unregister / register I want to be able to view confirmation / error messages during my activity within the website.
18. As admin I want to be able to add a product.
19. As admin I want to be able to edit a product.
20. As admin I want to be able to update a product.
21. As admin I want to be able to delete a product.

## **_Features_**

### **_Existing Features_**

* The navbar contains a logo on top right hand corner to redirect to the landing page. There is a search box to search products, the cart total always visible and the account menu. If the user is not logged the account menu will open a window with 2 links: Register and login. If the user is logged the account submenu will show 2 links: Profile and Logout.
If the admin is logged the account submenu will show 3 links: Profile, Logout and Products menu.  
* The footer will show the contact us page where any user can contact the website admin/owner.
* The website is visible in all screen sizes.
* The unregistered User can register an account via the "Register" page.
* The register User can log in via the log in link in the navbar.
* The User can log out via the log out link in the navbar.
* Any User can browse different climbing products.
* Any User can buy different climbing products.
* Any User can checkout securely.
* Any User can see confirmations / error messages when completing actions on the website.
* Any User can receive confirmation emails for order when compliting order form during checkout.
* The register user can save delivery information safely.
* The admin can modify , edit and remove products / categries via admin page.
* The products and user information will be strored in a Sql type database.

### **_Features to be implemented_**

* Ability to log in via social media.
* Add side advertisement in product page.
* Add special offers in product page.
* Add ability to pay via paypal and other payment methods.
* Add the star rating to reviews to enable the automatic update of product's rating when a customer adds a review.


## **_Technology Used_** 

* [HTML](https://en.wikipedia.org/wiki/HTML) has been used in this project because is the standard markup language for documents designed to be displayed in a web browser.

* [CSS](https://en.wikipedia.org/wiki/CSS)
is a style sheet language. It is used to style markup language such as HTML.

* [Gitpod](https://gitpod.io) has been used as an on-line IDE followed by [Heroku](https://www.heroku.com/) for deployment. IDE is a software application used by computer programmers for software development.
* [Github](https://github.com/) has been used to store the code.
* Stripe

## **_Testing_**  

For the testing section please refer to TESTING.md file.

## **_Bugs and fixes_*

* Due to some of my products having numbers and other product having sizes and other product having no sizing and no numbers, I had a problem with my cart.view.py where I could not work out the right looping methods to adjust the bags. After trying a few different methods and with the help of tutoring I have manage to create all the functions with consistent "if statements".

* When updating products via cart I had an issue with the product that are shoes which has a number. When adding the product to the cart everything is correct but If I update the shoes in the cart the value for number doesn't show and also N/A doesn't show. At the end with tutoring we discovered that the issue was in the cart.html specifically an issue with the variable used.

* At checkout Stripe payment where the card details need to be entered, the postcode area let input a number indefinetly without stopping after the 5th digit. I cannot find a solution to this but it does not cause any issue for the payment. The event in the Stripe dashboard is flagged as succeded and also the order is saved in the admin panel. After fixing the issue with gitpod this problem has disappeared. Now the postcode area input accepts only 5 numbers.

* When viewing some products in the products_details page, some of the product description are not rendering the same as the others. I have tried to remove or add more description but the result does not change.


## **_Deployment_**
### **_Local deployment_**
### **_Heroku deployment_**

## **_Credits_**

* This project is inspired by [GoOutdoors](https://www.gooutdoors.co.uk/). The code is taken by following the Boutique Ado project from Code Institute. On top of codes and functions you can see the reference for the code.
* To adjust the font size ,for mobile view, of the icons in the navbar-mobile, the toggle-button and the increse/decrese buttons in product detail page, the code come from Boutique Ado.
* To use the widget from Django for the contact form I looked at this post from [StackOverflow.com](https://stackoverflow.com/questions/4101258/how-do-i-add-a-placeholder-on-a-charfield-in-django).
* To start the reviews app I have looked at [Slack](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1622458371215100) 
* To start the wishlist app I have looked at [Slack](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1613328233372000?thread_ts=1613310583.353100&cid=C7HS3U3AP)




color main #545659
color 2nd  #92a396
color 2nd  #9c9c9c
