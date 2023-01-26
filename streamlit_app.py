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
#streamlit.header("Fruityvice Fruit Advice!")
#fruit_choice = streamlit.text_input ('what fruit would you like to information about?','Kiwi')
#streamlit.write('The user entered', fruit_choice)


#import requests
#streamlit.text(fruityvice_response.json())
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice")
#take the json verson and normalized it   
#fruitvice_normalized = pandas.json_normalize (fruitvice_response.json())
# Output as table
#streamlit.dataframe(fruitvice_normalized)

# Revised
#new section to display fruitvice api response
#streamlit.header("Fruityvice Fruit Advice!")
#try:
  #fruit_choice = streamlit.text_input ('what fruit would you like to information about?')
  #if not fruit_choice:
    #streamlit.error("Please select a fruit to get information.")
   #else:
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    #fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
    #streamlit.dataframe(fruitvice_normalized)
 #except urlerror as e:
    #streamlit.error()  
                                       
 #Revised for Function Call / Repetable Code Block
def get_fruitvice_data(this_fruit_choice):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
 fruitvice_normalized = pandas.json_normalize(fruitvice_response.json())
 return fruitvice_normalized

#new section to display fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
fruit_choice = streamlit.text_input ('what fruit would you like to information about?')
if not fruit_choice:
streamlit.error("Please select a fruit to get information.")
else:
back_from_function = get_fruitvice_data (fruit_choice)  
streamlit.dataframe(back_from_function)                             
except urlerror as e:
streamlit.error()                                      
                                      

# import snowflake.connector
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)
#my_data_row = my_cur.fetchone()
#streamlit.header( "The Fruit list Load Contains:")
#streamlit.dataframe(my_data_row)

#fruit load list for all
#my_cur.execute("select * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header( "The Fruit list Load Contains:")
#streamlit.dataframe(my_data_rows)
                                   
# Revised-- fruit load list for all and load into a button
                                 
streamlit.header( "The Fruit list Load Contains:")
#snowflake related functions:
def get_fruit_load_list():
with my_cnx.cursor() as my_cur: 
my_cur.execute("select * from fruit_load_list")
return my_cur.fetchall()
 # add a button to load the list
if streamlit.button('Get fruit load list') :
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cnx.close()                                   
my_data_rows = get_fruit_load_list()
streamlit.dataframe(my_data_rows)                                   
                                   
 #allow end user to add fruit to the list
#add_my_fruit = dtreamlit.text_input('what fruit would you like to add')  
#streamlit.write ('Thanks for adding', add_my_fruit )                                  

#will not work correctly
#my_cur.execute("insert into fruit_load_list values ('from streamlit')")
                                   
# Revised - allow end user to add fruit to the list
def insert_row_snowflake (new_fruit):
with my_cnx.cursor() as my_cur():
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
return  'Thanks for adding' + new_fruit                               
add_my_fruit = dtreamlit.text_input('what fruit would you like to add')  
if streamlit.button ('Add a fruit to the list'):
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
back_from_function = insert_row_snowflake(add_my_fruit)
streamlit.text(back_from_function)

   #streamlit.stop()




