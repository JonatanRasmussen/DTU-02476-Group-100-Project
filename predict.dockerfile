# Base image
FROM python:3.10-slim

# Install Python and essentials
RUN apt-get update && \
    apt-get install --no-install-recommends -y build-essential gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the necessary files
COPY requirements.txt requirements.txt
COPY pyproject.toml pyproject.toml
COPY project_winegrape_src_files/ project_winegrape_src_files/
COPY data/ data/
COPY checkpoints/ checkpoints/

# Install Python dependencies

WORKDIR /
RUN --mount=type=cache,target=~/pip/.cache pip install -r requirements.txt --no-cache-dir
RUN pip install . --no-deps --no-cache-dir

# Set the entrypoint for the container
ENTRYPOINT ["python", "-u", "project_winegrape_src_files/predict_model.py"]

# to run:
# docker build -f predict.dockerfile . -t predict:latest
# docker run --name predict1 predict:latest