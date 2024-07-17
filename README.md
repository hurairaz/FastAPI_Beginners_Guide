# FastAPI Beginners Guide

A simple Student Management System built with FastAPI and Python, showcasing basic CRUD operations for managing student records.

---

## API Endpoints

- **GET /all-student**: Retrieve all student records.
- **GET /read-student/{student_id}**: Retrieve a specific student record by ID.
- **GET /query-student**: Query a student record by name.
- **POST /write-student/{student_id}**: Create a new student record.
- **PUT /update-student/{student_id}**: Update an existing student record.
- **DELETE /delete-student/{student_id}**: Delete a student record by ID.

---

## Installation and Setup

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/hurairaz/FastAPI_Beginners_Guide.git
   cd FastAPI_Beginners_Guide
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the FastAPI Application

1. Ensure that port 8000 is not already in use:
   ```bash
   netstat -ano | findstr :8000
   ```

2. If port 8000 is in use, terminate the process (replace `PID` with the appropriate process ID):
   ```bash
   taskkill /PID <PID> /F
   ```

3. Check for any remaining Python processes:
   ```bash
   tasklist | findstr python
   ```

4. If Python processes are still active, terminate them:
   ```bash
   taskkill /PID <PID> /F
   ```

5. Run the FastAPI application using uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

6. Access the API at `http://localhost:8000` in your browser or API client.

