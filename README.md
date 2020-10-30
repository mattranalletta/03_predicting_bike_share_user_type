### Metis Project 3: Classification and Web Apps

# Predicting Bike Share User Type

### [Matt Ranalletta](https://www.linkedin.com/in/matthewranalletta/)

## Goal

The goal of this project is to use machine learning classification methods to determine, based on a list of features, what type of Bay Area Bay Wheels bike share rider someone is — a subscribing member or casual customer, referred to in the raw data set as "Subscriber" or "Customer."

This could be useful for Lyft (the Bay Wheels operator) to better understand how to better target riders and how to best grow operations.

Turning casual users into regular riders seems to to be a big goal of Lyft itself, as many calls to action on the [Bay Wheels website](https://www.lyft.com/bikes/bay-wheels) are prompting people to become members (see slide 3 of my presentation [here](https://docs.google.com/presentation/d/1SD74RgLegORcC0ilPPGmCsjnTEjG0r2kU4tdTO4vxLc/edit#slide=id.g6320de4b7d_0_424).

## Methodologies

1. Researched different sources and found three relevant data sets:
      - [Bay Wheels by Lyft](https://www.lyft.com/bikes/bay-wheels/system-data) - ridership data
      - [General Bikeshare Feed Specification](https://gbfs.baywheels.com/gbfs/gbfs.json) - additional station data, like bike capacity at each dock
      - [Bureau of Transportation](https://data-usdot.opendata.arcgis.com/datasets/bikeshare) - transit connections to each bike dock
2. Joined the collected data about station information with Bay Wheels' own data regarding ridership (PostGreSQL and Pandas).
3. One-hot encoded categorical information into dummy variables.
4. Accomodated for class imbalance using Random Over Sampler.
5. Tested out seven different classification models.
6. Optimized, evaluated, and selected the best model - XGBClassifier.
7. Discovered feature importance.
8. Built a basic application in Streamlit.

## Findings and Conclusions

After training and optimizing seven different classification models, I found that an XGBClassifier performed the best. It had the best AUC-ROC score of all the models and a high recall (0.77) for the Casual Customer class, meaning that the model is correctly identifying 77% of Bay Wheels' non-subscribing riders. The XGB model

## Deliverables

Sequentially:

- [Data Collection](https://github.com/mattranalletta/03_predicting_bike_share_user_type/tree/main/data)
- [EDA](https://github.com/mattranalletta/03_predicting_bike_share_user_type/blob/main/code/baywheels_EDA.ipynb)
- [Classification Modeling]()
- [Web App code](https://github.com/mattranalletta/03_predicting_bike_share_user_type/blob/main/code/baywheels_app.py)
- [Presentation Slides](https://docs.google.com/presentation/d/1SD74RgLegORcC0ilPPGmCsjnTEjG0r2kU4tdTO4vxLc/edit?usp=sharing)

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
- Classification Scoring Metrics (Accuracy, Precision, Recall, f1, AUC-ROC score)
- ROC-AUC Curves
- Precision-Recall Trade-off
