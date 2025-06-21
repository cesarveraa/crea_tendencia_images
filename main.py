# main.py
from fastapi import FastAPI
from routers.images import router as images_router

app = FastAPI(title="Image Uploader")

app.include_router(images_router, prefix="/images", tags=["images"])
