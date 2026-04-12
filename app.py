import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(r"C:\Users\Moyam\OneDrive\Escritorio\TripleTen\Proyecto_7\vehicles_us.csv")

st.header("Análisis de datos de vehículos")

hist_button = st.button('Construir histograma')

if hist_button: # al hacer clic en el botón
        # escribir un mensaje
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        
        # crear un histograma
        ig = px.histogram(car_data, x="odometer")

        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(ig, use_container_width=True)

disp_button = st.checkbox("Creación de un gráfica de dispersión")

if disp_button: # al hacer click
        # Diagrama de dispersión
        st.write("Creación de un diagrama de dispersión con los datos de los vehiculos")
        
        # Crea la gráfica
        gi = px.scatter(car_data, x="odometer", y="price")
        
        # Gráfico interactivo
        st.plotly_chart(gi, use_container_width=True)
        
