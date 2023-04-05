import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import streamlit as st

st.set_page_config(page_title= 'SMU Koufu')
st.header('No. of people in queue')

koufu_image = Image.open('Images/Koufu_logo.png')
drinks_image = Image.open('Images/drinks.jpeg')
banmian_image = Image.open('Images/banmian.jpeg')
caifan_image =Image.open('Images/caifan.jpeg')
dimsum_image =Image.open('Images/dimsum.jpeg')
fishball_image =Image.open('Images/fishball.jpeg')
fruitjuice_image =Image.open('Images/fruits.jpeg')
Mala_image =Image.open('Images/mala.jpeg')
Taiwan_image =Image.open('Images/taiwan.jpeg')
YongTauFoo_image=Image.open('Images/yongtaufoo.jpeg')

excel_file = 'Data_Collection.xlsm'
sheet_name ='Dashboard'

drinks1=st.empty()
banmian1=st.empty()
caifan1=st.empty()
dimsum1=st.empty()
fishball1=st.empty()
fruitjuice1=st.empty()
Mala1=st.empty()
Taiwan1=st.empty()
YongTauFoo1=st.empty()

col1, mid, col2 =st.columns([2,5,2])

with col1:
    st.subheader('Stores Directory')
with col2:
    st.image(koufu_image,
         width=100)



drinks = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='V',
                   header =8,
                   skiprows=[9,11,12,13,14])

banmian = pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        usecols='Z',
                        header=2,
                        skiprows=[3,5,6,7,8,9,10,11,12,13,14,15,16])

caifan =pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        usecols='AA',
                        header=2,
                        skiprows=[3,5,6,7,8,9,10,11,12,13,14,15,16])

dimsum =pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        usecols='AB',
                        header=2,
                        skiprows=[3,5,6,7,8,9,10,11,12,13,14,15,16])

fishball = pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        usecols='AD',
                        header=2,
                        skiprows=[3,5,6,7,8,9,10,11,12,13,14,15,16])

fruitjuice = pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        usecols='AE',
                        header=2,
                        skiprows=[3,5,6,7,8,9,10,11,12,13,14,15,16])

Mala= pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        usecols='AA',
                        header=9,
                        skiprows=[10,12,13,14,15,16,17])

Taiwan =pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        usecols='AB',
                        header=9,
                        skiprows=[10,12,13,14,15,16,17])

YongTauFoo =pd.read_excel(excel_file,
                        sheet_name=sheet_name,
                        usecols='AE',
                        header=9,
                        skiprows=[10,12,13,14,15,16,17])
                
with col1:
    st.dataframe(drinks)             
with col2:
    st.dataframe(banmian)
    
    
with col1:
    st.image(drinks_image,
             width=200)
with col2:
    st.image(banmian_image,
             width=133)
    
with col1:
    st.dataframe(caifan)
with col2:
    st.dataframe(dimsum)
    
    
with col1:
    st.image(caifan_image,
             width=300)
with col2:
    st.image(dimsum_image,
             width=170)

with col1:
    st.dataframe(fishball)
with col2:
    st.dataframe(fruitjuice)
    
with col1:
    st.image(fishball_image,
             width=220)
with col2:
    st.image(fruitjuice_image,
             width=200)

with col1:
    st.dataframe(Mala)
with col2:
    st.dataframe(Taiwan)
    
with col1: 
    st.image(Mala_image,
             width=200)
with col2:
    st.image(Taiwan_image,
             width=200)


st.dataframe(YongTauFoo)
st.image(YongTauFoo_image,
         width=200)

if st.button('Refresh'):
    st.experimental_rerun()
        
