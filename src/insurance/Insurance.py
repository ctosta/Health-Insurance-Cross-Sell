import os 
import pickle
import pandas as pd
import numpy as np

class Insurance(): 
    def __init__(self):
        self.home_path = '/home/caroline/repos/pa-004/src/'
        self.annual_premium_scaler = pickle.load(open(self.home_path + 'features/annual_premium_scaler.pkl', 'rb'))
        self.age_scaler = pickle.load(open(self.home_path + 'features/age_scaler.pkl', 'rb'))
        self.days_associated_scaler = pickle.load(open(self.home_path + 'features/days_associated_scaler.pkl', 'rb'))
        self.target_encoder_gender = pickle.load(open(self.home_path + 'features/target_encoder_gender.pkl', 'rb'))
        self.fe_region_code = pickle.load (open(self.home_path + 'features/fe_region_code.pkl', 'rb'))
        self.fe_vehicle_age = pickle.load (open(self.home_path + 'features/fe_vehicle_age.pkl', 'rb'))
        self.fe_policy_sales_channel = pickle.load (open(self.home_path + 'features/fe_policy_sales_channel.pkl', 'rb'))


    def data_cleaning(self, df1):
    
        # rename columns
        df1.columns = [x.lower() for x in df1.columns]
        df1 = df1.rename(columns={'vintage' :'days_associated'})
            
        return df1
    
    def feature_engineering(self, df2):
        # vehicle_age
        df2['vehicle_age'] = df2['vehicle_age'].apply(lambda x: 'over_2_years' if x == '> 2 Years' 
                                                         else 'between_1_2_year' if x == '1-2 Year' 
                                                         else 'below_1_year')
        # vehicle_damage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
    
        return df2


    def data_preparation(self, df3):
        # annual_premium
        df3['annual_premium'] = self.annual_premium_scaler.transform(df3[['annual_premium']].values)

        # age
        df3['age'] = self.age_scaler.transform(df3[['age']].values)

        # days_associated
        df3['days_associated'] = self.days_associated_scaler.transform(df3[['days_associated']].values)

        # gender
        df3.loc[:,'gender'] = df3['gender'].map(self.target_encoder_gender)
        
        # region_code
        df3.loc[:,'region_code'] = df3['region_code'].map(self.fe_region_code)

        # vehicle_age
        df3.loc[:,'vehicle_age'] = df3['vehicle_age'].map(self.fe_vehicle_age)

        # policy_sales_channel
        df3.loc[:,'policy_sales_channel'] = df3['policy_sales_channel'].map(self.fe_policy_sales_channel)
       
        
        cols_selected = ['age', 'region_code', 'previously_insured', 'vehicle_age', 'vehicle_damage', 'annual_premium', 'policy_sales_channel']

        return df3[cols_selected]
    
    def get_prediction( self, model, original_data, test_data ):

        #model prediction
        pred = model.predict_proba( test_data )

        #join prediction into original data and sort
        original_data['Score'] = pred[:, 1].tolist()
        original_data = original_data.sort_values('Score', ascending=False)

        return original_data.to_json( orient= 'records', date_format = 'iso' )
