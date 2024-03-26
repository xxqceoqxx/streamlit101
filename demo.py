import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("ทดสอบ Demo")
st.header("Hello World!")
st.write("This is my first app")

st.image("./images/Porto.jpg", width=650, caption="Porto, Portugal")



path = "./data/bank.csv"
data = pd.read_csv(path, sep=";")
st.subheader("Data Visualization")
st.write(data)


st.subheader("Value Counts of a Categorical Column")
selected_column = st.selectbox("Select a categorical column"
,
data.select_dtypes(include=object).columns)
st.write(f"Value counts of column: {selected_column}")
st.write(data[selected_column].value_counts())


st.subheader("Bar Plot")
columns = list(data.columns)
column = st.selectbox("Select column", columns)
st.bar_chart(data[column].value_counts())

st.subheader("Age Option")
option = st.radio("Select your age option to see the data", ('Youngest','Middle','Oldest'))
if option == 'Youngest':
    st.write("The youngerst person is ", min(data['age'])," years old.")
elif option == 'Middle':
    st.write("The middle person is ", int(data['age'].median())," years old.")
else:
    st.write("The oldest person is ", max(data['age'])," years old.")

st.subheader("Basic Statistics of the Dataset")
st.write(data.describe())

st.subheader("Scatter Plot")
st.write("Select the columns for the scatter plot:")
x_column = st.selectbox("X Axis", data.columns, index=0)
y_column = st.selectbox("Y Axis", data.columns, index=1)
st.write(f"Creating scatter plot between {x_column} and {y_column}")
plt.scatter(data[x_column], data[y_column])
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)

st.subheader("Distribution Plot")
selected_column = st.selectbox("Select a numerical column",data.select_dtypes(include=[int, float]).columns)
st.write(f"Displaying distribution of column: {selected_column}")
plt.hist(data[selected_column])
st.pyplot()

VIDEO_URL = "https://www.youtube.com/watch?v=QQYgCxu988s"
st.subheader("Video Display")
st.video(VIDEO_URL)


option = st.radio("Select dataset option", ('bank','titanic'))
if option == 'bank':
    path = "./data/bank.csv"
    data = pd.read_csv(path, sep=";")
elif option == 'titanic':
    path = "./data/titanic.csv"
    data = pd.read_csv(path, sep=",")
    data.columns = data.columns.str.lower()