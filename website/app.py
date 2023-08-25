import streamlit as st
import time
import pandas as pd

secret = st.secrets["secret"]

st.header(f"this is secret {secret}")


@st.cache_data
def get_data():
    time.sleep(3)
    df = pd.read_csv("example.csv")
    return df


st.markdown(
    """# This is a header
## This is a sub header
This is text"""
)

df = get_data()

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider("Select a line count", 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df
