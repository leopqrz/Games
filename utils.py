import streamlit as st
from st_clickable_images import clickable_images   
import base64
import os


def date_time():
    ph = st.empty()
    now = dt.now()
    ph.metric("", now.strftime("%Y/%m/%d  %H:%M:%S"))


def set_bg_hack(main_bg):
    """
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    """
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-position: 50% 55%;
             background-repeat: no-repeat;
             background-size: 33%
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def encode_img(image):
    encoded = base64.b64encode(image.read()).decode()
    encoded = f"data:image/jpeg;base64,{encoded}"
    return encoded

def display_game(files, player1, player2):
    images = []
    for file in files:
        if os.path.isfile(file):
            with open(file, "rb") as image:
                encoded = encode_img(image)
                images.append(encoded)
        else:
            print(f"{file} is not a valid file path")

    placeholder = st.empty()
    clicked = clickable_images(
        images,
        titles=[f"Image #{str(i)}" for i in range(len(images))],
        div_style={
            "display": "flex", 
            "justify-content": "center", 
            "flex-wrap": "wrap"},
        img_style={
            "margin": "0px", 
            "height": "200px"},
    )
    return clicked