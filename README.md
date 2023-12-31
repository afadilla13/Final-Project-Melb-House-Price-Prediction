# Melbourne House Pricing Prediction with Machine Learning Model

![Melbourne-2](https://github.com/afadilla13/Final-Project-Melb-House-Price-Prediction/assets/128363337/6533aeb6-0fde-4243-9d2a-c0c8b638e837)


## Table of Contents

- [Introduction](#introduction)
- [Objective](#objective)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
- [Results](#results)
- [Conclusion](#conclusion)

## Introduction

In today's competitive property market, it's essential to make informed decisions, whether you're a family looking for a dream home or an investor seeking profitable opportunities. Traditional methods often involve manual research, intuition, or relying on real estate agents. This project aims to harness the power of machine learning to predict property prices and identify potential investment opportunities.

## Objective

- **For families:** Provide recommendations on properties that offer the best value for their budget and preferences.
- **For investors:** Identify undervalued properties that have the potential for higher returns.

## Data Sources

The Melbourne Housing Market dataset is a comprehensive and detailed dataset containing information on the real estate market of Melbourne, Australia. It includes various features such as the price, number of bedrooms, bathrooms, location, and many other aspects related to the properties.

To access this dataset, visit the following link: [Melbourne Housing Market Dataset](https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market).

Please note that you may need a Kaggle account to download the dataset or interact with it on their platform.

- Property details (rooms. type, bathroom, car, land size, etc)
- Location data (suburb, address, distance, postcode, council area, region, ect)
- Historical price data from 2016-2018

All data files can be found in the `Raw_Data` directory of this repository. A csv file of the data is available in `Melbourne_housing_FULL.csv`.

## Methodology

1. **Data Cleaning & Preprocessing**: 
    - Dropping unnecessary columns
    - Renaming columns
    - Handling missing values
    - Checking duplicates value and removing them
    - Changing the format date column and extracting the year
    - Encoding categorical variables
    - Feature scaling

2. **Exploratory Data Analysis (EDA)**:
    - Visualizing data distributions
    ![Number of Bathrooms Distribution](./EDA_Output/data_distribution_Bathroom.jpg)
    ![Number of Car Garages Distribution](./EDA_Output/data_distribution_Car.jpg)
    ![Distance Distribution](./EDA_Output/data_distribution_Distance.jpg)
    ![data_distribution_Land Size](https://github.com/afadilla13/Final-Project-Melb-House-Price-Prediction/assets/128363337/a8cd0450-89ce-41e8-85e8-13226ae8aeac)
    ![Price Distribution](./EDA_Output/data_distribution_Price.jpg)
    ![data_distribution_Property Count](https://github.com/afadilla13/Final-Project-Melb-House-Price-Prediction/assets/128363337/34431d69-9b11-496c-8379-63557bc6d402)
    ![Number of Rooms Distribution](./EDA_Output/data_distribution_Rooms.jpg)
    ![Suburb Distribution](./EDA_Output/data_distribution_Suburb.jpg)
    ![Year Distribution](./EDA_Output/data_distribution_Year.jpg)
    - Categorical analysis

    - Correlation analysis
    ![Features correlation with Price](./EDA_Output/features_correlation_with_price.jpg)

    - Visualizing correlations between price and features
    ![Distance with Price](./EDA_Output/price_vs_distance.jpg)
    ![Type with Price](./EDA_Output/price_distribution_by_type.jpg)
    ![Region with Price](./EDA_Output/price_distribution_by_region.jpg)
    ![Suburb with Price](./EDA_Output/price_distribution_by_suburb.jpg)

    - Analyzing prize as target variable
    ![Histogram with Price](./EDA_Output/price_feature_distribution_histogram.jpg)
    ![Box Plot with Price](./EDA_Output/price_feature_distribution_boxplot.jpg)

    - Identifying skewness in the data
    ![enumerated_skewness](https://github.com/afadilla13/Final-Project-Melb-House-Price-Prediction/assets/128363337/86b4f918-7b5b-46f2-8ce7-775e518efa4b)
    ![enumerated_heatmap](https://github.com/afadilla13/Final-Project-Melb-House-Price-Prediction/assets/128363337/7f206180-365a-4082-a1e2-ce3b6163baf3)

    - Applying Log transformation to price
    ![Histogram  with Log Price](./EDA_Output/log_price_feature_distribution_histogram.jpg)
    ![Box Plot with Log Price](./EDA_Output/log_price_feature_distribution_boxplot.jpg)

3. **Model Training & Evaluation**:
    - Splitting the data into training and testing sets
    ![Splitting Data](https://github.com/afadilla13/Final-Project-Melb-House-Price-Prediction/assets/128363337/4e810cc8-8f94-407f-8ba8-e00d8f544b61)
    - Training multiple regression models (Linear Regression, Decision Trees, Gradient Boosting, Random Forests, Decision Tree, Support Vector Regressor, Lasso, Ridge)
    - Evaluating model performance using metrics like Root Mean Squared Error (RMSE), Mean Squared Error (MSE), Mean Absolute Error (MAE) and R-squared.

4. **Recommendation Engine**:
    - **For families:** Suggesting properties based on their preferences and budget.
    - **For investors:** Highlighting properties that are priced lower than the predicted value, indicating potential undervaluation.

## Results

After evaluating multiple models, **the Random Forest Regression model using Randomized Search CV showed the best performance with an MSE of 0.05231951273435163, RMSE of 0.22873459015713304, MAE of 0.17046033421544568 and an R-squared value of 0.8017764493321988**. This model was then used to predict property prices on unseen data.

![Best_Model](https://github.com/afadilla13/Final-Project-Melb-House-Price-Prediction/assets/128363337/e51d0db8-2a20-4dc6-891e-e54ef8648beb)

Our recommendation engine was able to:

- Suggest suitable properties for families based on their inputs.
- Identify potential undervalued properties for investors, which could yield higher returns upon investment.

## Webpage Display with interactive Google maps background

![Google_maps](https://github.com/afadilla13/Final-Project-Melb-House-Price-Prediction/assets/128363337/9493035e-8684-4ba2-aac6-aed526ee0271)

Webpage display before features selection:
![Webpage 1](https://github.com/afadilla13/Final-Project-Melb-House-Price-Prediction/assets/128363337/776f88f7-cfe8-4ff4-8c6b-a0dfc9b337f8)

Webpage display after features selection:
![Webpage 2](https://github.com/afadilla13/Final-Project-Melb-House-Price-Prediction/assets/128363337/b6aced9a-55da-4fa6-b024-87f8f8a0e126)


## Conclusion

Machine learning offers a powerful tool for making informed decisions in the property market. By utilizing historical data and predictive modeling, both families and investors can benefit from insights that weren't previously accessible. We encourage users to explore our model, provide feedback, and even contribute to its further development.
