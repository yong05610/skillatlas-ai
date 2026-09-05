from http.server import BaseHTTPRequestHandler
import os
import json
import urllib.request
import urllib.error


def call_gemini(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

    if not api_key:
        return None, "GEMINI_API_KEY 환경변수가 설정되지 않았습니다."

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))

        candidates = result.get("candidates", [])
        if not candidates:
            return None, f"Gemini 응답이 비어 있습니다: {result}"

        content = candidates[0].get("content", {})
        parts = content.get("parts", [])
        if not parts:
            return None, f"Gemini 응답 parts가 없습니다: {result}"

        text = parts[0].get("text", "")
        if not text:
            return None, f"Gemini 텍스트 응답이 없습니다: {result}"

        return text, None

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="ignore")
        return None, f"Gemini API HTTP 오류: {e.code}\n{error_body}"

    except Exception as e:
        return None, f"Gemini 호출 중 오류: {str(e)}"


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        prompt = (
            "This is a SkillAtlas AI connection test. "
            "Please reply in Korean with one short sentence saying that the Gemini connection works."
        )

        text, error = call_gemini(prompt)

        if error:
            self.send_response(500)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(error.encode("utf-8"))
            return

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(text.encode("utf-8"))