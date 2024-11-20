import streamlit as st
from PIL import Image


st.title('Calculator UI')
# Header
st.header("This is a header")
st.subheader("This is a subheader")
# Text
st.text("Hello this is text")

# Markdown
st.markdown("###### This is a markdown")
st.write('''Hello we are doing Streamlit UI 
         and Python coding but we are unable 
         to understand that what is going on..''')

st.code('conda create -n env_name Python==3.12')

img = Image.open("logo-removebg-preview.png")
st.image(img, width=200)

st.video("https://youtu.be/_OVnXw2ldog?si=2qsVAd3WdTUAlRVH")


