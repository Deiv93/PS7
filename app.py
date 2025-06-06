
# sourcery skip: use-named-expression
import pandas as pd
import plotly.express as px
import streamlit as st

st.header("ANALISIS DE VENTA DE VEHICULOS USADOS  DAVID MONTES DE OCA")

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
dispersion_button= st.button('Diagrama de dispersion')

if dispersion_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion  para el conjunto de datos de anuncios de venta de coches')
    
    #crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price") # 
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
    
    
build_histogram = st.checkbox('Construir Evolucion de precio')
if build_histogram:
    st.write('Evolucion de precio promedio')
    df_car=car_data.groupby(['date_posted','condition'])['price'].mean().reset_index()
    fig3= px.line(df_car, x="date_posted", y="price", color='condition')
    st.plotly_chart(fig3, use_container_width=True)