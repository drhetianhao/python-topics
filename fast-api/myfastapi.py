from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# uvicorn myfastapi:app --reload
app = FastAPI()

students = {1: {"name": "jj", "age": 17, "class": "1st"}}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID to view", gt=0, lt=3)):
    return students[student_id]


@app.get("/get-by-name")
def get_by_name(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


@app.post("/create-stu/{student_id}")
def create_stu(student_id: int, student: Student):
    if student_id in students:
        return {"error": "exists already"}
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_stu(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"er": "student not exist"}

    if student.name != None:
        students[student_id].name = student.name

    students[student_id] = student
    return students[student_id]


@app.delete("/delete/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"errr": "not"}

    del students[student_id]
    return {"msg": "done"}
