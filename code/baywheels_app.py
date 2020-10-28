import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_auc_score


st.write(
'''
## Bay Area Bike Share Data
This combined data frame includes information from Lyft, owner of Bay Wheels, as well as the General Bikeshare Feed Specification and the U.S. Bureau of Transportation.
''')

bw = pd.read_pickle('bw_sf.pkl')
bw = bw.rename(columns={'start_lat': 'lat', 'start_long': 'lon'})
bw = bw.replace(r'', np.NaN, regex=True)

st.write(
'''
### Mapping the Stations by Distance Traveled
'''
)

time_input = st.slider('Ride Duration (in Seconds)', 65, 1800, 65 )

time_filter = bw['duration_sec'] < time_input
st.map(bw.loc[time_filter, ['lat', 'lon']])

st.write(
'''
## Train on XGBoost
I created a model to predict classifier from list of features:
- Duration on bike
- Start latitude/longitude
- End latitude/longitude
- Manhattan distance traveled on bike
- Number of transit connections at start and end of journey
- Start and end station station capacity
'''
) 
from xgboost import XGBClassifier
import xgboost as xgb
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split, cross_val_score, KFold, StratifiedKFold
from sklearn.preprocessing import StandardScaler

bw_plus = pd.read_pickle('bw.pkl')
bw_plus.drop(['access_method'],axis=1,inplace=True)
bw_plus = bw_plus.replace(r'', np.NaN, regex=True)
bw_plus.dropna(axis = 1, inplace=True)

features = ['duration_sec','start_lat','end_lat','start_long', 'end_long', 'manhattan_dist','start_transit','end_transit','start_cap','end_cap']

X = bw_plus[features]
y = bw_plus['user_type']

ros = RandomOverSampler(random_state=0)

X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.3, random_state=2, stratify=y)

final_model = XGBClassifier(max_depth = 7)
    
kf = StratifiedKFold(n_splits = 5, shuffle = True, random_state = 42)
kf.get_n_splits(X, y)
    
for train, test in kf.split(X, y):
        
    #Set up train and val for each fold
    X_train, X_test = X.iloc[train], X.iloc[test]
    y_train, y_test = y.iloc[train], y.iloc[test]

    #Scale data
    ss = StandardScaler()

    #fit transform X train
    X_train_scaled = ss.fit_transform(X_train)
    #transform X val
    X_test_scaled = ss.transform(X_test)
    X_test_scaled_pd = pd.DataFrame(X_test_scaled, columns=X_test.columns)

    #Oversample train data
    X_train_ROS, y_train_ROS = ros.fit_sample(X_train_scaled, y_train)

    X_train_ROS_pd = pd.DataFrame(X_train_ROS, columns=X_train.columns)
    #fit model
    final_model.fit(X_train_ROS_pd, y_train_ROS)

    #make prediction using y-val
    y_pred = final_model.predict(X_test_scaled_pd)

#metrics
st.write("ROC AUC score = ", roc_auc_score(y_test, final_model.predict_proba(X_test_scaled_pd)[:,1]))

st.write(
'''
## Make predictions from user input
'''
)
features = ['duration_sec','start_lat','end_lat','start_long', 'end_long', 'manhattan_dist','start_transit','end_transit','start_cap','end_cap']

duration = st.number_input('Duration (seconds)', value=2000)
start_latitude = st.number_input('Start Latitude', value=37.355693)
end_latitude = st.number_input('End Latitude', value=37.770030)
start_longitude = st.number_input('Start Longitude', value=-122.416040)
end_longitude = st.number_input('End Longitude', value=-122.51)
manh_dist = np.abs(start_latitude - end_latitude) + np.abs(start_longitude - end_longitude)
start_t = st.number_input('Start Transit', value=0)
end_t = st.number_input('End Transit', value=0)
start_c = st.number_input('Start Station Bike Capacity', value=15)
end_c = st.number_input('End Station Bike Capacity', value=15)


input_data = pd.DataFrame({'duration_sec': [duration], 'start_lat': [start_latitude], 'end_lat': [end_latitude], 'start_long': [start_longitude], 'end_long': [end_longitude], 'manhattan_dist': [manh_dist], 'start_transit': [start_t], 'end_transit':[end_t], 'start_cap':[start_c], 'end_cap':[end_c]})
pred = final_model.predict(input_data)[0]
st.write('Predicted Type: ',pred
)
