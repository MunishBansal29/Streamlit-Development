from queue import Empty
import streamlit as sl

with open("style.css") as f:
    sl.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


sl.title("Aao bacchaa....pucho apne guru se !")
sl.image("Images/Guru1.png")
text = sl.text_input("Enter your query:")

if len(text) > 0:
    sl.image("Images/Guru2.jpeg",  width=300)

