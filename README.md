# Manage-Followers-For-Instagram
Project that lists people you follow, that dont follow you back and/or vise versa
Requires that the instagram user has a public account</br></br>

##Unfinished project!!! </br></br>

#Instructions
Set Up Configuration: Replace placeholders in config.py with your actual Instagram app credentials.
Install Dependencies: Run pip install -r requirements.txt to install the required packages.
Run the Application: Execute python main.py to start the Flask server.
Authorize the App: Open a web browser and go to http://127.0.0.1:5000/. Click the "Login with Instagram" link, authorize the app, and handle the callback to see the result.

#Clarification of files
config.py: Contains configuration details such as client ID, client secret, and redirect URI.
instagram_api.py: Handles interactions with the Instagram API (getting the authorization URL, exchanging code for access token, and fetching followers and following lists).
main.py: Uses Flask to create a web server that handles user login and displays the results.
requirements.txt: Lists the dependencies needed for the project

#How to get client ID and client secret
First create Facebook Developer Account
When logged in, go to App Dashoard
Navigate to and press "create app"
Follow the following instructions, make sure to choose Instagram Basic Display (and Instagram Graph API)
Configure instagram basic display, add a test instagram user. The instagram user will receive an invitation which they have to accept. 
Inn your app dashboard under instagram basic display, you will now see your client id and client secret
