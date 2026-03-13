# Kubernetes CI/CD Experiment: Learning & Integration

## Overview

This repository is a dedicated **learning sandbox** designed to refine my DevOps and Kubernetes skills. Rather than a final production project, this experiment serves as a hands-on test to master the integration between local development, automated pipelines, and a "bare-metal" cluster.

The primary goal was to move away from manual SSH operations and implement a modern, automated workflow, bridging the gap between writing code in WSL and seeing it live on a **Kubeadm-orchestrated** environment.

## 🏗️ Architecture

* **Application:** A simple Python Flask web server.
* **CI/CD:** GitHub Actions.
* **Container Registry:** GitHub Container Registry (GHCR).
* **Cluster:** 2-node Kubeadm cluster (Master + 1 Worker) running on Ubuntu VMs.
* **Infrastructure Management:** Orchestrated via `kubectl` directly from WSL.

## 🛠️ The Pipeline

The workflow is triggered on every `git push` to the `main` branch:

1. **Dynamic Formatting:** Automates the conversion of the repository name to lowercase to comply with Docker registry standards.
2. **Containerization:** Builds a lightweight Docker image based on `python:3.9-slim`.
3. **Secure Push:** Authenticates and pushes the artifact to **GHCR** using encrypted Personal Access Tokens (PAT).

## 🚢 Kubernetes Deployment

The deployment on the cluster features:

* **ImagePullSecrets:** Secure authentication to pull private images from GHCR.
* **Replicas:** 2 pods for basic high availability.
* **Resource Governance:** Defined `requests` and `limits` for CPU and Memory to ensure cluster stability.
* **Networking:** Exposed via a **NodePort** Service on port `30007`.

## 📝 Skills Refined & Lessons Learned

* **Automation Logic:** Solving case-sensitivity issues within GitHub Actions.
* **Remote Orchestration:** Configuring **WSL** as a professional control plane for a remote K8s cluster.
* **Secret Management:** Mastering Kubernetes Secrets for registry authentication.
* **Workload Control:** Implementing resource quotas and managing container lifecycles.

## ⚡ Quick Start

```bash
# Apply the deployment
kubectl apply -f k8s-deploy.yml

# Check pod status
kubectl get pods -l app=flask-app

# Force an update after a new image push
kubectl rollout restart deployment flask-app

```

---

