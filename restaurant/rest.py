from fastapi import APIRouter, Depends
from core.utils import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/")
def post_list(db: Session = Depends(get_db)):
    return {}

