import streamlit as st
import os
local_dir = 'streamlits3sedownload' 
bucket_name = 'sentiment3193'
st.title("Sentiment Analysis Using TineBERT")
import boto3
from transformers import pipeline
import torch
def download_s3_directory(bucket_name, local_dir, s3_prefix=''):
    s3 = boto3.client('s3')

    # Ensure the local directory exists
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # List all objects within the specified prefix (or root if prefix is empty)
    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        if 'Contents' in page:
            for obj in page['Contents']:
                s3_key = obj['Key']

                # Remove the prefix from the S3 key to create the local file path
                local_file_path = os.path.join(local_dir, os.path.relpath(s3_key, s3_prefix))

                # Ensure the local directory for the file exists
                local_file_dir = os.path.dirname(local_file_path)
                if not os.path.exists(local_file_dir):
                    os.makedirs(local_file_dir)

                # Download the file from S3
                s3.download_file(bucket_name, s3_key, local_file_path)
                print(f"Downloaded {s3_key} to {local_file_path}")

# Example usage
bucket_name = 'sentiment3193'
 # Local directory to download to
button = st.button("Download model")
if button:
    with st.spinner("Downloading model...please wait"):


        download_s3_directory(bucket_name, local_dir)
text = st.text_area("enter text")
predict = st.button("Predict")

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

classifier = pipeline('text-classification', model='streamlits3sedownload', device=device)
if predict:
    with st.spinner("Predicting..."):
        output = classifier(text)
        st.write(output)
        # st.info(output)
