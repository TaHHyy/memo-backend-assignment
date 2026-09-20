# 메모장 백엔드 API (FastAPI)

KAIST 클라우드컴퓨팅실습 개인과제의 백엔드입니다. 프론트엔드는 [memo-frontend-assignment](https://github.com/TaHHyy/memo-frontend-assignment) 저장소를 참고하세요. 프로젝트 소개, 배포 주소는 그 저장소의 README에 정리했습니다.

## 주요 구성

| 메서드 | 경로 | 설명 |
|---|---|---|
| GET | `/memos` | 메모 목록 조회 |
| POST | `/memos` | 메모 생성 (본문: `{"content": "..."}`) |
| DELETE | `/memos/{memo_id}` | 메모 삭제 (없으면 404) |

- 메모는 서버 메모리(리스트)에 저장되어, 서버가 재시작되면 초기화됩니다. 초기화 후에도 안내용 기본 메모 1개는 들어 있습니다.
- CORS 허용 출처는 환경변수 `ALLOWED_ORIGINS`(쉼표로 구분)로 지정하며, 없으면 `http://localhost:5173`입니다.
- Swagger UI: 배포 주소의 `/docs`

## 배포 (Render)

| 항목 | 값 |
|---|---|
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |
| Environment Variables | `ALLOWED_ORIGINS` = Vercel 배포 주소 (끝에 `/` 없이) |

## 로컬 실행 방법

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
fastapi dev main.py           # http://127.0.0.1:8000/docs
```
