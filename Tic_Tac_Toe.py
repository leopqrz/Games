import streamlit as st
import utils
from glob import glob
import os

st.set_page_config(
    layout='centered',
    initial_sidebar_state='expanded',
    page_title='Games',
    page_icon='🧊',
)

st.markdown("<h1 style='text-align: center; color: gray;'>Tic Tac Toe Game</h1>", unsafe_allow_html=True)

# --------------------------- Layout setting ---------------------------
# Create an empty container in the sidebar
window_selection_c = st.sidebar.container()

# Add the players name
player1 = window_selection_c.text_input("Type the name of the player 1","Player 1")
player2 = window_selection_c.text_input("Type the name of the player 2","Player 2")


# Set the game display
files = sorted( # Load the image's paths
    map(os.path.basename, glob("img/none/*.png")), 
    key=lambda s: s[-5]+s[-7]
    )
paths = ["none", "x", "o"]  # The images are splitted into paths
values = [list(map(lambda s: "img/"+paths[i]+"/"+s, files)) for i in range(3)]  # Join all images into one list (0-none, 1-x, 2-o)

if 'values' not in st.session_state:
    st.session_state['values'] = values[0]

clicked = utils.display_game(st.session_state['values'], player1, player2)

# Game logic
if clicked in range(9):
    s = st.session_state['values'][clicked]
    mark = s.split("/")[1]  # none | x | o

    idx = paths.index(mark)
    if idx == 2:
        idx = -1
    st.session_state['values'][clicked] = values[idx+1][clicked]
