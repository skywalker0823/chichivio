from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')



# How to exit venv?
# deactivate

# About Docker running at local
# docker image build -t chi_vio .
# docker run --env-file .env -dp5000:5000 --name chi_vio_container chi_vio
# Limit hardware edition:
# docker run --env-file .env -dp5000:5000 --name chi_vio_container --cpus=1 --memory=512m chi_vio
# open 127.0.0.1:5000

# Start website with docker-compose
# docker-compose -f docker-compose.yaml up -d --build(Development)
# Open localhost on browser(sometimes need to wait for mysql and flask to start completely)
# docker-compose down

# Development mode
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# python3 run.py
# open 127.0.0.1:5000


# Production mode
# Use -> waitress <- as a WSGI server, easy to use
# pip install waitress
# waitress-serve --port=5000 run:app


# K8S test
# kubectl apply -f deployment.yaml
# kubectl get deployments
# kubectl apply -f service.yaml
# kubectl get svc

# DELETE
# kubectl delete -f deployment.yaml
# kubectl delete -f service.yaml
