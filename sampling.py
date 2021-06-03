import pandas as pd

df_crop = pd.read_csv('crop_production.csv')
df_air = pd.read_csv('data.csv', encoding="ISO-8859-1")

df_air = df_air.replace({'Industrial Area': 'Industrial', 'Industrial Areas':'Industrial', 'Sensitive Areas':'Sensitive', 'Sensitive Area': 'Sensitive'})
df_air.drop(df_air[df_air['type']=='Industrial'].index, inplace = True)
df_air.drop(df_air[df_air['type']=='Residential'].index, inplace = True)

sample_states = ['Chhattisgarh', 'Gujarat', 'Haryana', 'Karnataka', 'Madhya Pradesh', 'Punjab', 'Uttar Pradesh', 'West Bengal']
df_air.drop(df_air[~df_air['state'].isin(sample_states)].index, inplace = True)
df_crop.drop(df_crop[~df_crop['State_Name'].isin(sample_states)].index, inplace = True)

df_crop['District_Name'] = df_crop['District_Name'].str.title()
df_air['location'] = df_air['location'].str.title()

#West Bengal
df_air['location'] = df_air['location'].str.replace('Haldia','Medinipur East')
df_air['location'] = df_air['location'].str.replace('Baruipur','24 Paraganas South')
df_air['location'] = df_air['location'].str.replace('Kalyani','Nadia')
df_air['location'] = df_air['location'].str.replace('Dankuni','Hooghly')
df_air['location'] = df_air['location'].str.replace('Sankrail','Howrah')

#Uttar Pradesh
df_air['location'] = df_air['location'].str.replace('Kanpur','Kanpur Nagar')
df_air['location'] = df_air['location'].str.replace('Gajraula','Amroha')
df_air['location'] = df_air['location'].str.replace('Khurja','Bulandshahr')
df_air['location'] = df_air['location'].str.replace('Rai Bareilly','Rae Bareli')

#Punjab
df_air['location'] = df_air['location'].str.replace('Gobindgarh','Fatehgarh Sahib')
df_air['location'] = df_air['location'].str.replace('Naya Nangal','Rupnagar')
df_air['location'] = df_air['location'].str.replace('Khanna','Ludhiana')
df_air['location'] = df_air['location'].str.replace('Dera Baba','Gurdaspur')

#Madhya Pradesh
df_air['location'] = df_air['location'].str.replace('Nagda','Ujjain')
df_air['location'] = df_air['location'].str.replace('Khajuraho','Chhatarpur')

#Karnataka
df_air['location'] = df_air['location'].str.replace('Hubli-Dharwad','Dharwad')
df_air['location'] = df_air['location'].str.replace('Hubli','Dharwad')
df_air['location'] = df_air['location'].str.replace('Bangalore','Bengaluru Urban')
df_air['location'] = df_air['location'].str.replace('Domlur','Bengaluru Urban')

#Gujarat
df_air['location'] = df_air['location'].str.replace('Baroda','Vadodara')
df_air['location'] = df_air['location'].str.replace('Ahmedabad','Ahmadabad')
df_air['location'] = df_air['location'].str.replace('Vapi','Valsad')
df_air['location'] = df_air['location'].str.replace('Ankleshwar','Bharuch')
df_air['location'] = df_air['location'].str.replace('Bhuj','Kachchh')
df_air['location'] = df_air['location'].str.replace('Sanand','Ahmadabad')
df_air['location'] = df_air['location'].str.replace('Sarigam','Valsad')

#Chattisgarh
df_air['location'] = df_air['location'].str.replace('Bhilai','Durg')
df_air['location'] = df_air['location'].str.replace('Bhilai Nagar','Durg')

for st in sample_states:
    location = df_air.loc[df_air['state'] == st]['location'].unique()
    District_Name = df_crop.loc[df_crop['State_Name'] == st]['District_Name'].unique()
    
    similar_location = [i for i in location if i in District_Name]
    df_air.drop(df_air.loc[df_air['state'] == st][~df_air['location'].isin(similar_location)].index, inplace = True)
    df_crop.drop(df_crop.loc[df_crop['State_Name'] == st][~df_crop['District_Name'].isin(similar_location)].index, inplace = True)
    

df_air.to_csv('sampled_air.csv',index=False)
df_crop.to_csv('sampled_crop.csv',index=False)