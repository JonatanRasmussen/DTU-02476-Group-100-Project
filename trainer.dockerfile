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
COPY .dvc/tmp/default.json /root/.cache/pydrive2fs/710796635688-iivsgbgsb6uv1fap6635dhvuei09o66c.apps.googleusercontent.com/default.json

# Install Python dependencies

WORKDIR /
RUN --mount=type=cache,target=~/pip/.cache pip install -r requirements.txt --no-cache-dir
RUN pip install . --no-deps --no-cache-dir
RUN pip install dvc
RUN pip install "dvc[gdrive]"

RUN dvc init --no-scm
COPY .dvc/config .dvc/config
COPY *.dvc *.dvc
RUN dvc config core.no_scm true
RUN dvc pull

# Set the entrypoint for the container
ENTRYPOINT ["python", "-u", "project_winegrape_src_files/train_model.py"]

# To run in docker:
# docker run --shm-size=1g --name experiment1 trainer:latest
# with wandb:
# docker run -e WANDB_API_KEY=<your-api-key> wandb:latest

# final:
# docker run --shm-size=1g -v $PWD/checkpoints/:/checkpoints/ -e WANDB_API_KEY=<your-api-key> --name experiment3 trainer:latest
