from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Employee model using Pydantic
class Employee(BaseModel):
    id: int
    name: str
    age: int
    department: str

# In-memory employee storage
employees = []

# Create an Employee
@app.post("/employee/", response_model=Employee)
def create_employee(employee: Employee):
    employees.append(employee)
    return employee

# Read all Employees
@app.get("/employees/", response_model=List[Employee])
def get_employees():
    return employees

# Read a single Employee
@app.get("/employee/{id}", response_model=Employee)
def get_employee(id: int):
    employee = next((e for e in employees if e.id == id), None)
    if employee:
        return employee
    raise HTTPException(status_code=404, detail="Employee not found")

# Update an Employee
@app.put("/employee/{id}", response_model=Employee)
def update_employee(id: int, updated_employee: Employee):
    for index, employee in enumerate(employees):
        if employee.id == id:
            employees[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")

# Delete an Employee
@app.delete("/employee/{id}")
def delete_employee(id: int):
    global employees
    employees = [e for e in employees if e.id != id]
    return {"message": "Employee deleted successfully"}



if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)