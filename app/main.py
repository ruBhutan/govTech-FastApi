from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND

from .crud import get_all_students, get_student_by_id, create_student, update_student, delete_student
from .citizen import fetch_citizen_details

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

# Other CRUD routes remain unchanged


@app.get("/citizen/")
async def get_citizen_form(request: Request):
    return templates.TemplateResponse("citizen.html", {"request": request})


@app.post("/citizen/")
async def fetch_citizen(request: Request, cid: str = Form(...)):
    citizen_details = await fetch_citizen_details(cid)
    return templates.TemplateResponse("citizen.html", {"request": request, "citizen": citizen_details})
