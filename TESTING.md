## **_Testing_**

### **_Browser compatibility_**
  
The project has been tested in the following browsers without any compatibility issue:  
* Google Chrome    
* Microsoft Edge  
* Firefox  
* Opera  

The project has also been tested on different screen sizes. 15" and 14" inch laptop, 24" screen and 20" screen.

### **_Responsiveness_**

As already specified in the "Surface" part in README file, the project has been developed with mobile first approach.

The project has been tested in mobile view in the following devices without any compatibility issue: 

* Motorola G5, G8 and G9
* Iphone 6
* Ipad 2

### **_Automated testing_**

The HTML files has been validating using [W3 markup validator](https://validator.w3.org/).
No error or warnings detected.

To validate the CSS I have used [W3 CSS validator](https://jigsaw.w3.org/css-validator/).
No error or warnings detected.

To validate JavaScript files I have used [Jshint](https://jshint.com/).
No error detected.


To validate Python code I have used [Pep8 online](http://pep8online.com/checkresult) and the built in Flake8 in Gitpod. The only errors left in the Python pages are only present in pages pre created by Django, migrations file and settings.py file.

I have also used [Google Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools) to test this project.

Below are the screen shots for the Lighthouse testing for mobile and desktop views.  

[desktop](docs/light_house_desktop.jpg)

[mobile](docs/light_house_mobile.jpg)

### **_Manual testing_**

#### **_Landing page_**

action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking "Enter" button | Redirect to Product page | Yes
Clicking "Contact us" icon | Redirect to the Contact page | Yes

#### **_Nav bar_**

action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking the "Logo" | Redirected to landing page | Yes  
Clicking the "Account" link | Open drop down menu | Yes  
Clicking the "Register" link in the "Account" dropdown | Redirect to register page | Yes
Clicking the "Login" link in the "Account" dropdown | Redirect to login page | Yes
Clicking the "Profile" link in the "Account" dropdown | Redirect to profile page | Yes
Clicking the "Wishlist" link in the "Account" dropdown | Redirect to wishlist page | Yes
Clicking the "Logout" link in the "Account" dropdown | Redirect to logout page | Yes
Clicking the "Products menu" link in the "Account" dropdown (Only visible to superuser)| Redirect to add product page | Yes
Clicking the "Cart" icon | Redirect to the Cart page | Yes  
Writing in the search bar | Return the items searched | Yes  
Clicking the "Our product" link | Open drop down menu |Yes  
Clicking the "Price" link in the "Our product" dropdown | Display product by price | Yes
Clicking the "Ratings" link in the "Our product" dropdown | display product by ratings | Yes
Clicking the "Categories" link in the "Our product" dropdown | display product by categories | Yes
Clicking the "All products" link in the "Our product" dropdown | display all product | Yes
Clicking the "Equipment" link | Open drop down menu |Yes  
Clicking the "Ropes" link in the "Equipment" dropdown | Display all rope products | Yes
Clicking the "Helmets" link in the "Equipment" dropdown | Display all helmet product | Yes
Clicking the "Harnesses" link in the "Equipment" dropdown | Display all harnesses product | Yes
Clicking the "Clothing" link | Open drop down menu |Yes  
Clicking the "Shoes" link in the "Equipment" dropdown | Display all shoes products | Yes
Clicking the "Trousers" link in the "Equipment" dropdown | Display all trousers product | Yes
Clicking the "Camping" link | Open drop down menu |Yes  
Clicking the "Tent" link in the "Equipment" dropdown | Display all tent products | Yes
Clicking the "Sleeping bags" link in the "Equipment" dropdown | Display all sleeping bags product | Yes
Clicking the "Climbing shoes" link | Open drop down menu |Yes  
Clicking the "Mens" link in the "Equipment" dropdown | Display all Mens climbing shoes products | Yes
Clicking the "Womens" link in the "Equipment" dropdown | Display all womens climbing shoes product | Yes


#### **_Product page_**

action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking on any product image | Redirect to the product detail page of the selected product | Yes
Clicking on "edit" link in the product card | Redirect to the edit product page to related product selected, message alert displayed | Yes
Clicking on "delete" link in the product card | Delete the related product also in database and message confirmation appear| Yes
Clicking on the "category" link in the product card | Redirect to the products' category displaying all product in that category | Yes
Clicking in the sort box | Drop down menu display | Yes
Clicking "Price low to high" link in the sort box drop down | Display products by low to high price | Yes
Clicking "Price high to low" link in the sort box drop down | Display products by high to low price | Yes
Clicking "Rating high to low" link in the sort box drop down | Display products by high to low ratings | Yes
Clicking "Rating low to high" link in the sort box drop down | Display products by low to high Rating | Yes
Clicking "Name (A-Z)" link in the sort box drop down | Display products by alphabetical order from A to Z | Yes
Clicking "Name (Z-A)" link in the sort box drop down | Display products by alphabetical order from Z to A | Yes
Clicking "Category (Z-A)" link in the sort box drop down | Display products by category order from Z to A | Yes
Clicking "Category (A-Z)" link in the sort box drop down | Display products by category order from A to Z | Yes


#### **_Product detail page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
By clicking the plus or minus button in the quantity box | Number is changing related to the plus or minus click | Yes
By adjusting the quantity box and then clicking "Add to cart" | Product added with the right quantity to cart | Yes
Clicking "Add to cart" | The selected product is added to the cart and message confirmation displayed with pricing | Yes
Clicking "go to checkout" button in the message confirmation box | redirect to the checkout page | Yes
By clicking "Keep shopping " button | Redirect to the product page | Yes
Clicking "Add to wishlist" | The selected product is added to the wishlist and message confirmation displayed | Yes
Clicking on the "category" link | Redirect to the products' category displaying all product in that category | Yes
Clicking on "edit" product link | Redirect to the edit product page to related product selected, message alert displayed | Yes
Clicking on "delete" product link | Delete the related product also in database and message confirmation appear | Yes
Clicking on "Add review" | Redirect to add review page | Yes
Clicking on "Edit" review link if review is present| Redirect to edit review page | Yes
Clicking on "Delete" review link if review is present | Review deleted, remove from database and message confirmation displayed | Yes


#### **_Add review page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
By clicking the "Add review" button without writing in the text box | Message "Please fill in this field" appear | Yes
By clicking the "Cancel" button | Redirect to product detail page | Yes
Filling the text box and click "Add Review" button |Redirected to product detail page, review added to product, added to database and message confirmation displayed| Yes


#### **_Edit review page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking on "Edit" review link if review is present| Redirect to edit review page | Yes
Modifying the text then click "Edit review" button | Edit review , edit in database message confirmation displayed| Yes
By clicking the "Cancel" button | Redirect to product detail page | Yes


#### **_Product menu page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking category dropdown | Showing all categories | Yes
Clicking has sizes dropdown | Showing Unknown, yes, no | Yes
Clicking has numbers dropdown | Showing Unknown, yes, no | Yes
By not filling the star marked field | Message "Please fill in this field" appear | Yes
Clicking "Select Image" button | Opens a window to select picture from hard disk | Yes
By filling the form completely and clicking " Add product" button | Form submitted , message confirmation displayed, product added to database | Yes
Clicking "Cancel" button | Redirect to products page | Yes


#### **_Edit Product page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Modifying the fields, filling the starred fields  clicking "edit product" button | Product modified and message confirmation displayed | Yes
Selecting the remove box and clicking "edit product" button | Picture successfully removed | Yes
Clicking "Select Image" button | Opens a windows to select picture from harddisk | Yes
If the starred fields are not populated | Message "Please fill in this field" appear on field not populated, form cannot be submitted | Yes
Clicking "Cancel" button | Redirect to products page | Yes


#### **_Profile page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking country dropdown | Showing all country | Yes
Populating the fields in the form and click "Update information" button | Details for user saved in database and message confirmation displayed | Yes
Clicking on the Order number link | Redirect to display the order selected | Yes


#### **_Order history page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking "Back to profile" button | Redirect to profile page | Yes


#### **_Wishlist page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking "Add to cart" button | Redirect to product details page for the selected product | Yes
Clicking "Delete" link | Product removed from wishlist and message confirmation displayed  | Yes
Clicking "Keep shopping" button | Redirect to products page | Yes


#### **_Logout page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking "Cancel" button | Redirect to landing page | Yes
Clicking "Sign out" button | Redirect to landing page as logged out user | Yes


#### **_Login page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Not filling the fields in the form and pressing "Sign in" button | Message "Please fill in this field" appear on field not populated | Yes
By filling the form correctly | User logged in | Yes
By selecting the "Remember me" box | User logged in and credential saved for next  | Yes


#### **_Cart page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking the plus or minus button in the quantity box | Number is changing related to the plus or minus button click | Yes
Clicking the "Update" link after selecting a new quantity | Message confirmation displayed with pricing and quantity updated | Yes
Clicking the "Delete" link | Item removed from the cart | Yes
Clicking the "Checkout" button | Redirect to checkout page | Yes
Clicking the "Keep shopping" button | Redirect to products page | Yes


#### **_Checkout page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Not filling the fields in the form marked with the * and pressing "Complete Order" button | Message "Please fill in this field" appear on field not populated | Yes
Clicking the dropdown menu "Country" | Display all countries | Yes
By filling the mandatory field and using the Stripe card number for testing "4242 4242 4242 4242  04 / 24  242  42424" then click "Complete Order" | Redirect to Checkout success page, Success message displayed, confirmation email received ( Also in terminal) with correct order number, order details, user's details and email address, Stripe Webhooks Succeeded for "payment_intent.created", "payment_intent.Succeeded", "Charge.Succeeded", Webhooks received in terminal 200 message, Stripe Events dashboard " new payment created" and "The payment Succeeded" | Yes

#### **_Checkout success page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Page correctly display User's email address, Order number and order details | All details displaying correctly after success payment | Yes
Clicking the "Keep shopping" button | Redirect to products page | Yes

#### **_Contact us page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Not filling the fields in the form marked with the * and clicking "Send" button | Message "Please fill in this field" appear on field not populated | Yes
By filling the mandatory field and clicking "Send" button | Message confirmation displayed and in terminal email printed | Yes


#### **_Error pages_**
action taken | expected result | functional 
------------ | --------------- | ----------
Add an non existing page name on URL ending | page 404 shown to user | Yes

#### **_User story_**
user story | action taken | expected result | functional 
-----------|------------ | --------------- | ----------
1 | As an unregister / register User by going to https://mountain-gear-ms4.herokuapp.com/ and then click Enter | I can view all the products | Yes
2 | As an unregister / register User by adding product to cart and then checkout | I get confirmation of my purchase via email and on the screen | Yes
3 | As an unregister / register User by going to contact page and filling the form correctly | Message confirmation displayed and email receive to developer with User's message | Yes
4, 9| As an unregister User by clicking "Register" link and filling the form correctly | Email to confirm registration received by the User and User registered in database | Yes
5 | As a registered User by filling the Log in form correctly | User logged in | Yes
6 | As a registered User by filling form correctly after clicking "Forgot password" | Email received by User with instruction to reset password | Yes
7 | As a registered User by clicking "Log out" and then confirm log out | User logged out and redirect to landing page | Yes
8 | As a registered User by clicking "Profile" link | Profile page open | Yes
10| As a unregister / register User after adding any product to the cart | The cart logo display the sum of the cost of the products added to the cart visible if navigating the site in different pages | Yes
11 | As a registered User by clicking "Profile" link | The User can see a list of orders made | Yes
12 | As a registered User by clicking "Profile" link fill the "Default delivery information" form then click " Update information | Default delivery information save in the User account and in the database | Yes
12 | As a registered User by filling the form during checkout and ticking the "Save delivery information to my profile" box | Delivery information save in the User account and in the database | Yes
13 | As a registered User by filling correctly the form during checkout |  Confirmation email with details of the purchase received | Yes 
14 | As an unregister / register User by typing products name or desciption in the search box | Products displayed correctly | Yes
15 | As an unregister / register User by clicking the "Category" link under "Our product" link | Products displaying by category | yes
16 | As an unregister / register User by clicking "Cart" logo after adding products to cart | The page shopping cart will display with the product added by the User | Yes
17 | As an unregister / register User by interacting with the website | Messages for confirmation and alert are displayed at the top right of the screen with meaningful messages related to the action taken by the User | Yes
18 | As Admin by clicking "Products menu" link under "Account" link and by filling the form correctly | Product added to the web site and in the database | Yes
19 | As Admin by going to a product detail page and clicking the "Edit" link | Edit product page open and Admin able to edit details and save edited product. Display correctly in the web site and in the database | Yes
20 | As Admin by going to the admin page and log in correctly | Access grated to the Admin panel | Yes
21 | As Admin by going to a product detail page and clicking the "Delete" link | Product removed form website and from database | Yes
22 | As Admin by going to the admin panel opening the "Review" section and selecting a review then delete review | Review deleted from website and database | Yes
23 | As Admin by going to the admin panel opening the "Wishlist" section and selecting a wishlist then delete wishlist | Wishlist deleted from website and database | Yes
24 | As Admin by going to the admin panel opening the "User" section and selecting a user then delete user | user deleted from  database | Yes
25 | As Admin by going to the admin panel opening the "Order" section and selecting an Order then delete Order | Order deleted from website and database | Yes
26 | As Admin by going to the admin panel opening the "Category" section and selecting a Category then delete Category | Category deleted from website and database | Yes
