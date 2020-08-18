import streamlit as st 
import pandas as pd 
import numpy as np
import base64 as base64

# This is the source code for the OCG Synaptic Gene Finder.
# Designed to take in text input and output a list of synaptic genes that are shared between our list and the input list.

st.title('OCG Synaptic Gene Finder 🔬')
st.markdown("Note that this only works if your input file extension is .txt or .csv and *only* contains FlyBase gene IDs.")

st.text("Here's the list of our genes that we are comparing your input to:")
synaptic_df = pd.read_csv("/Users/MOON/Documents/summer_utra_2020/synaptic_gene_list.csv")
synaptic_df.columns = ['Gene', 'GeneName']
st.dataframe(synaptic_df, width=8000)

selected = st.selectbox("Does this file contain:", ['FlyBase IDs', 'FlyBase Names'])
input_file = st.file_uploader("Choose your input file:", type=('txt','csv'))

def compare_geneID(in_file):
    # This function compares gene IDs/names. 
    if in_file == None:
        st.markdown("No file inserted!")
    else:    
        input_df = pd.read_csv(in_file, delim_whitespace=True, header=None)
        if selected == 'FlyBase IDs':
            input_df = input_df.rename(columns={input_df.columns[0]: 'gene_id'})
            merged_df = input_df.merge(synaptic_df, left_on='gene_id', right_on='Gene')
            final_df = merged_df.drop('gene_id', axis=1)
        else:
            input_df = input_df.rename(columns={input_df.columns[0]: 'gene_name'})
            merged_df = input_df.merge(synaptic_df, left_on='gene_name', right_on='GeneName')
            final_df = merged_df.drop('gene_name', axis=1)
        
        return final_df

# Display results.
results = compare_geneID(input_file)
if input_file != None:
    st.text("Here are the gene " + selected.split()[1].lower() + " both lists have in common:")
    st.dataframe(results)
    
    # Download the results.
    file_name = st.text_input("Insert file name (ex.myfile.csv):")
    clicked = st.button("Download as .csv file")
    if clicked:
        if file_name == None:
            st.text("You must insert a file name above!")
        else:
            csv = results.to_csv(index=False, header=True)  
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}">Download csv file</a>'
        
        st.markdown(href, unsafe_allow_html=True)