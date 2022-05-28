# -*- coding: utf-8 -*-
"""
Created on Sat May 28 16:56:01 2022

@author: marlo
"""

import streamlit as st

emprestimo = st.number_input('Valor Crédito')
st.write('The current number is ', emprestimo)


taxa_juros= st.number_input('Taxa de Juros')
st.write('The current number is ', taxa_juros)

prazo = st.number_input('prazo')
st.write('The current number is ', prazo)

#Exercício financiamento SAC rodrigo mais completo




if st.button('Calcular'):
    prazo = int(prazo)
    juros_valor = emprestimo*taxa_juros/100
    valor_amort = emprestimo/prazo
    parcela = valor_amort + juros_valor
    resultado = 'O valor de cada parcela é de R$', parcela
    total2 = ((parcela*prazo)-emprestimo)
    jurostotal = 'O valor total de juros foi de',total2
st.success(resultado)
        #   st.success(f'O saldo devedor no fim de cada período será de R$ {saldosdevedores}')
st.success(jurostotal)
        
