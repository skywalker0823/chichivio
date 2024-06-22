# Personal website with CICD

* Now using GCP CICD to deploy the website to Cloud Run.

## Introduction
https://pikxl.link/

## 待
1. TG
2. Grafana
3. CloudFunction API 串接


On push to main branch, the website will be deployed to GCP cloud run.

<img width="1139" alt="截圖 2023-02-22 下午3 07 15" src="https://user-images.githubusercontent.com/56625237/220548044-e5b6db60-7411-4fff-84d4-f152bdf2eba6.png">

## General Architecture
### Cloud Build/CodeBuild
When a push is made to the main branch, the Cloud Build will be triggered. The Cloud Build will build and push the image to Artifact Registry. Then, will deploy the website to Cloud Run.

### Cloud Run
The Cloud Run will pull the image from Artifact Registry and deploy the fresh website.

### Cloud Functions
When new content is pushed to the main branch and deployed to Cloud Run, the Cloud Functions will automatically triggered cloudFlare to purge the cache.

### Secret Manager
The secret manager is used to store the token of the cloudFlare and other keys.

## Databases
### Database-MongoDB Atlas
The database is hosted on MongoDB Atlas, used to store the comments of the website.

## Static files storage

### CloudFlare
The CloudFlare will cache the website and provide CDN service.

### Google Storage(working)


