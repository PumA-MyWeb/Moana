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

NAMES_TH = {
    "Cat": "แคท",
    "Fairway": "แฟร์เวย์",
    "Ice": "ไอซ์",
    "Phu": "ภู",
    "Plewai": "เปลหวาย",
    "Primo": "พรีโม่",
    "Puma": "พูม่า",
}

TEXT = {
    "EN": {
        "title": "Moana Opportunity",
        "start_instruction": "Click below to start the random selection.",
        "good_luck": "Good luck!",
        "random": "Random",
        "suite1_title": "The people who will sit on Suite Seat 1 are",
        "and": "and",
        "suite2_title": "The people who will sit on Suite Seat 2 are",
        "prime_title": "Next, these are the people who will sit on Prime Seat",
        "next": "Next",
        "summary_title": "Summary of Seating Arrangements",
        "suite1_row": "Suite Seat 1 (AA5 and AA6) : ",
        "suite2_row": "Suite Seat 2 (AA7 and AA8) : ",
        "prime1_row": "Prime Seat 1 (A7) : ",
        "prime2_row": "Prime Seat 2 (A8) : ",
        "prime3_row": "Prime Seat 3 (A9) : ",
        "reset": "Reset Selection",
        "change_language": "Change language",
        "lang_th": "ภาษาไทย",
        "lang_en": "English",
    },
    "TH": {
        "title": "โมอาน่า นั่งไหนดี?",
        "start_instruction": "กดปุ่มข้างล่างนี้เพื่อเริ่มทำการสุ่ม",
        "good_luck": "ขอให้โชคดี",
        "random": "เริ่มสุ่ม",
        "suite1_title": "คนที่จะได้นั่งโซฟาหมายเลข 1 ได้แก่",
        "and": "และ",
        "suite2_title": "คนที่จะได้นั่งโซฟาหมายเลข 2 ได้แก่",
        "prime_title": "ต่อไปนี้คือบุคคลที่จะได้นั่งแถวล่างลงมา",
        "next": "ถัดไป",
        "summary_title": "สรุปผลการสุ่มที่นั่ง",
        "suite1_row": "โซฟาหมายเลข 1 (AA5 กับ AA6) : ",
        "suite2_row": "โซฟาหมายเลข 1 (AA7 กับ AA8) : ",
        "prime1_row": "แถวล่าง 1 (A7) : ",
        "prime2_row": "แถวล่าง 2 (A8) : ",
        "prime3_row": "แถวล่าง 3 (A9) : ",
        "reset": "สุ่มใหม่ดีกว่า",
        "change_language": "เปลี่ยนภาษา",
        "lang_th": "ภาษาไทย",
        "lang_en": "English",
    },
}


def t(key):
    return TEXT[st.session_state.lang][key]


def tname(name):
    if st.session_state.lang == "TH":
        return NAMES_TH.get(name, name)
    return name


lang = st.session_state.lang

FONT_STACK = "'Prompt', Arial, Helvetica, sans-serif" if lang == "TH" else "Arial, Helvetica, sans-serif"
PADDING_TOP = 118 if st.session_state.step == 0 else 20

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

MAIN_CSS = """
    <style>
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
        padding: __PADDING_TOP__px 20px 20px 20px !important;
        margin: 0 auto !important;
        box-sizing: border-box !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
        z-index: 999997 !important;
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
        font-family: __FONT_STACK__ !important;
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

    .luck-marker { display: none; }
    
    div[data-testid="stElementContainer"]:has(.luck-marker) + div[data-testid="stElementContainer"] {
        margin-top: -14px !important;
    }

    div[data-testid="stElementContainer"]:has(.luck-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button {
        background: transparent !important;
        border: none !important;
        color: rgb(255, 255, 255) !important;
        font-family: __FONT_STACK__ !important;
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

    .topbar-gradient {
        position: fixed !important;
        top: 48px !important;
        left: 0 !important;
        width: 100vw !important;
        height: 52px !important;
        background: linear-gradient(90deg, #2062af, #6a7ebe) !important;
        z-index: 999998 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-sizing: border-box !important;
    }
    .topbar-gradient svg { height: 28px !important; }

    .lang-btn-marker { display: none; }

    div[data-testid="stElementContainer"]:has(.lang-btn-marker) + div[data-testid="stElementContainer"] {
        position: fixed !important;
        top: 59px !important;
        right: 16px !important;
        z-index: 999999 !important;
        width: auto !important;
        margin: 0 !important;
    }
    div[data-testid="stElementContainer"]:has(.lang-btn-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] {
        margin: 0 !important;
    }
    div[data-testid="stElementContainer"]:has(.lang-btn-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button {
        background: #05162a !important;
        color: rgb(255, 255, 255) !important;
        border: none !important;
        border-radius: 999px !important;
        padding: 6px 16px !important;
        font-size: 13px !important;
        min-height: auto !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.35) !important;
    }
    div[data-testid="stElementContainer"]:has(.lang-btn-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button:hover {
        background: #0a2848 !important;
        color: rgb(255, 255, 255) !important;
    }

    div[data-testid="stDialog"] * {
        color: #16213a !important;
        text-align: left !important;
        text-shadow: none !important;
    }
    div[data-testid="stDialog"] div[data-testid="stVerticalBlock"] > div {
        align-items: stretch !important;
    }
    div[data-testid="stDialog"] div[data-testid="stButton"] {
        width: 100% !important;
        max-width: 100% !important;
        margin: 6px 0 !important;
        display: block !important;
    }
    div[data-testid="stDialog"] div[data-testid="stButton"] button {
        width: 100% !important;
        max-width: 100% !important;
        text-align: left !important;
        justify-content: flex-start !important;
        background: #ffffff !important;
        color: #16213a !important;
        border: 1px solid #d7dbe3 !important;
        border-radius: 10px !important;
        padding: 13px 18px !important;
        font-size: 15px !important;
        box-shadow: none !important;
    }
    div[data-testid="stDialog"] div[data-testid="stButton"] button:hover {
        border-color: #2062af !important;
        color: #16213a !important;
    }
    </style>
"""
st.markdown(
    MAIN_CSS.replace("__FONT_STACK__", FONT_STACK).replace("__PADDING_TOP__", str(PADDING_TOP)),
    unsafe_allow_html=True,
)

if st.session_state.step == 0 or st.session_state.step == 11:
    st.markdown("""
        <style>
        div[data-testid="stButton"] > button {
            background-color: #05162a !important;
            color: rgb(255, 255, 255) !important;
            border: none !important;
            font-family: __FONT_STACK__ !important;
            padding: 11px 36px !important;
            border-radius: 4px !important;
            font-size: 16px !important;
            width: auto !important;
            max-width: max-content !important;
            margin: 0 auto !important;
            box-shadow: none !important;
        }
        </style>
    """.replace("__FONT_STACK__", FONT_STACK), unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        div[data-testid="stButton"] > button {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: rgb(255, 255, 255) !important;
            border: 1px solid rgba(255, 255, 255, 0.4) !important;
            text-decoration: none !important;
            font-size: 13px !important;
            font-family: __FONT_STACK__ !important;
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
    """.replace("__FONT_STACK__", FONT_STACK), unsafe_allow_html=True)

if st.session_state.step > 0 and st.session_state.step < 11:
    st.markdown("""
        <style>
        .curtain-panel {
            position: fixed;
            top: 0;
            height: 100vh;
            width: 50vw !important;
            background: repeating-linear-gradient(90deg, #150000, #260000 15px, #3b0000 30px, #260000 45px, #150000 60px);
            z-index: 99999 !important;
            animation: curtainClose 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
            box-shadow: inset 0 0 40px rgba(0, 0, 0, 0.6);
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
            width: 50vw !important;
            background: repeating-linear-gradient(90deg, #150000, #260000 15px, #3b0000 30px, #260000 45px, #150000 60px);
            z-index: 99999 !important;
            animation: curtainOpen 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards;
            box-shadow: inset 0 0 40px rgba(0, 0, 0, 0.6);
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

@st.dialog(t("change_language"))
def language_dialog():
    th_marker = "\u25cf" if lang == "TH" else "\u25cb"
    en_marker = "\u25cf" if lang == "EN" else "\u25cb"
    if st.button(f"{th_marker}   {t('lang_th')}", key="lang_opt_th"):
        st.session_state.lang = "TH"
        st.session_state.step = 0
        st.rerun()
    if st.button(f"{en_marker}   {t('lang_en')}", key="lang_opt_en"):
        st.session_state.lang = "EN"
        st.session_state.step = 0
        st.rerun()


if st.session_state.step == 0:
    st.markdown("""
        <div class="topbar-gradient">
            <svg viewBox="0 0 160 40" xmlns="http://www.w3.org/2000/svg">
                <rect x="0" y="4" width="34" height="32" rx="7" fill="#ffffff"></rect>
                <text x="17" y="27" font-family="Arial, Helvetica, sans-serif" font-size="17" font-weight="700" fill="#1a4c83" text-anchor="middle">SF</text>
                <text x="42" y="26" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="600" letter-spacing="2" fill="#ffffff">CINEMA</text>
            </svg>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="lang-btn-marker"></div>', unsafe_allow_html=True)
    if st.button(f"\U0001f310 {lang}", key="lang_toggle_btn"):
        language_dialog()

if st.session_state.step == 0:
    st.markdown(f"<h1>{t('title')}</h1>", unsafe_allow_html=True)
    st.image("https://lumiere-a.akamaihd.net/v1/images/moa_canon_poster-4x5now_6eed187f.jpeg", width=210)
    
    st.markdown(f"<p style='margin-bottom: 0px !important;'>{t('start_instruction')}</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="luck-marker"></div>', unsafe_allow_html=True)
    if st.button(t("good_luck"), key="invisible_good_luck_trigger"):
        st.session_state.secret_lock = not st.session_state.secret_lock

    if st.button(t("random")):
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
    st.markdown(f"<h2>{t('suite1_title')}</h2>", unsafe_allow_html=True)
    if st.button(t("next"), key="n1"):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.markdown(f"<h2>{tname(st.session_state.names_ordered[0])} {t('and')}</h2>", unsafe_allow_html=True)
    if st.button(t("next"), key="n2"):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.markdown(f"<h2>{tname(st.session_state.names_ordered[1])}</h2>", unsafe_allow_html=True)
    if st.button(t("next"), key="n3"):
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.markdown(f"<h2>{t('suite2_title')}</h2>", unsafe_allow_html=True)
    if st.button(t("next"), key="n4"):
        st.session_state.step = 5
        st.rerun()

elif st.session_state.step == 5:
    st.markdown(f"<h2>{tname(st.session_state.names_ordered[2])} {t('and')}</h2>", unsafe_allow_html=True)
    if st.button(t("next"), key="n5"):
        st.session_state.step = 6
        st.rerun()

elif st.session_state.step == 6:
    st.markdown(f"<h2>{tname(st.session_state.names_ordered[3])}</h2>", unsafe_allow_html=True)
    if st.button(t("next"), key="n6"):
        st.session_state.step = 7
        st.rerun()

elif st.session_state.step == 7:
    st.markdown(f"<h2>{t('prime_title')}</h2>", unsafe_allow_html=True)
    if st.button(t("next"), key="n7"):
        st.session_state.step = 8
        st.rerun()

elif st.session_state.step == 8:
    st.markdown(f"<h2>1. {tname(st.session_state.names_ordered[4])}</h2>", unsafe_allow_html=True)
    if st.button(t("next"), key="n8"):
        st.session_state.step = 9
        st.rerun()

elif st.session_state.step == 9:
    st.markdown(f"<h2>2. {tname(st.session_state.names_ordered[5])}</h2>", unsafe_allow_html=True)
    if st.button(t("next"), key="n9"):
        st.session_state.step = 10
        st.rerun()

elif st.session_state.step == 10:
    st.markdown(f"<h2>3. {tname(st.session_state.names_ordered[6])}</h2>", unsafe_allow_html=True)
    if st.button(t("next"), key="n10"):
        st.session_state.step = 11
        st.rerun()

elif st.session_state.step == 11:
    st.markdown(f"<h2>{t('summary_title')}</h2>", unsafe_allow_html=True)
    try:
        st.image("https://i.ibb.co/1Y5vNx9m/cinema-seats.png", width=315)
    except:
        pass
    n = st.session_state.names_ordered
    st.markdown(f"<p>{t('suite1_row')}{tname(n[0])} {t('and')} {tname(n[1])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>{t('suite2_row')}{tname(n[2])} {t('and')} {tname(n[3])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>{t('prime1_row')}{tname(n[4])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>{t('prime2_row')}{tname(n[5])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p>{t('prime3_row')}{tname(n[6])}</p>", unsafe_allow_html=True)
    
    if st.button(t("reset")):
        st.session_state.step = 0
        st.session_state.names_ordered = []
        st.session_state.secret_lock = False
        st.rerun()