# Pikxl & Wizper
## Introduction
* https://wizper.cc/
* https://pikxl.link/
This is a personal project which contains multiple features.
### Message

### Chat

### GeoGuessr

## Techstacks & Tools
### Cloud
1. EC2(Ubuntu)
2. Route53(one from Route53, one from Godaddy)
3. S3(private)
4. CloudFront
5. DynamoDB/MongoDB/PlanetScale(originally for comments, now disabled)
6. IAM
7. System Manager
8. Cloud Watch
9. GitHub/Action
10. Google Cloud services attaching(pending)
11. Google Map API
12. CloudFlare
13. Grafana Cloud
14. 

### Backend & CICD & Databases
1. Flask
2. MySQL
3. SQLAlchemy
4. Docker(compose)
5. Git
6. NGINX


### Frontend
1. moment.js
2. RWD
3. HTML/CSS
4. Aseprite(All icons is hand crafted by myself)


## Memo & Todo
1. Grafana is Done.
2. DynamoDB(replaced with MySQL)
3. S3+CloudFront soon or later for image upload function is Done.
4. Websocket is Done, will add WebRTC support for streaming.
5. Taiwan Guessr(with Google map API) is good to go, but lots of things to be fixed.
6. Image uploader for message.


## DB migrate & upgrade (自動的必要性?)
1. Change the sqlalchemy database settings.
2. run -> flask db migrate -m "comments"(first time needs to run -> flask db init)
3. For local run -> flask db upgrade, then check the db is updated. Test&Check.
4. For production, After pushed to server, in "running" app container, do -> flask db upgrade, then check the db is updated. Done.



## Test area
1. IP updated.