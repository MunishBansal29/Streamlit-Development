from sys import maxsize
import streamlit as sl
import time
from streamlit_extras.switch_page_button import switch_page

sl.title("Hi ! This is my first Streamlit app !!")
sl.write("Happy Learning ! [Streamlit](https://streamlit.io/)")
sl.markdown("-----")

sl.video("https://www.youtube.com/watch?v=_b6nfGNcTdw&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=7")

sl.markdown("-----")

sl.text("Our application starts from here.....")

input = sl.text_input("Enter something:", max_chars=500)

sl.text_area("More details:")

sl.write(input)

myfile = sl.file_uploader("Upload your image file here", type=["jpg", "jpeg"]) #should not allow any other file type

if myfile is not None:
    sl.image(myfile) #display that image

#Date picker
dval = sl.date_input("Enter your DOB:") #default value is the current date
sl.write(dval)

bar = sl.progress(0) #Current/ initial value is set to 0 (integer values allowed)
for i in range(11):
    bar.progress(i*10) #Value can be taken from user and accordingly manipulate the progress
    time.sleep(1) #put some delay to see the progress


pageSelected = sl.selectbox("Select the page", ("About", "Products", "Summary"))

# if pageSelected == "About":
#     sl.about()
# elif pageSelected == "Products":
#     sl.products()
# elif pageSelected == "Products":
#     sl.summary()

