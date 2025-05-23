import streamlit as st
import pandas as pd
import mag4 as mg
import matplotlib.pyplot as plt

st.title("Title")

st.write('Hello World')

df = mg.get_data('bastcrat')

xEl,yEl = df['Mg'],df['Si']

elements = df.columns.tolist()[27:]
xEl = st.selectbox("Select First Element",elements,0)
yEl = st.selectbox("Select Second Element",elements,9)

fig, ax = plt.subplots()
ax.scatter(df[xEl],df[yEl])
ax.set_xlabel(f'{xEl} (w%)')
ax.set_ylabel(f'{yEl} (w%)')
st.pyplot(fig)