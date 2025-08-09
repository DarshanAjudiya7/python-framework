import streamlit as st

st.title("Currency Converter")

currency = st.selectbox(
    "Select the currency you want to convert from:",
    ("USD", "EURO", "AUD", "YEN", "POUND", "CAD", "CHIN_YUAN")
)

amount = st.number_input(f"Enter the amount in {currency}:", min_value=0, step=1)

usd = 87.58
euro = 101.84
aud = 56.18
yen = 0.62
pound = 117.52
cad =  63.60    
chin_yuan = 12.09

if st.button("Convert"):
    if currency == "USD":
        converted = amount * usd
        st.write(f"The converted {currency} amount in INR is: {converted:.2f}")
    elif currency == "EURO":
        converted = amount * euro
        st.write(f"The converted {currency} amount in INR is: {converted:.2f}")
    elif currency == "AUD":
        converted = amount * aud
        st.write(f"The converted {currency} amount in INR is : {converted:.2f}")
    elif currency == "YEN":
        converted = amount * yen
        st.write(f"The converted {currency} amount in INR is : {converted:.2f}")
    elif currency == "POUND":
        converted = amount * pound
        st.write(f"The converted {currency} amount in INR is : {converted:.2f}")
    elif currency == "CAD":
        converted = amount * cad
        st.write(f"The converted {currency} amount in INR is : {converted:.2f}")
    elif currency == "CHIN_YUAN":
        converted = amount * chin_yuan
        st.write(f"The converted {currency} amount in INR is : {converted:.2f}")


st.write("This app is created on 10-08-2025. Data is not updated daily.")

