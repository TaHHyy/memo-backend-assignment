import os                                       # 환경변수를 읽기 위해 추가
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ── CORS: 허용할 프론트 주소를 환경변수(ALLOWED_ORIGINS)에서 읽는다 ──
# 로컬에서는 환경변수가 없으니 기본값(5173)이 쓰이고, 배포 시에는 Vercel 주소를 넣는다.
origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],      # GET, POST, DELETE 등 모두 허용
    allow_headers=["*"],
)

# ── 주고받을 데이터의 모양 (Pydantic) ──
class MemoIn(BaseModel):     # 요청 본문: 클라이언트가 보내는 데이터
    content: str
class MemoOut(BaseModel):    # 응답 본문: 서버가 돌려주는 데이터
    id: int
    content: str

# ── 인메모리 저장소 (리스트에 저장 → 서버 끄면 사라짐) ──
# 서버가 다시 시작되면 목록이 비므로, 안내용 기본 메모 하나를 미리 넣어 둔다.
memos: list[dict] = [{"id": 1, "content": "위 링크를 클릭하시면 개인 소개 페이지가 보입니다."}]
next_id = 2

@app.get("/memos", response_model=list[MemoOut])
def list_memos():
    return memos

@app.post("/memos", response_model=MemoOut)
def create_memo(memo: MemoIn):
    global next_id
    new = {"id": next_id, "content": memo.content}
    memos.append(new)
    next_id += 1
    return new

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    global memos
    for m in memos:
        if m["id"] == memo_id:
            memos = [x for x in memos if x["id"] != memo_id]
            return {"ok": True}
    raise HTTPException(status_code=404, detail="Memo not found")
