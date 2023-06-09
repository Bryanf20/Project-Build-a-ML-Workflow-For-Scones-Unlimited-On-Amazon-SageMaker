# Project-Build-a-ML-Workflow-For-Scones-Unlimited-On-Amazon-SageMaker
In this project, you'll be building an image classification model that can automatically detect which kind of vehicle delivery drivers have, in order to route them to the correct loading bay and orders. Assigning delivery professionals who have a bicycle to nearby orders and giving motorcyclists orders that are farther can help Scones Unlimited optimize their operations.

As an MLE, your goal is to ship a scalable and safe model. Once your model becomes available to other teams on-demand, it’s important that your model can scale to meet demand, and that safeguards are in place to monitor and control for drift or degraded performance.

In this project, you’ll use AWS Sagemaker to build an image classification model that can tell bicycles apart from motorcycles. You'll deploy your model, use AWS Lambda functions to build supporting services, and AWS Step Functions to compose your model and services into an event-driven application. At the end of this project, you will have created a portfolio-ready demo that showcases your ability to build and compose scalable, ML-enabled, AWS applications.

## Project Steps Overview
* Step 1: Data staging
* Step 2: Model training and deployment
* Step 3: Lambdas and step function workflow
* Step 4: Testing and evaluation

## Content
### lambda.py
Contains three lambda functions for
* Serialization
* Classification
* Filtering

### stepfunction.json
JSON file of created step function from lambda functions

### starter.ipynb
Notebook file with complete solution and key results displayed

### Two image file
* One shows a succesful step function execution
* The other is a failed step function execution
