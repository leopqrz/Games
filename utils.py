"""Module with all useful functions."""
import base64
import os

import streamlit as st
from st_clickable_images import clickable_images


def date_time():
    """Display the current date and time."""
    ph = st.empty()
    now = dt.now()
    ph.metric('', now.strftime('%Y/%m/%d  %H:%M:%S'))


def set_bg_hack(main_bg):
    """Set a image as background."""
    # set bg name
    main_bg_ext = 'png'

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
    """Encode the image as base64.

    :param image: Path of the image
    :return: Encoded image
    """
    encoded = base64.b64encode(image.read()).decode()
    encoded = f'data:image/jpeg;base64,{encoded}'
    return encoded


def display_game(files, player1, player2):
    """Display the game.

    :param files: All image files to be displayed
    :param player1: Name of the player 1
    :param player2: Name of the player 2
    :return: Number with the order of the clicked image
    """
    images = []
    for file in files:
        if os.path.isfile(file):
            with open(file, 'rb') as image:
                encoded = encode_img(image)
                images.append(encoded)
        else:
            print(f'{file} is not a valid file path')

    placeholder = st.empty()
    clicked = clickable_images(
        images,
        titles=[f'Image #{str(i)}' for i in range(len(images))],
        div_style={
            'display': 'flex',
            'justify-content': 'center',
            'flex-wrap': 'wrap'},
        img_style={
            'margin': '0px',
            'height': '200px'},
    )
    
    # Movement order
    m = st.session_state['values']
    move = sum(map(lambda s: s.split('/')[1] != 'none', m))

    return clicked, move
