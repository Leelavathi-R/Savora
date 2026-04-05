import streamlit as st
from logic.spoilage import estimate_impact


def format_days_left(days_left: int, risk: str) -> str:
    if days_left < 0:
        return "Check smell/appearance before using"

    if days_left == 0:
        return "at risk of spoilage"

    if days_left == 1:
        return "1 day left — high spoilage risk"

    if risk == "Medium":
        return f" {days_left} days left — plan to use soon"

    return f" {days_left} days left — safe for now"


def render_results():
    results = st.session_state.get("analysis_results")
    if not results:
        st.markdown(
            """
            <div class="true-card">
                <div class="true-card-title use-first-title">What to use first</div>
                <div class="true-card-muted">
                    Analyze your items to see spoilage insights and savings.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    expired = [r for r in results if r["days_left"] < 0]
    urgent = [r for r in results if r["days_left"] == 0 or r["days_left"] == 1]
    medium_risk = [r for r in results if r["days_left"] > 1 and r["risk"] == "Medium"]
    low_risk = [r for r in results if r["days_left"] > 1 and r["risk"] == "Low"]

    impact = estimate_impact(results)

    html = ['<div class="true-card">']
    html.append('<div class="true-card-title use-first-title">What to use first</div>')

    if urgent:
        html.append('<div class="true-card-subtitle">🔴 Use today</div>')
        for r in urgent:
            html.append(
                f'<div class="true-card-muted">{r["item"].title()} — {format_days_left(r["days_left"], r["risk"])}</div>'
            )

    if expired:
        html.append('<div class="true-card-subtitle" style="margin-top:16px;">⚠️ Exceeded shelf life</div>')
        for r in expired:
            html.append(
                f'<div class="true-card-muted">{r["item"].title()} — {format_days_left(r["days_left"], r["risk"])}</div>'
            )

    if medium_risk:
        html.append('<div class="true-card-subtitle" style="margin-top:16px;">🟡 Use soon</div>')
        for r in medium_risk:
            html.append(
                f'<div class="true-card-muted">{r["item"].title()} — {format_days_left(r["days_left"], r["risk"])}</div>'
            )

    if low_risk:
        html.append('<div class="true-card-subtitle" style="margin-top:16px;">🟢 Safe</div>')
        for r in low_risk:
            html.append(
                f'<div class="true-card-muted">{r["item"].title()} — {format_days_left(r["days_left"], r["risk"])}</div>'
            )

    html.append('<hr class="true-card-divider">')

    if not urgent and not expired and not medium_risk:
        html.append('<div class="true-card-good">💡 No immediate waste risk — great job managing your food!</div>')
    else:
        html.append('<div class="true-card-impact-row">')
        html.append(
            f'<div class="true-card-impact-box">'
            f'<div class="true-card-impact-label money">💰 Estimated savings</div>'
            f'<div class="true-card-impact-value money">${impact["money_saved"]}</div>'
            f'</div>'
        )
        html.append(
            f'<div class="true-card-impact-box">'
            f'<div class="true-card-impact-label waste">🌱 Estimated waste avoided</div>'
            f'<div class="true-card-impact-value waste">{impact["waste_avoided"]} kg</div>'
            f'</div>'
        )
        html.append('</div>')

    html.append('</div>')

    st.markdown("".join(html), unsafe_allow_html=True)