from fastapi import FastAPI
import json

# Run local server on port 8000:
# uvicorn --reload --port 8000 project_winegrape_src_files.results_api:app

f = open('project_winegrape_src_files/data/API_image/results.json')
results = json.load(f)

app = FastAPI()

@app.get("/")
def root():
    return results