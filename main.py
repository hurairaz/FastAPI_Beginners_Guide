from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# In-memory storage for student records
students = {
    1: {"name": "Dale Cooper", "age": 21},
    2: {"name": "Laura Palmer", "age": 21},
    3: {"name": "Sarah James", "age": 21},
}


# Pydantic model for student data validation
class Student(BaseModel):
    name: str
    age: int


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Management System!"}


# Get all students
@app.get("/all-student")
def all_student():
    return students


# Get a specific student by ID
@app.get("/read-student/{student_id}")
def read_student(student_id: int):
    if student_id in students:
        return students[student_id]
    else:
        return {"message": "No student record found"}


# Query a student by name
@app.get("/query-student")
def query_student(name: Optional[str] = None):
    if name is not None:
        for student_id, info in students.items():
            if info["name"] == name:
                return info
        return {"message": "No student record found"}
    else:
        return {"message": "No student name provided"}


# Create a new student
@app.post("/write-student/{student_id}")
def write_student(student_id: int, student: Student):
    if student_id in students:
        return {"message": "Student record already exists"}
    else:
        students[student_id] = dict(student)
        return {"message": "Student record created successfully", "student": student}


# Update a student
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"message": "Student record does not exist"}

    if student.name:
        students[student_id]["name"] = student.name
    if student.age:
        students[student_id]["age"] = student.age

    return students[student_id]


# Delete a student
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"message": "No student record with the provided ID exists"}

    students.pop(student_id)
    return {"message": "Student record deleted successfully"}
