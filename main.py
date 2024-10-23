from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class TodoItem(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory database
todo_db: List[TodoItem] = []

@app.post("/todos", response_model=TodoItem)
def create_todo_item(todo: TodoItem):
    for item in todo_db:
        if item.id == todo.id:
            raise HTTPException(status_code=400, detail="Todo with this ID already exists.")
    todo_db.append(todo)
    return todo

@app.get("/todos", response_model=List[TodoItem])
def read_todo_items():
    return todo_db

@app.get("/todos/{todo_id}", response_model=TodoItem)
def read_todo_item(todo_id: int):
    for todo in todo_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found.")

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo_item(todo_id: int, updated_todo: TodoItem):
    for index, todo in enumerate(todo_db):
        if todo.id == todo_id:
            todo_db[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found.")

@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int):
    for index, todo in enumerate(todo_db):
        if todo.id == todo_id:
            del todo_db[index]
            return {"detail": "Todo deleted."}
    raise HTTPException(status_code=404, detail="Todo not found.")