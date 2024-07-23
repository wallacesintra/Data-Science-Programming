# Linear Model

Linear Model: a statistical method for modelling relationship between dependent variables(response) and independent variables(features)

## Assumptions of linear model

* there is linear relationship between the dependent and independent variables
* no outliers
* noise
* little or no autocorrelation

## Scikit-Learn's Estimator API

### Steps

1. Choose a class of a model, import from Scikit-Learn.
2. Choose model hyperparameters by instantiating the class with desired values
3. Arrange data into a feature matrix and target vactor
4. Fit the model to data
5. Apply the model to new data:
    * supervised learning, predict labels for unknown data using predict() method
    * unsupervised learning, transform/infer properties of the data using the transform() or predict() method.
6. Check the result of the model fitting to know whether the model is satisfactory.

## Simple Linear Regression

predicting a dependent variable based on a single independent variable

Linear regression involves coming up with the a straight-line fit to data.

y = ax + b

a is the slope
b is the intercept

## Rigid Regression

