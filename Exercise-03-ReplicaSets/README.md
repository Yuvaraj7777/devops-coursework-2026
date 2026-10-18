\# Exercise 3: Scaling Flask App Using ReplicaSets



\## Objective

Deploy a Flask-based flash-sale application on Kubernetes using a ReplicaSet with three replicas.



\## Application Endpoints

\- `/` — Returns a welcome message, pod hostname, and timestamp.

\- `/buy?user=Yuvaraj` — Simulates a purchase and returns a randomly selected product, username, and serving pod.

\- `/health` — Returns the application health status and pod hostname.



\## Technologies Used

\- Python and Flask

\- Gunicorn

\- Docker

\- Kubernetes and Minikube

\- YAML



\## Implementation

1\. Created the Flask application and Dockerfile.

2\. Built the `flashsale:1.0` image inside Minikube.

3\. Created the `flashsale-rs` ReplicaSet with three replicas.

4\. Configured readiness and liveness probes using `/health`.

5\. Created the `flashsale-svc` ClusterIP Service.

6\. Tested the homepage, health-check, and purchase endpoints using port forwarding.



\## Verification

All three Flash Sale pods reached `1/1 Running`. The ReplicaSet reported three desired, current, and ready replicas. All three application endpoints returned successful responses.



\## Evidence

Screenshots are stored in the `Evidence` folder:

\- `01-replicas-running.png`

\- `02-api-tests.png`

\- `03-replicaset-status.png`



\## Deployment Commands



```powershell

kubectl apply -f .\\flashsale-replicaset.yaml

kubectl get pods -l app=flashsale

kubectl get replicasets

kubectl port-forward service/flashsale-svc 8080:80

```



With port forwarding running, access the homepage at `http://localhost:8080/`.



