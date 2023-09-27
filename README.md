## Theoritical Tasks

**Q1. Turbit primarily deals with time-series data generated by sensors for temperature, pressure and other quantities. Which modern time-series forecasting approach would you choose to model such data? Describe its advantages and disadvantages. How would you implement it using tensorflow?**

Ans1. There are several modern forecasting approaches. Listing the following:
1. RNN/LSTM based approach (both univariate and multivariate)
2. Temoral Convolutional Neural Network (1-d convolutional)
3. DeepAR (based on RNN)
4. Temporal Fusion Transformer (LSTM, self-attention)

With tensorflow, it is easily possible as creating deep neural network architecture is easy to implement with Keras (high-level API - sequential or Functional API).
For time series data we have to use windowing technique to generate (process) data to feed to neural network.

I have also provided one example for univariate model using LSTM with tensorflow.

**Q2. When it comes to electrical power generation, we observed that the measured power values fluctuate a lot from one moment to the next. What are the implications of this behavior for modeling the power data?**

Ans2. There can be key considerations when dealing with power data from wind turbines -:

1. Noise: High fluctuations can sometimes be noise. It is crucial to do the robust data preprocessing for it.
2. Data Smoothing: Smoothing techniques like moving average and exponential smoothing can be applied to smoothen the data.
3. Data Granuality: Grouping the data based on hourly, weekly also matters which can again smoothen out these fluctuations.

**Q3. When reporting turbine anomalies, customers usually want to know the underlying reason for the unusual data points. Imagine that a thermometer in the gearbox of a turbine suddenly started reporting temperatures ten degrees higher than expected. List possible causes for such a pattern and how Turbit could distinguish between them?**

Ans3. Gearbox oil temperature is one of the indicators for gearbox codition monitoring.
Predicting the gearbox oil temperature helps in maintaining the safety and reliability of the wind turbines.
I study about the sudden change in the temperature in wind turbine can be because of different reasons, one of them is gaerbox oil temeprature.
There are proven research which can predict the early faulty warning of wind turbines. Turbit can adapt the existing solutions in the reasearch work 
for thier data.
