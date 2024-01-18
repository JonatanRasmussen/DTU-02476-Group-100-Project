---
layout: default
nav_exclude: true
---

# Exam template for 02476 Machine Learning Operations

This is the report template for the exam. Please only remove the text formatted as with three dashes in front and behind
like:

```--- question 1 fill here ---```

where you instead should add your answers. Any other changes may have unwanted consequences when your report is auto
generated in the end of the course. For questions where you are asked to include images, start by adding the image to
the `figures` subfolder (please only use `.png`, `.jpg` or `.jpeg`) and then add the following code in your answer:

```markdown
![my_image](figures/<image>.<extension>)
```

In addition to this markdown file, we also provide the `report.py` script that provides two utility functions:

Running:

```bash
python report.py html
```

will generate an `.html` page of your report. After deadline for answering this template, we will autoscrape
everything in this `reports` folder and then use this utility to generate an `.html` page that will be your serve
as your final handin.

Running

```bash
python report.py check
```

will check your answers in this template against the constrains listed for each question e.g. is your answer too
short, too long, have you included an image when asked to.

For both functions to work it is important that you do not rename anything. The script have two dependencies that can
be installed with `pip install click markdown`.

## Overall project checklist

The checklist is *exhaustic* which means that it includes everything that you could possible do on the project in
relation the curricilum in this course. Therefore, we do not expect at all that you have checked of all boxes at the
end of the project.

### Week 1

* [x] Create a git repository
* [x] Make sure that all team members have write access to the github repository
* [x] Create a dedicated environment for you project to keep track of your packages
* [x] Create the initial file structure using cookiecutter
* [x] Fill out the `make_dataset.py` file such that it downloads whatever data you need and
* [x] Add a model file and a training script and get that running
* [x] Remember to fill out the `requirements.txt` file with whatever dependencies that you are using
* [x] Remember to comply with good coding practices (`pep8`) while doing the project
* [x] Do a bit of code typing and remember to document essential parts of your code
* [x] Setup version control for your data or part of your data
* [x] Construct one or multiple docker files for your code
* [x] Build the docker files locally and make sure they work as intended
* [x] Write one or multiple configurations files for your experiments
* [x] Used Hydra to load the configurations and manage your hyperparameters
* [x] When you have something that works somewhat, remember at some point to to some profiling and see if
      you can optimize your code
* [x] Use Weights & Biases to log training progress and other important metrics/artifacts in your code. Additionally,
      consider running a hyperparameter optimization sweep.
* [x] Use Pytorch-lightning (if applicable) to reduce the amount of boilerplate in your code

### Week 2

* [x] Write unit tests related to the data part of your code
* [x] Write unit tests related to model construction and or model training
* [x] Calculate the coverage.
* [x] Get some continuous integration running on the github repository
* [x] Create a data storage in GCP Bucket for you data and preferable link this with your data version control setup
* [x] Create a trigger workflow for automatically building your docker images
* [x] Get your model training in GCP using either the Engine or Vertex AI
* [x] Create a FastAPI application that can do inference using your model
* [x] If applicable, consider deploying the model locally using torchserve
* [ ] Deploy your model in GCP using either Functions or Run as the backend

### Week 3

* [ ] Check how robust your model is towards data drifting
* [ ] Setup monitoring for the system telemetry of your deployed model
* [ ] Setup monitoring for the performance of your deployed model
* [ ] If applicable, play around with distributed data loading
* [ ] If applicable, play around with distributed model training
* [ ] Play around with quantization, compilation and pruning for you trained models to increase inference speed

### Additional

* [x] Revisit your initial project description. Did the project turn out as you wanted?
* [x] Make sure all group members have a understanding about all parts of the project
* [x] Uploaded all your code to github

## Group information

### Question 1
> **Enter the group number you signed up on <learn.inside.dtu.dk>**
>
> Answer:

100

### Question 2
> **Enter the study number for each member in the group**
>
> Example:
>
> *sXXXXXX, sXXXXXX, sXXXXXX*
>
> Answer:

*s183649, s223280, s184364, s205339, s232897*

### Question 3
> **What framework did you choose to work with and did it help you complete the project?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the third-party framework ... in our project. We used functionality ... and functionality ... from the*
> *package to do ... and ... in our project*.
>
> Answer:

We selected the TIMM framework (PyTorch Image Models) for our project as the primary tool for implementing and training deep learning models. TIMM is a pre-built library particularly designed for computer vision tasks. Using this framework gave us the flexibility to not be locked into a specific architecture, and just as importantly, it has good PyTorch Integration, which is helpful for our existing PyTorch workflow from the exercises as well as earlier DTU courses. Additionally, TIMM is quite user-friendly, which meant that we could focus on model development and experimentation time. It allowed us to quickly implement and test models without too much trouble, and we trusted the framework to be both robust and efficient in achieving our image classification task.

## Coding environment

> In the following section we are interested in learning more about you local development environment.

### Question 4

> **Explain how you managed dependencies in your project? Explain the process a new team member would have to go**
> **through to get an exact copy of your environment.**
>
> Answer length: 100-200 words
>
> Example:
> *We used ... for managing our dependencies. The list of dependencies was auto-generated using ... . To get a*
> *complete copy of our development environment, one would have to run the following commands*
>
> Answer:

We used a requirements.txt for managing any dependencies used within our project. Auto-generating this file something like `pipreqs` was not completely fulfilling our needs since libraries like `dvc` or `pytest` are not used by normal invoked python scripts and are skipped in the process. We therefore decided to manually add these dependencies to the requirements.txt file.

Getting a copy of our development environment:

* [Download Git](https://git-scm.com/downloads)
* [Register on GitHub](https://github.com/signup)
* [Connect to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
* Clone the repository with `git clone git@github.com:JonatanRasmussen/DTU-02476-Group-100-Project.git`
* [Install Python 3.10+](https://www.python.org/downloads/)
* Install dependencies with `pip install -r requirements.txt`
* Adjust the config files in the conf directory to your liking
* Run the training with `python project_winegrape_src_files/train_model.py`
* Run the prediction with `python project_winegrape_src_files/predict_model.py`
* Run the tests with `pytest`

### Question 5

> **We expect that you initialized your project using the cookiecutter template. Explain the overall structure of your**
> **code. Did you fill out every folder or only a subset?**
>
> Answer length: 100-200 words
>
> Example:
> *From the cookiecutter template we have filled out the ... , ... and ... folder. We have removed the ... folder*
> *because we did not use any ... in our project. We have added an ... folder that contains ... for running our*
> *experiments.*
> Answer:

Our project's structure is primarily derived from the `mlops_template`, a cookiecutter template designed for Machine Learning Operations (MLOps). The main directories we utilized and filled out are:

* Data: Contains raw data and processed datasets. We emphasized the management of these datasets, ensuring they are immutable once created.
* Models: This is where our trained models, predictions, and summaries are stored.
* Notebooks: Jupyter notebooks were used for exploratory data analysis and initial model prototyping.
* Reports: All our reports, including figures, are stored here. Additionally, the report template for the exam can be found here as well. We have used it as a todo-list to split and coordinate project requirements.
* Tests: Self-explanatory.
* Other directories, like docs and visualization, were not extensively used in our project. We decided to focus on the core aspects of model development and data handling.

### Question 6

> **Did you implement any rules for code quality and format? Additionally, explain with your own words why these**
> **concepts matters in larger projects.**
>
> Answer length: 50-100 words.
>
> Answer:

In our project, we aimed at following PEP8 standards and we used tools like flake8 and mypy for linting (this partly came down to personal preference). We decided to be a bit loose regarding the max characters per line limit.

Code quality and formatting matters in larger projects, as you reach a point where you lose overview of all the code that has been written. At this point, you need to easily be able to browse through the codebase while being able to understand it without misunderstandings.

## Version control

> In the following section we are interested in how version control was used in your project during development to
> corporate and increase the quality of your code.

### Question 7

> **How many tests did you implement and what are they testing in your code?**
>
> Answer length: 50-100 words.
>
> Example:
> *In total we have implemented X tests. Primarily we are testing ... and ... as these the most critical parts of our*
> *application but also ... .*
>
> Answer:

In total we have implemented 2 tests using `pytest`. We are testing the completeness of a config file in one, and our DataModule in the other test. Only the second test is relevant in regards to coverage. We did not implement further tests due to the project's scope. We aimed at a resonable tradeoff between time and test coverage.

### Question 8

> **What is the total code coverage (in percentage) of your code? If you code had an code coverage of 100% (or close**
> **to), would you still trust it to be error free? Explain you reasoning.**
>
> Answer length: 100-200 words.
>
> Example:
> *The total code coverage of code is X%, which includes all our source code. We are far from 100% coverage of our **
> *code and even if we were then...*
>
> Answer:

The coverage of our DataModule test is 89%. To evaluate the robustness of our entire codebase more tests would be needed. High code coverage is desirable, but it doesn't guarantee the absence of bugs or the consideration of every possible edge case. We focused on understand the context and logic of the code rather than just achieving high coverage statistics (if you aim for X% code coverage as an arbitrary goal, you can end up with group members implementing useless tests just to reach their quota.) Practical manual testing and monitoring are just as crucial for ensuring the reliability of software. However, even if we achieved 100% code coverage for our complete codebase, we wouldn't entirely trust it to be error-free. A lot of bugs do not exist at the unit level, but rather as a consequence of how the code interacts with eachother. End-to-end testing can help catch these bugs, but due to the scope of our project, we allowed ourselves to not be too strict regarding testing.

### Question 9

> **Did you workflow include using branches and pull requests? If yes, explain how. If not, explain how branches and**
> **pull request can help improve version control.**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of both branches and PRs in our project. In our group, each member had an branch that they worked on in*
> *addition to the main branch. To merge code we ...*
>
> Answer:

In our project, we utilized Git branches and pull requests to manage code changes and maintain code quality. We decided to have each team member create their own branches for specific features. This ensured that the main branch always remained stable.

Once a feature was completed and locally tested, a pull request was created. We did not do code reviews or PRs for each other, as this added needless bureaucracy. Instead we decided to trust eachother in managing their own commits.

On top of that, when creating a PR, it also triggers our chosen Continuous Integration (CI) tool - Github Actions. This process involved running our suite of tests on the proposed code changes. The primary purpose of this CI tool was to provide reassurance that the new code did not introduce any errors or failures. If all tests passed, we could confidently merge the new code into the main branch, knowing that it maintained the stability and integrity of our project.

### Question 10

> **Did you use DVC for managing data in your project? If yes, then how did it improve your project to have version**
> **control of your data. If no, explain a case where it would be beneficial to have version control of your data.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did make use of DVC in the following way: ... . In the end it helped us in ... for controlling ... part of our*
> *pipeline*
>
> Answer:

GitHub is not designed to handle large files, so we used a separate dedicated remote storage system. Using Data Version Control (DVC) first on a Google Drive and later in a Google Storage Bucket on Google Cloud Provider (GCP), we were able to version control our data set. This allowed us to track the changes made to our data set. This allowed us to revert back to earlier versions of the data set if needed. Additionally, we were able to easily share data with other team members. Adding the storage bucket on GCP as a remote to our DVC repository enabled us to more easily develop and deliver Docker images with the same state of data.

### Question 11

> **Discuss you continues integration setup. What kind of CI are you running (unittesting, linting, etc.)? Do you test**
> **multiple operating systems, python version etc. Do you make use of caching? Feel free to insert a link to one of**
> **your github actions workflow.**
>
> Answer length: 200-300 words.
>
> Example:
> *We have organized our CI into 3 separate files: one for doing ..., one for running ... testing and one for running*
> *... . In particular for our ..., we used ... .An example of a triggered workflow can be seen here: <weblink>*
>
> Answer:

We organized our continous integration (CI) pipeline using GitHub actions for tests. Whenever a push is made or a pull request is opened to the main branch, a worker from GitHub automatically runs our unit tests. In the [actions tab of our GitHub repository](https://github.com/JonatanRasmussen/DTU-02476-Group-100-Project/actions) one can get an overview of each run. If a run is successful this is indicated on the pushed commit or inside the pull request by a green checkmark, if not a red cross is shown. This report is attached to every run and when downloaded provides a nice little HTML website with a detailed overview of the test coverage, see [coverage report](figures/coverageReport.png). An example of a triggered GitHub action in our project can be seen here: [FastAPI implementation pull request merge](https://github.com/JonatanRasmussen/DTU-02476-Group-100-Project/actions/runs/7569967481).

The workflow action runs on ubuntu. It first checks out the current state of the repository using `actions/checkout@v4`. After, it sets up python 3.10 using `actions/setup-python@v5`. With that action step we are setting that pip installs are cached by specifying `cache: 'pip'` to reduce running time. It then installs the project dependencies and runs our unit tests producing an HTML report. Finally `actions/upload-artifact@v4` is used to upload this report to GitHub and attach it to the workflow.

## Running code and tracking experiments

> In the following section we are interested in learning more about the experimental setup for running your code and
> especially the reproducibility of your experiments.

### Question 12

> **How did you configure experiments? Did you make use of config files? Explain with coding examples of how you would**
> **run a experiment.**
>
> Answer length: 50-100 words.
>
> Example:
> *We used a simple argparser, that worked in the following way: python my_script.py --lr 1e-3 --batch_size 25*
>
> Answer:

In our project, we configured experiments using configuration files with Hydra. Hydra allows us to organize and customize experiment settings easily. Here's an example of how to run an experiment using the train_model.py script with a specific configuration file "config1":

python project_winegrape_src_files/train_model.py --config-file=conf/config1.yaml

We also have a test_config.yaml file with a unique setup and dataset for running our unit tests.

### Question 13

> **Reproducibility of experiments are important. Related to the last question, how did you secure that no information**
> **is lost when running experiments and that your experiments are reproducible?**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of config files. Whenever an experiment is run the following happens: ... . To reproduce an experiment*
> *one would have to do ...*
>
> Answer:

To ensure the reproducibility of our experiments, we used many of the tools taught during the course. We used config files to maintain consistent configurations, so that all the settings and parameters are saved for later use. This made it easy to replicate or modify experiments. Additionally, we also used version control for both code and configs (we used Git for this). This ensured that we could always revert to or examine the state of the code for any given experiment. Logging were also used to document what happened each time the code was run, which helps for both debugging as well as validating a succesful reproduction of results. We also used DVC to handle the changes made to very large files, while also ensuring that we could revert back to earlier version of said files.

e it.We also used Docker, which is great for environmental consistency and portability, and being able to reprodu Docker containers encapsulate the application and its environment, ensuring that it works uniformly across different systems. This encapsulation includes the application, its dependencies, and the environment settings. As a result, Docker significantly reduces the ‘it works on my machine’ problem, providing a consistent environment for the application from development to production.

### Question 14

> **Upload 1 to 3 screenshots that show the experiments that you have done in W&B (or another experiment tracking**
> **service of your choice). This may include loss graphs, logged images, hyperparameter sweeps etc. You can take**
> **inspiration from [this figure](figures/wandb.png). Explain what metrics you are tracking and why they are**
> **important.**
>
> Answer length: 200-300 words + 1 to 3 screenshots.
>
> Example:
> *As seen in the first image when have tracked ... and ... which both inform us about ... in our experiments.*
> *As seen in the second image we are also tracking ... and ...*
>
> Answer:

We have used W&B (Weights & Biases) to log and track the parameters, metrics, and artifacts (such as models, datasets, and images) of our machine learning experiments. This allows us to neatly store a record of all experiments, making it easier to compare and reproduce results. It also provides interactive visualizations for metrics and results, making it easier to understand the performance of models over time. Additionally, it stores information about the developer environment used to carry out the experiment, linking it to specific models, datasets, or code versions.

```markdown
![Screenshot1](figures/<JonatanTestWB>.<png>)
```

[Here](figures/JonatanTestWB.png) is a visual summary of running the train_model script for a short duration with the default parameters. It highlights key training and validation metrics such as accuracy and loss, graphing the improvements over the course of the iterations. The results are not groundbreaking; the screenshot is meant to showcase why using W&B is useful for ML projects such as ours.

```markdown
![Screenshot2](figures/<JonatanTestOverviewWB>.<png>)
```

[Here](figures/JonatanTestOverviewWB.png) is an overview of the environment used to perform the training, including training duration, hardware and Git repository + state. Again, the screenshot is meant to showcase the utility of W&B and why we are using it for our ML project.

By using W&B, we are able to track key training and validation metrics such as accuracy and loss, as well as visualizing them. This is key data to track for a classification-project such as our winegrape project, as they indicate to what extend our model is able to classify the winegrape leaves.

### Question 15

> **Docker is an important tool for creating containerized applications. Explain how you used docker in your**
> **experiments? Include how you would run your docker images and include a link to one of your docker files.**
>
> Answer length: 100-200 words.
>
> Example:
> *For our project we developed several images: one for training, inference and deployment. For example to run the*
> *training docker image: `docker run trainer:latest lr=1e-3 batch_size=64`. Link to docker file: <weblink>*
>
> Answer:

replicatedDocker is a tool that can be used to build, share, and run container applications, which ensures that a code execution environment can be replecated across machines.

For our project we developed several images: one for training and one for prediction.

To run the training Docker images, we used the following commands respectively:

```bash
docker run --shm-size=1g -v $PWD/checkpoints/:/checkpoints/ -e WANDB_API_KEY=<W&B_KEY> --name experiment1 trainer:latest
docker run --name predict1 predict:latest
```

The `shm-size` is used to increase the space for the container. Then we would like to save the trained model into `/checkpoints`. The `WANDB_API_KEY` links the docker to weights and biases in order to see the progress of the trained model even when run through with a docker image.

 https://github[Link](.com/JonatanRasmussen/DTU-02476-Group-100-Project/blob/main/trainer.dockerfile)Link to Docker:

We integrated DVC into our Docker images for reproducibility and versioning. DVC enables us to systematically track and manage datasets alongside our code, ensuring that modifications to the data are diligently recorded and can be easily replicated across various stages of the project.

### Question 16

> **When running into bugs while trying to run your experiments, how did you perform debugging? Additionally, did you**
> **try to profile your code or do you think it is already perfect?**
>
> Answer length: 100-200 words.
>
> Example:
> *Debugging method was dependent on group member. Some just used ... and others used ... . We did a single profiling*
> *run of our main code at some point that showed ...*
>
> Answer:

Our approach to debugging varied among team members. Some preferred traditional debugging techniques using Python's pdb debugger, which provided ways to inspect code at runtime. Others used more sophisticated IDE-based debugging tools, such as setting breakpoints and inspecting variable states at certain points during execution. Simple print-statements may or may not have been used as well.

Regarding code profiling, we attemped to identify bottlenecks, although it was not something we focused too much on. The data processing and model training phases were the lenghtiest code executions, so optimizations could ideally be made here. We don't think our code is perfect in anyway, but we did not spend all that much time profiling it either. We made attempts at refining our code, but it was not our biggest focus.

## Working in the cloud

> In the following section we would like to know more about your experience when developing in the cloud.

### Question 17

> **List all the GCP services that you made use of in your project and shortly explain what each service does?**
>
> Answer length: 50-200 words.
>
> Example:
> *We used the following two services: Engine and Bucket. Engine is used for... and Bucket is used for...*
>
> Answer:

In our project, we used the following GCP services: Compute Engine for running virtual machines and applications, Cloud Storage to create a bucket with the data that we managed to transfer with DVC. We also used Vertex AI for model training and deployment and to do so we used Cloud Build for continuous integration and deployment to create a docker image each time.something new was pushed to the repository

### Question 18

> **The backbone of GCP is the Compute engine. Explained how you made use of this service and what type of VMs**
> **you used?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the compute engine to run our ... . We used instances with the following hardware: ... and we started the*
> *using a custom container: ...*
>

We used GCP's Compute Engine initially to try to run our container images, but after creating a VM and accessing it, the python version seemed to be blocked at version 3.7.8, and would therefore not work with our code (needed python 3.10.X or higher). Because of that and further instructions from the course we chose to go down a different route and use Vertex AI instead. It enabled us to run our models using the trainer docker image. We did this by running a command line such as the following:

```{python}
gcloud ai custom-jobs create \
    --region=europe-west1 \
    --display-name=vine-run-X \
    --config=config_cpu.yaml
```

With the configuration:

```{python}
workerPoolSpecs:
    machineSpec:
        machineType: n1-highmem-2
    replicaCount: 1
    containerSpec:
        imageUri: gcr.io/<project-id>/trainer
        env:
            - name: WANDB_API_KEY
              value: <MY_WANDB_KEY>
```

We believe that this also creates a VM with the machine specs from the `config_cpu.yaml`. We tried to also use a configuration with gpu, but without any success. However this was not a problem for us since the docker image was able to run with the cpu configs for 10 epochs in 5-7 minutes. If we were to train the mod### Question 19

### Question 19

> **Insert 1-2 images of your GCP bucket, such that we can see what data you have stored in it.**
> **You can take inspiration from [this figure](figures/bucket.png).**
>
> Answer:

Here are two images with the data placed in our GCP bucket:

[the folders](figures/bucket.png).
[the data](figures/bucket2.png).

### Question 20

> **Upload one image of your GCP container registry, such that we can see the different images that you have stored.**
> **You can take inspiration from [this figure](figures/registry.png).**
>
> Answer:

Here is an image of the GCP Artifacts Registry with our current trainer docker image:
[registry](figures/registry.png).

### Question 21

> **Upload one image of your GCP cloud build history, so we can see the history of the images that have been build in**
> **your project. You can take inspiration from [this figure](figures/build.png).**
>
> Answer:

Here is an image of the Cloud Build history. We had some problems with copying the data from GCP bucket to our image, but managed to make it work after the 15th attempt.
[history](figures/registry.png).

### Question 22

> **Did you manage to deploy your model, either in locally or cloud? If not, describe why. If yes, describe how and**
> **preferably how you invoke your deployed service?**
>
> Answer length: 100-200 words.
>
> Example:
> *For deployment we wrapped our model into application using ... . We first tried locally serving the model, which*
> *worked. Afterwards we deployed it in the cloud, using ... . To invoke the service an user would call*
> *`curl -X POST -F "file=@file.json"<weburl>`*
>
> Answer:

Unfortunately we did not have the time to deploy the model, neither locally or on the cloud. The reason for this is because we spent a lot of time working on setting everything up in Google Cloud Platform, which included setting up the data in a bucket, linking the github repository such that we had a trigger workflow to automatically build a docker image and making everything work together with Vertex AI. Deploying the model may have been a less cumbersome task, but we decided to focus on having all the other elements in place (dvc, docker, W&B and all the aspects on GCP).

### Question 23

> **Did you manage to implement monitoring of your deployed model? If yes, explain how it works. If not, explain how**
> **monitoring would help the longevity of your application.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could*
> *measure ... and ... that would inform us about this ... behaviour of our application.*
>
> Answer:

We did not prioritize to implement monitoring for our deployed model due to time constraints and other tasks requiring our focus. In an actual production environment however, implement monitoring would have saved us many headaches down the road, as it allows us to track the performance of the model over time, identify any degradation in prediction accuracy, and detect anomalies or unexpected behavior. Implementing monitoring would help in ensuring the long-term health and reliability of our project. It would give us an overview of how the model is performing in the real world, alert us to any issues that might arise post-deployment. This give us the chance to fix bugs and provide maintenance as soon as possible, before the issues affect a lot of users. For machine learning models particularly, this is especially important, as data drift or changes in input patterns can significantly affect performance.

### Question 24

> **How many credits did you end up using during the project and what service was most expensive?**
>
> Answer length: 25-100 words.
>
> Example:
> *Group member 1 used ..., Group member 2 used ..., in total ... credits was spend during development. The service*
> *costing the most was ... due to ...*
>
> Answer:

Regarding the total credits, since we trained our models only on a CPU we were able to keep quite a lot of credits. Also during the implementation stage we only trained with a maximum of 10 epochs. Therefore we only used around $1.00, with most of the price being cloud storage.

## Overall discussion of project

> In the following section we would like you to think about the general structure of your project.

### Question 25

> **Include a figure that describes the overall architecture of your system and what services that you make use of.**
> **You can take inspiration from [this figure](figures/overview.png). Additionally in your own words, explain the**
> **overall steps in figure.**
>
> Answer length: 200-400 words
>
> Example:
>
> *The starting point of the diagram is our local setup, where we integrated ... and ... and ... into our code.*
> *Whenever we commit code and puch to github, it auto triggers ... and ... . From there the diagram shows ...*
>
> Answer:

The starting point of the diagram is our local development setup, where we can perform basic training and predictions using a Python venv or building and running a Dockerfile. 
To add/update local data, DVC is used which stores and keeps track of the data using a Google Storage Bucket and our Google Drive. Whenever we commit code and push to GitHub, it triggers a GitHub action that runs our unit tests using `pytest` and produces a coverage report. Also, a cloud build trigger is executed that builds a Docker image using the `cloudbuild.yaml` file and the current state of data and links the Weights & Biases API key to the image. After build, our image is stored in Google's Container Registry and we are able to create a custom AI job using Vertex AI. To monitor this training job, its status is regurlarly sent to our Weight & Biases account. For future work a Docker image for predictions could be served as a pre-trained model which could be retrieved from a Google Storage Bucket. A potential user could then automatically identify vineleaves using this image or retrain another model provided that the training image is made available.

Here is an image of our architecture: [Link](reports/architecture.png).

### Question 26

> **Discuss the overall struggles of the project. Where did you spend most time and what did you do to overcome these**
> **challenges?**
>
> Answer length: 200-400 words.
>
> Example:
> *The biggest challenges in the project was using ... tool to do ... . The reason for this was ...*
>
> Answer:

The primary challenges we faced in this project revolved around integrating various technologies and tools into a smooth workflow. A lot of time was spent configuring the development environment and ensuring compatibility among different tools and libraries, some of which were external tools that none of us fully knew how to use. We experienced "integration hell" which is trying (and failing) to make multiple separate systems interact in harmony. But in the end, it worked out (mostly).

Collaboration and code management was challenging due to the diverse backgrounds of the team members. Some members were way more experienced in ML than others, but they could compensate by having experience on the "Ops"-side. On order to parallelize the work process as much as possible, we agreed on coding practices and standards that clearly delegated responsibility to each group member based on their preferences and strengths. Another challenge was the fact that our group mostly worked from home, with the occasional online meeting to coordinate the workflow and solve miscommunications. This made it a bit unclear what each member of the team was currently working on, and we tried out different ways of handeling this throughout the project, but we never found a solution that fully worked.

Overall, while these challenges were initially time-consuming and sometimes frustrating, they provided us with a deeper understanding of the complexities involved in the development of a real-world machine learning project as part of 5-person team. It gave us perspective on the importance of a well-structured development process, not just for our own sanity, but also for the sake of avoiding bottlenecks and keeping everyone productive.

### Question 27

> **State the individual contributions of each team member. This is required information from DTU, because we need to**
> **make sure all members contributed actively to the project**
>
> Answer length: 50-200 words.
>
> Example:
> *Student sXXXXXX was in charge of developing of setting up the initial cookie cutter project and developing of the*
> *docker containers for training our applications.*
> *Student sXXXXXX was in charge of training our models in the cloud and deploying them afterwards.*
> *All members contributed to code by...*
>
> Answer:
The following is a description of the contributions of each group member:

- Contributions from Jonatan Rasmussen s183649: Github, mlops_template, test_data, reports/README questions

- Contributions from Lucca Seyther s223280: python tests, Hydra setup, GitHub actions, GCP setup, reports/README questions.

- Contributions from Oskar Kristoffersen s184364: Models development, Pytorch lightning, W&B, Docker, DVC, Hydra configs, GCP setup, FastAPI, reports/README questions.

- Contributions from Pelle Andersen s205339: Docker, GCP, DVC, FastAPI, reports/README questions.

- Contributions from Siyao Gui s232897: Suggestions, Model ideas, reports/README questions