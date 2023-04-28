# Personal website with CICD
## Introduction
A static website, and CICD with love.
推版到部署+快取清理，一鍵完成。
~~https://violin.vivien.fun/~~ (暫時關閉)

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

### Secret Manager
The secret manager is used to store the token of the cloudFlare.

### Pub/Sub(working)

### Google Storage(working)




## How to use
### Development mode
* python3 -m venv venv(only need to do once, if you have already created a virtual environment, you can skip this step)
* source venv/bin/activate
* pip install -r requirements.txt
* python3 run.py
* open 127.0.0.1:5000
* Exit venv : deactivate

### Docker mode on local
* docker image build -t chi_vio . (Don't miss the ".")
* docker run -dp5000:5000 --name chi_vio_container chi_vio
* open 127.0.0.1:5000

### Production mode for uWSGI(uwsgi)(still configuring)
* pip install uwsgi
* pip freeze > requirements.txt
* (uwsgi --ini uwsgi.ini) for local test
* docker image build -t chi_vio Dockerfile.prod
* docker run -dp5000:5000 --name chi_vio_container chi_vio

