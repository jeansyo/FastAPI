from fastapi import APIRouter, Depends, status
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.post('/')
def create(request:schemas.Blog, db:Session = Depends(get_db)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session = Depends(get_db)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db:Session = Depends(get_db)):
    return blog.update(id, request, db)


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)


@router.get('/{id}', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def show(id:int, db: Session = Depends(get_db)):
    return blog.get_show(id, db)

