
#importing libraries
import streamlit as st
import qrcode
from PIL import Image
from matplotlib.pyplot import imshow
from matplotlib import colors as mcolors

#title 
st.title('*****QR Code Generator*****')


st.sidebar.header("About")
st.sidebar.subheader("What's a QRCode ?")
st.sidebar.info('A QR Code is a two-dimensional barcode that is readable by smartphones.It allows to encode over 4000 characters in a two dimensional barcode. QR Codes may be used to display text to the user, to open a URL, save a contact to the address book or to compose text messages.')

st.sidebar.subheader("What are the benefits of using QRCodes ?")
st.sidebar.info("They are gaining popularity because of their versatility. You can use them to gather feedback to improve your products or services, increase customer engagement with images or videos, or even promote your business via events and coupons. All of these can be done with just a single scan!")

st.sidebar.subheader("How Do I scan QR Codes ?")
st.sidebar.info("Depending on your device, you might already have a built-in QR Code reader or scanner. Open the camera app on your mobile phone and hold it over a Code for a few seconds until a notification pops up. ")

#image
img = Image.open('qrcode.jpg')
st.image(img , width=600)

st.header('Create your own QR Code')

# Add the data to QR
#data = st.text_input("Enter the data you want to embed")
#data_title = data.title()

status = st.radio('Enter the type-of Data you want to embed',('Free Text','URL','Phone','SMS'))

if status == 'Free Text':
    data = st.text_input("Enter the text here ")
    data_title = data.title()
elif status == 'URL':
    data = st.text_input("Enter the URL here ")
    data_title = data.title()
elif status == 'Phone':
    data = st.text_input("Enter the Phone number here ")
    data_title = data.title()
else:
    data = st.text_input("Enter the Phone number here ")
    data_title = data.title()
    data1 = st.text_input('Enter the Message here ')
    data_title = data1.title()    
    
    

# Number Inputs
box_size = st.number_input("Enter the box size")
border = st.number_input("Enter the border spacing value")

# Select Box Inputs
from matplotlib import colors as mcolors

colors = mcolors.CSS4_COLORS
colors_list = list(colors.keys())

fill = st.selectbox("Select the fill color", colors_list)
back = st.selectbox("Select the background color", colors_list)


# Create a QR Code

if(st.button("Generate QR Code")):
    qr = qrcode.QRCode(
        box_size=box_size,
        border=border
    )
    
    qr.add_data(data_title)
    qr.make()
    img = qr.make_image(fill_color = fill, back_color = back)
    img.save('myqr.png')
    
    
    # Display the QR Code
    img = Image.open('myqr.png')
    st.image(img)

