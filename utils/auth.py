import streamlit as st


def check_password() -> bool:
    """비밀번호 확인. 통과하면 True, 아니면 로그인 화면 표시 후 False."""
    if st.session_state.get("authenticated"):
        return True

    st.markdown("""
    <div style="max-width:360px; margin:80px auto 0; text-align:center;">
        <div style="font-size:2.8rem; margin-bottom:8px;">🚃</div>
        <div style="font-size:1.2rem; font-weight:700; color:#1a2332; margin-bottom:4px;">
            레일연마차 업무자동화
        </div>
        <div style="font-size:0.82rem; color:#64748b; margin-bottom:28px;">
            대저궤도장비분소 전용 시스템
        </div>
    </div>
    """, unsafe_allow_html=True)

    col = st.columns([1, 2, 1])[1]
    with col:
        pw = st.text_input("비밀번호", type="password", placeholder="비밀번호를 입력하세요")
        if st.button("로그인", use_container_width=True):
            if pw == st.secrets["PASSWORD"]:
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("비밀번호가 올바르지 않습니다.")
    return False
