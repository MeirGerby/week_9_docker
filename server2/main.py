from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
import json


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
    try:
        with open(r"server2\db\shopping_list.json", "r") as f:
            data = json.load(f)
    except:
        with open(r"server2\db\shopping_list.json", "w") as f:
            f.write('[]')
    return data 

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

    json_str = json.dumps(items, indent=4)
    with open(r"server2\db\shopping_list.json", "w") as f:
        f.write(json_str)
    
    return new_item 


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)