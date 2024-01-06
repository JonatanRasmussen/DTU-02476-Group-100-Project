## Project Plan

### Overall goal of the project
This is the project description of group 100 for the 02476 MLOps course at DTU. Classification of winegrape leaves is important to define the type of wine that is being produced. Given a dataset with five different types of grapevine leaves. The goal of the project is to predict, given the image of a vine leaf, which grape type it comes from.

### What framework are you going to use and do you intend to include the framework into your project?
The model used in this project is chosen from the TIMM framework for Computer Vision (PyTorch Image Models). This framework will be used to implement and train one/several different deep learning model(s).

### What data are you going to run on (initially, may change)
We want to perform training and predictions using the grapevine leaves image dataset from kaggle, available here: https://www.kaggle.com/datasets/muratkokludataset/grapevine-leaves-image-dataset/data. It was collected in 2022 and contains the classification of five different types of grapevine leaves. https://www.sciencedirect.com/science/article/abs/pii/S0263224121013142

### What models do you expect to use
The idea is to implement a baseline Fully Connected Neural Network to classify the leaves, as well as an improved Convolutional Neural Network (CNN) model (either made from scratch or using a pretrained model such as a ResNet or VGG).

#### Group members
- Jonatan Rasmussen: s183649
- Lucca Seyther: s223280
- Oskar Kristoffersen: s184364
- Pelle Andersen: s205339
- Siyao Gui: s232897

#### Repository structure
See the project_structure.md file for an overview of how the repository is structured. Note that our repository is using [this Cookiecutter template for MLOps](https://github.com/SkafteNicki/mlops_template).