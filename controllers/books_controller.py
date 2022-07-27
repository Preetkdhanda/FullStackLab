from crypt import methods
from flask import Flask, render_template, redirect, request
from repositories import author_repository, book_repository
from models.book import Book
from models.author import Author
from flask import Blueprint

books_blueprint = Blueprint('books', __name__)

@books_blueprint.route('/books')
def books():
    book = book_repository.select_all()
    return render_template('books/index.html', book = book)
    
@books_blueprint.route('/books/<id>')
def show(id):
    book = book_repository.select(id)
    return render_template('/books/show.html', book=book)