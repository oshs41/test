import streamlit as st
import random

# -----------------------------
# 상의 중심 코디 데이터
# -----------------------------
coordi_db = {
    "캐주얼": {
        "흰 티": {
            "하의": ["청바지", "조거팬츠", "반바지"],
            "아우터": ["가디건", "바람막이", "없음"]
        },
        "후드티": {
            "하의": ["조거팬츠", "청바지"],
            "아우터": ["없음", "바람막이"]
        },
        "맨투맨": {
            "하의": ["청바지", "조거팬츠"],
            "아우터": ["가디건", "없음"]
        }
    },

    "스트릿": {
        "그래픽 티": {
            "하의": ["와이드 팬츠", "카고 팬츠"],
            "아우터": ["바람막이", "후드 집업", "없음"]
        },
        "오버핏 티": {
            "하의": ["와이드 팬츠", "조거팬츠"],
            "아우터": ["없음", "바람막이"]
        }
    },

    "포멀": {
        "셔츠": {
            "하의": ["슬랙스", "면바지"],
            "아우터": ["자켓", "없음"]
        },
        "니트": {
            "하의": ["슬랙스", "청바지"],
            "아우터": ["코트", "자켓"]
        }
    }
}

# -----------------------------
# 추천 함수
# -----------------------------
def make_outfit(style, top, weather):
    try:
        style_data = coordi_db.get(style, {})

        if top not in style_data:
            return None, None, "선택한 상의에 대한 데이터가 없습니다."

        bottom = random.choice(style_data[top]["하의"])
        outer = random.choice(style_data[top]["아우터"])

        # 날씨 보정
        if weather == "더움":
            outer = "없음"
        elif weather == "추움" and outer == "없음":
            outer = "자켓"

        return bottom, outer, None

    except Exception as e:
        return None, None, str(e)

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="상의 중심 코디 앱", page_icon="👕")

st.title("👕 상의 중심 코디 추천 앱")
st.write("상의 하나를 선택하면 전체 코디를 완성해드립니다.")

# 입력
style = st.selectbox("스타일 선택", list(coordi_db.keys()))

top = st.selectbox(
    "상의 선택",
    list(coordi_db[style].keys())
)

weather = st.selectbox("날씨", ["더움", "보통", "추움"])

# 실행
if st.button("코디 완성하기"):
    bottom, outer, error = make_outfit(style, top, weather)

    st.subheader("🎯 코디 결과")

    if error:
        st.error(error)
    else:
        st.success(f"상의: {top}")
        st.success(f"하의: {bottom}")
        st.success(f"아우터: {outer}")

        # 스타일 설명
        if style == "캐주얼":
            st.info("👉 편안하고 자연스러운 스타일")
        elif style == "스트릿":
            st.info("👉 트렌디하고 개성 있는 스타일")
        else:
            st.info("👉 깔끔하고 단정한 스타일")

st.divider()
st.caption("Top-based Outfit Styler App 👕")
