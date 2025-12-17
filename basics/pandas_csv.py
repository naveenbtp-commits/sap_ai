import pandas as pd 
df = pd.read_csv('dataset/nyc_weather.csv')
# print(df.head())  # Output the first 5 rows of the DataFrame
# print(df)  # Output the entire DataFrame
# print(df['Temperature'].max())  # Output the maximum temperature from the 'Temperature' column
# print(df['EST'][df['Events'] == 'Rain'])  # Output the 'EST' column values where the 'Events' column has the value 'Rain'
# print(df['WindSpeedMPH'].mean())  # Output the mean wind speed in mph from the 'WindSpeedMPH' column
# print(df['EST'] [0])  # Output the 'EST' column values for the specified rows
# print(df[['EST', 'Temperature', 'Sea Level PressureIn']])  # Output the 'EST' and 'Temperature' column values for the specified rows
# print(df['EST'][df['Events'] == 'Rain'])  # Output the 'EST' column values where the 'Events' column has the value 'Rain'
# df['naveen'] = df['Temperature'] + 10
# print(df)
df.fillna(0, inplace=True)
print(df)