from django.db import connection
from contextlib import closing
from collections import OrderedDict
from rest_framework.exceptions import NotFound

def dictfetchall(cursor):
    #"Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def query_get_author_all():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM myapi_author""")
        authors = dictfetchall(cursor)
    return authors

def query_get_author_one():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM myapi_author WHERE """)
        authors = dictfetchall(cursor)
    return authors


def get_author_all():
    authors = query_get_author_all()
    items = []
    for data in authors:
        items.append(
            OrderedDict(
                {
                    "id": data['id'],
                    "first_name": data['first_name'],
                    "last_name": data['last_name'],
                    "age": data['age'],
                }
            )
        )
    return items

def get_book_all():
    books = query_get_book_all()
    items = []
    for data in books:
        items.append(
            OrderedDict(
                {
                    "id": data['id'],
                    "name": data['name'],
                    "category": {
                        "id": data['category_id'],
                        "name": data['category_name']
                    },
                    "author": {
                        "id": data['author_id'],
                        "first_name": data['first_name']
                    },
                    "description": data['description'],
                }
            )
        )
    return items


def get_book_one(book_id):
    book = query_get_book_one(book_id)
    return OrderedDict(
            {
                "id": book['id'],
                "name": book['name'],
                "category": {
                    "id": book['category_id'],
                    "name": book['category_name']
                },
                "author": {
                    "id": book['author_id'],
                    "first_name": book['first_name']
                },
                "description": book['description'],
            }
        )


def query_get_book_all():
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            """SELECT myapi_book.*, myapi_author.first_name, myapi_category.name as category_name FROM myapi_book
            INNER JOIN myapi_author ON myapi_book.author_id = myapi_author.id
            INNER JOIN myapi_category ON myapi_book.category_id = myapi_category.id""")
        books = dictfetchall(cursor)
    return books


def query_get_book_one(book_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT myapi_book.*, myapi_author.first_name, myapi_category.name as category_name FROM myapi_book
            INNER JOIN myapi_author ON myapi_book.author_id = myapi_author.id
            INNER JOIN myapi_category ON myapi_book.category_id = myapi_category.id WHERE myapi_book.id = %s""", [book_id])
        book = dictfetchone(cursor)
    return book

