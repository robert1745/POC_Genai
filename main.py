import streamlit as st  
from langchainhelper import generate_restaurant_name

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "Pick a cuisine",
    ["Italian", "Chinese", "Mexican", "Indian", "American"]
)


if cuisine:
    response = generate_restaurant_name(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items']
    
    for item in menu_items:
        st.write(f"- {item}")
        
