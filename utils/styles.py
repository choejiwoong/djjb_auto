COMMON_CSS = """
<style>
    /* 전체 */
    [data-testid="stAppViewContainer"] { background: #f0f4f8; }

    /* 사이드바 */
    [data-testid="stSidebar"] { background: #1a2332; padding-top: 0; }
    [data-testid="stSidebar"] * { color: #e2e8f0 !important; }
    [data-testid="stSidebar"] .stFileUploader label {
        color: #94a3b8 !important;
        font-size: 0.75rem !important;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    /* 사이드바 앱 타이틀 */
    .sb-brand {
        padding: 20px 16px 14px;
        border-bottom: 1px solid #2d3f55;
        margin-bottom: 8px;
    }
    .sb-brand .sb-icon { font-size: 1.5rem; }
    .sb-brand .sb-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #f1f5f9 !important;
        margin-top: 4px;
        line-height: 1.3;
    }
    .sb-brand .sb-sub {
        font-size: 0.7rem;
        color: #64748b !important;
        margin-top: 2px;
    }

    /* 메인 콘텐츠 */
    .page-header {
        background: linear-gradient(135deg, #1a2332 0%, #2d3f55 100%);
        border-radius: 12px;
        padding: 24px 28px 20px;
        margin-bottom: 20px;
    }
    .page-header .ph-badge {
        display: inline-block;
        background: #0f766e33;
        color: #5eead4 !important;
        font-size: 0.65rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        padding: 3px 10px;
        border-radius: 99px;
        border: 1px solid #0f766e66;
        margin-bottom: 8px;
    }
    .page-header h2 {
        margin: 0;
        font-size: 1.4rem;
        font-weight: 700;
        color: white !important;
        letter-spacing: -0.02em;
    }
    .page-header p {
        margin: 6px 0 0;
        font-size: 0.82rem;
        color: #94a3b8 !important;
    }

    /* 업로드 카드 */
    .upload-section {
        background: white;
        border-radius: 12px;
        padding: 20px 24px;
        border: 1px solid #e2e8f0;
        margin-bottom: 16px;
    }
    .upload-section .us-title {
        font-size: 0.7rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 14px;
        padding-bottom: 8px;
        border-bottom: 1px solid #f1f5f9;
    }

    /* 상태 배지 */
    .status-row {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 8px 12px;
        border-radius: 8px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        margin-bottom: 8px;
        font-size: 0.82rem;
    }
    .status-row.ok { background: #f0fdf4; border-color: #bbf7d0; }
    .status-row.wait { background: #fafafa; border-color: #e5e7eb; }
    .dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
    .dot.green { background: #22c55e; }
    .dot.gray { background: #d1d5db; }

    /* 지표 카드 */
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 16px 20px;
        border: 1px solid #e2e8f0;
    }
    .metric-card .mc-label {
        font-size: 0.68rem;
        font-weight: 700;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 4px;
    }
    .metric-card .mc-value {
        font-size: 1.9rem;
        font-weight: 800;
        color: #1a2332;
        line-height: 1;
    }
    .metric-card .mc-value.green { color: #0f766e; }
    .metric-card .mc-value.amber { color: #b45309; }
    .metric-card .mc-value.sm { font-size: 1.2rem; margin-top: 4px; }

    /* 경고/정보 */
    .warn-box {
        background: #fffbeb;
        border-left: 4px solid #f59e0b;
        border-radius: 0 8px 8px 0;
        padding: 12px 16px;
        font-size: 0.83rem;
        color: #92400e;
        margin: 8px 0;
    }

    /* 홈 기능 카드 */
    .feature-card {
        background: white;
        border-radius: 12px;
        padding: 22px 24px;
        border: 1px solid #e2e8f0;
        height: 100%;
    }
    .feature-card .fc-icon { font-size: 1.8rem; margin-bottom: 10px; }
    .feature-card .fc-title { font-size: 1rem; font-weight: 700; color: #1a2332; margin-bottom: 4px; }
    .feature-card .fc-desc { font-size: 0.8rem; color: #64748b; line-height: 1.5; }
    .feature-card .fc-tag {
        display: inline-block;
        margin-top: 10px;
        font-size: 0.65rem;
        font-weight: 700;
        padding: 3px 8px;
        border-radius: 4px;
        background: #f0fdf4;
        color: #0f766e;
        border: 1px solid #bbf7d0;
    }
    .feature-card .fc-tag.soon {
        background: #f8fafc;
        color: #94a3b8;
        border-color: #e2e8f0;
    }

    /* 버튼 */
    .stButton > button {
        background: #0f766e;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        font-size: 0.88rem;
        width: 100%;
    }
    .stButton > button:hover { background: #0d5e58; }

    /* 테이블 */
    [data-testid="stDataFrame"] { border-radius: 8px; overflow: hidden; }
</style>
"""
