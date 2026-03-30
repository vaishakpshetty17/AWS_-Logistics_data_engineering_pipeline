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
