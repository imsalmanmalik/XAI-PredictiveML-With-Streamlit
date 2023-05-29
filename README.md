## Project Overview

This project aimed to develop a machine learning model to predict the prices of Airbnb listings. The dataset used for the analysis consisted of housing data, including features such as location, number of rooms, availability, and reviews. The project fol- lowed a systematic approach, including data preprocessing, feature engineering, model selection, and evaluation.

The dataset was preprocessed by handling missing values, encoding categorical variables, and performing feature scaling. Exploratory data analysis was conducted to gain insights into the data distribution and relationships between variables. Feature engineering techniques were applied to extract meaningful information from the data, including one-hot encoding for categorical variables.

Multiple regression models were evaluated, including linear regression, random forest regression, gradient boosting regression, and XGBoost regression. The models were trained and evaluated using various performance metrics such as mean squared error (MSE) and coefficient of determination (R-squared). Hyperparameter tuning was performed using techniques such as grid search and cross-validation to optimize the model’s performance. Additionally, feature importance analysis using methods like LIME and SHAP was conducted to gain insights into the model’s decision-making process.
The results showed that the Gradient Boosting Regressor model (Stacking) achieved the highest R-squared value of 0.8645 on the training data, indicating a strong fit.

In conclusion, the developed machine learning model demonstrated promising predictive capabilities for estimating Airbnb listing prices. The findings highlight the importance of feature selection, model tuning, and interpretability techniques in improving the model’s performance and understanding its behavior.


After successfully installing all the packages and libraries in app.py file 
```bash
streamlit run app.py
```
To view the dashboard on streamlit
