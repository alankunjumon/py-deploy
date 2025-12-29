# AWS DevOps Deployment Pipeline

## Project Overview

This project demonstrates an **AWS-focused DevOps workflow** for deploying and operating a containerized Python web application on cloud infrastructure.

The system covers the **full lifecycle** from infrastructure provisioning to application deployment, configuration management, monitoring, and CI/CD automation.

The primary objective of this project is to showcase **practical DevOps responsibilities**—infrastructure as code, automated deployments, environment configuration, and operational visibility—rather than application development.

The architecture is intentionally kept **simple and single-node** to emphasize clarity, reproducibility, and explainability, while still reflecting real-world DevOps patterns used in small to mid-scale production systems.

---

## Problem Statement

Deploying applications on cloud infrastructure often involves multiple manual steps—server provisioning, environment setup, application deployment, and monitoring—which increases the risk of configuration drift, inconsistent environments, and operational errors.

This project addresses the problem of **reliable and repeatable deployment** by automating infrastructure provisioning, application deployment, and configuration using Infrastructure as Code and configuration management practices.

The goal is to demonstrate how a DevOps engineer can design a system where application changes are deployed through a controlled CI/CD pipeline, infrastructure changes are version-controlled, and operational visibility is available without manual intervention.

---

## Architecture Overview

The system is deployed on **AWS using a single EC2 instance** as the compute layer, intentionally chosen to keep the architecture simple and easy to reason about while demonstrating core DevOps workflows.

Infrastructure is provisioned using **Terraform**, which defines the cloud resources required to run the application. Once the instance is created, **Ansible** is used to configure the server, install dependencies, and deploy supporting services.

The application itself is containerized using **Docker** and executed on the EC2 instance, allowing consistent runtime behavior across environments. A **CI/CD pipeline** is responsible for building the container image and triggering deployments when changes are pushed to the repository.

**Prometheus** is configured to collect application-level metrics, and **Grafana** is used to visualize those metrics, providing basic observability into system health.

The architecture follows a clear separation of responsibilities:

- **Terraform** manages infrastructure  
- **Ansible** manages configuration  
- **Docker** manages application runtime  
- **CI/CD** manages deployment automation  
- **Prometheus and Grafana** provide monitoring  

---

## Infrastructure Components

**Terraform** is used to define and provision the cloud infrastructure required for the application. This includes the EC2 instance and associated AWS resources. Terraform execution is automated as part of the CI/CD workflow using a remote backend, with state stored in an **S3 bucket** and state locking enabled via **DynamoDB** to prevent concurrent executions.

**Ansible** is used for configuration management after infrastructure provisioning. It connects to the EC2 instance to install system dependencies, configure services, deploy the application container, and set up the monitoring stack. Ansible uses a combination of declarative Docker modules and Docker Compose commands to balance clarity and simplicity for CI/CD-driven redeployments.

**Docker** is used to package the application into a container image, enabling consistent runtime behavior across environments. The container image is built during the CI/CD process and pulled onto the EC2 instance during deployment.

This layered approach ensures that infrastructure provisioning, configuration management, and application runtime are clearly separated, minimizing configuration drift and improving reproducibility.

---

## CI/CD Workflow

A CI/CD pipeline is implemented using **GitHub Actions** and is triggered on pushes to the `main` branch or `feature/*` branches.

The pipeline is structured into three sequential jobs:

### Test
Automated tests are executed to validate application behavior before proceeding with build or deployment steps.

### Build and Push
A Docker image of the application is built and pushed to **Docker Hub**, ensuring deployment artifacts are reproducible and environment-independent.

### Deploy
The deploy stage provisions infrastructure and deploys the application. Terraform is executed using a remote backend with state locking to ensure consistent infrastructure state and prevent concurrent pipeline executions. After infrastructure provisioning, Ansible configures the EC2 instance, deploys the application container, and sets up monitoring services.

---

## Deployment Flow (Git → Production)

When changes are pushed to the repository, the CI/CD pipeline builds a new Docker image and publishes it to Docker Hub using the `latest` tag.

During the deploy stage, Ansible connects to the provisioned EC2 instance, pulls the latest application image from Docker Hub, and updates the running container.

This deployment approach prioritizes simplicity and clarity for demonstration purposes. While effective for learning and controlled environments, it does not provide explicit version pinning or automated rollback, which are addressed as future improvements.

---

## Security Considerations

Access to the EC2 instance is configured using **SSH key-based authentication**, avoiding password-based access. SSH access is restricted at the network level using **AWS security group rules**.

AWS credentials and sensitive configuration values required by the CI/CD pipeline are stored securely using **GitHub Secrets**, ensuring that secrets are not hardcoded in the repository.

The EC2 instance is **publicly accessible**, which simplifies deployment and testing but increases the attack surface. Network access is restricted to required ports only. Advanced security measures such as private networking, bastion hosts, IAM role-based instance access, and automated secret rotation are not implemented but are acknowledged as potential improvements.

---

## Monitoring & Observability

Basic observability is implemented using **Prometheus and Grafana**.

Prometheus is configured to scrape **application-level metrics** exposed by the running service. Grafana is used to visualize these metrics through dashboards, providing insight into application performance and system health.

This monitoring setup focuses on metrics collection and visualization only. Alerting and automated incident response are not implemented.

---

## Limitations & Trade-offs

- The system runs on a **single EC2 instance**, providing no high availability or fault tolerance  
- Application deployments use the `latest` Docker image tag, limiting reproducibility and rollback capability  
- The EC2 instance is publicly accessible, increasing exposure compared to private networking setups  
- Monitoring is limited to metrics visualization without alerting  

These trade-offs are intentional to keep the project focused, understandable, and suitable for demonstration purposes.

---

## Improvements & Next Steps

With additional time and scope, the following improvements could be made:

- Introduce **versioned Docker image tags** and deploy specific image versions to enable safer rollbacks  
- Separate infrastructure provisioning and application deployment pipelines with approval gates  
- Move the EC2 instance into a **private network** and introduce secure access patterns such as bastion hosts  
- Replace SSH-based access with **IAM role-based instance access**  
- Add alerting rules in Prometheus and integrate notification mechanisms  
- Expand the architecture to support horizontal scaling and higher availability  

