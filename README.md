### Metis Project 3: Classification and Web Apps

# Predicting Bike Share User Type

### Matt Ranalletta

## Goal

The goal of this project is to use machine learning classification methods to determine, based on a list of features, what type of Bay Area bike share rider someone is — subscriber or casual user.

This could be useful for Lyft (the bike share system operator in the Bay) to better understand how to better target riders and how to best grow operations.

## Context

By trying to accurately predict a type of yoga based solely on what positions are practiced, I am attempting to use data science to answer the question of what actually defines the various classifications of yoga, so that both students and teachers alike can have more concrete definitions and better communication.

The end goal of this project is to create a web-based yoga sequencing application for yoga teachers, where they can create their own yoga classes from drop down menus of all 3600+ yoga poses and variations, sorted by their various features, and have their sequence analyzed to find out what genre it most closely falls into.

## Methodologies

1. ) Researched different sources and found 
2. ) Paired the collected data to include diagnostic info about every pose in every class.
3. ) One-hot encoded categorical information into dummy variables to get binary stats about whether each pose fell into each category.


6. ) Accomodated for class imbalance using RandomOverSampler.
7. ) Tested 6 different classification models.
8. ) Optimized, evaluated, and selected the best model -- Logistic Regression.
9. ) Discovered feature importance.
10. ) Built a [flask app](https://yoga-class-ification.herokuapp.com/) for yoga teachers to build their own yoga classes, and have them classified by percentage likelihood of falling into each genre!

## Findings and Conclusions

In scraping and analyzing yoga class data, I found that the vast majority (over 60%) of yoga classes had been labelled by their teachers as "Vinyasa" or "Hatha". Far fewer classes get labeled with the other class types, even if technically the class being offered actually is more closely aligned with one of those types.

This can be problematic for both yoga teachers and yoga practitioners. For practitioners, if the vast majority of classes have the same 2 labels, but of course vary wildly in content, you could go in expecting one thing, but recieve a class of an entirely different intensity level you did not desire, since they've been obscured to be extremely broad and non-descript terms. As a teacher, it is important to be candid about what you are actually offering.

After training and optimizing 6 different classification models, I found that a Logistic Regression performed the best. It had good ROC-AUC and high recall for all classes except Hatha.

And this is actually a good thing! Many classes that probably really should fall into other categories get naively mis-labeled by their teachers as "Hatha", and now I can help classify them correctly.

I essentially used Data Science to find aggregate decisions across thousands of individual teachers' yoga classes about what poses are included in each type of class, to better define those ambiguous definitions. As it turns out, the most influential factors on class type are how much of the class is spent in Strengthening, Standing, Inversion, and Balance poses.

## Deliverables

Sequentially:

- [Data Collection](https://github.com/anterra/yoga-class-ifying/tree/master/data_collection)
- [EDA and Feature Engineering](https://github.com/anterra/yoga-class-ifying/blob/master/classification_modeling/eda_feature_engineering.ipynb)
- [Pipeline Modules](https://github.com/anterra/yoga-class-ifying/blob/master/classification_modeling/pipeline_modules.py)
- [Classification Modeling](https://github.com/anterra/yoga-class-ifying/blob/master/classification_modeling/classification_modeling.ipynb)
- [Flask App](https://github.com/anterra/yoga-class-ifying/tree/master/flask_app)
- [Presentation Slides](https://github.com/anterra/yoga-class-ifying/blob/master/presentation/Yoga%20Classification.pdf)

## Project Team

- [Anterra Kennedy](https://www.linkedin.com/in/anterrakennedy/)

## Technologies Used

- Jupyter Notebook
- Python
- Scikit-learn
- Flask
- HTML/CSS
- Pandas
- Matplotlib
- Seaborn

## Approaches and Skills

**Classification Algorithms**:

- KNN
- Logistic Regression
- Decision Tree
- Random Forest
- Bernoulli Naive Bayes
- XGBoost

**Other**

- Classification Scoring Metrics
- ROC-AUC Curves
- Precision-Recall Trade-off
- EDA
- Webscraping
