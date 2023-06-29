from videos_maker.main import create_tiktok_video
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VideoContent(BaseModel):
    title: str
    description: str


@app.get('/api')
async def hello_api():
    return "Hello World from API"


@app.post('/api/video')
async def create_video(item: VideoContent):

    title = item.title
    text = item.description

    create_tiktok_video(title, text)

    return {'message': 'Video created with success'}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
