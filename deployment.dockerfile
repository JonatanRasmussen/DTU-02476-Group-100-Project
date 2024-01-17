# Dockerfile to run a FastAPI application locally

FROM python:3.9
WORKDIR /
COPY /requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt
RUN pip install requests
RUN pip install fastapi
RUN pip install uvicorn
COPY /project_winegrape_src_files /project_winegrape_src_files

CMD ["uvicorn", "project_winegrape_src_files.main:app", "--host", "0.0.0.0", "--port", "8000"]

# to run:
# docker build -f deployment.dockerfile . -t deployment:latest
# docker run --name fastapi_app -p 8000:8000 deployment:latest
# Open http://localhost:8000/ in your web browser to see if it works