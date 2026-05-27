import streamlit as st
from google import genai
from google.genai import types
from google.genai.errors import APIError

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="달콤살벌 연애상담소", page_icon="💖", layout="centered")
st.title("💖 달콤살벌 연애상담소")
st.caption("gemini-2.5-flash-lite 기반의 스마트한 연애 코치")

# 2. API 클라이언트 초기화 및 오류 처리
try:
    # streamlit secrets에서 API 키 로드
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except KeyError:
    st.error("❌ `.streamlit/secrets.toml` 파일에 'GEMINI_API_KEY'가 설정되지 않았습니다.")
    st.stop()
except Exception as e:
    st.error(f"❌ 초기화 중 오류가 발생했습니다: {e}")
    st.stop()

# 3. 챗봇의 페르소나(System Instruction) 설정
system_instruction = """
당신은 공감 능력이 뛰어나고 위트 있는 전문 연애 상담사입니다. 
사용자의 연애 고민에 대해 진솔하고 다정하게 답변해 주세요. 
필요할 때는 뼈 때리는(?) 현실적인 조언도 아끼지 마세요. 
답변은 친근한 말투(해요체 등)를 사용하고, 이모지를 적절히 섞어 가며 가독성 있게 작성해 주세요.
"""

# 4. 세션 상태(Session State)를 활용한 채팅 기록 유지
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! 당신의 연애 고민을 들어드릴게요. 무슨 일이 있으신가요? 🥰"}
    ]

# 5. 기존 채팅 기록 화면에 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. 사용자 입력 및 챗봇 응답 처리
if user_input := st.chat_input("고민을 이야기해 주세요..."):
    # 사용자 메시지 화면 표시 및 저장
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 챗봇 응답 생성 중 로딩 표시
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # 대화 맥락 유지를 위해 이전 기록을 Gemini 형식으로 변환
            # (단, system_instruction은 config로 따로 전달하므로 제외)
            history_contents = []
            for msg in st.session_state.messages[:-1]: # 현재 입력 제외한 과거 기록
                role = "model" if msg["role"] == "assistant" else "user"
                history_contents.append(types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=msg["content"])]
                ))
            
            # 현재 사용자 입력 추가
            history_contents.append(types.Content(
                role="user",
                parts=[types.Part.from_text(text=user_input)]
            ))

            # Gemini 2.5 Flash Lite 모델 호출
            response = client.models.generate_content(
                model='gemini-2.5-flash-lite',
                contents=history_contents,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.7, # 창의성 조절
                )
            )
            
            # 답변 출력 및 저장
            ai_response = response.text
            message_placeholder.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

        except APIError as e:
            # 구글 API 측 에러 처리 (한도 초과, 서버 다운 등)
            error_msg = f"⚠️ Gemini API 오류가 발생했습니다: {e.message}"
            message_placeholder.error(error_msg)
        except Exception as e:
            # 기타 시스템 에러 처리
            error_msg = f"⚠️ 알 수 없는 오류가 발생했습니다: {str(e)}"
            message_placeholder.error(error_msg)
