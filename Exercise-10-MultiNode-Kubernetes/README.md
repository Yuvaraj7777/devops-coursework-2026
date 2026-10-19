# Exercise 10: Multi-Node Kubernetes Cluster

## Objective

Deploy two Flask applications on a three-node Minikube cluster, using multiple replicas distributed across different nodes.

## Applications

| Application | Replicas | Namespace | Endpoint |
|---|---:|---|---|
| Product Catalog | 2 | default | `/products` |
| Shopping Cart | 3 | devops-exercise | `/cart` |

Both applications are exposed using NodePort services.

## Prerequisites

- Docker Desktop
- Minikube
- kubectl
- Python Flask applications and Dockerfiles

## 1. Start the cluster

```powershell
minikube start --nodes 3 -p devops-multinode --force
minikube -p devops-multinode addons enable registry
kubectl get nodes -o wide
```

## 2. Build Docker images

Run these commands from the Exercise 10 folder.

```powershell
docker build -t product-catalog:latest -f Dockerfile.product .
docker build -t shopping-cart:latest -f Dockerfile.shopping .
```

## 3. Load images into Minikube

```powershell
minikube -p devops-multinode image load product-catalog:latest
minikube -p devops-multinode image load shopping-cart:latest
```

## 4. Create the namespace and deploy applications

```powershell
kubectl create namespace devops-exercise
kubectl apply -f product_catalog_deployment.yaml
kubectl apply -f shopping_cart_deployment.yaml
kubectl apply -f product_catalog_service.yaml
kubectl apply -f shopping_cart_service.yaml
```

If the namespace already exists, Kubernetes may report that it already exists; continue with the deployment commands.

## 5. Verify deployments and node distribution

```powershell
kubectl get deployments -A
kubectl get pods -n default -o wide
kubectl get pods -n devops-exercise -o wide
kubectl get services -A
```

Expected replicas:

- Product Catalog: 2
- Shopping Cart: 3

Required pod anti-affinity should distribute replicas of each application across separate nodes.

## 6. Test the applications

Use Minikube to open each service:

```powershell
minikube -p devops-multinode service product-catalog-service
minikube -p devops-multinode service shopping-cart-service -n devops-exercise
```

Use the URLs displayed by Minikube to test the endpoints.

Product Catalog:

```text
GET /products
```

Expected response: a JSON array containing Laptop, Phone and Headphones.

Shopping Cart:

```text
GET /cart
```

Expected initial response:

```json
[]
```

Add an item:

```text
POST /cart
Content-Type: application/json

{"id": 1, "name": "Laptop", "quantity": 1}
```

Expected response: HTTP 201 and a JSON array containing the added item.

## 7. Evidence

Save screenshots in the `evidence/` folder showing:

- All three Kubernetes nodes in Ready state
- Both Deployments and their replica counts
- Pods distributed across nodes
- NodePort services
- Product Catalog JSON response
- Shopping Cart GET and POST responses

## Conclusion

This exercise demonstrates multi-node Kubernetes deployment, replica management, pod anti-affinity, container image deployment and NodePort service exposure.
