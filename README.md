# Phase 1: Foundation Setup – Real-Time Logistics Data Platform

## 📌 Overview

Phase 1 focuses on setting up the foundational components required to build a production-grade data engineering pipeline. This includes creating data sources, configuring cloud infrastructure, and preparing the development environment.

---

## 🏗️ Components Implemented

### 1. Development Environment

* Python virtual environment setup
* Dependency management using `requirements.txt`
* Project structure initialized in VS Code

---

### 2. AWS Setup

* Created Amazon S3 bucket to act as a Data Lake
* Implemented Medallion Architecture folder structure:

  * `bronze/` → Raw data
  * `silver/` → Cleaned data (future)
  * `gold/` → Aggregated data (future)
* Configured IAM user and AWS CLI for secure access

---

### 3. Database (Transactional Source)

* PostgreSQL database created (`logistics_db`)
* `shipments` table designed to simulate order/consignment data
* Synthetic data generated using Python (Faker library)

---

### 4. File-Based Data Source

* Created terminal scan logs in JSON format
* Simulated real-world warehouse/terminal events such as:

  * ARRIVED
  * DEPARTED
  * SCANNED

---

### 5. Real-Time API (Flask)

* Built a mock shipment tracking API
* Endpoints:

  * `/shipment` → single shipment event
  * `/shipments` → multiple shipment events
* Generates dynamic, real-time data

---

### 6. AWS Connectivity Test

* Verified AWS connection using `boto3`
* Successfully listed S3 buckets from local environment

---


## 🔗 Architecture (Phase 1)

Data Sources:

* PostgreSQL (Shipments)
* Flask API (Real-time updates)
* File logs (Terminal events)

Storage:

* Amazon S3 (Bronze Layer)

---
# Phase 2: Data Ingestion Pipelines (Batch Layer)

## 📌 Overview

Phase 2 focuses on building **data ingestion pipelines** that extract data from multiple heterogeneous sources and load it into a centralized data lake (Amazon S3) in the **Bronze layer**.

This phase simulates real-world data engineering workflows where data is ingested from APIs, databases, and file-based systems.

---

## 🏗️ Data Sources

### 1. REST API (Real-Time Simulation)

* Built a custom Flask-based API to simulate shipment tracking events
* Endpoints:

  * `/shipment` → single shipment record
  * `/shipments` → multiple shipment records
* Generates dynamic, near real-time data

---

### 2. PostgreSQL Database (Transactional Source)

* Database: `Logistics`
* Table: `shipments`
* Represents structured business data (orders, shipment status, etc.)

---

### 3. File-Based Logs (Operational Data)

* JSON-based terminal logs
* Simulates warehouse/terminal scan events
* Generated via Python script (continuous event simulation)

---

## ⚙️ Pipelines Implemented

### 1. API → S3 Ingestion

* Extracts data from Flask API using `requests`
* Converts response to JSON
* Uploads to S3 Bronze layer

**Path:**

```
bronze/api_data/YYYY-MM-DD/shipments_<timestamp>.json
```

---

### 2. Database → S3 Ingestion

* Connects to PostgreSQL using `psycopg2`
* Executes SQL query:

  ```
  SELECT * FROM shipments;
  ```
* Loads data into Pandas DataFrame
* Converts to JSON and uploads to S3

**Path:**

```
bronze/db_data/YYYY-MM-DD/shipments_<timestamp>.json
```

---

### 3. File → S3 Ingestion

* Reads local JSON log files
* Uploads raw file content directly to S3

**Path:**

```
bronze/file_data/YYYY-MM-DD/terminal_logs_<timestamp>.json
```

---

## 🧠 Key Concepts Implemented

### 🔹 Multi-Source Data Ingestion

Handling different data formats:

* API (JSON)
* Database (structured → DataFrame)
* Files (raw logs)

---

### 🔹 Data Lake (Amazon S3)

* Centralized storage for all raw data
* Organized using **Medallion Architecture (Bronze layer)**

---
## 🔗 Architecture (Phase 2)

```
            Flask API --------\
                               \
            PostgreSQL -------- → Python Ingestion → Amazon S3 (Bronze Layer)
                               /
            File Logs --------/
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* psycopg2
* boto3
* Flask (API simulation)
* Amazon S3 (Data Lake)

---

