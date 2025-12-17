from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

items = []
next_id = 1


class CreateItem(BaseModel):
    title: str
    quantity: int

class Item(BaseModel):
    id: int
    title: str
    quantity: int


@app.get("/items")
def get_items():
    return items 

@app.post("/items")
def create_item(item: CreateItem):
    global next_id
    
    new_item = {
        "id": next_id,
        "title": item.title,
        "quantity": item.quantity
    }
    
    items.append(new_item)
    next_id += 1
    
    return new_item 


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)