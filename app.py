import streamlit as st 

def apply_custom_css():
    st.markdown(
        """
        <style>
            body {
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
            }
            .stTextInput, .stSelectbox, .stButton {
                border-radius: 10px;
                padding: 10px;
            }
            .stButton button {
                background-color: #007BFF;
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
                border: none;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {"meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084, "inches": 39.3701, "centimeters": 100},
        "Weight": {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274, "stones": 0.000157473, "milligrams": 1000},
        "Temperature": {"celsius": (lambda c: c, lambda f: f), "fahrenheit": (lambda c: c * 9/5 + 32, lambda f: (f - 32) * 5/9)},
        "Volume": {"liters": 1, "milliliters": 1000, "gallons": 0.264172, "cups": 4.22675},
        "Speed": {"meters per second": 1, "kilometers per hour": 3.6, "miles per hour": 2.23694, "feet per second": 3.28084}
    }
    
    formulas = {
        "Temperature": {"celsius to fahrenheit": "(C × 9/5) + 32", "fahrenheit to celsius": "(F - 32) × 5/9"}
    }
    
    if category == "Temperature":
        convert_func = conversion_factors[category]
        if from_unit == "celsius" and to_unit == "fahrenheit":
            formula = formulas[category]["celsius to fahrenheit"]
            return convert_func[from_unit][0](value), formula
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            formula = formulas[category]["fahrenheit to celsius"]
            return convert_func[to_unit][1](value), formula
        return value, "N/A"
    else:
        formula = f"{value} × {conversion_factors[category][to_unit]} / {conversion_factors[category][from_unit]}"
        return value * conversion_factors[category][to_unit] / conversion_factors[category][from_unit], formula

st.title("Unit Converter")
apply_custom_css()

category = st.selectbox("Select a category", ["Length", "Weight", "Temperature", "Volume", "Speed"])

units = {
    "Length": ["meters", "kilometers", "miles", "feet", "inches", "centimeters"],
    "Weight": ["grams", "kilograms", "pounds", "ounces", "stones", "milligrams"],
    "Temperature": ["celsius", "fahrenheit"],
    "Volume": ["liters", "milliliters", "gallons", "cups"],
    "Speed": ["meters per second", "kilometers per hour", "miles per hour", "feet per second"]
}

from_unit = st.selectbox("From Unit", units[category])
to_unit = st.selectbox("To Unit", units[category])
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result, formula = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    st.info(f"Formula used: {formula}")

