import streamlit as st
import joblib

# -----------------------------
# Page Design
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #4facfe, #00f2fe);
}

h1 {
    color: navy;
    text-align: center;
}

div.stButton > button {
    background-color: #007BFF;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #0056b3;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load('insurance_model.pkl')

# -----------------------------
# Title
# -----------------------------
st.title('Insurance Premium Prediction')

st.write('Enter Customer Details')

# -----------------------------
# User Inputs
# -----------------------------
age = st.number_input('Age', 18, 100, 30)
sex = st.selectbox('Sex', [0, 1])
bmi = st.number_input('BMI', 10.0, 60.0, 25.0)
children = st.number_input('Children', 0, 10, 0)
smoker = st.selectbox('Smoker', [0, 1])
region = st.selectbox('Region', [0, 1, 2, 3])

# -----------------------------
# Prediction
# -----------------------------
if st.button('Predict Insurance Charges'):

    x = [[
        age,
        sex,
        bmi,
        children,
        smoker,
        region
    ]]

    prediction = model.predict(x)

    st.markdown(f"""
    <div style="
        background-color:#0B5ED7;
        padding:20px;
        border-radius:12px;
        text-align:center;
        color:white;
        font-size:28px;
        font-weight:bold;">
        💰 Predicted Insurance Charges <br><br>
        ₹ {prediction[0]:,.2f}
    </div>
    """, unsafe_allow_html=True)

st.markdown('---')
st.caption('Developed using Streamlit')