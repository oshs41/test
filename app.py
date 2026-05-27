import streamlit as st
from google import genai
from google.genai import types
from google.genai.errors import APIError

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="설렘 가득 연애 상담소", page_icon="💖", layout="centered")
st.title("💖 설렘 가득 연애 상담소")
st.caption("연애 고민, 썸, 이별... 혼자 끙끙 앓지 말고 제미나이 언니/오빠에게 물어보세요!")

# 2. Streamlit Secrets에서 API 키 불러오기 및 클라이언트 초기화
if "GEMINI_API_KEY" not in st.secrets:
    st.error(".streamlit/secrets.toml 파일에 'GEMINI_API_KEY'가 설정되지 않았습니다. 패널 측면의 설정을 확인해 주세요.")
    st.stop()

@st.cache_resource
def init_client():
    # 최신 google-genai 라이브러리 방식을 사용합니다.
    return genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

try:
    client = init_client()
except Exception as e:
    st.error(f"클라이언트 초기화 중 오류가 발생했습니다: {e}")
    st.stop()

# 3. 세션 상태(Session State)를 활용한 채팅 기록 유지
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. 이전 대화 기록 화면에 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. 사용자 입력 받기
if user_input := st.chat_input("연애 고민을 편하게 털어놓으세요..."):
    
    # 사용자 메시지 화면 표시 및 세션 저장
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 6. 제미나이 API 호출 및 답변 생성 (오류 처리 포함)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # 연애 상담사 페르소나 주입을 위한 시스템 지침(System Instruction) 설정
        system_instruction = (
            "당신은 공감 능력이 뛰어나고 다정한 연애 상담 전문가입니다. "
            "사용자의 연애 고민(썸, 연애, 이별 등)을 경청하고, 따뜻하게 위로하며, "
            "현실적이면서도 센스 있는 조언을 건네주세요. 친근하고 다정하게 대답해 주세요."
        )
        
        # 모델에 전달할 대화 내역 구성
        contents = []
        for msg in st.session_state.messages:
            role = "user" if msg["role"] == "user" else "model"
            contents.append(types.Content(
                role=role,
                parts=[types.Part.from_text(text=msg["content"])]
            ))

        try:
            with st.spinner("생각 중... 💬"):
                # 최신 gemini-2.5-flash-lite 모델 사용
                response = client.models.generate_content(
                    model='gemini-2.5-flash-lite',
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.7, # 창의적이고 공감대 높은 답변을 위해 0.7 설정
                    )
                )
            
            # 답변 출력 및 세션 저장
            ai_response = response.text
            message_placeholder.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            
        except APIError as e:
            # 구글 API 관련 에러 처리
            error_msg = f"구글 API 오류가 발생했습니다: {e.message} (코드: {e.code})"
            message_placeholder.error(error_msg)
        except Exception as e:
            # 기타 일반 에러 처리
            error_msg = f"예기치 못한 오류가 발생했습니다: {str(e)}"
            message_placeholder.error(error_msg)
