# Personal website
## Introduction
A static website, and CICD with love.

On push to main branch, the website will be deployed to GCP cloud run.

### Cloud Build
When a push is made to the main branch, the Cloud Build will be triggered. The Cloud Build will push the image to Artifact Registry. Then, will deploy the website to Cloud Run.

### Cloud Run
The Cloud Run will be triggered by the Cloud Build. The Cloud Run will pull the image from Artifact Registry and deploy the website.

### CloudFlare
The CloudFlare will cache the website and provide CDN service.