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

The html files has been validating using [W3 markup validator](https://validator.w3.org/).
I have a warning for the javascipt attribute type marked as unecessary which is present in the majority of the pages.
I also have an error coming from the html which state "Stray end tag div".
Pages affected:

1. Profile
2. Wishlist
3. Product menu
4. Log in

I have checked all the html via the validator and by hand without founding the missing bracket. It appears to be prominent in the pages under the account menu in the navbar. I have checked the includes for the mobile-top-header.html and includes main-nav.html without founding the issue. I cannot see any wrong displaying of the pages in the live site. Please refer to the picture below.
[HTML Error](docs/validator1.jpg)

To validate the css I have used [W3 css validator](https://jigsaw.w3.org/css-validator/).
No error or warnings detected.

To validate javascript files I have used [Jshint](https://jshint.com/).
No error detected.

Python code as been checked for PEP8 standard. The only errors left in the Python pages are only present in pages pre created by Django.

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
Clicking the "All products" link in the "Our product" dropdown | dispay all product | Yes
Clicking the "Equipment" link | Open drop down menu |Yes  
Clicking the "Ropes" link in the "Equipment" dropdown | Display all rope products | Yes
Clicking the "Helmets" link in the "Equipment" dropdown | Display all helmet product | Yes
Clicking the "Harnesses" link in the "Equipment" dropdown | Display all harnesses product | Yes
Clicking the "Clothing" link | Open drop down menu |Yes  
Clicking the "Shoes" link in the "Equipment" dropdown | Display all shoes products | Yes
Clicking the "Trousers" link in the "Equipment" dropdown | Display all torusers product | Yes
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
Clicking on the "category" link in the product card | Redirect to the products' category displaing all product in that category | Yes
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
Clicking "go to checkout" button in the message confirmation box | redirect to the checkout pgae | Yes
By clicking "Keep shopping " button | Redirect to the product page | Yes
Clicking on the "category" link | Redirect to the products' category displaying all product in that category | Yes
Clicking on "edit" product link | Redirect to the edit product page to related product selected, message alert displayed | Yes
Clicking on "delete" product link | Delete the related product also in database and message confirmation appear | Yes
Clicking on "Add review" | Redirect to add review page | Yes
Clicking on "Edit" review link if review is present| Redirect to edit review page | Yes
Clicking on "Delete" review link if review is present | Review deleted, remove from database and message confirmation displayed | Yes


#### **_Add review page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
By clicking the "Add review" button without writing in the text box | Message "Please fill in this field" apper | Yes
By clicking the "Cancel" button | Redirect to product detail page | Yes
Filling the text box and click "Add Review" button |Redirected to product detail page, review added to product, added to database and message confirmation displayed| Yes


#### **_Edit review page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking on "Edit" review link if review is present| Redirect to edit review page | Yes
Modifing the text then click "Edit review" button | Edit review , edit in database message confirmation displayed| Yes
By clicking the "Cancel" button | Redirect to product detail page | Yes


#### **_Product menu page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking category dropdown | Showing all categories | Yes
Clicking has sizes dropdown | Showing Unknown ,yes,no | Yes
Clicking has numbers dropdown | Showing Unknown ,yes,no | Yes
By not filling the star marked field | Message "Please fill in this field" appear | Yes
Clicking "Select Image" button | Opens a windows to select picture from harddisk | Yes
By filling the form completelyand clicking " Add product" button | Form submitted , message confirmation displayed, product added to database | Yes
Clicking "Cancel" button | Redirect to products page | Yes


#### **_ Edit Product page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Modifing the fields, filling the starred field  clicking "edit product" button | Product modified and message confirmation displayed | Yes
Selecting the remove box and clicking "edit product" button | Picture succesfully removed | Yes
Clicking "Select Image" button | Opens a windows to select picture from harddisk | Yes
If the starred fields are not populated | Message "Please fill in this field" appear on field not populated, form cannot be submitted | Yes
Clicking "Cancel" button | Redirect to products page | Yes


#### **_ Profile page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking country dropdown | Showing all country | Yes
Populating the fields in the form and click "Update information" button | Details fo user saved in database and message confirmation displayed | Yes
Clicking on the Order number link | Redirect to display the order selected | Yes


#### **_ Order history page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking "Back to profile" button | Redirect to profile page | Yes


#### **_ Wishlist page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking "Add to cart" button | Redirect to product details page for the selected product | Yes
Clicking "Delete" link | Product removed from wishlist and message confirmation displayed  | Yes
Clicking "Keep shopping" button | Redirect to products page | Yes


#### **_ Logout page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking "Cancel" button | Redirect to landing page | Yes
Clicking "Sign out" button | Redirect to landing page as logged out user | Yes


#### **_ Login page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Not filling the fields in the form and pressing "Sign in" button | Message "Please fill in this field" appear on field not populated | Yes
By filling the form correctly | User logged in | Yes
By selecting the "Remember me" box | User logged in and credential saved for next  | Yes


#### **_ Cart page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Clicking the plus or minus button in the quantity box | Number is changing related to the plus or minus click | Yes
Clicking the "Update" link after selecting a new quantity | Message confirmation displayed with pricing and quantiy updated | Yes
Clicking the "Delete" link | Irem removed form the cart | Yes
Clicking the "Checkout" button | Redirect to checkout page | Yes
Clicking the "Keep shopping" button | Redirect to products page | Yes


#### **_ Checkout page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Not filling the fields in the form marked with the * and pressing "Complete Order" button | Message "Please fill in this field" appear on field not populated | Yes
Clicking the dropdown menu "Coutnry" | Display all countries | Yes
By filling the mandatory field and using the Stripe card number for testing "4242 4242 4242 4242  04 / 24  242  42424" then click "Complete Order" | Redirect to Checkout success page, Success message displayed, confirmation email reveived ( Also in terminal) with correct order number, order details, user's details and email address, Stripe Webhooks Succeded for "payment_intent.created", "payment_intent.suceeded", "Charge.suceeded", Webhooks received in terminal 200 message, Stripe Events dashboard " new payment created" and "The payment Succeeded" | Yes

#### **_ Checkout success page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Page correctly display User's email address, Order number and order details | All detaild displaying correctly after success paymnet | Yes
Clicking the "Keep shopping" button | Redirect to products page | Yes

#### **_ Contact us page_**
action taken | expected result | functional 
------------ | --------------- | --------- |
Not filling the fields in the form marked with the * and clicking "Send" button | Message "Please fill in this field" appear on field not populated | Yes
By filling the mandatory field and clicking "Send" button | Message confirmation displayed and in terminal received | Yes
DO NOT FORGET TO CHECK IF EMAIL ARRIVES IN INBOX AFTER DEPLOYMENT.