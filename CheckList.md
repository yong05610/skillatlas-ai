# SkillAtlas AI 구현/검증 체크리스트

작성일: 2026-09-06

배포 URL: https://skillatlas-ai-sigma.vercel.app

## 1. 현재 완료 상태

### 프로젝트 구조

- [x] `index.html` 생성 및 구현
- [x] `css/style.css` 생성 및 구현
- [x] `js/main.js` 생성 및 구현
- [x] `api/generate-roadmap.py` 생성 및 구현
- [x] `README.md` 작성
- [x] `SERVICE_PLAN.md` 유지
- [x] `requirements.txt` 작성
- [x] `images/` 폴더 유지용 `.gitkeep` 생성
- [x] 테스트용 `api/hello.py` 제거
- [x] 테스트용 `js/app.js` 제거

### 화면 구성

- [x] 단일 페이지 웹서비스 구현
- [x] Home 섹션 구현
- [x] About 섹션 구현
- [x] Roadmap AI 섹션 구현
- [x] Resources 섹션 구현
- [x] FAQ 섹션 구현
- [x] Footer 구현
- [x] 상단 네비게이션에서 각 섹션으로 이동 가능
- [x] Hero 영역에 서비스명, 핵심 문구, CTA 버튼 포함

### Roadmap AI 입력 폼

- [x] 현재 수준 입력
- [x] 목표 입력
- [x] 학습 기간 입력
- [x] 학습 가능 시간 입력
- [x] 관심 분야 입력
- [x] 추가 요청사항 입력
- [x] 필수 입력값 지정: 현재 수준, 목표, 학습 기간, 학습 가능 시간
- [x] 선택 입력값 지정: 관심 분야, 추가 요청사항
- [x] 프론트엔드 필수 입력 누락 검증
- [x] 백엔드 필수 입력 누락 검증
- [x] 너무 긴 입력값 제한 처리

### 프론트엔드 동작

- [x] HTML, CSS, JavaScript만 사용
- [x] `fetch("/api/generate-roadmap")`로 POST 요청
- [x] 요청 중 로딩 메시지 표시
- [x] 요청 중 버튼 비활성화로 중복 클릭 방지
- [x] 응답 수신 후 결과 영역에 로드맵 표시
- [x] AI 응답을 `innerHTML`이 아니라 `textContent`로 삽입
- [x] 결과 영역에 `white-space: pre-wrap` 적용
- [x] Markdown 응답을 HTML로 변환하지 않고 텍스트 그대로 표시

### 백엔드/API

- [x] Vercel Python Serverless Function으로 구현
- [x] `POST /api/generate-roadmap` 엔드포인트 구현
- [x] 요청 Body: `level`, `goal`, `duration`, `studyTime`, `interests`, `extra`
- [x] 성공 응답 형식: `{ "result": "..." }`
- [x] 실패 응답 형식: `{ "error": "..." }`
- [x] 백엔드 필수 입력값 검증
- [x] Gemini API 호출을 백엔드에서만 수행
- [x] `GET /api/generate-roadmap` 요청은 405로 제한

### Gemini/API Key 보안

- [x] Gemini API 사용
- [x] API Key는 `GEMINI_API_KEY` 환경 변수에서만 읽음
- [x] API Key를 프론트엔드 코드에 노출하지 않음
- [x] `.env`, `.env.local`, `.vercel` Git 제외 설정
- [x] API Key 미설정/오류 상황에서 사용자에게 일반 오류 메시지만 반환
- [x] 내부 오류 상세, 스택 트레이스, 환경 변수명, API Key 정보, Gemini 원본 오류 메시지를 사용자 응답에 노출하지 않음

### AI 프롬프트/응답

- [x] AI 역할: IT-AI 학습 로드맵 전문 코치
- [x] 한국어 응답 지시
- [x] 사용자 수준에 맞는 쉬운 설명 지시
- [x] 15개 학습 영역 기준 반영
- [x] 추천 학습 순서 포함 지시
- [x] 기간별/단계별 학습 계획 포함 지시
- [x] 추천 학습 자료 URL 포함 지시
- [x] 실습 프로젝트 아이디어 최소 1개 포함 지시
- [x] 취업/수익/자격 보장 표현 금지 지시
- [x] 마지막에 바로 실행 가능한 다음 액션 포함 지시

### Resources 섹션

- [x] roadmap.sh
- [x] MDN Web Docs
- [x] JavaScript.info
- [x] Python 공식 튜토리얼
- [x] Google Python Class
- [x] Kaggle Learn
- [x] Git 공식 문서
- [x] GitHub Docs
- [x] Vercel Docs
- [x] Google ML Crash Course
- [x] scikit-learn User Guide
- [x] DeepLearning.AI
- [x] Gemini API Docs
- [x] Hugging Face Learn
- [x] LangChain Docs
- [x] OWASP Top 10

### UI/반응형

- [x] 밝고 깔끔한 학습 플랫폼 느낌
- [x] 블루/퍼플 계열 포인트 컬러 사용
- [x] 카드형 레이아웃 사용
- [x] 섹션 간 여백 적용
- [x] 초보자도 이해하기 쉬운 UI 문구 적용
- [x] 데스크톱 중앙 정렬 레이아웃
- [x] 데스크톱 네비게이션 가로 표시
- [x] 모바일에서 섹션 세로 배치
- [x] 모바일에서 입력 폼 한 줄씩 표시
- [x] 모바일에서 버튼 화면 너비 대응
- [x] 결과 텍스트 가로 넘침 방지 스타일 적용

### README

- [x] 서비스 소개 포함
- [x] 주요 기능 포함
- [x] 기술 스택 포함
- [x] 프로젝트 구조 포함
- [x] 실행 방법 포함
- [x] 환경 변수 `GEMINI_API_KEY` 설명 포함
- [x] GitHub/Vercel 배포 방법 포함
- [x] AI 기능 설명 포함
- [x] 배포 URL 작성 완료

### 배포/GitHub

- [x] Vercel 프로덕션 배포 완료
- [x] `https://skillatlas-ai-sigma.vercel.app` alias 적용 확인
- [x] 배포 URL에서 새 SkillAtlas AI 화면 응답 확인
- [x] 배포된 API에서 정상 입력 시 `200` 응답 확인
- [x] 최신 구현 커밋 완료
- [x] GitHub `main` 브랜치 푸시 완료

## 2. 수행한 검증

- [x] `node --check js/main.js` 통과
- [x] Vercel CLI 임시 실행 확인: `59.11.7`
- [x] `vercel dev` 로컬 서버 기동 확인: `http://127.0.0.1:3000`
- [x] `/` 정적 페이지 `200 OK`
- [x] `/css/style.css` `200 OK`
- [x] `/js/main.js` `200 OK`
- [x] Python Serverless Function Vercel dev 빌드 성공
- [x] 빈 POST 요청 시 `400`과 일반 오류 메시지 반환
- [x] 잘못된 JSON 요청 시 `400`과 일반 오류 메시지 반환
- [x] 너무 긴 입력 요청 시 `400`과 일반 오류 메시지 반환
- [x] GET 요청 시 `405` 반환
- [x] 정상 입력 요청 시 실제 Gemini 연동 성공 및 `200` 반환
- [x] 배포 URL에서 HTML 최신 내용 확인
- [x] 배포 URL의 API 정상 입력 요청 `200` 확인
- [x] 정적 점검 스크립트로 다음 조건 확인:
  - [x] 필수 섹션 존재
  - [x] `fetch("/api/generate-roadmap")` 사용
  - [x] `textContent` 사용
  - [x] `innerHTML` 미사용
  - [x] `white-space: pre-wrap` 적용
  - [x] 반응형 media query 존재
  - [x] 프론트엔드 API Key 미노출
  - [x] 백엔드에서 `GEMINI_API_KEY` 사용

## 3. 환경 문제로 직접 처리/검증하지 못한 사항

아래 항목은 프로젝트 코드 문제라기보다 현재 로컬/실행 환경 문제로 보입니다. 환경 지원 스레드에서 정리하면 좋습니다.

### Python 직접 실행 상태 (해결 완료)

- [x] `python --version` 정상 실행 (Python 3.14.7 확인)
- [x] `python -m py_compile api/generate-roadmap.py` 구문 검사 성공 (정상 통과)

### PowerShell npm 실행 정책 문제

- [x] `npm.cmd --version` 정상 동작 (11.17.0)
- [x] `npx.cmd` 정상 동작
- [ ] PowerShell Execution Policy 설정 (`Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` 권장)

### Vercel CLI 전역 명령

- [ ] `vercel` 전역 명령 미설치 상태
- [x] 대안인 `npx.cmd vercel`을 통해 빌드/배포 정상 동작 확인 완료
- [ ] 필요시 `npm.cmd install -g vercel` 설치 권장

### 이미지 및 UI 에셋 개선 사항

- [ ] `images/` 폴더 내 서비스 스크린샷 또는 대표 썸네일/파비콘 에셋 추가
- [ ] Open Graph 메타 태그(`og:image`) 및 파비콘(`favicon.ico`) 적용 검토

## 4. 현재 남은 작업

- [ ] 사용자가 실제 브라우저에서 `https://skillatlas-ai-sigma.vercel.app` 접속 확인
- [ ] 실제 브라우저 개발자 도구에서 375px/390px 모바일 화면 최종 육안 확인
- [ ] 환경 설정 (PowerShell 실행 정책 / 전역 Vercel CLI 설치)
- [ ] 대표 이미지/파비콘 에셋 제작 및 적용

## 5. 참고 메모

- 배포는 완료됐고 URL은 최신 화면을 반환합니다.
- 배포된 API는 정상 입력으로 Gemini 응답을 반환했습니다.
- `.env`, `.env.local`, `.vercel`은 Git 제외 대상입니다.
- `CheckList.md`는 현재 로컬 작업 파일이며 아직 GitHub에 커밋하지 않았습니다.

