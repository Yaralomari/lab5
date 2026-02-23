from django.shortcuts import render


def index(request):
    return render(request, "bookmodule/index.html")


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def view_one_book(request, bookId):

    books = {
        1: {
            "title": "Internet & World Wide Web How to Program",
            "author": "author name",
            "image": "book1.jpg",
            "description": "provides a clear introduction to web programming."
        },
        2: {
            "title": "C++ How to Program",
            "author": "author name",
            "image": "book2.jpg",
            "description": "A comprehensive guide to C++ programming."
        },
        3: {
            "title": "Images in Another Folder",
            "author": "author name",
            "image": "book3.jpg",
            "description": "Example book demonstrating images."
        }
    }

    book = books.get(bookId)

    return render(request, "bookmodule/one_book.html", {
        "book": book
    })


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")