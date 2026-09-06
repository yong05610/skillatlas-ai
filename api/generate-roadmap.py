from http.server import BaseHTTPRequestHandler
import json
import os
import urllib.error
import urllib.request


GENERIC_ERROR = "로드맵 생성 중 문제가 발생했습니다. 잠시 후 다시 시도해주세요."
MISSING_INPUT_ERROR = "필수 항목을 입력한 후 다시 시도해주세요."

SYSTEM_PROMPT = """
당신은 IT-AI 분야 학습 로드맵을 설계하는 전문 학습 코치입니다.
사용자의 현재 수준, 목표, 학습 기간, 학습 가능 시간, 관심 분야를 바탕으로 현실적인 학습 계획을 제안하세요.

반드시 다음 원칙을 지키세요.
1. 사용자의 수준에 맞는 쉬운 설명을 사용합니다.
2. 다음 15개 학습 영역 중 사용자에게 필요한 영역을 선별합니다.
   - IT 기초
   - HTML/CSS/JavaScript
   - Python/JavaScript 프로그래밍
   - Git/GitHub
   - 백엔드 API
   - 데이터베이스
   - 배포/클라우드
   - CS 기초
   - 데이터 분석
   - 머신러닝
   - 딥러닝
   - 생성형 AI/LLM
   - MLOps/LLMOps
   - 보안/윤리
   - 포트폴리오
3. 학습 순서를 단계별로 제시합니다.
4. 사용자의 학습 기간에 맞춰 주차별 또는 단계별 계획을 제시합니다.
5. 추천 학습 자료 URL을 포함합니다.
6. 실습 프로젝트 아이디어를 최소 1개 이상 제안합니다.
7. 취업 보장, 수익 보장, 자격 보장 같은 과장된 표현은 피합니다.
8. 한국어로 답변합니다.
9. 출력은 읽기 쉬운 Markdown 섹션 형태로 구성합니다.
10. 사용자가 바로 실천할 수 있는 다음 액션을 마지막에 제시합니다.

출력 형식:
# 맞춤형 학습 로드맵

## 1. 학습 방향 요약
## 2. 추천 학습 순서
## 3. 기간별 학습 계획
## 4. 추천 학습 자료
## 5. 실습 프로젝트 아이디어
## 6. 주의사항
## 7. 다음 액션
""".strip()

RESOURCES = """
- roadmap.sh: https://roadmap.sh/
- MDN Web Docs: https://developer.mozilla.org/ko/
- JavaScript.info: https://javascript.info/
- Python 공식 튜토리얼: https://docs.python.org/3/tutorial/
- Google Python Class: https://developers.google.com/edu/python
- Kaggle Learn: https://www.kaggle.com/learn
- Git 공식 문서: https://git-scm.com/book/ko/v2
- GitHub Docs: https://docs.github.com/ko
- Vercel Docs: https://vercel.com/docs
- Google Machine Learning Crash Course: https://developers.google.com/machine-learning/crash-course
- scikit-learn User Guide: https://scikit-learn.org/stable/user_guide.html
- DeepLearning.AI: https://www.deeplearning.ai/
- Gemini API Docs: https://ai.google.dev/gemini-api/docs
- Hugging Face Learn: https://huggingface.co/learn
- LangChain Docs: https://python.langchain.com/docs/introduction/
- OWASP Top 10: https://owasp.org/www-project-top-ten/
""".strip()


def json_response(handler, status, payload):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Cache-Control", "no-store")
    handler.end_headers()
    handler.wfile.write(body)


def read_json_body(handler):
    content_length = int(handler.headers.get("Content-Length", "0"))
    if content_length <= 0 or content_length > 12000:
        return None

    raw_body = handler.rfile.read(content_length)
    return json.loads(raw_body.decode("utf-8"))


def clean_text(value, limit):
    text = str(value or "").strip()
    return text[:limit]


def validate_payload(payload):
    required = ["level", "goal", "duration", "studyTime"]
    if not isinstance(payload, dict):
        return False

    for field in required:
        if not clean_text(payload.get(field), 120):
            return False

    if len(str(payload.get("interests", ""))) > 200:
        return False
    if len(str(payload.get("extra", ""))) > 500:
        return False

    return True


def build_user_prompt(payload):
    return f"""
다음 사용자 정보를 바탕으로 IT-AI 맞춤형 학습 로드맵을 생성해주세요.

현재 수준: {clean_text(payload.get("level"), 120)}
목표: {clean_text(payload.get("goal"), 120)}
학습 기간: {clean_text(payload.get("duration"), 120)}
학습 가능 시간: {clean_text(payload.get("studyTime"), 120)}
관심 분야: {clean_text(payload.get("interests"), 200) or "없음"}
추가 요청사항: {clean_text(payload.get("extra"), 500) or "없음"}

가능하면 아래 참고 자료 중 적절한 자료를 골라 추천해주세요.

참고 자료:
{RESOURCES}

위 정보를 바탕으로 사용자가 바로 실천할 수 있는 현실적인 학습 계획을 제안해주세요.
추천 자료는 가능한 한 제공된 참고 자료 목록에서 선택해주세요.
""".strip()


def call_gemini(payload):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Gemini API key is not configured.")
        return None

    model = "gemini-3.7-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    request_body = {
        "systemInstruction": {
            "parts": [{"text": SYSTEM_PROMPT}]
        },
        "contents": [
            {
                "role": "user",
                "parts": [{"text": build_user_prompt(payload)}]
            }
        ],
        "generationConfig": {
            "maxOutputTokens": 3000
        }
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(request_body, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=35) as response:
            response_body = json.loads(response.read().decode("utf-8"))

        candidates = response_body.get("candidates") or []
        parts = candidates[0].get("content", {}).get("parts", []) if candidates else []
        text = parts[0].get("text", "").strip() if parts else ""
        return text or None
    except urllib.error.HTTPError as error:
        print(f"Gemini HTTP error status: {error.code}")
        return None
    except Exception as error:
        print(f"Roadmap generation failed: {type(error).__name__}")
        return None


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            payload = read_json_body(self)
        except Exception:
            json_response(self, 400, {"error": MISSING_INPUT_ERROR})
            return

        if not validate_payload(payload):
            json_response(self, 400, {"error": MISSING_INPUT_ERROR})
            return

        result = call_gemini(payload)
        if not result:
            json_response(self, 500, {"error": GENERIC_ERROR})
            return

        json_response(self, 200, {"result": result})

    def do_GET(self):
        json_response(self, 405, {"error": "지원하지 않는 요청입니다."})
