### Metis Project 3: Classification and Web Apps

# Predicting Bike Share User Type

### [Matt Ranalletta](https://www.linkedin.com/in/matthewranalletta/)

## Goal

The goal of this project is to use machine learning classification methods to determine, based on a list of features, what type of Bay Area Bay Wheels bike share rider someone is — a subscribing member or casual user.

This could be useful for Lyft (the bike share system operator in the Bay) to better understand how to better target riders and how to best grow operations.

## Context

I am attempting to use data science to answer the question of what actually defines the two classifications of bike share riders, so that the data can be used to improve system efficiency, station placement, and marketing efforts.

## Methodologies

1. ) Researched different sources and found three data sets:
      - [Bay Wheels by Lyft](https://www.lyft.com/bikes/bay-wheels/system-data) - ridership data
      - [General Bikeshare Feed Specification](https://gbfs.baywheels.com/gbfs/gbfs.json) - additional station data
      - [Bureau of Transportation](https://data-usdot.opendata.arcgis.com/datasets/bikeshare) - transit connections
      
2. ) Joined the collected data about station information with Bay Wheels' own data regarding ridership.
SQL
3. ) One-hot encoded categorical information into dummy variables.
4. ) Accomodated for class imbalance using _____ .
5. ) Tested seven different classification models.
6. ) Optimized, evaluated, and selected the best model -- ______ .
7. ) Discovered feature importance.
8. ) Built a visualization

## Findings and Conclusions

In scraping and analyzing yoga class data, I found that the vast majority (over 60%) of yoga classes had been labelled by their teachers as "Vinyasa" or "Hatha". Far fewer classes get labeled with the other class types, even if technically the class being offered actually is more closely aligned with one of those types.

This can be problematic for both yoga teachers and yoga practitioners. For practitioners, if the vast majority of classes have the same 2 labels, but of course vary wildly in content, you could go in expecting one thing, but recieve a class of an entirely different intensity level you did not desire, since they've been obscured to be extremely broad and non-descript terms. As a teacher, it is important to be candid about what you are actually offering.

After training and optimizing seven different classification models, I found that a _____ performed the best. It had good ROC-AUC and high recall for all classes.

I essentially used Data Science to find aggregate decisions across thousands of individual teachers' yoga classes about what poses are included in each type of class, to better define those ambiguous definitions. As it turns out, the most influential factors on class type are how much of the class is spent in Strengthening, Standing, Inversion, and Balance poses.

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
- SQL

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

- Classification Scoring Metrics
- ROC-AUC Curves
- Precision-Recall Trade-off
- EDA
