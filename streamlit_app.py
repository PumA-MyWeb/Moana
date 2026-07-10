import streamlit as st
import random
st.set_page_config(page_title="ระบบจัดที่นั่งสุดพิเศษ", page_icon="🎬", layout="centered")
st.title("🎬 ระบบสุ่มจัดที่นั่งโรงภาพยนตร์")
st.write("กดปุ่มด้านล่างเพื่อทำการสุ่มจัดที่นั่งให้กับทุกคนในระบบ")
if st.button("🎰 เริ่มสุ่มที่นั่งใหม่", type="primary"):
    a = ["Cat", "Fairway", "Ice", "Phu", "Plewai", "Primo", "Puma"]
    b = random.randint(1, 4)
    suite1 = []
    suite2 = []
    prime = [None, None, None]
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
    st.success("🎉 ทำการสุ่มและจัดที่นั่งเรียบร้อยแล้ว!")
    st.balloons()
    st.subheader("🛋️ โซน Suite Seats (เบาะคู่)")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Suite Seat 1** (AA5, AA6)")
        st.markdown(f"👤 **คนที่ 1:** {suite1[0]}")
        st.markdown(f"👤 **คนที่ 2:** {suite1[1]}")
    with col2:
        st.info("**Suite Seat 2** (AA7, AA8)")
        st.markdown(f"👤 **คนที่ 1:** {suite2[0]}")
        st.markdown(f"👤 **คนที่ 2:** {suite2[1]}")
    st.write("---")
    st.subheader("💺 โซน Prime Seats (เบาะเดี่ยว)")
    p_col1, p_col2, p_col3 = st.columns(3)
    with p_col1:
        st.metric(label="Prime 1 (A7)", value=prime[0])
    with p_col2:
        st.metric(label="Prime 2 (A8)", value=prime[1])
    with p_col3:
        st.metric(label="Prime 3 (A9)", value=prime[2])
    st.caption(f"ℹ️ ระบบคำนวณผ่านโครงสร้างเงื่อนไขรูปแบบที่ {b}")
else:
    st.info("💡 กรุณากดปุ่มด้านบนเพื่อเริ่มสุ่มตำแหน่งที่นั่ง")
    st.write("**📋 ข้อมูลหมายเลขที่นั่งในระบบ:**")
    st.markdown("""
    *   **Suite Seat 1:** ที่นั่งหมายเลข AA5 และ AA6
    *   **Suite Seat 2:** ที่นั่งหมายเลข AA7 และ AA8
    *   **Prime Seat 1:** ที่นั่งหมายเลข A7
    *   **Prime Seat 2:** ที่นั่งหมายเลข A8
    *   **Prime Seat 3:** ที่นั่งหมายเลข A9
    """)