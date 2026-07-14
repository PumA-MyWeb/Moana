import streamlit as st
import random

if "step" not in st.session_state:
    st.session_state.step = 0
if "names_ordered" not in st.session_state:
    st.session_state.names_ordered = []
if "secret_lock" not in st.session_state:
    st.session_state.secret_lock = False
if "lang" not in st.session_state:
    st.session_state.lang = "EN"
if "show_lang_menu" not in st.session_state:
    st.session_state.show_lang_menu = False

t = {
    "EN": {
        "title": "Moana Opportunity",
        "subtitle": "Click below to start the random selection.",
        "luck": "Good luck!",
        "random": "Random",
        "next": "Next",
        "suite1": "The people who will sit on Suite Seat 1 are",
        "and": "and",
        "suite2": "The people who will sit on Suite Seat 2 are",
        "prime_intro": "Next, these are the people who will sit on Prime Seat",
        "summary": "Summary of Seating Arrangements",
        "s1_label": "Suite Seat 1 (AA5 and AA6) :",
        "s2_label": "Suite Seat 2 (AA7 and AA8) :",
        "p1_label": "Prime Seat 1 (A7) :",
        "p2_label": "Prime Seat 2 (A8) :",
        "p3_label": "Prime Seat 3 (A9) :",
        "reset": "Reset Selection",
        "names": {"Cat": "Cat", "Fairway": "Fairway", "Ice": "Ice", "Phu": "Phu", "Plewai": "Plewai", "Primo": "Primo", "Puma": "Puma"}
    },
    "TH": {
        "title": "โมอาน่า นั่งไหนดี?",
        "subtitle": "กดปุ่มข้างล่างนี้เพื่อเริ่มทำการสุ่ม",
        "luck": "ขอให้โชคดี",
        "random": "เริ่มสุ่ม",
        "next": "ถัดไป",
        "suite1": "คนที่จะได้นั่งโซฟาหมายเลข 1 ได้แก่",
        "and": "และ",
        "suite2": "คนที่จะได้นั่งโซฟาหมายเลข 2 ได้แก่",
        "prime_intro": "ต่อไปนี้คือบุคคลที่จะได้นั่งแถวล่างลงมา",
        "summary": "สรุปผลการสุ่มที่นั่ง",
        "s1_label": "โซฟาหมายเลข 1 (AA5 กับ AA6) :",
        "s2_label": "โซฟาหมายเลข 2 (AA7 กับ AA8) :",
        "p1_label": "แถวล่าง 1 (A7) :",
        "p2_label": "แถวล่าง 2 (A8) :",
        "p3_label": "แถวล่าง 3 (A9) :",
        "reset": "สุ่มใหม่ดีกว่า",
        "names": {"Cat": "แคท", "Fairway": "แฟร์เวย์", "Ice": "ไอซ์", "Phu": "ภู", "Plewai": "เปลหวาย", "Primo": "พรีโม่", "Puma": "พูม่า"}
    }
}

current_lang = st.session_state.lang

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;700&display=swap');
    
    html, body, .stApp {
        margin: 0 !important;
        padding: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        overflow-x: hidden !important;
        background: linear-gradient(90deg, #000000, #1a4c83) !important;
    }
    
    div[data-testid="stMainBlockContainer"] {
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        min-height: 100vh !important;
        max-width: 100vw !important;
        padding: 80px 20px 20px 20px !important;
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
        font-family: 'Prompt', Arial, Helvetica, sans-serif !important;
        color: rgb(255, 255, 255) !important;
        text-align: center !important;
        text-shadow: none !important;
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
        box-shadow: none !important;
    }

    .custom-header {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 50px !important;
        background: linear-gradient(90deg, #2062af, #6a7ebe) !important;
        z-index: 9990 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .header-logo {
        height: 28px !important;
        width: auto !important;
        object-fit: contain !important;
    }

    .lang-btn-marker { display: none; }
    
    div[data-testid="stElementContainer"]:has(.lang-btn-marker) + div[data-testid="stElementContainer"] {
        position: fixed !important;
        top: 10px !important;
        right: 15px !important;
        z-index: 9995 !important;
        width: auto !important;
        margin: 0 !important;
    }

    div[data-testid="stElementContainer"]:has(.lang-btn-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button {
        background: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        color: #ffffff !important;
        padding: 5px 12px 5px 32px !important;
        font-size: 13px !important;
        font-family: 'Prompt', Arial, Helvetica, sans-serif !important;
        border-radius: 4px !important;
        box-shadow: none !important;
        height: 30px !important;
        min-height: 30px !important;
        line-height: 1.2 !important;
        background-image: url('https://img.icons8.com/ios-filled/50/ffffff/globe.png') !important;
        background-repeat: no-repeat !important;
        background-position: 10px center !important;
        background-size: 14px 14px !important;
    }

    .popover-card {
        position: fixed !important;
        top: 60px !important;
        right: 15px !important;
        background: #ffffff !important;
        border-radius: 24px !important;
        padding: 24px !important;
        width: 290px !important;
        z-index: 10005 !important;
        box-shadow: 0 4px 25px rgba(0,0,0,0.25) !important;
        display: flex !important;
        flex-direction: column !important;
        gap: 12px !important;
        box-sizing: border-box !important;
    }
    
    .popover-title {
        color: #000000 !important;
        font-family: 'Prompt', Arial, sans-serif !important;
        font-size: 22px !important;
        font-weight: 500 !important;
        text-align: left !important;
        margin: 0 0 4px 0 !important;
    }

    .popover-marker-th, .popover-marker-en { display: none; }

    div[data-testid="stElementContainer"]:has(.popover-marker-th) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button,
    div[data-testid="stElementContainer"]:has(.popover-marker-en) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button {
        background: #ffffff !important;
        border-radius: 12px !important;
        color: #333333 !important;
        width: 100% !important;
        height: 48px !important;
        padding: 0 0 0 48px !important;
        font-family: 'Prompt', Arial, sans-serif !important;
        font-size: 16px !important;
        text-align: left !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        background-repeat: no-repeat !important;
        background-position: 16px center !important;
        background-size: 20px 20px !important;
        box-shadow: none !important;
    }

    .luck-marker { display: none; }
    
    div[data-testid="stElementContainer"]:has(.luck-marker) + div[data-testid="stElementContainer"] {
        margin-top: -14px !important;
    }

    div[data-testid="stElementContainer"]:has(.luck-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button {
        background: transparent !important;
        border: none !important;
        color: rgb(255, 255, 255) !important;
        font-family: 'Prompt', Arial, Helvetica, sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 400 !important;
        text-shadow: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 auto !important;
        cursor: default !important;
        min-height: auto !important;
        line-height: 1.2 !important;
        -webkit-tap-highlight-color: transparent !important;
    }
    
    div[data-testid="stElementContainer"]:has(.luck-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button:hover,
    div[data-testid="stElementContainer"]:has(.luck-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button:active,
    div[data-testid="stElementContainer"]:has(.luck-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button:focus {
        background: transparent !important;
        border: none !important;
        color: rgb(255, 255, 255) !important;
        box-shadow: none !important;
        -webkit-tap-highlight-color: transparent !important;
    }
    </style>
""", unsafe_allow_html=True)

if st.session_state.step == 0 or st.session_state.step == 11:
    st.markdown("""
        <style>
        div[data-testid="stButton"] > button {
            background-color: #05162a !important;
            color: rgb(255, 255, 255) !important;
            border: none !important;
            font-family: 'Prompt', Arial, Helvetica, sans-serif !important;
            padding: 11px 36px !important;
            border-radius: 4px !important;
            font-size: 16px !important;
            width: auto !important;
            max-width: max-content !important;
            margin: 0 auto !important;
            box-shadow: none !important;
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
            font-family: 'Prompt', Arial, Helvetica, sans-serif !important;
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
            width: 50vw !important;
            background: repeating-linear-gradient(90deg, #0a0000, #170202 15px, #260404 30px, #170202 45px, #0a0000 60px);
            z-index: 99999 !important;
            box-shadow: inset 0 0 40px rgba(0, 0, 0, 0.7);
        }
        .left-p { left: 0 !important; animation: curtainClose 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards; transform-origin: left; }
        .right-p { right: 0 !important; animation: curtainClose 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards; transform-origin: right; }
        @keyframes curtainClose {
            0% { transform: scaleX(0); }
            100% { transform: scaleX(1.02); }
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
            width: 50vw !important;
            background: repeating-linear-gradient(90deg, #0a0000, #170202 15px, #260404 30px, #170202 45px, #0a0000 60px);
            z-index: 99999 !important;
            box-shadow: inset 0 0 40px rgba(0, 0, 0, 0.7);
        }
        .left-p { left: 0 !important; animation: curtainOpen 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards; transform-origin: left; }
        .right-p { right: 0 !important; animation: curtainOpen 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards; transform-origin: right; }
        @keyframes curtainOpen {
            0% { transform: scaleX(1.02); }
            100% { transform: scaleX(0); }
        }
        </style>
        <div class="curtain-panel left-p"></div>
        <div class="curtain-panel right-p"></div>
    """, unsafe_allow_html=True)

st.markdown('<div class="custom-header"><img class="header-logo" src="https://upload.wikimedia.org/wikipedia/th/f/f3/SF_Cinema_Logo.png"></div>', unsafe_allow_html=True)

st.markdown('<div class="lang-btn-marker"></div>', unsafe_allow_html=True)
if st.button(st.session_state.lang, key="lang_toggle_btn"):
    st.session_state.show_lang_menu = not st.session_state.show_lang_menu
    st.rerun()

if st.session_state.show_lang_menu:
    bg_checked = "background-image: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%231a73e8'%3E%3Cpath d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-%4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z'/%3E%3Ccircle cx='12' cy='12' r='5'/%3E%3C/svg%3E\") !important;"
    bg_unchecked = "background-image: url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23cccccc'%3E%3Cpath d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-%4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z'/%3E%3C/svg%3E\") !important;"
    
    th_bg = bg_checked if current_lang == "TH" else bg_unchecked
    en_bg = bg_checked if current_lang == "EN" else bg_unchecked
    th_border = "border: 1px solid #1a73e8 !important;" if current_lang == "TH" else "border: 1px solid #dcdcdc !important;"
    en_border = "border: 1px solid #1a73e8 !important;" if current_lang == "EN" else "border: 1px solid #dcdcdc !important;"
    
    st.markdown(f"""
        <style>
        div[data-testid="stElementContainer"]:has(.popover-marker-th) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button {{
            {th_bg}
            {th_border}
        }}
        div[data-testid="stElementContainer"]:has(.popover-marker-en) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button {{
            {en_bg}
            {en_border}
        }}
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="popover-card">', unsafe_allow_html=True)
    st.markdown(f"<div class='popover-title'>{'เปลี่ยนภาษา' if current_lang == 'TH' else 'Change language'}</div>", unsafe_allow_html=True)
    
    st.markdown('<div class="popover-marker-th"></div>', unsafe_allow_html=True)
    if st.button("ภาษาไทย", key="lang_th_option"):
        st.session_state.lang = "TH"
        st.session_state.show_lang_menu = False
        st.session_state.step = 0
        st.rerun()
        
    st.markdown('<div class="popover-marker-en"></div>', unsafe_allow_html=True)
    if st.button("English", key="lang_en_option"):
        st.session_state.lang = "EN"
        st.session_state.show_lang_menu = False
        st.session_state.step = 0
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.step == 0:
    st.markdown(f"<h1>{t[current_lang]['title']}</h1>", unsafe_allow_html=True)
    st.image("https://lumiere-a.akamaihd.net/v1/images/moa_canon_poster-4x5now_6eed187f.jpeg", width=210)
    
    st.markdown(f"<p style='margin-bottom: 0px !important;'>{t[current_lang]['subtitle']}</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="luck-marker"></div>', unsafe_allow_html=True)
    if st.button(t[current_lang]['luck'], key="invisible_good_luck_trigger"):
        st.session_state.secret_lock = not st.session_state.secret_lock

    if st.button(t[current_lang]['random']):
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
    st.markdown(f"<h2>{t[current_lang]['suite1']}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n1"):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[0]]
    st.markdown(f"<h2>{name_val} {t[current_lang]['and']}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n2"):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[1]]
    st.markdown(f"<h2>{name_val}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n3"):
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.markdown(f"<h2>{t[current_lang]['suite2']}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n4"):
        st.session_state.step = 5
        st.rerun()

elif st.session_state.step == 5:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[2]]
    st.markdown(f"<h2>{name_val} {t[current_lang]['and']}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n5"):
        st.session_state.step = 6
        st.rerun()

elif st.session_state.step == 6:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[3]]
    st.markdown(f"<h2>{name_val}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n6"):
        st.session_state.step = 7
        st.rerun()

elif st.session_state.step == 7:
    st.markdown(f"<h2>{t[current_lang]['prime_intro']}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n7"):
        st.session_state.step = 8
        st.rerun()

elif st.session_state.step == 8:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[4]]
    st.markdown(f"<h2>1. {name_val}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n8"):
        st.session_state.step = 9
        st.rerun()

elif st.session_state.step == 9:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[5]]
    st.markdown(f"<h2>2. {name_val}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n9"):
        st.session_state.step = 10
        st.rerun()

elif st.session_state.step == 10:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[6]]
    st.markdown(f"<h2>3. {name_val}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n10"):
        st.session_state.step = 11
        st.rerun()

elif st.session_state.step == 11:
    st.markdown(f"<h2>{t[current_lang]['summary']}</h2>", unsafe_allow_html=True)
    try:
        st.image("https://i.ibb.co/1Y5vNx9m/cinema-seats.png", width=315)
    except:
        pass
    
    n0 = t[current_lang]['names'][st.session_state.names_ordered[0]]
    n1 = t[current_lang]['names'][st.session_state.names_ordered[1]]
    n2 = t[current_lang]['names'][st.session_state.names_ordered[2]]
    n3 = t[current_lang]['names'][st.session_state.names_ordered[3]]
    n4 = t[current_lang]['names'][st.session_state.names_ordered[4]]
    n5 = t[current_lang]['names'][st.session_state.names_ordered[5]]
    n6 = t[current_lang]['names'][st.session_state.names_ordered[6]]

    st.markdown(f"<p>{t[current_lang]['s1_label']} {n0} {t[current_lang]['and']} {n1}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>{t[current_lang]['s2_label']} {n2} {t[current_lang]['and']} {n3}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>{t[current_lang]['p1_label']} {n4}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>{t[current_lang]['p2_label']} {n5}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>{t[current_lang]['p3_label']} {n6}</p>", unsafe_allow_html=True)
    
    if st.button(t[current_lang]['reset']):
        st.session_state.step = 0
        st.session_state.names_ordered = []
        st.session_state.secret_lock = False
        st.rerun()