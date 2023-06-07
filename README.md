# **IHD Prediction Model**

This repository contains code for a machine learning model that predicts the risk of Ischemic Heart Disease (IHD) based
on health indicators. The model utilizes an MLP classifier, which is trained on a dataset of heart disease health
indicators.

## **Dataset**

The dataset used for training the model is stored in the file heart_disease_health_indicators_BRFSS2015.csv. It contains
various health indicators, along with the corresponding labels indicating the presence or absence of heart disease.

### Getting Started

To run the code and train the IHD prediction model, follow these steps:

### Clone the repository:

git clone https://github.com/Abdelrahman-2222/my-ml-model.git

### Install the required dependencies. You can use pip to install them:

pip install pandas scikit-learn joblib

### Modify the file path in the code to match the location of the dataset on your system:

data = pd.read_csv('path/to/heart_disease_health_indicators_BRFSS2015.csv')

### Run the code. Execute the Python script containing the code:

python predictor.py

### The model will be trained, and the accuracy on the testing set will be printed.

The trained model will be saved as MLP_model.joblib in the savedModels directory.

## **Model Architecture and Training Process**

The model architecture consists of a Multi-Layer Perceptron (MLP) classifier with three hidden layers, each containing
100 neurons. The model is trained using the Stochastic Gradient Descent (SGD) optimization algorithm.

The training process involves the following steps:

### 1. Data Preprocessing:

Categorical features are converted to numerical features using one-hot encoding.
Missing values in the dataset are imputed with the mean of the respective feature.
The features are standardized using the StandardScaler.

### 2. Feature Selection:

The top 18 features are selected using the SelectKBest algorithm based on their relevance to the target variable.

### 3. Splitting the Data:

The dataset is split into training, validation, and testing sets.
The training set is further divided into training and validation sets for model evaluation during training.

### 4. Model Training:

The MLP classifier is trained on the training set using the selected features.
The model's hyperparameters are set to appropriate values, such as the number of hidden layers, learning rate, and
maximum number of iterations.

### 5. Model Evaluation:

The accuracy of the trained model is computed on the testing set to assess its performance.

## **Results**

The model achieves a testing accuracy of X% on the provided dataset. However, please note that the accuracy may vary
depending on the quality and representativeness of the dataset used. It is advisable to evaluate the model's performance
on a diverse range of data to assess its generalization capabilities.

## **Saved Model**

The trained MLP classifier model is saved as MLP_model.joblib in the savedModels directory. You can load this model
using the joblib library to make predictions on new, unseen data.

## **Example code to load and use the saved model**

import joblib

model = joblib.load('savedModels/MLP_model.joblib')

## **Use the model to make predictions on new data**

Please note that this model is trained on the specific dataset provided and might not perform optimally on different
datasets without appropriate modifications.

## **License**

Feel free to explore the code, experiment with different configurations, and adapt it to your specific requirements. If
you have any questions or suggestions, please feel free to reach out.