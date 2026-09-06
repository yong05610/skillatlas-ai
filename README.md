# SkillAtlas AI

SkillAtlas AI는 사용자의 현재 수준, 목표, 학습 기간, 관심 분야를 바탕으로 IT-AI 맞춤형 학습 로드맵을 생성하는 AI 기반 웹서비스입니다.

## 주요 기능

- 사용자 입력 기반 학습 로드맵 생성
- Gemini API를 활용한 맞춤형 추천
- 추천 학습 자료 URL 제공
- 실습 프로젝트 아이디어 제공
- 반응형 웹 UI
- 로딩, 입력 검증, 일반 오류 안내 처리

## 기술 스택

- HTML
- CSS
- JavaScript
- Python
- Vercel Serverless Functions
- Gemini API

## 프로젝트 구조

```text
skillatlas-ai/
├── index.html
├── README.md
├── SERVICE_PLAN.md
├── requirements.txt
├── css/
│   └── style.css
├── js/
│   └── main.js
├── api/
│   └── generate-roadmap.py
└── images/
    ├── .gitkeep
    ├── logo-icon.jpg
    └── og-thumbnail.jpg
```

## 실행 방법

정적 화면은 `index.html`을 브라우저에서 열어 확인할 수 있습니다.

API까지 함께 확인하려면 Vercel 개발 환경에서 실행합니다.

```powershell
vercel dev
```

## 환경 변수

Gemini API Key는 코드에 직접 작성하지 않고 서버 측 환경 변수로만 관리합니다.

```text
GEMINI_API_KEY=your_gemini_api_key
```

`.env` 파일과 실제 API Key는 GitHub에 업로드하지 않습니다.

## 배포 방법

1. GitHub 저장소에 소스 코드를 업로드합니다.
2. Vercel에서 저장소를 연결합니다.
3. Vercel 프로젝트 환경 변수에 `GEMINI_API_KEY`를 등록합니다.
4. 배포 후 `/api/generate-roadmap` 서버리스 함수와 웹 화면을 확인합니다.

## AI 기능 설명

사용자가 현재 수준, 목표, 학습 기간, 학습 가능 시간, 관심 분야, 추가 요청사항을 입력하면 프론트엔드가 `/api/generate-roadmap`으로 요청을 보냅니다. Python 서버리스 함수는 서버 측 환경 변수로 Gemini API Key를 읽고 Gemini API를 호출한 뒤, Markdown 텍스트 형식의 학습 로드맵을 JSON으로 반환합니다.

AI 응답은 보안을 위해 HTML로 변환하지 않고 `textContent`로 화면에 표시합니다.

## 배포 URL

https://skillatlas-ai-sigma.vercel.app
