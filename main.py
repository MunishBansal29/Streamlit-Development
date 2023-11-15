import streamlit as sl

sl.title("Hi ! This is my first Streamlit app !!")
sl.markdown("-----")

sl.video("https://www.youtube.com/watch?v=_b6nfGNcTdw&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=7")

sl.markdown("-----")

sl.text("Our application starts from here.....")

input = sl.text_input("Enter something:")

sl.write(input)

