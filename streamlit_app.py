import streamlit as st
import random

if "names_ordered" not in st.session_state:
    st.session_state.names_ordered = []
if "secret_lock" not in st.session_state:
    st.session_state.secret_lock = False
if "lang" not in st.session_state:
    st.session_state.lang = "EN"

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
        "names": {"Cat": "Cat", "Fairway": "Fairway", "Ice": "Ice", "Phu": "Phu", "Plewai": "Plewai", "Primo": "Primo", "Puma": "Puma"},
        "change_lang": "Change language"
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
        "names": {"Cat": "แคท", "Fairway": "แฟร์เวย์", "Ice": "ไอซ์", "Phu": "ภู", "Plewai": "เปลหวาย", "Primo": "พรีโม่", "Puma": "พูม่า"},
        "change_lang": "เปลี่ยนภาษา"
    }
}

current_lang = st.session_state.lang

# กำหนดสเต็ปเริ่มต้นถ้ายังไม่มี
if f"step_{current_lang}" not in st.session_state:
    st.session_state[f"step_{current_lang}"] = 0

step_key = f"step_{current_lang}"
current_step = st.session_state[step_key]

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;700&display=swap');
    
    /* ซ่อน UI ส่วนเกินของ Streamlit */
    header[data-testid="stHeader"], footer, div[data-testid="stDecoration"] {
        display: none !important;
    }
    
    html, body, .stApp {
        margin: 0 !important;
        padding: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        overflow-x: hidden !important;
        background: linear-gradient(90deg, #000000, #1a4c83) !important;
    }
    
    /* ปรับระยะห่างของเนื้อหาไม่ให้ห่างจากแถบด้านบนเกินไปในมือถือ */
    div[data-testid="stMainBlockContainer"] {
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        min-height: 100vh !important;
        max-width: 100vw !important;
        padding: 65px 20px 20px 20px !important;
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

    /* บังคับฟอนต์ไม่มีหัวสำหรับภาษาไทยและอังกฤษทั่วทั้งแอป */
    html, body, [class*="css"], .stMarkdown, p, div, h1, h2, h3, h4, h5, h6, span, label, input, button, select, textarea {
        font-family: 'Prompt', Arial, sans-serif !important;
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
    }

    /* แถบ Header สีฟ้า */
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
        padding: 0 15px !important;
        box-sizing: border-box !important;
    }

    /* โลโก้ SF เวอร์ชันใหม่ ขึ้นร้อยเปอร์เซ็นต์ */
    .header-logo {
        height: 24px !important;
        width: auto !important;
        object-fit: contain !important;
    }

    /* จัดการปุ่ม Popover เปลี่ยนภาษาให้เกาะขอบขวาและกึ่งกลางแนว Y */
    .popover-container-marker { display: none; }
    
    div[data-testid="stElementContainer"]:has(.popover-container-marker) + div[data-testid="stElementContainer"] {
        position: fixed !important;
        top: 0 !important;
        right: 15px !important;
        z-index: 9995 !important;
        height: 50px !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important; /* กึ่งกลางแนว Y เสมอ */
    }

    /* แต่งปุ่มกดหลักของ Popover */
    div[data-testid="stElementContainer"]:has(.popover-container-marker) + div[data-testid="stElementContainer"] div[data-testid="stPopover"] > button {
        background: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        color: #ffffff !important;
        padding: 4px 12px 4px 32px !important;
        font-size: 13px !important;
        border-radius: 4px !important;
        height: 30px !important;
        min-height: 30px !important;
        line-height: 1.2 !important;
        background-image: url('https://img.icons8.com/ios-filled/50/ffffff/globe.png') !important;
        background-repeat: no-repeat !important;
        background-position: 10px center !important;
        background-size: 14px 14px !important;
        width: auto !important;
    }

    /* แต่งกล่อง Popover คาร์ดสีขาวด้านในให้เหมือน Mockup ของผู้ใช้ */
    div[data-testid="stPopoverWindow"] {
        background: #ffffff !important;
        border-radius: 24px !important;
        padding: 10px !important;
        box-shadow: 0 4px 25px rgba(0,0,0,0.3) !important;
        border: none !important;
    }

    /* ปรับแต่งส่วนประกอบวิทยุ (Radio) ภายใน Popover */
    div[data-testid="stPopoverWindow"] [data-testid="stWidgetLabel"] p {
        color: #000000 !important;
        font-size: 20px !important;
        font-weight: 500 !important;
        text-align: left !important;
        margin-bottom: 12px !important;
    }

    div[data-testid="stPopoverWindow"] [data-testid="stRadio"] > div {
        flex-direction: column !important;
        gap: 8px !important;
    }

    div[data-testid="stPopoverWindow"] [data-testid="stRadio"] label {
        background: #ffffff !important;
        border: 1px solid #dcdcdc !important;
        border-radius: 12px !important;
        padding: 10px 16px !important;
        width: 230px !important;
        min-height: 48px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        box-sizing: border-box !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
    }

    div[data-testid="stPopoverWindow"] [data-testid="stRadio"] label:has(input:checked) {
        border-color: #1a73e8 !important;
    }

    div[data-testid="stPopoverWindow"] [data-testid="stRadio"] label p {
        color: #333333 !important;
        font-size: 16px !important;
        text-align: left !important;
        margin: 0 0 0 8px !important;
    }

    .luck-marker { display: none; }
    
    div[data-testid="stElementContainer"]:has(.luck-marker) + div[data-testid="stElementContainer"] {
        margin-top: -14px !important;
    }

    div[data-testid="stElementContainer"]:has(.luck-marker) + div[data-testid="stElementContainer"] div[data-testid="stButton"] button {
        background: transparent !important;
        border: none !important;
        color: rgb(255, 255, 255) !important;
        font-size: 0.95rem !important;
        font-weight: 400 !important;
        box-shadow: none !important;
        padding: 0 !important;
        cursor: default !important;
        min-height: auto !important;
    }
    </style>
""", unsafe_allow_html=True)

# ปรับปรุงสไตล์ปุ่มหลัก
if current_step == 0 or current_step == 11:
    st.markdown("""
        <style>
        div[data-testid="stAppViewBlockContainer"] div[data-testid="stButton"] > button {
            background-color: #05162a !important;
            color: rgb(255, 255, 255) !important;
            border: none !important;
            padding: 11px 36px !important;
            border-radius: 4px !important;
            font-size: 16px !important;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        div[data-testid="stAppViewBlockContainer"] div[data-testid="stButton"] > button {
            background-color: rgba(255, 255, 255, 0.1) !important;
            color: rgb(255, 255, 255) !important;
            border: 1px solid rgba(255, 255, 255, 0.4) !important;
            font-size: 13px !important;
            padding: 5px 18px !important;
            border-radius: 4px !important;
        }
        </style>
    """, unsafe_allow_html=True)

# แอนิเมชันผ้าม่าน
if 0 < current_step < 11:
    st.markdown("""
        <style>
        .curtain-panel {
            position: fixed; top: 0; height: 100vh; width: 50vw !important;
            background: repeating-linear-gradient(90deg, #0a0000, #170202 15px, #260404 30px, #170202 45px, #0a0000 60px);
            z-index: 99999 !important; box-shadow: inset 0 0 40px rgba(0, 0, 0, 0.7);
        }
        .left-p { left: 0 !important; animation: curtainClose 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards; transform-origin: left; }
        .right-p { right: 0 !important; animation: curtainClose 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards; transform-origin: right; }
        @keyframes curtainClose { 0% { transform: scaleX(0); } 100% { transform: scaleX(1.02); } }
        </style>
        <div class="curtain-panel left-p"></div><div class="curtain-panel right-p"></div>
    """, unsafe_allow_html=True)
elif current_step == 11:
    st.markdown("""
        <style>
        .curtain-panel {
            position: fixed; top: 0; height: 100vh; width: 50vw !important;
            background: repeating-linear-gradient(90deg, #0a0000, #170202 15px, #260404 30px, #170202 45px, #0a0000 60px);
            z-index: 99999 !important; box-shadow: inset 0 0 40px rgba(0, 0, 0, 0.7);
        }
        .left-p { left: 0 !important; animation: curtainOpen 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards; transform-origin: left; }
        .right-p { right: 0 !important; animation: curtainOpen 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards; transform-origin: right; }
        @keyframes curtainOpen { 0% { transform: scaleX(1.02); } 100% { transform: scaleX(0); } }
        </style>
        <div class="curtain-panel left-p"></div><div class="curtain-panel right-p"></div>
    """, unsafe_allow_html=True)

# วาดส่วนของแถบด้านบน
st.markdown('<div class="custom-header"><img class="header-logo" src="https://worldvectorlogo.com/download/sf-1.svg"></div>', unsafe_allow_html=True)

# ตัวเลือกภาษา Popover แท้ ยึดขวาเกาะกลาง Y แม่นยำ
st.markdown('<div class="popover-container-marker"></div>', unsafe_allow_html=True)
with st.popover(st.session_state.lang):
    selected_lang = st.radio(
        t[current_lang]["change_lang"],
        options=["ภาษาไทย", "English"],
        index=0 if current_lang == "TH" else 1,
        label_visibility="visible"
    )
    new_lang = "TH" if selected_lang == "ภาษาไทย" else "EN"
    if new_lang != st.session_state.lang:
        st.session_state.lang = new_lang
        st.rerun()

# --- ตรรกะแสดงผลตามสเต็ปเดิม ---
if current_step == 0:
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
            else:
                suite1 = [others.pop(), others.pop()]
                suite2 = [others.pop(), others.pop()]
                p_pair = fixed_pair.copy()
                random.shuffle(p_pair)
                prime = [others.pop(), p_pair[0], p_pair[1]]
            st.session_state.names_ordered = suite1 + suite2 + prime
        else:
            random.shuffle(all_names)
            st.session_state.names_ordered = all_names
            
        st.session_state[step_key] = 1
        st.rerun()

elif current_step == 1:
    st.markdown(f"<h2>{t[current_lang]['suite1']}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n1"):
        st.session_state[step_key] = 2
        st.rerun()

elif current_step == 2:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[0]]
    st.markdown(f"<h2>{name_val} {t[current_lang]['and']}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n2"):
        st.session_state[step_key] = 3
        st.rerun()

elif current_step == 3:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[1]]
    st.markdown(f"<h2>{name_val}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n3"):
        st.session_state[step_key] = 4
        st.rerun()

elif current_step == 4:
    st.markdown(f"<h2>{t[current_lang]['suite2']}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n4"):
        st.session_state[step_key] = 5
        st.rerun()

elif current_step == 5:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[2]]
    st.markdown(f"<h2>{name_val} {t[current_lang]['and']}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n5"):
        st.session_state[step_key] = 6
        st.rerun()

elif current_step == 6:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[3]]
    st.markdown(f"<h2>{name_val}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n6"):
        st.session_state[step_key] = 7
        st.rerun()

elif current_step == 7:
    st.markdown(f"<h2>{t[current_lang]['prime_intro']}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n7"):
        st.session_state[step_key] = 8
        st.rerun()

elif current_step == 8:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[4]]
    st.markdown(f"<h2>1. {name_val}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n8"):
        st.session_state[step_key] = 9
        st.rerun()

elif current_step == 9:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[5]]
    st.markdown(f"<h2>2. {name_val}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n9"):
        st.session_state[step_key] = 10
        st.rerun()

elif current_step == 10:
    name_val = t[current_lang]['names'][st.session_state.names_ordered[6]]
    st.markdown(f"<h2>3. {name_val}</h2>", unsafe_allow_html=True)
    if st.button(t[current_lang]['next'], key="n10"):
        st.session_state[step_key] = 11
        st.rerun()

elif current_step == 11:
    st.markdown(f"<h2>{t[current_lang]['summary']}</h2>", unsafe_allow_html=True)
    st.image("https://i.ibb.co/1Y5vNx9m/cinema-seats.png", width=315)
    
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
        st.session_state[step_key] = 0
        st.session_state.names_ordered = []
        st.session_state.secret_lock = False
        st.rerun()