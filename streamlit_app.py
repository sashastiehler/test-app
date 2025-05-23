import streamlit as st
import pandas as pd
import mag4 as mg
import matplotlib.pyplot as plt

st.title("Title")

st.write('Hello World')

df_mag4_available = mg.available_datasets()[['Source', 'Short Title', 'Title']]
fil = df_mag4_available['Source'] == 'Georoc'
df_georoc_datasets = df_mag4_available[fil]['Title'].tolist()

locals = st.multiselect("Select Location",df_georoc_datasets, default=df_georoc_datasets[0])

def make_plot(name):    
    df = mg.get_data(locals[0])
    elements = df.columns.tolist()[27:]

    xEl = st.selectbox(f'Select first element for {name}',elements,0)
    yEl = st.selectbox(f'Select second element for {name}',elements,9)

    fig, ax = plt.subplots()

    for dataset in locals:
        df = mg.get_data(dataset)
        ax.scatter(df[xEl]/10000, df[yEl]/10000, label=dataset)

    ax.set_xlabel(f'{xEl} (wt%)')
    ax.set_ylabel(f'{yEl} (wt%)')
    fig.legend(bbox_to_anchor=(.7, 0))

    st.pyplot(fig)

if len(locals) > 0:
    make_plot('first plot')
    make_plot('second plot')