from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.models.contact_form import ContactFormDTO
from app.services.email_service import email_service

# Equivalent to @RestController + @RequestMapping("/api/contact")
router = APIRouter(tags=["contact"])


# Equivalent to @PostMapping("/send")
@router.post("/send")
async def send_contact_form(form_data: ContactFormDTO):
    try:
        email_service.send_contact_form_email(form_data)
        return {"message": "Message sent successfully!", "status": "success"}

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": "Failed to send message. Please try again.",
                "status": "error",
                "error": str(e),
            },
        )

