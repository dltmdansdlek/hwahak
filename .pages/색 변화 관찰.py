import streamlit as st

st.set_page_config(page_title="산성과 염기성 지시약 색 변화", page_icon="🧪")

st.title("산성과 염기성 지시약 실험 색 변화 보기")
st.write(
    "산성과 염기성 용액에서 흔히 쓰이는 지시약의 색 변화를 pH에 따라 확인해보세요."
)

indicators = {
    "페놀프탈레인": {
        "range": "pH 8.2 - 10.0",
        "colors": [
            (0, "투명 (무색)"),
            (8, "연분홍"),
            (10, "진한 분홍")
        ]
    },
    "메틸 오렌지": {
        "range": "pH 3.1 - 4.4",
        "colors": [
            (0, "빨강"),
            (3.5, "주황"),
            (5, "노랑")
        ]
    },
    "리트머스": {
        "range": "pH 4.5 - 8.3",
        "colors": [
            (0, "빨강"),
            (5, "보라"),
            (9, "파랑")
        ]
    },
    "브롬티몰 블루": {
        "range": "pH 6.0 - 7.6",
        "colors": [
            (0, "노랑"),
            (6.5, "초록"),
            (8, "파랑")
        ]
    }
}

indicator_name = st.selectbox("지시약 선택", list(indicators.keys()))
selected = indicators[indicator_name]
ph_value = st.slider("pH 값", min_value=0.0, max_value=14.0, value=7.0, step=0.1)

st.subheader(f"선택된 지시약: {indicator_name}")
st.write(f"전환 범위: {selected['range']}")

# Determine approximate color by pH
color_label = ""
color_hex = "#FFFFFF"

if indicator_name == "페놀프탈레인":
    if ph_value < 8.2:
        color_label = "투명 (무색)"
        color_hex = "#F6F8FF"
    elif ph_value < 10.0:
        color_label = "연분홍"
        color_hex = "#FFB6C1"
    else:
        color_label = "진한 분홍"
        color_hex = "#FF1493"
elif indicator_name == "메틸 오렌지":
    if ph_value < 3.1:
        color_label = "빨강"
        color_hex = "#FF4500"
    elif ph_value < 4.4:
        color_label = "주황"
        color_hex = "#FFA500"
    else:
        color_label = "노랑"
        color_hex = "#FFFF66"
elif indicator_name == "리트머스":
    if ph_value < 4.5:
        color_label = "빨강"
        color_hex = "#DC143C"
    elif ph_value < 8.3:
        color_label = "보라"
        color_hex = "#800080"
    else:
        color_label = "파랑"
        color_hex = "#1E90FF"
else:  # 브롬티몰 블루
    if ph_value < 6.0:
        color_label = "노랑"
        color_hex = "#FFD700"
    elif ph_value < 7.6:
        color_label = "초록"
        color_hex = "#32CD32"
    else:
        color_label = "파랑"
        color_hex = "#4169E1"

st.markdown(
    f"#### 예상 색: {color_label}"
)

st.markdown(
    f"<div style='width:100%;height:120px;border-radius:12px;background:{color_hex};border:1px solid #999'></div>",
    unsafe_allow_html=True,
)

st.write("---")
st.subheader("지시약별 색 변화 설명")
for name, info in indicators.items():
    st.markdown(f"**{name}** — 전환 범위: {info['range']}")
    cols = st.columns(len(info['colors']))
    for col, (pH, text) in zip(cols, info['colors']):
        display_hex = "#FFFFFF"
        if "빨강" in text:
            display_hex = "#FF6347"
        elif "연분홍" in text or "분홍" in text:
            display_hex = "#FFB6C1"
        elif "진한 분홍" in text:
            display_hex = "#FF1493"
        elif "주황" in text:
            display_hex = "#FFA500"
        elif "노랑" in text:
            display_hex = "#FFFF66"
        elif "보라" in text:
            display_hex = "#800080"
        elif "파랑" in text:
            display_hex = "#1E90FF"
        elif "초록" in text:
            display_hex = "#32CD32"
        elif "투명" in text:
            display_hex = "#F6F8FF"
        col.markdown(f"<div style='padding:12px;border-radius:10px;background:{display_hex};text-align:center;color:#000'>pH {pH}<br>{text}</div>", unsafe_allow_html=True)
