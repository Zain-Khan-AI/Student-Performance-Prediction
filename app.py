import streamlit as st
import numpy as np
import pickle

# Page config
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📊",
    layout="centered"
)

# Load model
model = pickle.load(open("student_performance_model.pkl", "rb"))

# Custom CSS for Background Gradient & Premium Glow Button
st.html("""
    <style>
    /* Main Background Gradient */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #111827 100%) !important;
        color: white;
    }
    
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    
    /* Dynamic Premium Glowing Button */
    div.stButton > button {
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 18px !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        padding: 14px 28px !important;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100% !important;
        height: auto !important;
    }
    
    /* Button Hover Effect */
    div.stButton > button:hover {
        background: linear-gradient(135deg, #66BB6A 0%, #388E3C 100%) !important;
        box-shadow: 0 6px 20px rgba(76, 175, 80, 0.5) !important;
        transform: translateY(-2px);
    }
    
    /* Button Click Effect */
    div.stButton > button:active {
        transform: translateY(1px);
        box-shadow: 0 3px 10px rgba(76, 175, 80, 0.2) !important;
    }

    /* Input Boxes & Sliders Custom Styling */
    .stNumberInput, .stSelectbox, div[data-testid="stSlider"] {
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.03);
        padding: 10px;
        border-radius: 12px;
    }
    
    /* Labels Readability */
    h1, h2, h3, p, label, span, .stMarkdown {
        color: #ffffff !important;
    }
    </style>
""")

# Title Section
st.title("📊 Student Performance Predictor")
st.write("Predict Student Academic performance using Machine Learning Multiple Linear Regression Model")

st.markdown("---")

# Layout (2 columns)
col1, col2 = st.columns(2)

with col1:
    hours_studied = st.slider("📘 Hours Studied", 0, 12, 5)
    previous_scores = st.slider("📈 Previous Scores", 0, 100, 50)
    sleep_hours = st.slider("😴 Sleep Hours", 0, 12, 6)

with col2:
    extracurricular = st.selectbox("🎯 Extracurricular Activities", ["No", "Yes"])
    sample_papers = st.slider("📝 Sample Papers Practiced", 0, 10, 3)

# Convert categorical
extra = 1 if extracurricular == "Yes" else 0

st.markdown("---")

# Predict button trigger
# Predict button trigger
if st.button("🚀 Predict Performance"):
    features = np.array([[hours_studied, previous_scores, extra, sleep_hours, sample_papers]])
    prediction = model.predict(features)
    
    # Extracting prediction values safely using index
    pred_val = float(prediction[0])

    # Premium Analytical Glassy Card for output using st.html
    st.html(f"""
        <div style="
            background: linear-gradient(135deg, rgba(76, 175, 80, 0.15) 0%, rgba(27, 94, 32, 0.25) 100%);
            padding: 25px; 
            border-radius: 12px; 
            border: 1px solid rgba(76, 175, 80, 0.3); 
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            margin-top: 20px;
            margin-bottom: 15px;
            text-align: center;
        ">
            <span style="color: #81C784; font-size: 14px; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 600;">Prediction Result</span>
            <h2 style="color: #ffffff; margin: 10px 0; font-size: 32px; font-weight: 700;">🎯 {pred_val:.2f}</h2>
            <p style="color: rgba(255, 255, 255, 0.7); font-size: 14px; margin: 0;">Predicted Student Performance Index</p>
        </div>
    """)

    # Crash-proof Logic: value ko 0 aur 100 ke beech lock kar diya gaya hai
    if pred_val < 0:
        progress_val = 0
    elif pred_val > 100:
        progress_val = 100
    else:
        progress_val = int(pred_val)

    # Extra visual feedback (Progress Bar) - Ab yeh crash nahi hoga
    st.progress(progress_val)


# Footer Divider
st.markdown("---")

# Professional Flex Contact Grid Footer using st.html to block source leak
st.html("""
<div style="
    background: rgba(255, 255, 255, 0.04); 
    padding: 20px; 
    border-radius: 16px; 
    border: 1px solid rgba(255, 255, 255, 0.08); 
    backdrop-filter: blur(12px);
    text-align: center;
">
    <h3 style="color: white !important; margin-bottom: 18px; font-weight: 600; font-size: 16px; letter-spacing: 0.5px;">👨‍💻 Connect With Me</h3>
    <div style="
        display: flex; 
        justify-content: center; 
        gap: 12px; 
        flex-wrap: wrap;
    ">
        <a href="https://linkedin.com" target="_blank" style="
            background-color: #0077B5; 
            color: white !important; 
            padding: 10px 20px; 
            border-radius: 8px; 
            text-decoration: none; 
            font-weight: 600; 
            font-size: 13px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.15);
        ">🔗 LinkedIn</a>
        
        <a href="https://github.com" target="_blank" style="
            background-color: #24292e; 
            color: white !important; 
            padding: 10px 20px; 
            border-radius: 8px; 
            text-decoration: none; 
            font-weight: 600; 
            font-size: 13px;
            border: 1px solid rgba(255,255,255,0.15);
            box-shadow: 0 4px 6px rgba(0,0,0,0.15);
        ">💻 GitHub</a>
        
        <a href="mailto:m.zainkhan311@gmail.com" style="
            background-color: #EA4335; 
            color: white !important; 
            padding: 10px 20px; 
            border-radius: 8px; 
            text-decoration: none; 
            font-weight: 600; 
            font-size: 13px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.15);
        ">📧 Email</a>
    </div>
    
    <div style="text-align: center; color: rgba(255, 255, 255, 0.4) !important; font-size: 12px; margin-top: 18px; border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 12px;">
        Generated by <a href="https://linkedin.com" target="_blank" style="color: #4CAF50 !important; text-decoration: none; font-weight: 500;">Zain Khan</a>
    </div>
</div>
""")

# ==========================================
# ANIMATED BACKGROUND WATERMARK (ZAIN KHAN)
# ==========================================
# ==========================================
# SINGLE ANIMATED BACKGROUND WATERMARK
# ==========================================
# ==========================================
# FULL SCREEN FOUR-CORNER MOVING WATERMARK
# ==========================================
st.html("""
<div class="watermark-container">
    <div class="floating-watermark">M.Zain Khan</div>
</div>

<style>
/* Watermark Container Layer */
.watermark-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 0; 
    pointer-events: none; /* Is par click nahi ho sakega */
    overflow: hidden;
}

/* Single Floating Text */
.floating-watermark {
    position: absolute;
    font-size: clamp(45px, 6vw, 85px);
    font-weight: 900;
    color: rgba(255, 255, 255, 0.035); /* Soft premium visibility */
    font-family: 'Segoe UI', sans-serif;
    white-space: nowrap;
    letter-spacing: 2px;
    animation: cornerToCorner 28s ease-in-out infinite alternate;
}

/* Chaaron Taraf Ghoomne Ki Full Animation Grid */
@keyframes cornerToCorner {
    0% {
        /* Top-Left Corner */
        top: 5%;
        left: 5%;
        transform: rotate(-12deg);
    }
    20% {
        /* Top-Right Corner */
        top: 5%;
        left: 65%;
        transform: rotate(10deg);
    }
    40% {
        /* Bottom-Right Corner */
        top: 80%;
        left: 65%;
        transform: rotate(-8deg);
    }
    60% {
        /* Bottom-Left Corner */
        top: 80%;
        left: 5%;
        transform: rotate(12deg);
    }
    80% {
        /* Center Area Display */
        top: 45%;
        left: 35%;
        transform: rotate(-5deg);
    }
    100% {
        /* Back to Start Angle smoothly */
        top: 10%;
        left: 10%;
        transform: rotate(8deg);
    }
}

/* Main Dashboard Elements Wrapper */
[data-testid="stAppViewContainer"] {
    position: relative;
    z-index: 1 !important;
}
</style>
""")

