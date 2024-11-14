from fastapi import APIRouter
from chroma.database import chroma_db
from pydantic import BaseModel


class Document(BaseModel):
    page_content: str


router = APIRouter(
    prefix="/database",
    responses={404: {"description": "Not found"}},
)


@router.post("/add-document")
async def add_document(document: Document):
    return {
        "message": "Document added successfully",
        "document": chroma_db.add_documents(
            [Document(page_content=document.page_content)]
        ),
    }


@router.get("/search")
async def search(query: str):
    return chroma_db.search(query)