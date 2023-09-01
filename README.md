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

- Python
- Firebase Admin SDK
- BigQuery
- Google Data Studio
- HTML/CSS
- Faker
- pytz
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

Go to the extensions pane and install “Stream Firestore to BigQuery”  extension for each collection. 
This extension transfer data from Firestore to Bigquery

## Generating Mock Data

### Run the Script

Execute the Python script to populate your Firestore database with mock data:

bash
python [mock_data_firebase.py](https://github.com/engnp/Roofstacks_Case_Solution/blob/3d1f005f94069445c18ba1b3e5050110ab9e5002/mock_data_firebase.py)


This script will:

Generate 1000 mock user records in the Users collection.
Generate between 0 and 7 mock item records for each user in the Items collection.

## Processing Data in BigQuery

Go to the https://console.cloud.google.com/ and select your project which one is related with firebase. 
Find your dataset and related view coming from firebase

You can process your data with sample codes and make it meaningful for users.
bash
- [Items.sql](https://github.com/engnp/Roofstacks_Case_Solution/blob/4ee1b145458c5d3b1835f3683002b89682c5f6e1/Items.sql)
- [Users.sql](https://github.com/engnp/Roofstacks_Case_Solution/blob/4ee1b145458c5d3b1835f3683002b89682c5f6e1/Users.sql)

## Processing Data in BigQuery

After the view with your processed data are ready. 
You can use this query to build your model to visualize your data
bash
- [model_query.sql](https://github.com/engnp/Roofstacks_Case_Solution/blob/3d1f005f94069445c18ba1b3e5050110ab9e5002/model_query.sql)
This model include all users & items data

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

You can go to the file([roofstacks.html](https://github.com/engnp/Roofstacks_Case_Solution/blob/3d1f005f94069445c18ba1b3e5050110ab9e5002/roofstacks.html)) to view sample report.
Download the file and open it with any browser.

Run a simple HTTP server to serve your web app:

bash
python -m http.server 8000


Navigate to http://localhost:8000 to view your embedded Data Studio report.

#Sample Screanshots

Are there in blabla folder
