"""
레일연마차 업무자동화 — 진입점
실행: streamlit run rail_match_app.py
"""

import streamlit as st
from utils.auth import check_password
from utils.styles import COMMON_CSS

# ── 페이지 설정 ───────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="레일연마차 업무자동화",
    page_icon="🚃",
    layout="wide",
)

# ── 로그인 체크 ───────────────────────────────────────────────────────────────

if not check_password():
    st.stop()

# ── 공통 CSS ─────────────────────────────────────────────────────────────────

st.markdown(COMMON_CSS, unsafe_allow_html=True)

# ── 사이드바 ──────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("""
    <div class="sb-brand">
        <div class="sb-icon">🚃</div>
        <div class="sb-title">레일연마차<br>업무자동화</div>
        <div class="sb-sub">대저궤도장비분소</div>
    </div>
    """, unsafe_allow_html=True)

# ── 홈 화면 ───────────────────────────────────────────────────────────────────

st.markdown("""
<div class="page-header">
    <div class="ph-badge">레일연마차 업무자동화</div>
    <h2>🚃 업무자동화 시스템</h2>
    <p>레일연마차 운영 관련 반복 업무를 자동화합니다. 아래에서 기능을 선택하세요.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="fc-icon">🔍</div>
        <div class="fc-title">일정-실적 매칭</div>
        <div class="fc-desc">궤도정비공사 일정과 레일연마차 작업실적을 비교해 구간 겹침을 자동 확인합니다.</div>
        <span class="fc-tag">사용 가능</span>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/1_일정실적매칭.py", label="바로가기 →")

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="fc-icon">📊</div>
        <div class="fc-title">월간 실적 보고서</div>
        <div class="fc-desc">레일연마차 월간 작업실적을 자동 집계하고 보고서 형태로 출력합니다.</div>
        <span class="fc-tag soon">준비 중</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="fc-icon">🗓️</div>
        <div class="fc-title">작업 일정 관리</div>
        <div class="fc-desc">연마차별 작업 일정을 캘린더 형태로 시각화하고 이동일·검수일을 관리합니다.</div>
        <span class="fc-tag soon">준비 중</span>
    </div>
    """, unsafe_allow_html=True)
