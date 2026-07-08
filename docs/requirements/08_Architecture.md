# Software Architecture

React
│
▼
FastAPI
│
▼
API Layer
│
▼
Service Layer
│
▼
Repository Layer
│
▼
SQL Server

# Software Architecture

## Introduction

The Hospital Management System follows a layered architecture to ensure scalability, maintainability, and separation of concerns. Each layer has a specific responsibility and communicates only with the appropriate adjacent layer.

---

# Architecture Style

Layered Architecture

---

# Technology Stack

## Frontend

- React
- HTML5
- CSS3
- JavaScript

---

## Backend

- Python
- FastAPI

---

## Database

- Microsoft SQL Server

---

## Version Control

- Git
- GitHub

# System Layers

## 1. Presentation Layer

Technology:

React

Responsibilities:

- User Interface
- Forms
- Dashboards
- Tables
- Sending API Requests
- Displaying API Responses

---

## 2. API Layer

Technology:

FastAPI

Responsibilities:

- Receive HTTP Requests
- Validate Requests
- Route Requests
- Return JSON Responses

---

## 3. Service Layer

Responsibilities:

- Business Logic
- Validation
- Business Rules
- Workflow Execution

Examples:

- Register Patient
- Book Appointment
- Generate Bill

---

## 4. Repository Layer

Responsibilities:

- Execute SQL Queries
- Read Data
- Insert Data
- Update Data
- Delete Data

This layer communicates directly with SQL Server.

---

## 5. Database Layer

Technology:

Microsoft SQL Server

Responsibilities:

- Store Data
- Maintain Relationships
- Ensure Data Integrity
- Execute Stored Procedures

# Layer Communication

Browser

↓

React Frontend

↓

HTTP / JSON

↓

FastAPI

↓

Service Layer

↓

Repository Layer

↓

SQL Server

# Project Structure

Hospital-Management-System/

│

├── backend/

│ ├── app/

│ │ ├── api/

│ │ ├── core/

│ │ ├── db/

│ │ ├── models/

│ │ ├── repositories/

│ │ ├── schemas/

│ │ ├── services/

│ │ └── utils/

│ │

│ ├── tests/

│ ├── requirements.txt

│ └── main.py

│

├── frontend/

│

├── database/

│ ├── schema/

│ ├── scripts/

│ └── backups/

│

├── docs/

│

├── .gitignore

│

└── README.md

# Architecture Principles

The system follows the following software engineering principles:

- Separation of Concerns (SoC)
- Single Responsibility Principle (SRP)
- Layered Architecture
- Role-Based Access Control (RBAC)
- Database Normalization
- Modular Design
- Reusable Components
- Scalable Folder Structure
