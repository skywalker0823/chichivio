# Personal website with CICD
## Introduction
A static website, and CICD with love.
推版到部署，一鍵完成。
https://violin.vivien.fun/

On push to main branch, the website will be deployed to GCP cloud run.

### Cloud Build
When a push is made to the main branch, the Cloud Build will be triggered. The Cloud Build will build and push the image to Artifact Registry. Then, will deploy the website to Cloud Run.

### Cloud Run
The Cloud Run will pull the image from Artifact Registry and deploy the fresh website.

### CloudFlare
The CloudFlare will cache the website and provide CDN service.

### Google Storage(working)

### Cloud SQL(working)