```python
import random
import urllib.parse
import streamlit as st

st.set_page_config(
    page_title="악세사리 코디 스타일링",
    page_icon="👔",
    layout="wide"
)

# -------------------
# 데이터
# -------------------

ACCESSORIES = [
    "목걸이",
    "시계",
    "반지",
    "가방",
    "선글라스",
    "모자"
]

GENDERS = [
    "남성",
    "여성",
    "공용"
]

SEASONS = [
    "봄",
    "여름",
    "가을",
    "겨울"
]

STYLE_TIPS = {
    "목걸이": "무지 티셔츠와 레이어드 목걸이를 매치하면 포인트를 줄 수 있습니다.",
    "시계": "심플한 시계는 캐주얼부터 포멀룩까지 활용 가능합니다.",
    "반지": "여러 개의 얇은 반지를 레이어드하면 트렌디한 느낌을 줍니다.",
    "가방": "상의와 가방 색상을 맞추면 통일감 있는 코디가 됩니다.",
    "선글라스": "얼굴형에 맞는 프레임을 선택하면 스타일이 완성됩니다.",
    "모자": "볼캡은 캐주얼룩, 페도라는 클래식룩에 잘 어울립니다."
}

# -------------------
# 제목
# -------------------

st.title("👔 악세사리 코디 스타일링")
st.caption("악세사리를 활용한 옷 코디 유튜브 검색 앱")

st.divider()

# -------------------
# 선택 영역
# -------------------

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "성별",
        GENDERS
    )

with col2:
    season = st.selectbox(
        "계절",
        SEASONS
    )

with col3:
    accessory = st.selectbox(
        "악세사리",
        ACCESSORIES
    )

# -------------------
# 랜덤 추천
# -------------------

if st.button("🎲 랜덤 코디 추천"):

    gender = random.choice(GENDERS)
    season = random.choice(SEASONS)
    accessory = random.choice(ACCESSORIES)

    st.success(
        f"추천: {gender} · {season} · {accessory}"
    )

# -------------------
# 검색어 생성
# -------------------

search_query = f"{gender} {season} {accessory} 코디"

st.subheader("🔍 추천 검색어")
st.info(search_query)

# -------------------
# 유튜브 검색 링크
# -------------------

encoded_query = urllib.parse.quote(search_query)

youtube_url = (
    f"https://www.youtube.com/results?search_query={encoded_query}"
)

st.link_button(
    "▶ 유튜브에서 코디 영상 보기",
    youtube_url,
    use_container_width=True
)

# -------------------
# 코디 팁
# -------------------

st.subheader("✨ 스타일링 팁")

st.success(
    STYLE_TIPS.get(
        accessory,
        "악세사리를 활용해 포인트를 주세요."
    )
)

# -------------------
# 추천 검색어
# -------------------

st.subheader("📌 인기 검색어")

popular_keywords = [
    f"{gender} {accessory} 코디",
    f"{season} {accessory} 스타일링",
    f"{gender} 패션 악세사리 추천",
    f"{accessory} 활용 코디",
    f"{season} 데일리룩"
]

for keyword in popular_keywords:
    encoded = urllib.parse.quote(keyword)

    url = (
        f"https://www.youtube.com/results?search_query={encoded}"
    )

    st.markdown(
        f"- [{keyword}]({url})"
    )

st.divider()

st.caption(
    "유튜브 검색 결과를 활용하여 악세사리 중심 코디 영상을 쉽게 찾을 수 있습니다."
)
```
