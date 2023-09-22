# Purpose

Detects Sentiment in a given data set using Google Cloud's Natural Language API and generates magnitude, score, and identifies entities present in the data.

# Instructions

Create a Service Account on Google Cloud
          
        IAM & Admin --> Service Account --> Create Service Account.

Create a new key

        Manage keys --> Create New Key (JSON)

Clone the repository to your local machine

        git clone https://github.com/HarisMahmood8/Sentiment_Analysis.git

Install the necessary packages

        pip install google-cloud-language

Replace the "credential_path" variable with the address of the JSON key on your machine

Change the directory to Collecting Daily Prices

        cd "Sentiment_Analysis/Sentiment_Analysis_GCP"

Execute

        python3 sentimentcode.py

        
