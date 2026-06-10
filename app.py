import streamlit as st
import pandas as pd
import plotly.express as px
import google.generativeai as genai
from datetime import datetime

# 1. 페이지 기본 설정 및 테마
st.set_page_config(
    page_title="스마트 AI 데일리 플래너",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Gemini API 세팅 및 예외 처리
ai_available = False
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # 가볍고 빠른 gemini-2.5-flash-lite 모델 지정
        model = genai.GenerativeModel('gemini-2.5-flash-lite')
        ai_available = True
    except Exception as e:
        st.sidebar.error(f"AI 모델 로드 실패: {e}")
else:
    st.sidebar.warning("⚠️ 세크리트(Secrets)에 'GEMINI_API_KEY'를 등록하면 AI 코칭 기능을 사용할 수 있습니다.")

# 3. 데이터 및 상태 초기화 (Session State)
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"할일": "Streamlit 플래너 앱 만들기", "카테고리": "개발/공부", "우선순위": "높음", "완료": True},
        {"할일": "깃허브에 코드 푸시하기", "카테고리": "개발/공부", "우선순위": "높음", "완료": False},
        {"할일": "물 2리터 마시기", "카테고리": "건강/라이프", "우선순위": "보통", "완료": False},
    ]

# 4. 사이드바 - 오늘 나의 다짐 & AI 피드백
st.sidebar.header("🎯 오늘의 다짐 & AI 코칭")
today_quote = st.sidebar.text_area("오늘의 한 줄 다짐이나 목표를 적어보세요:", "오늘 하루도 알차고 생산성 있게 보내기!")

if st.sidebar.button("🤖 AI에게 응원받기"):
    if ai_available:
        with st.sidebar.spinner("AI 라이프 코치가 분석 중..."):
            try:
                prompt = f"사용자의 오늘 다짐: '{today_quote}'. 이 다짐을 한 사람에게 동기부여를 줄 수 있는 따뜻하고 명확한 조언과 행동 팁 3가지를 짤막하게 작성해줘."
                response = model.generate_content(prompt)
                st.sidebar.success("💡 AI 코치의 메시지")
                st.sidebar.info(response.text)
            except Exception as e:
                st.sidebar.error(f"AI 요청 중 오류가 발생했습니다: {e}")
    else:
        st.sidebar.info("API 키가 설정되지 않아 기본 응원을 보냅니다: '오늘도 파이팅입니다! 할 수 있어요!'")

# 5. 메인 화면 - 헤더 영역
st.title("📅 스마트 AI 데일리 플래너 & 트래커")
st.markdown(f"**오늘은 {datetime.now().strftime('%Y년 %m월 %d일')} 입니다.** 목표를 달성하고 시각화된 통계를 확인하세요!")
st.write("---")

# 6. 메인 화면 - 할 일 추가 레이아웃 (3
