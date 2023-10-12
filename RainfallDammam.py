import streamlit as st
import pandas as pd
import plotly.express as px

#Naming and Creating a Streamlit app
st.title('Rainfall in Dammam, Saudi Arabia')
st.write('by Charbel Hanna Daou - 202371726 - American University of Beirut')

#Visualization N1 - Bar Chart with a time slider
#Loading the CSV file
df = pd.read_csv('RainfallDammam.csv')

#Converting the "YearMonth" column to a proper datetime format
df['YearMonth'] = pd.to_datetime(df['YearMonth'])

#Naming the first visualization
st.title('Bar Chart')

#Annotating the first visualization
st.write('Rainfall in mm from 2009 till 2019')
st.write("In the following bar chart, we illustrate the monthly rainfall data in Dammam, Saudi Arabia, spanning from January 2009 to December 2019. We have the flexibility to choose the end date we wish to focus on using the slider. Upon analyzing data for all the years, it becomes evident that the months of November through January, corresponding to the winter season, exhibit the highest levels of rainfall. April, in particular, stands out as a month with high levels of rainfall. The peak rainfall recorded during this entire decade occurred in November 2018, with a remarkable 78.1 mm of rainfall.")

#Adding a slider to select a specific year or month
min_date = df['YearMonth'].min()
max_date = df['YearMonth'].max()

selected_date_timestamp = st.slider("Select a Date", min_value=min_date.timestamp(), max_value=max_date.timestamp(), format="")

#Converting the selected timestamp back to a datetime object
selected_date = pd.to_datetime(selected_date_timestamp, unit='s')

#Filtering the data based on the selected date
filtered_df = df[df['YearMonth'] <= selected_date]

#Displaying the selected date as text
st.write(f'Selected Date: {selected_date.strftime("%B %Y")}')

#Creating and plotting the bar chart
fig = px.bar(filtered_df, x=filtered_df['YearMonth'].dt.strftime('%Y-%m'), y='Rainfallmm',
             title=f'Rainfall in Dammam Over Time (Selected Date: {selected_date.strftime("%B %Y")})',
             labels={'x': 'YearMonth (Categorical)', 'Rainfallmm': 'Rainfall (mm)'})
st.plotly_chart(fig, use_container_width=True)


#Visualization N2 - Heat Map with option to select year and month

# Loading the CSV file with Year, Month, and Rainfall in mm
dff = pd.read_csv('RainfallDammamxyz.csv')

# Naming the second visualization
st.title('Heat map')

# Annotating the second visualization
st.write('Rainfall in mm from 2009 till 2019')
st.write("In the heatmap, you can select specific years and months for a visual representation. The y-axis represents the months, while the x-axis displays the years. Each box in this matrix represents a unique combination of a month and year, with the box's color indicating the intensity of rainfall in Dammam during that specific period. What makes this visualization particularly useful is the ability to compare specific months on a year-to-year basis, helping us identify the years with the highest rainfall. When we select all years and months, clusters with more vivid colors stand out, suggesting periods of substantial rainfall, and vice versa. It's clear that, on average, the winter season from November to January consistently exhibits the highest levels of rainfall.")
         
# Creating a multiselect for selecting specific years
selected_years = st.multiselect('Select Year(s)', dff['Year'].unique())

# Creating a multiselect for selecting specific months
selected_months = st.multiselect('Select Month(s)', dff['Month'].unique())

# Filtering the data based on selected years and months
filtered_dff = dff[(dff['Year'].isin(selected_years)) & (dff['Month'].isin(selected_months))]

# Explicitly converting the "Rainfallmm" column to float
filtered_dff['Rainfallmm'] = filtered_dff['Rainfallmm'].astype(float)

# Pivoting the data for the heatmap
pivot_dff = filtered_dff.pivot_table(index='Month', columns='Year', values='Rainfallmm', aggfunc='mean')

# Creating the heatmap
fig2 = px.imshow(pivot_dff, labels={'x': 'Year', 'y': 'Month', 'color': 'Rainfallmm'}, title='Rainfall in Dammam Over Time (Heatmap)', color_continuous_scale='Viridis')
st.plotly_chart(fig2, use_container_width=True)
