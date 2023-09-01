# Roofstacks_Case_Solution
# Firestore and Data Studio Integration Project

This project demonstrates how to generate mock data for Firestore collections using Python, visualize it using Google Data Studio, and finally embed the Data Studio report into a simple web application.

## Table of Contents

Technologies Used
Setup
Generating Mock Data
Visualizing Data in Data Studio
Embedding Data Studio Report in Web App
## Technologies Used

Python
Firebase Admin SDK
Google Data Studio
HTML/CSS
Faker
pytz
## Setup

### Clone the Repository

bash
git clone https://github.com/engnp/Roofstacks_Case_Solution.git
cd firestore_mock_data


### Install Dependencies

Install the required Python packages:

bash
pip install firebase-admin Faker pytz


### Firebase Setup

Go to the Firebase Console and create a new project if you haven't already.
Navigate to Project settings > Service accounts, then click on "Generate new private key".
Download the serviceAccountKey.json file and place it in the project directory.
## Generating Mock Data

### Run the Script

Execute the Python script to populate your Firestore database with mock data:

bash
python mock_data_firebase.py


This script will:

Generate 1000 mock user records in the Users collection.
Generate between 0 and 7 mock item records for each user in the Items collection.
## Visualizing Data in Data Studio

Navigate to Google Data Studio and create a new report.
Connect the report to your Firestore database via BigQuery.
Design your report to visualize the data as you see fit.
## Embedding Data Studio Report in Web App

### Get the Embed Code

In Data Studio, go to File > Embed Report, and copy the iframe code.
### Modify the Web App

Open roofstacks.html in a text editor.
Replace the existing iframe code with the one you copied from Data Studio.
### Serve the Web App

Run a simple HTTP server to serve your web app:

bash
python -m http.server 8000


Navigate to http://localhost:8000 to view your embedded Data Studio report.
