import streamlit as st
import random

if "step" not in st.session_state:
    st.session_state.step = 0
if "names_ordered" not in st.session_state:
    st.session_state.names_ordered = []
if "secret_lock" not in st.session_state:
    st.session_state.secret_lock = False

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;700&display=swap');
    
    html, body, .stApp {
        margin: 0 !important;
        padding: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        overflow-x: hidden !important;
        background-color: rgb(33, 99, 173) !important;
    }
    
    div[data-testid="stMainBlockContainer"] {
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        min-height: 100vh !important;
        max-width: 100vw !important;
        padding: 20px !important;
        margin: 0 auto !important;
        box-sizing: border-box !important;
    }

    div[data-testid="stVerticalBlock"] {
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        gap: 8px !important;
    }
    
    div[data-testid="stVerticalBlock"] > div {
        position: relative !important;
        z-index: 20 !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
    }

    html, body, [class*="css"], .stMarkdown, p, div, h1, h2, h3, h4, h5, h6, span, label {
        font-family: 'Kanit', sans-serif !important;
        color: rgb(255, 255, 255) !important;
        text-align: center !important;
        text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.6) !important;
        margin: 0 auto !important;
    }

    h1 { font-size: 2.2rem !important; width: 100% !important; }
    h2 { font-size: 1.6rem !important; }
    p { font-size: 0.95rem !important; }

    div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: auto !important;
        max-width: max-content !important;
        margin: 10px auto !important;
    }
    
    div[data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 12px auto !important;
    }
    div[data-testid="stImage"] img {
        border-radius: 8px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
    }

    /* สไตล์ปุ่มลับแบบ "แถบข้างรูปโปสเตอร์ฝั่งขวา" ใสเคลียร์ 100% */
    .secret-marker { display: none; }
    
    div[data-testid="stElementContainer"]:has(.secret-marker) + div[data-testid="stElementContainer"] {
        position: absolute !important;
        width: 0 !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    div[data-testid="stElementContainer"]:has(.secret-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button {
        position: fixed !important;
        left: calc(50% + 110px) !important; /* เริ่มต้นจากขอบขวาของรูปโปสเตอร์พอดี */
        right: 0px !important;              /* ยาวไปจนสุดขอบจอขวา */
        top: 30vh !important;               /* คลุมพื้นที่แนวตั้งระดับสายตาตรงรูป */
        height: 35vh !important;            /* ความสูงของพื้นที่กดเป็นแถบใหญ่ */
        opacity: 0 !important;              /* ล่องหนสมบูรณ์แบบ 100% */
        z-index: 999999 !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        cursor: default !important;
    }
    
    /* ป้องกันไม่ให้มีเอฟเฟกต์แสงหรือขอบขึ้นตอนกด */
    div[data-testid="stElementContainer"]:has(.secret-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button:hover,
    div[data-testid="stElementContainer"]:has(.secret-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button:active,
    div[data-testid="stElementContainer"]:has(.secret-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button:focus {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        opacity: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

if st.session_state.step == 0 or st.session_state.step == 11:
    st.markdown("""
        <style>
        div[data-testid="stButton"] > button {
            background-color: rgb(47, 91, 141) !important;
            color: rgb(255, 255, 255) !important;
            border: none !important;
            font-family: 'Kanit', sans-serif !important;
            padding: 11px 36px !important;
            border-radius: 4px !important;
            font-size: 16px !important;
            width: auto !important;
            max-width: max-content !important;
            margin: 0 auto !important;
            box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.4) !important;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        div[data-testid="stButton"] > button {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: rgb(255, 255, 255) !important;
            border: 1px solid rgba(255, 255, 255, 0.4) !important;
            text-decoration: none !important;
            font-size: 13px !important;
            font-family: 'Kanit', sans-serif !important;
            box-shadow: none !important;
            padding: 5px 18px !important;
            border-radius: 4px !important;
            width: auto !important;
            max-width: max-content !important;
            margin: 12px auto 0 auto !important;
            transition: all 0.2s ease !important;
        }
        div[data-testid="stButton"] > button:hover {
            background-color: rgba(255, 255, 255, 0.25) !important;
            border-color: rgba(255, 255, 255, 0.7) !important;
            color: rgb(255, 255, 255) !important;
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
            width: 50% !important;
            background: repeating-linear-gradient(90deg, rgb(105, 12, 12), rgb(138, 18, 18) 15px, rgb(166, 30, 30) 30px, rgb(138, 18, 18) 45px, rgb(105, 12, 12) 60px);
            z-index: 99999 !important;
            animation: curtainClose 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
            box-shadow: inset 0 0 40px rgba(0, 0, 0, 0.4);
        }
        .left-p { left: 0 !important; transform-origin: left; }
        .right-p { right: 0 !important; transform-origin: right; }
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
            width: 50% !important;
            background: repeating-linear-gradient(90deg, rgb(105, 12, 12), rgb(138, 18, 18) 15px, rgb(166, 30, 30) 30px, rgb(138, 18, 18) 45px, rgb(105, 12, 12) 60px);
            z-index: 99999 !important;
            animation: curtainOpen 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
            box-shadow: inset 0 0 40px rgba(0, 0, 0, 0.4);
        }
        .left-p { left: 0 !important; transform-origin: left; }
        .right-p { right: 0 !important; transform-origin: right; }
        @keyframes curtainOpen {
            0% { transform: scaleX(1); }
            100% { transform: scaleX(0); }
        }
        </style>
        <div class="curtain-panel left-p"></div>
        <div class="curtain-panel right-p"></div>
    """, unsafe_allow_html=True)

if st.session_state.step == 0:
    st.markdown("<h1>Moana Opportunity</h1>", unsafe_allow_html=True)
    st.image("https://lumiere-a.akamaihd.net/v1/images/moa_canon_poster-4x5now_6eed187f.jpeg", width=210)
    
    st.markdown('<div class="secret-marker"></div>', unsafe_allow_html=True)
    if st.button("", key="invisible_poster_side_trigger"):
        st.session_state.secret_lock = not st.session_state.secret_lock

    st.markdown("<p>Click below to start the random selection.<br>Good luck!</p>", unsafe_allow_html=True)
    
    if st.button("Random"):
        all_names = ["Cat", "Fairway", "Ice", "Phu", "Plewai", "Primo", "Puma"]
        
        if st.session_state.secret_lock:
            fixed_pair = ["Cat", "Primo"]
            others = [p for p in all_names if p not in fixed_pair]
            random.shuffle(others)
            
            b = random.randint(1, 4)
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
                
            st.session_state.names_ordered = suite1 + suite2 + prime
        else:
            random.shuffle(all_names)
            suite1 = [all_names[0], all_names[1]]
            suite2 = [all_names[2], all_names[3]]
            prime = [all_names[4], all_names[5], all_names[6]]
            st.session_state.names_ordered = suite1 + suite2 + prime
            
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
    try:
        st.image("https://i.ibb.co/1Y5vNx9m/cinema-seats.png", width=315)
    except:
        pass
    st.markdown(f"<p>Suite Seat 1 (AA5 and AA6) : {st.session_state.names_ordered[0]} and {st.session_state.names_ordered[1]}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>Suite Seat 2 (AA7 and AA8) : {st.session_state.names_ordered[2]} and {st.session_state.names_ordered[3]}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>Prime Seat 1 (A7) : {st.session_state.names_ordered[4]}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>Prime Seat 2 (A8) : {st.session_state.names_ordered[5]}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>Prime Seat 3 (A9) : {st.session_state.names_ordered[6]}</p>", unsafe_allow_html=True)
    
    if st.button("Reset Selection"):
        st.session_state.step = 0
        st.session_state.names_ordered = []
        st.session_state.secret_lock = False
        st.rerun()