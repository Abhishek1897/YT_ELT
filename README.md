# YT_ELT – End-to-End Data Engineering Pipeline

## 📌 Project Overview

YT_ELT is an end-to-end **Data Engineering project** that demonstrates how to build a **production-style ELT pipeline** using modern data engineering tools.  
The project extracts YouTube channel video data via APIs, processes and stores it in a PostgreSQL data warehouse, enforces data quality checks, and automates workflows using Apache Airflow.

This project focuses on **real-world data engineering practices**, including containerization, orchestration, testing, and data quality validation.

---

## 🚀 Key Features

- Extracts YouTube video metadata using **YouTube Data API**
- Implements an **ELT pipeline** using Python and PostgreSQL
- Uses **Apache Airflow** for workflow orchestration
- Stores raw and transformed data in **staging** and **core** schemas
- Applies **data quality checks using Soda**
- Containerized using **Docker & Docker Compose**
- Includes **unit, integration, and DAG integrity tests** using pytest
- Designed for **CI/CD readiness with GitHub Actions**

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Data Warehouse:** PostgreSQL  
- **Orchestration:** Apache Airflow  
- **Containerization:** Docker, Docker Compose  
- **Data Quality:** Soda  
- **Testing:** pytest (unit, integration, DAG tests)  
- **API Testing:** Postman  
- **Version Control & CI/CD:** GitHub, GitHub Actions  

---

## 🔄 High-Level Data Flow

1. Extract video and channel data from **YouTube API**
2. Store raw API responses as **JSON files**
3. Load raw data into **PostgreSQL staging schema**
4. Transform and enrich data into **PostgreSQL core schema**
5. Run **data quality checks** (missing values, duplicates, business rules)
6. Make clean data available for **analytics and consumption**

---

## 🧪 Testing & Data Quality

- **Unit Tests:** Validate environment variables, Airflow variables, and connections
- **Integration Tests:** Validate external API and database connectivity
- **DAG Tests:** Ensure DAGs load without errors and have expected tasks
- **Data Quality Checks:** Enforced using Soda (missing counts, duplicates, business rules)

---

## 📦 Project Structure (Simplified)


