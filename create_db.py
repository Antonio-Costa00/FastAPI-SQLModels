from sqlmodel import Session, SQLModel

from database import engine
from models import Book

print("Creating database...")

# book_1 = Book(
#     title="The Lord of the Rings",
#     description="The Lord of the Rings is an epic high fantasy novel written by English author and scholar J. R. R. Tolkien.",
# )
# book_2 = Book(
#     title="The Hobbit",
#     description="The Hobbit, or There and Back Again, is a children's fantasy novel written by English author and scholar J. R. R. Tolkien.",
# )
# book_3 = Book(
#     title="The Catcher in the Rye",
#     description="The Catcher in the Rye is a 1951 novel by J. D. Salinger. It was published in 1951 and is considered one of his best works.",
# )
# book_4 = Book(
#     title="The Grapes of Wrath",
#     description="The Grapes of Wrath is a novel by John Steinbeck, published in 1939. It is considered one of his best works and is considered one of America's best-loved novels.",
# )
# book_5 = Book(
#     title="The Great Gatsby",
#     description="The Great Gatsby is a 1925 novel written by American author F. Scott Fitzgerald. It follows the experiences of the fabulously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan, of whom he is unaware.",
# )

# SQLModel.metadata.create_all(engine)

# with Session() as session:
#     session.add(book_1)
#     session.add(book_2)
#     session.add(book_3)
#     session.add(book_4)
#     session.add(book_5)
#     session.commit()
