import streamlit as st

# Apply custom CSS to match the style of the "PCOS Personal Trainer" logo and make "Personal Trainer" a background element
st.markdown(
    """
    <style>
    /* Background gradient */
    .main {
        background: linear-gradient(90deg, rgba(255, 182, 193, 1), rgba(255, 255, 255, 1)); /* Baby pink to white gradient */
    }

    /* Container for center alignment */
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        height: 100vh;
    }

    /* Logo styling for 'PCOS' */
    .logo-title {
        font-family: Arial, sans-serif;
        font-size: 48px;
        font-weight: bold;
        color: #333; /* Dark gray for 'PCOS' text */
        display: flex;
        align-items: center;
        position: relative;
        z-index: 2;
    }
    
    /* Subtle background styling for 'Personal Trainer' */
    .logo-background {
        font-family: "Brush Script MT", cursive;
        font-size: 120px;
        font-weight: normal;
        color: #C71585; /* Tomato red color */
        opacity: 0.1; /* Make it subtle to appear like a background */
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        z-index: 1;
    }

    /* Style for 'the' */
    .logo-small-text {
        font-size: 18px;
        vertical-align: middle;
        color: #333;
        margin-right: 8px;
    }
    
    /* Circle icon style */
    .icon {
        background-color: #333;
        color: #FFFFFF;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin: 0 5px;
    }

    /* Subtitle styling for "PCOS Screening Questions" */
    .subtitle {
        font-family: Arial, sans-serif;
        font-size: 24px;
        font-weight: bold;
        color: #FF6347;
        margin-top: 20px;
    }

    /* Button styling */
    .stButton>button {
        width: 200px;
        height: 50px;
        font-size: 20px;
        background-color: #FF6347;
        color: #fff;
        border-radius: 5px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display content
st.markdown('<div class="centered">', unsafe_allow_html=True)

# Display the background "Personal Trainer" text
st.markdown(
    '<div class="logo-background">Personal Trainer</div>',
    unsafe_allow_html=True
)

# Display the main title with the icon
st.markdown(
    """
    <div class="logo-title">
        <span class="logo-small-text">the</span>
        PC<span class="icon">&#x1F527;</span>S
    </div>
    """,
    unsafe_allow_html=True
)

# Display the "PCOS Screening Questions" heading
st.markdown('<div class="subtitle">PCOS Screening Questions</div>', unsafe_allow_html=True)
st.markdown(
    """
    <a href="http://localhost:8502/app.py" target="_blank">
        <button style="
            width: 200px;
            height: 50px;
            font-size: 20px;
            background-color: #FF6347;
            color: #fff;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 20px;">
            Continue
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)


