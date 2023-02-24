# Personal website with CICD
## Introduction
A static website, and CICD with love.
推版到部署+快取清理，一鍵完成。
https://violin.vivien.fun/

On push to main branch, the website will be deployed to GCP cloud run.

<img width="1139" alt="截圖 2023-02-22 下午3 07 15" src="https://user-images.githubusercontent.com/56625237/220548044-e5b6db60-7411-4fff-84d4-f152bdf2eba6.png">


### Cloud Build
When a push is made to the main branch, the Cloud Build will be triggered. The Cloud Build will build and push the image to Artifact Registry. Then, will deploy the website to Cloud Run.

### Cloud Run
The Cloud Run will pull the image from Artifact Registry and deploy the fresh website.

### CloudFlare
The CloudFlare will cache the website and provide CDN service.

### Cloud Functions
When new content is pushed to the main branch and deployed to Cloud Run, the Cloud Functions will automatically triggered cloudFlare to purge the cache.

### Database-MongoDB Atlas
The database is hosted on MongoDB Atlas, used to store the comments of the website.

### Pub/Sub(working)

### Google Storage(working)




## How to use
### Development mode
* python3 -m venv venv(only need to do once, if you have already created a virtual environment, you can skip this step)
* source venv/bin/activate
* pip install -r requirements.txt
* python3 run.py
* open 127.0.0.1:5000
