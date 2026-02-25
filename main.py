from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import contact
from app.core.config import settings

print("MAIL USER:", settings.MAIL_USERNAME)
print("MAIL PASS:", settings.MAIL_PASSWORD[:4] + "****")

app = FastAPI(title="Tissues API")

# CORS Configuration (equivalent to CorsConfig.java)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://niyara.vercel.app",
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contact.router, prefix="/api/contact")


@app.get("/")
def root():
    return {"status": "Tissues API is running"}
