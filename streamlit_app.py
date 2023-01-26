import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import urlerror

  # import streamlit

streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega3 & Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔  🥑🍞Hard-boiled free range Egg')
streamlit.text('🥑🍞 Avocoda Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


# import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#new section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
my_data_row = my_cur.fetchone()
streamlit.header( "The Fruit list Load Contains:")
streamlit.dataframe(my_data_row)

my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header( "The Fruit list Load Contains:")
streamlit.dataframe(my_data_rows)


my_cur.execute("insert into fruit_load_list values ('from streamlit')")







