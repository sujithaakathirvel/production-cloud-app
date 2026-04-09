# Production Cloud Application on AWS

A production-style cloud application built on AWS demonstrating containerized workloads, infrastructure as code, CI/CD automation, and a self-healing, fault-tolerant architecture.

---

## Architecture Overview

![Architecture](screenshots/architecture-diagram.png)

---

## Architecture Decisions

- **Amazon Elastic Container Service (Fargate)** was selected to eliminate EC2 management and enable serverless container orchestration with automatic scaling.
- **Private subnets** are used for ECS services and the database to ensure no direct internet exposure and enforce network isolation.
- **Application Load Balancer (ALB)** distributes incoming traffic and performs health checks to maintain service availability.
- **Amazon RDS (PostgreSQL)** provides reliable, managed relational data storage with automated backups.
- The system follows a **stateless, horizontally scalable design**, allowing containers to scale independently.

---

## Tech Stack

**Cloud Services**
- AWS ECS (Fargate)  
- AWS RDS (PostgreSQL)  
- AWS Application Load Balancer  
- AWS ECR  
- AWS CloudWatch  
- AWS Lambda  
- AWS VPC (Public & Private Subnets)  

**DevOps & Tools**
- Terraform (Infrastructure as Code)  
- Docker (Containerization)  
- GitHub Actions (CI/CD)  

---

## Key Features

- Containerized backend deployed on ECS Fargate  
- Fully reproducible infrastructure using Terraform  
- Automated CI/CD pipeline with GitHub Actions  
- Load-balanced architecture using ALB  
- Real-time monitoring with CloudWatch  
- **Self-healing mechanism using Lambda + CloudWatch alarms**  
- Designed for **high availability and fault tolerance**

---

## Key Highlight

> Implemented an automated self-healing mechanism where CloudWatch alarms trigger a Lambda function to restart ECS services without manual intervention.

---

## CI/CD Pipeline

- Code push triggers GitHub Actions workflow  
- Docker image is built and tagged (latest + commit SHA)  
- Image is pushed to Amazon ECR  
- ECS service is updated with the new image  
- Rolling deployments ensure **zero downtime**

---

## Security

- Only ALB exposes public HTTP/HTTPS traffic  
- ECS services accept traffic only from ALB security group  
- RDS is deployed in a private subnet and not publicly accessible  
- IAM roles follow the principle of least privilege  
- Secrets are managed using AWS SSM Parameter Store / Secrets Manager  

---

## Monitoring & Observability

- CloudWatch collects logs and metrics from ECS services  
- Alarms are configured for CPU utilization and failure scenarios  
- Logs are used for debugging and performance monitoring  

---

## Resilience & Self-Healing

- ALB health checks detect unhealthy containers  
- ECS automatically replaces failed tasks  
- CloudWatch alarms trigger a Lambda function to restart ECS services  
- System is designed to recover automatically from failures  

---

## Screenshots

### Application Running
![App](screenshots/alb-app-live.png)

### ECS Service Running
![ECS](screenshots/ecs-service-running.png)

### CI/CD Pipeline Execution
![CI/CD](screenshots/github-actions.png)

### Self-Healing Logs (Lambda Trigger)
![Lambda](screenshots/lambda-self-healing-logs.png)

---

## How It Works

1. User sends request to Application Load Balancer  
2. ALB routes traffic to ECS containers (private subnet)  
3. Backend services interact with RDS database  
4. CI/CD pipeline deploys updates automatically  
5. CloudWatch monitors system health  
6. Lambda function automatically triggers recovery actions upon detecting failures 

---

## Outcome

- Fully automated deployment pipeline  
- Production-style cloud architecture  
- Fault-tolerant system with self-healing capabilities  
- Demonstrates real-world cloud engineering practices  

---

## Lessons Learned

- Designing secure VPC architectures with public/private isolation  
- Managing containerized workloads using ECS Fargate  
- Building CI/CD pipelines for automated deployments  
- Implementing monitoring, alerting, and recovery mechanisms  
- Debugging and maintaining distributed cloud systems  

---

