```python
import streamlit as st
import random
import urllib.parse

# -------------------------
# 페이지 설정
# -------------------------

st.set_page_config(
    page_title="악세사리 코디 스타일링",
    page_icon="👗",
    layout="centered"
)

# -------------------------
# 데이터
# -------------------------

accessories = [
    "목걸이",
    "시계",
    "반지",
    "가방",
    "선글라스",
    "모자"
]

genders = [
    "남성",
    "여성",
    "공용"
]

seasons = [
    "봄",
    "여름",
    "가을",
    "겨울"
]

tips = {
    "목걸이": "무지 티셔츠와 목걸이를 함께 착용하면 포인트를 줄 수 있습니다.",
    "시계": "심플한 시계는 대부분의 코디와 잘 어울립니다.",
    "반지": "얇은 반지를 여러 개 레이어드하면 세련된 느낌을 줍니다.",
    "가방": "가방 색상을 신발과 맞추면 통일감이 생깁니다.",
    "선글라스": "얼굴형에 맞는 프레임을 선택해보세요.",
    "모자": "볼캡은 캐주얼룩에 잘 어울립니다."
}

# -------------------------
# 제목
# -------------------------

st.title("👗 악세사리 코디 스타일링")
st.write("악세사리를 활용한 옷 코디 영상을 유튜브에서 쉽게 찾아보세요.")

st.divider()

# -------------------------
# 입력
# -------------------------

gender = st.selectbox(
    "성별 선택",
    genders
)

season = st.selectbox(
    "계절 선택",
    seasons
)

accessory = st.selectbox(
    "악세사리 선택",
    accessories
)

# -------------------------
# 랜덤 추천
# -------------------------

if st.button("🎲 랜덤 추천"):
    gender = random.choice(genders)
    season = random.choice(seasons)
    accessory = random.choice(accessories)

    st.success(
        f"추천 코디 : {gender} {season} {accessory}"
    )

# -------------------------
# 검색어 생성
# -------------------------

search_query = f"{gender} {season} {accessory} 코디"

st.subheader("추천 검색어")
st.info(search_query)

# -------------------------
# 유튜브 검색 링크
# -------------------------

youtube_url = (
    "https://www.youtube.com/results?search_query="
    + urllib.parse.quote(search_query)
)

st.link_button(
    "▶ 유튜브 코디 영상 보기",
    youtube_url
)

# -------------------------
# 스타일링 팁
# -------------------------

st.subheader("스타일링 팁")

st.success(
    tips.get(
        accessory,
        "악세사리를 활용해 포인트를 주세요."
    )
)

# -------------------------
# 추천 검색어
# -------------------------

st.subheader("인기 검색어")

keywords = [
    f"{accessory} 스타일링",
    f"{accessory} 코디",
    f"{season} 패션",
    f"{gender} 데일리룩"
]

for keyword in keywords:
    url = (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote(keyword)
    )

    st.write(f"• {keyword}")
    st.link_button(
        f"{keyword} 검색",
        url
    )

st.divider()

st.caption("유튜브 검색 결과를 활용한 악세사리 코디 추천 앱")
```
