import streamlit

streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega3 & Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔  🥑🍞Hard-boiled free range Egg')
streamlit.text('🥑🍞 Avocoda Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
