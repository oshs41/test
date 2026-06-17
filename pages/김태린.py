import streamlit as st

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(
    page_title="하의 코디 스타일링",
    page_icon="👖",
    layout="centered"
)

st.title("👖 하의 코디 스타일링")
st.write("원하는 하의 스타일을 선택하면 코디를 추천해드립니다.")

# ---------------------------
# 세션 초기화
# ---------------------------
if "saved_outfits" not in st.session_state:
    st.session_state.saved_outfits = []

# ---------------------------
# 입력 영역
# ---------------------------
try:
    pants_type = st.selectbox(
        "하의 종류",
        ["청바지", "슬랙스", "반바지", "스커트"]
    )

    color = st.color_picker("색상 선택", "#3366ff")

    fit = st.radio(
        "핏 선택",
        ["슬림", "레귤러", "와이드"],
        horizontal=True
    )

    occasion = st.selectbox(
        "착용 상황",
        ["캐주얼", "출근", "데이트", "운동"]
    )

except Exception as e:
    st.error("입력 UI 로딩 중 오류가 발생했습니다.")
    st.stop()

# ---------------------------
# 코디 추천 로직
# ---------------------------
def get_recommendation(pants, fit, occasion):
    tops = {
        "캐주얼": "흰 티셔츠 / 후드티",
        "출근": "셔츠 / 니트",
        "데이트": "슬림 니트 / 블라우스",
        "운동": "기능성 티셔츠"
    }

    shoes = {
        "청바지": "스니커즈",
        "슬랙스": "로퍼",
        "반바지": "슬라이드 / 운동화",
        "스커트": "플랫슈즈 / 샌들"
    }

    return tops.get(occasion, "기본 상의"), shoes.get(pants, "스니커즈")


top, shoe = get_recommendation(pants_type, fit, occasion)

# ---------------------------
# 결과 출력
# ---------------------------
st.subheader("✨ 코디 추천 결과")

st.markdown(f"""
### 👖 선택한 하의
- 종류: **{pants_type}**
- 핏: **{fit}**
- 상황: **{occasion}**
""")

st.markdown("### 👕 추천 상의")
st.success(top)

st.markdown("### 👟 추천 신발")
st.info(shoe)

# ---------------------------
# 시각적 미리보기 (단순 박스 UI)
# ---------------------------
st.markdown("### 🎨 스타일 미리보기")

st.markdown(f"""
<div style="
    width: 120px;
    height: 160px;
    background-color: {color};
    margin: auto;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
">
{pants_type}
</div>
""", unsafe_allow_html=True)

# ---------------------------
# 저장 기능
# ---------------------------
if st.button("💾 이 코디 저장하기"):
    outfit = f"{pants_type} / {fit} / {occasion} / {color}"
    st.session_state.saved_outfits.append(outfit)
    st.success("저장되었습니다!")

# ---------------------------
# 저장 목록
# ---------------------------
if st.session_state.saved_outfits:
    st.markdown("### 📌 저장된 코디")
    for i, o in enumerate(st.session_state.saved_outfits, 1):
        st.write(f"{i}. {o}")
