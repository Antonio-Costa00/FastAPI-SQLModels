from typing import List

from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from sqlmodel import Session
from sqlmodel.sql.expression import select

from database import engine
from models import Book

app = FastAPI()

session = Session(bind=engine)


@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    statement = select(Book).where(Book.id == book_id)

    result = session.exec(statement).first()

    if result != None:
        return result

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.get(
    "/books",
    response_model=List[Book],
    status_code=status.HTTP_200_OK,
)
async def get_all_books():
    statement = select(Book)
    results = session.exec(statement).all()

    return results


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    new_book = Book(title=book.title, description=book.description)
    session.add(new_book)
    session.commit()

    return new_book


@app.put("/book/{book_id}", response_model=Book)
async def get_book(book_id: int, book: Book):
    statement = select(Book).where(Book.id == book_id)

    result = session.exec(statement).first()

    if result != None:

        result.title = book.title
        result.description = book.description

        session.commit()

        return result

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    statement = select(Book).where(Book.id == book_id)

    result = session.exec(statement).one_or_none()

    if result != None:
        session.delete(result)
        session.commit()

        return result

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
