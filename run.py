from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')


# K8S test
# kubectl apply -f deployment.yaml
# kubectl get deployments
# kubectl apply -f service.yaml
# kubectl get svc

# DELETE
# kubectl delete -f deployment.yaml
# kubectl delete -f service.yaml
