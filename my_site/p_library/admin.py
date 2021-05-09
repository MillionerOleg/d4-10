from django.contrib import admin
from p_library.models import Book, Author, House


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'house')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

class BooksInstanceInline(admin.StackedInline):
    model = Book

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'book_count')
    # "Добавление издательства и связи Книга-Издательство нужно сделать в отдельной панели в админке."
    # Я нашёл только такой способ:
    inlines = [BooksInstanceInline]