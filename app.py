# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:23:29 2024

@author: jperezr
"""

import streamlit as st

# Mostrar la imagen al inicio
st.image("logo.jpg", width=710)  # Ajusta el ancho según tus necesidades

st.title("Desafío PensionISSSTE: ¡Pon a Prueba tu Conocimiento!")

# Descripción en la barra lateral
with st.sidebar:
    st.header("¿De qué trata?")
    st.write("""
    Este desafío está diseñado para ayudarte a conocer mejor tu AFORE PensionISSSTE. 
    Responde preguntas sobre el sistema de ahorro para el retiro, los beneficios del ahorro voluntario, 
    y mucho más. ¡Es una excelente oportunidad para aprender y asegurar tu futuro financiero!
    """)
    st.write("¡Participa y conviértete en un experto en tu AFORE!")

# Cambia el siguiente enlace por el de tu formulario
iframe_code = '''
<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeoGW7x2qru4bpel_7DXnJuVf0tV44YJSV67rN-j0mVymd-Bw/viewform?usp=sf_link" width="700" height="600"></iframe>
'''
st.components.v1.html(iframe_code, height=600)
