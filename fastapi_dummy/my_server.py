from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {'dummy_key': 'dummy_value'}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {'item_id': item_id}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {'item_id': item_id}