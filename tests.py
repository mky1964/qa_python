from main import BooksCollector

import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод add_new_book, имеет  2 книги
        assert len(list(collector.books_genre.keys())) == 2

    def test_default_genre_true(self): # testing of method __init__ in class BooksCollector (default set of genres)
        collector1 = BooksCollector()
        assert collector1.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_set_book_with_no_genre_empty_string(self): # У добавленной книги нет жанра. Возвращается пустая строка
        collector2 = BooksCollector()
        collector2.add_new_book('Гордость')
        collector2.set_book_genre('Гордость', None)
        assert collector2.books_genre['Гордость'] == ''

    @pytest.mark.parametrize('genre',['Ужастик', '1234','Ужастик1', '','#$%^&'])
    def test_getting_book_with_wrong_ganre_false(self, genre):
        # выводим список книг по несуществующему жанру. Выводит false
        collector3 = BooksCollector()
        collector3.books_genre = {'book1': 'Фантастика' , 'book2': 'Детективы'}
        assert not collector3.get_books_with_specific_genre(genre)


    def test_get_book_genre_from_bookname_genre(self): #получаем жанр книги по её имени (позитивный)
        collector4 = BooksCollector()
        collector4.books_genre = {'book1': 'Фантастика', 'book2': 'Детективы'}
        assert collector4.get_book_genre('book2') == 'Детективы'

    @pytest.mark.parametrize('name, genre',
                 [
                     ['Солярис', 'Фантастика'],
                     ['Армагеддон','Ужасы'],
                     ['Шерлок Холмс','Детективы'],
                     ['Простоквашино','Мультфильмы'],
                     ['12 стульев','Комедии' ]
                 ]
    )
    def test_get_book_genre_name_genre(self, name, genre): # Получение жанра по названию
        collector5 = BooksCollector()
        collector5.add_new_book(name)
        collector5.set_book_genre( name, genre)
        assert collector5.get_book_genre(name) == genre




    def test_get_books_with_specific_genre_genre_list_of_books(self):# выводим список книг с определённым жанром Позитивный тест
        collector6 = BooksCollector()
        collector6.books_genre = {
                     'Солярис': 'Фантастика',
                     'Армагеддон':'Ужасы',
                     'Микки Маус':'Мультфильмы',
                     'Простоквашино':'Мультфильмы',
                     '12 стульев':'Комедии'
        }

        assert collector6.get_books_with_specific_genre('Мультфильмы') == ['Микки Маус','Простоквашино' ]


    def test_get_books_genre(self): # Проверка геттера books_genre
        collector7 = BooksCollector()
        dictionary = {}
        names = ['Солярис','Армагеддон','Микки Маус','Простоквашино','12 стульев']
        genres = ['Фантастика','Ужасы', 'Мультфильмы','Мультфильмы','Комедии']
        for i in range(0,5):
            collector7.add_new_book(names[i])
            collector7.set_book_genre(names[i], genres[i])
        dictionary = collector7.get_books_genre()
        assert list(dictionary.keys()) == names and list(dictionary.values()) == genres


    def test_in_get_books_for_children_no_books_for_adult(self):
        # Проверка отсутствия  книг для взрослых в геттере для детских книг
        collector8 = BooksCollector()
        dictionary = {}
        names = ['Солярис', 'Армагеддон', 'Микки Маус', 'Мегрэ', '12 стульев']
        genres = ['Фантастика', 'Ужасы', 'Мультфильмы', 'Детективы', 'Комедии']
        for i in range(0,5):
            collector8.add_new_book(names[i])
            collector8.set_book_genre(names[i], genres[i])
        assert not 'Ужасы' in collector8.get_books_for_children() or 'Детективы' in collector8.get_books_for_children()

    def test_add_book_in_favorites_existing_book_false(self): # Добавление в список фаворитов уже существующую книгу
        collector9 = BooksCollector()
        collector9.favorites = ['Солярис', 'Армагеддон', 'Микки Маус', 'Мегрэ', '12 стульев']
        collector9.add_book_in_favorites('Солярис' )
        assert collector9.favorites == ['Солярис', 'Армагеддон', 'Микки Маус', 'Мегрэ', '12 стульев']
        #Исправленная проверка метода add_book_in_favorites()

    def test_delete_book_from_favorites_one_book(self): # Проверка удаления книги из списка фаворитов
        collector10 = BooksCollector()
        collector10.favorites = ['Солярис', 'Армагеддон', 'Микки Маус', 'Мегрэ', '12 стульев']
        collector10.delete_book_from_favorites('Микки Маус')

        assert collector10.favorites == ['Солярис', 'Армагеддон', 'Мегрэ', '12 стульев']

    def test_get_list_of_favorites_books(self):
        collector11 = BooksCollector()
        collector11.favorites = ['Солярис', 'Армагеддон', 'Микки Маус', 'Мегрэ', '12 стульев']
        assert collector11.get_list_of_favorites_books() == ['Солярис', 'Армагеддон', 'Микки Маус', 'Мегрэ', '12 стульев']
















