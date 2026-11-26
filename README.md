# Maryland Higher Education Transfer Analytics Pipeline

An automated cloud ETL (Extract, Transform, Load) and relational analytics pipeline engineered with **Python (Pandas)**, **AWS S3**, and **Amazon RDS PostgreSQL**. This project ingests raw University System of Maryland (USM) IRIS exports tracking community college transfer enrollment across 11 public institutions (FY 2022–FY 2026) and transforms them into normalized, query-ready SQL tables.

## Pipeline Architecture
`Raw USM IRIS CSV` $\rightarrow$ `AWS S3 (/data/raw/)` $\rightarrow$ `Python & Pandas ETL (etl_pipeline.py)` $\rightarrow$ `Amazon RDS PostgreSQL (schema.sql)` $\rightarrow$ `SQL & Geospatial Analytics`

## Key Findings (FY 2022 – FY 2026)
- **Top Receiving Institutions (FY 2026):** UMGC (3,303), UMD College Park (2,044), Towson University (1,544), and UMBC (901).
- **Sustained Multi-Year Growth:** UMES (+6.3% avg. annual), UMD College Park (+2.4%), and UMGC (+1.5%).
- **Strongest FY 2025–2026 Rebound:** University of Maryland, Baltimore (+17.0%) and Coppin State University (+10.8%).