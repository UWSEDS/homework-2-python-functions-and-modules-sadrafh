import pandas as pd


#Creating the ataFrame from URL

df = pd.read_csv(
    'https://data.seattle.gov/api/views/65db-xm6k/rows.csv')


#Tests

def test_create_dataframe(df,list_col):
    for k in list_col:
        if k not in list(df.columns):
            raise ValueError("check the column names")
    df_1=df[list_col]
    for j in list(df_1.columns):
        if len(list(df_1[j])) > 0 :
            result = all(type(df_1[j][i]) == type(df_1[j][0]) for i in range(len(df_1[j])))
        if result == False:
            raise TypeError("Values in each columns have diffrenet types")
        else:
            df_2=df_1
    if len(df_2)<10:
        raise ValueError("it should be at least 10 rows") 
    else:
        df_3=df_2
    return df_3

#print(test_create_dataframe(df,['Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk']))
