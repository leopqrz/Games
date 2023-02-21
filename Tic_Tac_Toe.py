"""_summary_."""
import os
from glob import glob

import numpy as np
import streamlit as st

import utils

st.set_page_config(
    layout='centered',
    initial_sidebar_state='expanded',
    page_title='Games',
    page_icon='🧊',
)

st.markdown("<h1 style='text-align: center; color: gray;'>Tic Tac Toe Game</h1>",
            unsafe_allow_html=True)

# --------------------------- Layout setting ---------------------------
# Create an empty container in the sidebar
window_selection_c = st.sidebar.container()

# Add the players name
player1 = window_selection_c.text_input(
    'Type the name of the player 1', 'Player 1')
player2 = window_selection_c.text_input(
    'Type the name of the player 2', 'Player 2')


# Set the game display

# Load the image's paths
files = sorted(
    map(os.path.basename, glob('img/none/*.png')),
    key=lambda s: s[-5]+s[-7]
)

# The images are splitted into paths
paths = np.array(['x', 'o', 'none'])

# Join all images into a list
values = [list(map(lambda s: 'img/'+paths[i]+'/'+s, files)) for i in range(3)]

if 'values' not in st.session_state:
    st.session_state['values'] = values[2]

clicked, move = utils.display_game(
    st.session_state['values'],
    player1, player2
    )


# Clicking logic
if clicked in range(9):
    s = st.session_state['values'][clicked]
    mark = s.split('/')[1]  # none | x | o
    idx = list(paths).index(mark)
    idx = move % 2 if idx == 2 else 2
    st.session_state['values'][clicked] = values[idx][clicked]
