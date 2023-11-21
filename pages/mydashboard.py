from turtle import width
import streamlit as sl
import pandas as pd
import os #to deal with files & paths etc.
import plotly.express as px

sl.set_page_config(page_title="My Dashboard", layout="wide")

sl.sidebar.header("Data inputs")
with sl.sidebar:
    ##this is to place a file uploader in the side bar
    fl = sl.sidebar.file_uploader(":file_folder: Upload your data file", type=(["csv", "dat"])) #:file_folder: is to give it an icon.

# sl.write("fl.name")
isDF = 0
if fl is not None:
    filename = fl.name
    sl.write("File uploaded: " + filename)
    df = pd.read_csv(filename, encoding="ISO-8859-1")  #filename is discoverable as file to streamlit as path 
                                                            #because the uploaded file it with streamlit server only on the same path
    isDF = 1    
    sl.write(df) #Just print the data uploaded    

# else: #in case we need to do thiss
# #     os.chdir(r"ABSOLUTLE PATH TO THE LOCAL FILE OR SO")
# #     df = pd.read_csv(Local_fileName, encoding="ISO-8859-1") #This will now point to the set path as above using os.chdir
#     isDF = 1
if isDF == 1:
    sl.title("Dashboard - Data Analysis of the uploaded data")

    #This data contains Order Date
    #Let's create StartDate & EndDate selector basis the min & max values of the OrderDate data available 

    #split the page width in two columns
    col1, col2 = sl.columns((2))

    #Convert the OrderDate within the dataframe as datetime from the existing string values. Again make use of pandas (pd) functions
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    #find the min & max values as the default dates for date pickers
    startDate = df["Order Date"].min()
    endDate = df["Order Date"].max()

    #now, let's create the date picker control in these columns with given OrderDate values as the default values
    with col1:
        fromDate = pd.to_datetime(sl.date_input("Start Date", startDate))

    with col2:
        toDate = pd.to_datetime(sl.date_input("End Date", endDate))

    #Now, let's filter the data based upon selected fromDate & toDate
    df_filtered = df[(df["Order Date"] >= fromDate) & (df["Order Date"] <= toDate)]
    # sl.write(df_filtered)  #Works fine

    #Let's create a chart on the filtered data
    #We will use plotty charts of Python
    #Cateogry vs Sales columns
    sales_df = df_filtered.groupby(by = "Category", as_index=False)["Sales"].sum()
    chart1 = px.bar(sales_df, x = "Category", y = "Sales", template="seaborn")
    sl.plotly_chart(chart1, use_container_width=True, width=200)

    col3, col4 = sl.columns((2))

    with col3:
        sl.subheader("Sales by Segment:", divider="rainbow")
        segment_df = df_filtered.groupby(by="Segment", as_index=False)["Sales"].sum()
        pc1 = px.pie(segment_df, names="Segment", values="Sales")
        sl.plotly_chart(pc1, use_container_width=True, width=200)

    with col4:
        sl.subheader("Sales by Region:", divider="rainbow")
        region_df = df_filtered.groupby(by="Region", as_index=False)["Sales"].sum()
        pc1 = px.pie(region_df, names="Region", values="Sales")
        sl.plotly_chart(pc1, use_container_width=True, width=200)    