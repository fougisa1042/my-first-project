from fastapi import FastAPI
import random

# FastAPI 인스턴스를 생성합니다.
# app 객체는 라우트(endpoint)와 핸들러 함수를 등록하는 데 사용됩니다.
app = FastAPI()

# 기본 경로('/') 요청 시 응답하는 핸들러 함수입니다.
# 브라우저에서 http://127.0.0.1:8000 으로 접속하면 이 함수가 실행됩니다.
@app.get("/")
def read_root():
    # 딕셔너리 형태로 JSON 응답을 반환합니다.
    return {"message": "Welcome to DevProfileAPI"}

# '/profile' 경로로 GET 요청을 하면 아래 함수가 실행됩니다.
# 이 함수는 가상의 개발자 프로필 정보를 JSON으로 반환합니다.
@app.get("/profile")
def get_profile():
    # 향후에는 DB나 별도 파일에서 데이터를 가져올 수 있지만,
    # 지금은 예제용으로 하드코딩한 딕셔너리를 사용합니다.
    profile_data = {
        "name": "정명수",            # 개발자 이름
        "title": "Backend Developer",  # 직무/포지션
        "skills": ["Python", "FastAPI", "AWS", "Docker", "CI/CD"],  # 보유 기술 리스트
        "experience": {
            "years": 3,  # 경력 연수
            "notable_projects": ["Project A", "Project B"]  # 진행했던 대표 프로젝트
        },
        "contact": {
            "email": "fougisa1042@gmail.com",
            "linkedin": "https://www.linkedin.com/in/yourname"
        }
    }
    # JSON 형태로 반환되며, FastAPI가 자동으로 JSON 변환을 처리합니다.
    return profile_data

# '/random_tip' 경로로 GET 요청 시 실행되는 함수입니다.
# 개발 관련 랜덤 팁을 하나 반환합니다.
@app.get("/random_tip")
def random_tip():
    # 임의의 개발 팁 목록
    tips = [
        "Write tests for your code to ensure reliability.",
        "Keep functions small and focused on a single task.",
        "Use version control (Git) for all your projects.",
        "Document your code and APIs for better maintainability.",
        "Learn about cloud-native deployments and scaling."
    ]
    # random.choice를 사용해 tips 리스트 중 하나를 랜덤하게 선택합니다.
    selected_tip = random.choice(tips)
    # {"tip": "..."} 형태의 딕셔너리를 반환하며, 자동으로 JSON 응답으로 변환됩니다.
    return {"tip": selected_tip}
