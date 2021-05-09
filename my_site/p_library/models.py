from django.db import models

class Author(models.Model):
    full_name = models.CharField('Имя', max_length = 20)
    birth_year = models.SmallIntegerField('Год рождения')
    title = models.CharField('Примечание',max_length = 200)
    country = models.CharField('Страна', max_length = 2)

    def __len__(self):
        book_count = 0
        for book in Book.objects.all():
            if book.author_id == self.id:
                book_count = book_count + 1
        return book_count
    
    def __str__(self):
        return self.full_name

class House(models.Model):
    title = models.TextField('Название')
    year = models.SmallIntegerField('Год выхода на рынок')
    book_count = models.SmallIntegerField('Издало книг')

    def __str__(self):
        return self.title

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    house = models.ForeignKey(House, on_delete = models.CASCADE, default = 1)
    title = models.TextField('Название')
    ISBN = models.CharField(max_length=13)
    description = models.TextField('Описание')  
    year_release = models.SmallIntegerField('Год выхода в печать')  
    copy_count = models.SmallIntegerField('Кол-во копий')
    price = models.DecimalField('Цена', max_digits = 10,  decimal_places = 2)

    def __str__(self):
        return self.title