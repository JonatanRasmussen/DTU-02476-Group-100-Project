from fastapi import FastAPI
from http import HTTPStatus
from enum import Enum

# Run local server on port 8000:
# uvicorn --reload --port 8000 project_winegrape_src_files.main:app

app = FastAPI()

@app.get("/")
def root():
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
    }
    return response

class ItemEnum(Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/restric_items/{item_id}")
def read_item(item_id: ItemEnum):
    return {"item_id": item_id}
