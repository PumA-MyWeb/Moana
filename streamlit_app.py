import streamlit as st
import random

if "step" not in st.session_state:
    st.session_state.step = 0
if "names_ordered" not in st.session_state:
    st.session_state.names_ordered = []

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;700&display=swap');
    
    .stApp {
        background-color: #2163ad !important;
    }
    html, body, [class*="css"], .stMarkdown, p, div, h1, h2, h3, h4, h5, h6, span, label {
        font-family: 'Kanit', sans-serif !important;
        color: #ffffff !important;
        text-align: center !important;
        text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.6) !important;
    }
    
    div[data-testid="stVerticalBlock"] > div {
        position: relative !important;
        z-index: 20 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }

    div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin: 20px auto !important;
    }
    div[data-testid="stButton"] > button {
        margin: 0 auto !important;
        display: block !important;
    }
    </style>
""", unsafe_allow_html=True)

if st.session_state.step == 0:
    st.markdown("""
        <style>
        div[data-testid="stButton"] > button {
            background-color: #2f5b8d !important;
            color: white !important;
            border: none !important;
            font-family: 'Kanit', sans-serif !important;
            padding: 12px 40px !important;
            border-radius: 4px !important;
            font-size: 18px !important;
            margin: 0 auto !important;
            box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.4) !important;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        div[data-testid="stButton"] > button {
            background-color: transparent !important;
            color: white !important;
            border: none !important;
            text-decoration: underline !important;
            font-size: 14px !important;
            font-family: 'Kanit', sans-serif !important;
            box-shadow: none !important;
            padding: 0 !important;
            margin: 15px auto 0 auto !important;
        }
        div[data-testid="stButton"] > button:hover {
            background-color: transparent !important;
            color: #d0d0d0 !important;
            text-decoration: underline !important;
        }
        </style>
    """, unsafe_allow_html=True)

if st.session_state.step > 0 and st.session_state.step < 11:
    st.markdown("""
        <style>
        .curtain-panel {
            position: fixed;
            top: 0;
            height: 100vh;
            width: 50vw;
            background: repeating-linear-gradient(90deg, #500000, #7a0000 15px, #990000 30px, #7a0000 45px, #500000 60px);
            z-index: 10 !important;
            animation: curtainClose 1s forwards;
            box-shadow: inset 0 0 60px rgba(0, 0, 0, 0.7);
        }
        .left-p { left: 0; transform-origin: left; }
        .right-p { right: 0; transform-origin: right; }
        @keyframes curtainClose {
            0% { transform: scaleX(0); }
            100% { transform: scaleX(1); }
        }
        </style>
        <div class="curtain-panel left-p"></div>
        <div class="curtain-panel right-p"></div>
    """, unsafe_allow_html=True)
elif st.session_state.step == 11:
    st.markdown("""
        <style>
        .curtain-panel {
            position: fixed;
            top: 0;
            height: 100vh;
            width: 50vw;
            background: repeating-linear-gradient(90deg, #500000, #7a0000 15px, #990000 30px, #7a0000 45px, #500000 60px);
            z-index: 10 !important;
            animation: curtainOpen 1.2s forwards;
            box-shadow: inset 0 0 60px rgba(0, 0, 0, 0.7);
        }
        .left-p { left: 0; transform-origin: left; }
        .right-p { right: 0; transform-origin: right; }
        @keyframes curtainOpen {
            0% { transform: scaleX(1); }
            100% { transform: scaleX(0); }
        }
        </style>
        <div class="curtain-panel left-p"></div>
        <div class="curtain-panel right-p"></div>
    """, unsafe_allow_html=True)

if st.session_state.step == 0:
    st.markdown("<h1>Moana Opportunity 101</h1>", unsafe_allow_html=True)
    st.markdown("<p>Click below to start the random selection. Good luck!</p>", unsafe_allow_html=True)
    
    if st.button("Random"):
        a = ["Cat", "Fairway", "Ice", "Phu", "Plewai", "Primo", "Puma"]
        b = random.randint(1, 4)
        fixed_pair = ["Cat", "Primo"]
        others = [p for p in a if p not in fixed_pair]
        random.shuffle(others)
        
        if b == 1:
            suite1 = fixed_pair.copy()
            random.shuffle(suite1)
            suite2 = [others.pop(), others.pop()]
            prime = others.copy()
        elif b == 2:
            suite2 = fixed_pair.copy()
            random.shuffle(suite2)
            suite1 = [others.pop(), others.pop()]
            prime = others.copy()
        elif b == 3:
            suite1 = [others.pop(), others.pop()]
            suite2 = [others.pop(), others.pop()]
            p_pair = fixed_pair.copy()
            random.shuffle(p_pair)
            prime = [p_pair[0], p_pair[1], others.pop()]
        elif b == 4:
            suite1 = [others.pop(), others.pop()]
            suite2 = [others.pop(), others.pop()]
            p_pair = fixed_pair.copy()
            random.shuffle(p_pair)
            prime = [others.pop(), p_pair[0], p_pair[1]]
            
        st.session_state.names_ordered = [suite1[0], suite1[1], suite2[0], suite2[1], prime[0], prime[1], prime[2]]
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    st.markdown("<h2>The people who will sit on Suite Seat 1 are</h2>", unsafe_allow_html=True)
    if st.button("Next", key="n1"):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.markdown(f"<h2>{st.session_state.names_ordered[0]} and</h2>", unsafe_allow_html=True)
    if st.button("Next", key="n2"):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.markdown(f"<h2>{st.session_state.names_ordered[1]}</h2>", unsafe_allow_html=True)
    if st.button("Next", key="n3"):
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.markdown("<h2>The people who will sit on Suite Seat 2 are</h2>", unsafe_allow_html=True)
    if st.button("Next", key="n4"):
        st.session_state.step = 5
        st.rerun()

elif st.session_state.step == 5:
    st.markdown(f"<h2>{st.session_state.names_ordered[2]} and</h2>", unsafe_allow_html=True)
    if st.button("Next", key="n5"):
        st.session_state.step = 6
        st.rerun()

elif st.session_state.step == 6:
    st.markdown(f"<h2>{st.session_state.names_ordered[3]}</h2>", unsafe_allow_html=True)
    if st.button("Next", key="n6"):
        st.session_state.step = 7
        st.rerun()

elif st.session_state.step == 7:
    st.markdown("<h2>Next, these are the people who will sit on Prime Seat</h2>", unsafe_allow_html=True)
    if st.button("Next", key="n7"):
        st.session_state.step = 8
        st.rerun()

elif st.session_state.step == 8:
    st.markdown(f"<h2>1. {st.session_state.names_ordered[4]}</h2>", unsafe_allow_html=True)
    if st.button("Next", key="n8"):
        st.session_state.step = 9
        st.rerun()

elif st.session_state.step == 9:
    st.markdown(f"<h2>2. {st.session_state.names_ordered[5]}</h2>", unsafe_allow_html=True)
    if st.button("Next", key="n9"):
        st.session_state.step = 10
        st.rerun()

elif st.session_state.step == 10:
    st.markdown(f"<h2>3. {st.session_state.names_ordered[6]}</h2>", unsafe_allow_html=True)
    if st.button("Next", key="n10"):
        st.session_state.step = 11
        st.rerun()

elif st.session_state.step == 11:
    st.markdown("<h2>Summary of Seating Arrangements</h2>", unsafe_allow_html=True)
    st.markdown(f"<p>Suite Seat 1 (AA5 and AA6) : {st.session_state.names_ordered[0]} and {st.session_state.names_ordered[1]}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>Suite Seat 2 (AA7 and AA8) : {st.session_state.names_ordered[2]} and {st.session_state.names_ordered[3]}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>Prime Seat 1 (A7) : {st.session_state.names_ordered[4]}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>Prime Seat 2 (A8) : {st.session_state.names_ordered[5]}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>Prime Seat 3 (A9) : {st.session_state.names_ordered[6]}</p>", unsafe_allow_html=True)
    
    if st.button("Reset Selection"):
        st.session_state.step = 0
        st.session_state.names_ordered = []
        st.rerun()