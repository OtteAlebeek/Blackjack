import streamlit as st
import pandas as pd
import numpy as np
import pickle

Predictor1 = pickle.load(open('C:\Users\ottev\Downloads\KNNPrediction1.pkl', 'rb'))
Predictor2 = pickle.load(open('C:\Users\ottev\Downloads\KNNPrediction2.pkl', 'rb'))
Predictor3 = pickle.load(open('C:\Users\ottev\Downloads\KNNPrediction3.pkl', 'rb'))

st.markdown("""
# Blackjack Predictor

This is the main page for the Blackjack Predictor. On this page you can select how many cards you have in hand,
so you can make a choice for the right predictor.

There are 3 different predictors where you can choose for:
    
First prediction
    
In this prediction you get to know if you need to hit or stand in a game of blackjack after receiving your first 2 cards.

Second prediction
    
In this prediction you get to know if you need to hit or stand in a game of blackjack after receiving your first 3 cards.

Third prediction
    
In this prediction you get to know if you need to hit or stand in a game of blackjack after receiving your first 4 cards.


""")

selected_page = st.selectbox("Select the prediction", ("Home", "First", "Second", "Third"))

if selected_page == 'First':

    st.write("""
    # First prediction
    On this page you will get to know if you need to hit or stand after receiving your first 2 cards.

    Fill in the filters and see what the best strategy for your next step is
    """)
 
    def user_input_features():
     card1 = st.number_input("The first card you get", min_value=1, max_value=11)
     card2 = st.number_input("The second card you get", min_value=1, max_value=11)
     dealcard1 = st.number_input("The first card the dealer get", min_value=1, max_value=11)
     ply2cardsum = st.number_input("The sum of the first 2 cards", card1+card2, max_value=21)
     data = {'The first card you get': card1,
            'The second card you get': card2,
            'The first card the dealer get': dealcard1,
            'Sum of the first 2 cards you get': ply2cardsum}
     features = pd.DataFrame(data, index=['Values'])
     return features

    df = user_input_features()
    st.write(df)

    if st.button('Submit'):
        Predictor1_load = Predictor1.predict(df)
        data = {'What is the next step?': Predictor1_load}
        features = pd.DataFrame(data, index=['Value'])
        st.write(features)

elif selected_page == 'Second':

    st.write("""
    # Second prediction
    On this page you will get to know if you need to hit or stand after receiving your first 3 cards.

    Fill in the filters and see what the best strategy for your next step is
    """)
 
    def user_input_features():
     card1 = st.number_input("The first card you get", min_value=1, max_value=11)
     card2 = st.number_input("The second card you get", min_value=1, max_value=11)
     card3 = st.number_input("The third card you get", min_value=1, max_value=11)
     dealcard1 = st.number_input("The first card the dealer get", min_value=1, max_value=11)
     ply3cardsum = st.number_input("Sum of the first 2 cards you get",  card1+card2+card3, max_value=21)
     data = {'The first card you get': card1,
            'The second card you get': card2,
            'The third card you get': card3,
            'The first card the dealer get': dealcard1,
            'Sum of the first 3 cards you get': ply3cardsum}
     features = pd.DataFrame(data, index=['Values'])
     return features

    df = user_input_features()
    st.write(df)

    if st.button('Submit'):
        Predictor2_load = Predictor2.predict(df)
        data = {'What is the next step?': Predictor2_load}
        features = pd.DataFrame(data, index=['Value'])
        st.write(features)


elif selected_page == 'Third':

    st.write("""
    # Third prediction
    On this page you will get to know if you need to hit or stand after receiving your first 4 cards.

    Fill in the filters and see what the best strategy for your next step is
    """)

    def user_input_features():
        card1 = st.number_input("The first card you get", min_value=1, max_value=11)
        card2 = st.number_input("The second card you get", min_value=1, max_value=11)
        card3 = st.number_input("The third card you get", min_value=1, max_value=11)
        card4 = st.number_input("The fourth card you get", min_value=1, max_value=11)
        dealcard1 = st.number_input("The first card the dealer get", min_value=1, max_value=11)
        ply4cardsum = st.number_input("Sum of the first 2 cards you get", card1+card2+card3+card4, max_value=21)
        data = {'The first card you get': card1,
            'The second card you get': card2,
            'The third card you get': card3,
            'The fourth card you get': card4,
            'The first card the dealer get': dealcard1,
            'Sum of the first 4 cards you get': ply4cardsum}
        features = pd.DataFrame(data, index=['Values'])
        return features

    df = user_input_features()
    st.write(df)

    if st.button('Submit'):
        Predictor3_load = Predictor3.predict(df)
        data = {'What is the next step?': Predictor3_load}
        features = pd.DataFrame(data, index=['Value'])
        st.write(features)
