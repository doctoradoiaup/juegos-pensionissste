# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:23:29 2024

@author: jperezr
"""

import streamlit as st

# Mostrar la imagen al inicio
st.image("logo.jpg", width=710)  # Ajusta el ancho según tus necesidades

st.subheader("")
st.subheader("")


st.title("Desafío PensionISSSTE: ¡Pon a Prueba tu Conocimiento!")

st.subheader("")
st.subheader("")

# Cambia el siguiente enlace por el de tu formulario
iframe_code = '''
<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeoGW7x2qru4bpel_7DXnJuVf0tV44YJSV67rN-j0mVymd-Bw/viewform?usp=sf_link" width="700" height="600"></iframe>
'''
st.components.v1.html(iframe_code, height=600)
