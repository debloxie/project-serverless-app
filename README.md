# project-serverless-app PROJECT
Serverless Python CRUD application with CI/CD using Github Actions

---

# 📘 **Serverless CRUD API — AWS Lambda, API Gateway, DynamoDB, Terraform, GitHub Actions**

A fully serverless CRUD API built on AWS using:

- **AWS Lambda (Python 3.11)**
- **API Gateway (REST API)**
- **DynamoDB (NoSQL)**
- **Terraform (Infrastructure as Code)**
- **GitHub Actions (CI/CD)**

This project demonstrates real‑world cloud engineering skills including IaC, serverless architecture, automated deployments, and API design.  
Recruiters, engineers, and hiring managers can deploy, test, and extend this API easily.

---

## 🚀 **Features**

### ✔ Fully serverless CRUD API  
- `POST /items` — Create an item  
- `GET /items` — List all items  
- `GET /items/{id}` — Get a single item  
- `PUT /items/{id}` — Update an item  
- `DELETE /items/{id}` — Delete an item  

### ✔ Infrastructure as Code  
All AWS resources are provisioned using **Terraform**.

### ✔ CI/CD Pipeline  
Every push to `main` triggers GitHub Actions to:

1. Run Terraform Init  
2. Run Terraform Plan  
3. Deploy automatically with Terraform Apply  

### ✔ Zero servers to manage  
No EC2, no containers — fully serverless.

---

## 🏗 **Architecture Diagram**

```
Client → API Gateway → Lambda → DynamoDB
```

- API Gateway handles routing  
- Lambda executes Python handlers  
- DynamoDB stores items  
- Terraform provisions everything  
- GitHub Actions deploys automatically  

---

## 📂 **Project Structure**

```
project-serverless-app/
│
├── app/
│   ├── handlers/
│   │   ├── create.py          # Unified CRUD Lambda with structured logging
│   │   ├── health.py          # Health check Lambda endpoint
│   │   └── utils.py           # DynamoDB helper functions
│   ├── requirements.txt       # Python dependencies for Lambda packaging
│   └── __init__.py
│
├── terraform/
│   └── dev/
│       ├── main.tf            # API Gateway, Lambda, DynamoDB, IAM
│       ├── monitoring.tf      # CloudWatch alarms (Lambda errors)
│       ├── variables.tf       # Input variables
│       ├── outputs.tf         # API URL + resource outputs
│       ├── versions.tf        # Terraform + provider versions
│       └── terraform.tfvars   # Environment-specific values
│
└── .github/
    └── workflows/
        └── deploy.yml         # CI/CD pipeline (Terraform Init/Plan/Apply)

---

## 🔧 **Prerequisites**

To deploy locally:

- Terraform ≥ 1.5  
- AWS CLI configured  
- Python 3.11  

To use CI/CD:

- GitHub repository  
- GitHub Secrets configured:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION`

---

## 🚀 **Deployment (CI/CD)**

This project uses **GitHub Actions** to deploy automatically.

### 1. Add GitHub Secrets  
Go to:

```
GitHub → Repo → Settings → Secrets → Actions
```

Add:

| Secret Name | Value |
|------------|--------|
| `AWS_ACCESS_KEY_ID` | IAM user access key |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret key |
| `AWS_REGION` | e.g., `us-east-1` |

### 2. Push to `main`  
Every push triggers:

- Terraform Init  
- Terraform Plan  
- Terraform Apply  

Your API updates automatically.

---

## 🌐 **Testing the API**

After deployment, Terraform outputs your API URL:

```bash
terraform output api_invoke_url
```

Example:

```
https://abc123.execute-api.us-east-1.amazonaws.com/dev
```

## Live API Endpoint
https://ofa40fsjk7.execute-api.us-east-1.amazonaws.com/dev/

You can test the API using:
curl "$API_URL/items"

### 🔹 **Create an item**

```bash
curl -X POST "$API_URL/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "description": "MacBook Pro"}'
```

### 🔹 **List all items**

```bash
curl "$API_URL/items"
```

### 🔹 **Get a single item**

```bash
curl "$API_URL/items/<id>"
```

### 🔹 **Update an item**

```bash
curl -X PUT "$API_URL/items/<id>" \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated", "description": "Updated description"}'
```

### 🔹 **Delete an item** Monitoring & Observability

```bash
curl -X DELETE "$API_URL/items/<id>"

MONITORING & OBSERVABILITY
 
This project includes lightweight, zero‑cost observability features similar to real production systems.

1. Health Check Endpoint
A dedicated health endpoint verifies API uptime and deployment status.
Endpoint:

GET /health


Example:

curl "https://YOUR-API-ID.execute-api.us-east-1.amazonaws.com/dev/health"


Sample Response:

{
  "status": "ok",
  "timestamp": 1700000000
}


STRUCTURED LOGGING (CloudWatch Logs)

All Lambda functions use structured JSON logging:
{
  "action": "create_item",
  "status": "success",
  "item_name": "Television",
  "timestamp": 1700000000
}


Benefits:
- Easy filtering in CloudWatch Logs
- Clear operational visibility
- Production‑grade debugging patterns

CLOUDWATCH ALARM FOR LAMBDA ERRORS

A CloudWatch alarm monitors Lambda failures:

This helps detect issues immediately.

CLOUDWATCH LOGS INSIGHTS QUERIES

Use these queries to analyze API behavior.
🔹 Recent Errors
fields @timestamp, @message
| filter @message like /"status":"error"/ or @message like /ERROR/
| sort @timestamp desc
| limit 50


🔹 Latency Distribution
fields @timestamp, @duration
| stats avg(@duration), max(@duration), pct(@duration, 95) by bin(1h)
| sort bin(1h) desc


```

---

## 🧪 **Local Development**

To test Lambda locally:

```bash
cd app
python handlers/create.py
```

Or use AWS SAM / LocalStack (optional).

---

## 🛠 **Terraform Commands**

Initialize:

```bash
terraform init
```

Plan:

```bash
terraform plan
```

Apply:

```bash
terraform apply
```

Destroy:

```bash
terraform destroy
```

---

## 🔒 **IAM & Security**

This project uses a dedicated IAM user:

- Least‑privilege permissions  
- Access keys stored in GitHub Secrets  
- No hardcoded credentials  


---

## 👤 **Author**

**Adebo Olufemi Ogunrinde**  
Cloud Operations Engineer | AWS | Terraform | Python | DevOps  
GitHub: https://github.com/debloxie  

---

## 📝 **License**

MIT License — free to use, modify, and distribute.


