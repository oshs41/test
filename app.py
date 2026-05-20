import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="운동 기록 앱", page_icon="💪")

st.title("💪 운동 기록 앱")

# 세션 상태 초기화
if "workouts" not in st.session_state:
    st.session_state.workouts = []

# 입력 폼
with st.form("workout_form"):
    workout_date = st.date_input("날짜", value=date.today())

    workout_type = st.selectbox(
        "운동 종류",
        ["러닝", "헬스", "수영", "자전거", "요가", "기타"]
    )

    duration = st.number_input(
        "운동 시간 (분)",
        min_value=0,
        step=10
    )

    memo = st.text_area("메모")

    submitted = st.form_submit_button("기록 저장")

# 저장
if submitted:
    st.session_state.workouts.append({
        "날짜": workout_date,
        "운동": workout_type,
        "시간(분)": duration,
        "메모": memo
    })

    st.success("운동 기록 저장 완료!")

# 데이터 표시
if st.session_state.workouts:
    st.subheader("📋 운동 기록")

    df = pd.DataFrame(st.session_state.workouts)

    st.dataframe(df, use_container_width=True)

    # 간단 통계
    total_time = df["시간(분)"].sum()

    st.metric("총 운동 시간", f"{total_time} 분")
else:
    st.info("아직 운동 기록이 없습니다.")
