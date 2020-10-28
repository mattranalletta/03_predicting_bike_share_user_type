### Metis Project 3: Classification and Web Apps

# Predicting Bike Share User Type

### [Matt Ranalletta](https://www.linkedin.com/in/matthewranalletta/)

## Goal

The goal of this project is to use machine learning classification methods to determine, based on a list of features, what type of Bay Area Bay Wheels bike share rider someone is — a subscribing member or casual user.

This could be useful for Lyft (the bike share system operator in the Bay) to better understand how to better target riders and how to best grow operations.

## Context

I am attempting to use data science to answer the question of what actually defines the two classifications of bike share riders, so that the data can be used to improve system efficiency, station placement, and marketing efforts.

## Methodologies

1. Researched different sources and found three data sets:
      - [Bay Wheels by Lyft](https://www.lyft.com/bikes/bay-wheels/system-data) - ridership data
      - [General Bikeshare Feed Specification](https://gbfs.baywheels.com/gbfs/gbfs.json) - additional station data
      - [Bureau of Transportation](https://data-usdot.opendata.arcgis.com/datasets/bikeshare) - transit connections
      
2. Joined the collected data about station information with Bay Wheels' own data regarding ridership.
SQL
3. One-hot encoded categorical information into dummy variables.
4. Accomodated for class imbalance using Random Over Sampler.
5. Tested seven different classification models.
6. Optimized, evaluated, and selected the best model - XGBClassifier.
7. Discovered feature importance.
8. Built a visualization in Streamlit.

## Findings and Conclusions

(more info here)

After training and optimizing seven different classification models, I found that an XGBClassifier performed the best. It had the best ROC-AUC and a high recall for the casual user class.

I used data science to find aggregate decisions across thousands of bike share rides in the Bay Area. As it turns out, the most influential factors on determining user type are the duration of the ride and the distance ridden.

## Deliverables

Sequentially:

- [Data Collection](https://github.com/mattranalletta/03_predicting_bike_share_user_type/tree/main/data)
- [EDA]()
- [Classification Modeling]()
- [Visualization]()
- [Presentation Slides]()

## Technologies Used

- Jupyter Notebook
- Python
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn
- PostGreSQL

## Approaches and Skills

**Classification Algorithms**:

- KNN
- Logistic Regression
- Decision Tree
- Random Forest
- Bernoulli Naive Bayes
- Gaussian Naive Bayes
- XGBoost

**Other**

- EDA
- Classification Scoring Metrics (Accuracy, Precision, Recall, f1)
- ROC-AUC Curves
- Precision-Recall Trade-off
