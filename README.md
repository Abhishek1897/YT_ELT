
# YT_ELT
# 📊 YT_ELT — End-to-End Data Engineering Pipeline

YT_ELT is a **production-style end-to-end Data Engineering ELT project** that demonstrates how modern data pipelines are built, orchestrated, tested, and validated using industry-standard tools.

The pipeline extracts data from the **YouTube Data API**, loads it into **PostgreSQL**, transforms it using an **ELT approach**, enforces **data quality with Soda**, orchestrates workflows using **Apache Airflow**, and validates everything through **unit, integration, and DAG tests**, all running inside **Docker containers**.

---

## 🚀 Project Objectives

- Build real-world ELT pipelines using Python and SQL
- Orchestrate workflows using Apache Airflow
- Store and transform data in PostgreSQL
- Enforce data quality using Soda
- Write unit, integration, and DAG integrity tests
- Run everything in a containerized Docker environment
- Structure the project for CI/CD readiness

---

## 🛠️ Tech Stack

| Category | Tools |
|--------|------|
| Programming | Python |
| API | YouTube Data API |
| Database | PostgreSQL |
| Orchestration | Apache Airflow |
| Containers | Docker, Docker Compose |
| Data Quality | Soda |
| Testing | Pytest |
| API Testing | Postman |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions (ready) |

---

## 🏗️ Architecture
┌───────────────────┐
│ YouTube API │
│ (Channel Videos) │
└─────────┬─────────┘
│
▼
┌──────────────────────────┐
│ Python API Extraction │
│ (video_stats.py) │
│ - Playlist ID │
│ - Video IDs │
│ - Video Statistics │
└─────────┬────────────────┘
│
▼
┌──────────────────────────┐
│ Raw JSON Storage │
│ (Local / Mounted Volume) │
│ - YT_data_YYYY-MM-DD │
└─────────┬────────────────┘
│
▼
┌──────────────────────────┐
│ PostgreSQL — STAGING │
│ Schema: staging │
│ - Raw API fields │
│ - Minimal validation │
└─────────┬────────────────┘
│
▼
┌──────────────────────────┐
│ PostgreSQL — CORE │
│ Schema: core │
│ - Transformed fields │
│ - Business logic │
│ - Video_Type derived │
└─────────┬────────────────┘
│
▼
┌──────────────────────────┐
│ Soda Data Quality │
│ - Missing checks │
│ - Duplicate checks │
│ - Business rule checks │
└─────────┬────────────────┘
│
▼
┌──────────────────────────┐
│ Analytics / Consumption │
│ (SQL, DBeaver, BI tools) │
└──────────────────────────┘
