import streamlit as st
import base64


def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def load_custom_css():
    bg_base64 = get_base64_image("assets/bg2.png")

    st.markdown(f"""
<style>
.stApp {{
    background:
        linear-gradient(rgba(3, 8, 18, 0.45), rgba(3, 8, 18, 0.70)),
        url("data:image/png;base64,{bg_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

.chip-container {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
    margin-top: 8px;
}}

.food-chip {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255,255,255,0.12);
    color: #e5e7eb;
    font-size: 16px;
}}

.chip-text {{
    white-space: nowrap;
}}

.chip-x {{
    width: 20px;
    height: 20px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: rgba(34, 197, 94, 0.25);
    color: #dcfce7;
    font-size: 12px;
    font-weight: 700;
}}

.true-card {{
    /*background: rgba(255, 255, 255, 0.08);*/
    background: linear-gradient(
        rgba(255,255,255,0.10),
        rgba(255,255,255,0.05)
    );
    color: #f8fbff;
    border-radius: 20px;
    padding: 20px 18px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 12px 30px rgba(0,0,0,0.25);

    backdrop-filter: none;
    -webkit-backdrop-filter: blur(16px);
    min-height: 520px;
}}

.true-card h3,
.true-card h4 {{
    color: #ffffff !important;
    font-weight: 700;
}}
.true-card p,
.true-card div,
.true-card span {{
    color: #e5e7eb !important;  /* softer white */
}}

.true-card-title {{
    font-size: 1.9rem;
    font-weight: 700;
    margin-bottom: 14px;
    color: #f59e0b !important; 
    letter-spacing: 0.3px;
}}

.true-card-subtitle {{
    font-size: 1.35rem;
    font-weight: 700;
    margin-bottom: 12px;
}}

.true-card .recipes-title {{
    color: #f59e0b !important;
}}

.true-card-item-title {{
    font-size: 1.05rem;
    font-weight: 700;
    margin-top: 14px;
    margin-bottom: 6px;
}}

.true-card-muted {{
    color: rgba(255,255,255,0.75) !important;
    font-size: 0.95rem;
    line-height: 1.5;
    margin-bottom: 6px;
}}

.true-card-divider {{
    border: none;
    border-top: 1px solid rgba(255,255,255,0.10);
    margin: 16px 0;
}}

.true-card-badge {{
    display: inline-block;
    background: rgba(255,255,255,0.18);
    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.25);
    padding: 5px 10px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-top: 6px;
}}

.true-card-impact-row {{
    display: flex;
    justify-content: space-between;
    gap: 16px;
    margin-top: 12px;
}}

.true-card-impact-box {{
    flex: 1;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 14px;
}}
.true-card-impact-label {{
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 8px;
}}

.true-card .true-card-impact-label.money {{
    color: #22c55e !important;
}}

.true-card .true-card-impact-label.waste {{
    color: #4ade80 !important;
}}

.true-card-impact-value {{
    font-size: 2.2rem;
    font-weight: 800;
    line-height: 1.05;
    text-shadow: 0 0 8px rgba(255,255,255,0.2);
}}

.true-card .true-card-impact-value.money {{
    color: #22c55e !important;
    font-weight: 800;
}}

.true-card .true-card-impact-value.waste {{
    color: #4ade80 !important;
    font-weight: 800;
}}

.true-card-good {{
    background: rgba(16, 185, 129, 0.12);
    color: #6ee7b7 !important;
    border: 1px solid #a7f3d0;
    border-radius: 14px;
    padding: 12px 14px;
    font-size: 0.95rem;
    margin-top: 12px;
}}

.true-card-warning {{
    background: rgba(251, 191, 36, 0.15);
    color: #fde68a !important;
    border: 1px solid rgba(251,191,36,0.4);
    border-radius: 14px;
    padding: 12px 14px;
    font-size: 0.95rem;
    margin-top: 12px;
}}

.center-panel {{
    background: rgba(8, 15, 28, 0.6);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 18px 20px 20px 20px;
}}

.block-container {{
    padding-top: 1rem;
    padding-bottom: 0.8rem;
}}

.app-title {{
    font-size: 2.2rem;
    font-weight: 800;
    margin-bottom: 0.2rem;
}}

.app-subtitle {{
    font-size: 1rem;
    color: #d1d5db;
    margin-bottom: 1rem;
}}

div.stButton > button {{
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    border-radius: 14px;
    height: 2.8rem;
    padding: 0 28px;
    border: none;
    font-weight: 700;
    width: auto !important;
    min-width: 160px;

    transition: all 0.2s ease;
}}

div.stButton > button:hover {{
    background: linear-gradient(135deg, #16a34a, #15803d);
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(34,197,94,0.35);
}}

div.stButton {{
    display: flex;
    justify-content: center;
    margin-top: 12px;
}}

/* ---------- white select / multiselect shell ---------- */
div[data-baseweb="select"] > div {{
    background: #ffffff !important;
    border-radius: 12px !important;
    border: 1px solid #e5e7eb !important;
    box-shadow: none !important;
}}

/* typed text / selected text */
div[data-baseweb="select"] input,
div[data-baseweb="select"] span {{
    color: #111827 !important;
    -webkit-text-fill-color: #111827 !important;
}}

/* placeholder */
div[data-baseweb="select"] input::placeholder {{
    color: #9ca3af !important;
    opacity: 1 !important;
    -webkit-text-fill-color: #9ca3af !important;
}}

/* arrow */
div[data-baseweb="select"] svg {{
    fill: #374151 !important;
    color: #374151 !important;
}}

/* selected tags */
div[data-baseweb="tag"] {{
    background: #cbd5e1 !important;
    border-radius: 10px !important;
    border: none !important;
}}

div[data-baseweb="tag"] span {{
    color: #111827 !important;
    -webkit-text-fill-color: #111827 !important;
}}

div[data-baseweb="tag"] svg {{
    fill: #111827 !important;
    color: #111827 !important;
}}

/* dropdown menu */
ul[role="listbox"] {{
    background: #ffffff !important;
    border: 1px solid #e5e7eb !important;
    border-radius: 12px !important;
    padding-top: 4px !important;
    padding-bottom: 4px !important;
}}

/* dropdown rows */
li[role="option"] {{
    background: #ffffff !important;
    color: #111827 !important;
}}

li[role="option"] * {{
    color: #111827 !important;
}}

/* hover / highlighted row */
li[role="option"]:hover,
li[aria-selected="true"] {{
    background: #f3f4f6 !important;
    color: #111827 !important;
}}

/* date input */
div[data-testid="stDateInput"] > div > div {{
    background: #ffffff !important;
    border-radius: 12px !important;
    border: 1px solid #e5e7eb !important;
}}

div[data-testid="stDateInput"] input {{
    color: #111827 !important;
    -webkit-text-fill-color: #111827 !important;
}}

/* ===== FORCE placeholder visibility (FINAL FIX) ===== */

/* main input */
div[data-baseweb="select"] input {{
    color: #111827 !important;
    -webkit-text-fill-color: #111827 !important;
}}
/* REAL placeholder fix */
div[data-baseweb="select"] input::placeholder {{
    color: #6b7280 !important;
    opacity: 1 !important;
    -webkit-text-fill-color: #6b7280 !important;
}}

/* THIS is the missing piece */
div[data-baseweb="select"] [data-testid="stMarkdownContainer"] {{
    color: #6b7280 !important;
}}
/* fallback internal text */
div[data-baseweb="select"] div {{
    color: #111827 !important;
}}

.side-card-wrap {{
    margin-top: 60px;
    margin-left: 6px;     
    margin-right: 6px;    
}}

/*.true-card > div.true-card-title.use-first-title {{
    color: #93c5fd !important;
}}*/

.recipe-loading {{
    font-size: 1.2rem;
    font-weight: 600;
    color: white;
    margin-top: 12px;
}}

.dots {{
    display: inline-block;
    width: 20px;
    text-align: left;
}}

.dots::after {{
    content: "...";
    animation: blink 1.2s infinite;
}}


</style>
""", unsafe_allow_html=True)