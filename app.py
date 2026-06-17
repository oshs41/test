import streamlit as st
import random

st.set_page_config(
    page_title="AI 옷 코디 추천",
    page_icon="👔",
    layout="wide"
)

# -----------------------------
# 코디 데이터
# -----------------------------

OUTFITS = {
    "캐주얼": {
        "봄": [
            ("오버핏 셔츠", "연청 데님", "스니커즈"),
            ("맨투맨", "조거팬츠", "화이트 운동화"),
            ("가디건", "슬랙스", "로퍼"),
        ],
        "여름": [
            ("반팔 티셔츠", "반바지", "샌들"),
            ("린넨 셔츠", "와이드 팬츠", "슬립온"),
            ("오버핏 반팔", "데님 반바지", "운동화"),
        ],
        "가을": [
            ("후드티", "청바지", "스니커즈"),
            ("니트", "슬랙스", "로퍼"),
            ("체크 셔츠", "면바지", "운동화"),
        ],
        "겨울": [
            ("패딩", "기모 청바지", "부츠"),
            ("코트", "슬랙스", "로퍼"),
            ("니트", "기모 팬츠", "스니커즈"),
        ]
    },
    "미니멀": {
        "봄": [
            ("화이트 셔츠", "블랙 슬랙스", "로퍼"),
            ("베이지 니트", "슬랙스", "스니커즈"),
            ("가디건", "와이드 팬츠", "로퍼"),
        ],
        "여름": [
            ("린넨 셔츠", "슬랙스", "샌들"),
            ("무지 반팔", "와이드 팬츠", "슬립온"),
            ("화이트 반팔", "블랙 팬츠", "로퍼"),
        ],
        "가을": [
            ("니트", "슬랙스", "로퍼"),
            ("셔츠", "와이드 팬츠", "스니커즈"),
            ("가디건", "슬랙스", "로퍼"),
        ],
        "겨울": [
            ("롱코트", "슬랙스", "첼시부츠"),
            ("터틀넥", "와이드 팬츠", "로퍼"),
            ("코트", "니트", "부츠"),
        ]
    },
    "스트릿": {
        "봄": [
            ("후드티", "카고팬츠", "하이탑"),
            ("오버핏 셔츠", "와이드 팬츠", "운동화"),
            ("바시티 자켓", "청바지", "스니커즈"),
        ],
        "여름": [
            ("그래픽 반팔", "카고 반바지", "운동화"),
            ("오버핏 반팔", "와이드 팬츠", "스니커즈"),
            ("민소매", "카고팬츠", "하이탑"),
        ],
        "가을": [
            ("후드집업", "카고팬츠", "운동화"),
            ("맨투맨", "와이드 팬츠", "스니커즈"),
            ("바람막이", "조거팬츠", "운동화"),
        ],
        "겨울": [
            ("숏패딩", "카고팬츠", "부츠"),
            ("후드티", "기모 조거팬츠", "운동화"),
            ("패딩", "와이드 팬츠", "하이탑"),
        ]
    }
}

SITUATION_TIPS = {
    "데이트": "깔끔하고 호감형 느낌을 주는 조합입니다.",
    "출근": "단정하면서도 편안한 인상을 줄 수 있습니다.",
    "여행": "활동성과 편안함을 고려한 코디입니다.",
    "학교": "편안하면서도 트렌디한 느낌을 줄 수 있습니다.",
    "주말 나들이": "가볍고 자연스러운 분위기를 연출합니다."
}


# -----------------------------
# 추천 함수
# -----------------------------
def recommend_outfits(style, season):
    outfits = OUTFITS.get(style, {}).get(season, [])

    if len(outfits) >= 3:
        return random.sample(outfits, 3)

    return outfits


# -----------------------------
# UI
# -----------------------------
st.title("👕 옷 코디 추천 앱")
st.caption("계절, 스타일, 상황에 맞는 코디를 3개 추천해드립니다.")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "성별",
        ["남성", "여성", "상관없음"]
    )

    season = st.selectbox(
        "계절",
        ["봄", "여름", "가을", "겨울"]
    )

with col2:
    style = st.selectbox(
        "스타일",
        ["캐주얼", "미니멀", "스트릿"]
    )

    situation = st.selectbox(
        "상황",
        ["데이트", "출근", "여행", "학교", "주말 나들이"]
    )

st.divider()

if st.button("✨ 코디 추천받기", use_container_width=True):
    try:
        recommendations = recommend_outfits(style, season)

        if not recommendations:
            st.warning("추천 데이터를 찾을 수 없습니다.")
        else:
            st.success("추천 완료!")

            for idx, outfit in enumerate(recommendations, start=1):
                top, bottom, shoes = outfit

                with st.container(border=True):
                    st.subheader(f"코디 {idx}")

                    st.write(f"👕 상의 : {top}")
                    st.write(f"👖 하의 : {bottom}")
                    st.write(f"👟 신발 : {shoes}")

                    st.info(
                        f"💡 {situation}에 어울리는 추천 조합입니다. "
                        f"{SITUATION_TIPS[situation]}"
                    )

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

st.divider()

with st.expander("🎲 랜덤 코디 추천"):
    if st.button("랜덤 추천"):
        try:
            random_style = random.choice(list(OUTFITS.keys()))
            random_season = random.choice(["봄", "여름", "가을", "겨울"])

            outfit = random.choice(
                OUTFITS[random_style][random_season]
            )

            st.write(f"스타일: {random_style}")
            st.write(f"계절: {random_season}")

            st.success(
                f"상의: {outfit[0]} / 하의: {outfit[1]} / 신발: {outfit[2]}"
            )

        except Exception as e:
            st.error(f"오류 발생: {e}")

st.divider()
st.caption("Made with Streamlit")
