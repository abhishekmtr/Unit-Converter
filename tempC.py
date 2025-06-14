import streamlit as st

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert input to Celsius
    if from_unit == "Fahrenheit":
        value = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        value = value - 273.15

    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        return (value * 9 / 5) + 32
    elif to_unit == "Kelvin":
        return value + 273.15
    return value

st.set_page_config(page_title="Temperature Converter", layout="centered")

st.title("🌡️ Temperature Converter")

value = st.number_input("Enter Temperature", value=0.0)
from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

if st.button("Convert"):
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {round(result, 2)} {to_unit}")
