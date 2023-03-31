#!/bin/bash

cd /home/azureuser-datascience-prod/vdezi_ai_category_predictor   

git stash

git pull origin master

source ./venv/bin/activate

pip3 install -r requirements.txt 

python3 serve.py



