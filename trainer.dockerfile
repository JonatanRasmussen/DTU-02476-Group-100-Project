# Base image
FROM python:3.9-slim

# Install Python and essentials
RUN apt-get update && \
    apt-get install --no-install-recommends -y build-essential gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory to the root of the project
WORKDIR /DTU-02476-Group-100-Project/

# Copy the necessary files
COPY requirements.txt /DTU-02476-Group-100-Project/
COPY project_winegrape_src_files/ /DTU-02476-Group-100-Project/project_winegrape_src_files/

# Install Python dependencies
RUN pip install -r requirements.txt --no-cache-dir

# Set the entrypoint for the container
ENTRYPOINT ["python", "-u", "project_winegrape_src_files/train_model.py"]
