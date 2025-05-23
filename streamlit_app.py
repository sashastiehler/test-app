import streamlit as st
import pandas as pd
import mag4 as mg
import matplotlib.pyplot as plt

st.title("Title")

st.write('Hello World')

df_mag4_available = mg.available_datasets()[['Source', 'Short Title', 'Title']]
fil = df_mag4_available['Source'] == 'Georoc'
df_georoc_datasets = df_mag4_available[fil]['Title'].tolist()

locals = st.selectbox("Select Location",df_georoc_datasets,0)

df = mg.get_data(locals)

elements = df.columns.tolist()[27:]
xEl = st.selectbox("Select First Element",elements,0)
yEl = st.selectbox("Select Second Element",elements,9)

fig, ax = plt.subplots()
ax.scatter(df[xEl]/10000,df[yEl]/10000)
ax.set_xlabel(f'{xEl} (w%)')
ax.set_ylabel(f'{yEl} (w%)')
st.pyplot(fig)