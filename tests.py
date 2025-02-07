from main import BooksCollector





# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    import pytest


    def test_add_new_books_books_genre_is_empty_str(self, collector):

        collector.add_new_book('Bible')
        books_dict = collector.books_genre

        assert books_dict.get('Bible') == ''

    names = [
        ' ',
        'R',
        'Да',
        'Данный параметр показывает количество с',
        'Данный параметр показывает количество сл'
    ]



    @pytest.mark.parametrize('name', names)
    def test_add_new_book_valid_name_book_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        books_dict = collector.books_genre
        assert name in books_dict

    names = ['','Данный параметр показывает количество сло', 'Данный параметр показывает количество слов', 'Данный параметр показывает количество слов, состоящих из букв']
    @pytest.mark.parametrize('name', names)
    def test_add_new_book_ivalid_name_book_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        books_dict = collector.books_genre
        assert len(books_dict) == 0

    def test_add_new_book_same_book_not_added_twice(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Bible')
        collector.add_new_book('Bible')
        books_dict = collector.books_genre
        assert len(books_dict) == 1


    def test_set_book_genre_name_and_genre_in_list_genre_setted(self, collector):
        collector.books_genre['Пуаро'] = ''
        collector.set_book_genre('Пуаро', 'Детективы')
        books_dict = collector.books_genre
        genre = books_dict.get('Пуаро')
        assert genre == 'Детективы'

    @pytest.mark.parametrize('name, genre', [['Пуаро', 'Запутанный'], ['Идиот', 'Мультфильмы'], ['Как я съел собаку', 'Аудиоспектакль']])
    def test_set_book_genre_or_name_not_in_list_genre_not_setted(self, name, genre, collector):
        collector.books_genre['Пуаро'] = ''
        collector.set_book_genre(name, genre)
        new_genre = collector.books_genre.get(name)
        assert new_genre is None or len(new_genre) == 0


    def test_get_book_genre_name_in_collection_gengre_getted(self, collector):
        collector.books_genre['Колобок'] = 'Мультфильмы'
        genre = collector.get_book_genre('Колобок')
        assert genre == 'Мультфильмы'

    books_1 = [
        ['Fairytale', 'Ужасы'],
        ['Puaro', 'Детективы'],
        ['The clue', 'Детективы'],
        ['Shrek', 'Мультфильмы']

    ]


    def test_get_books_with_specific_genre_name_and_genre_in_list_get_names_list(self, collector):
        collector.books_genre['Fairytale'] = 'Ужасы'
        collector.books_genre['Puaro'] = 'Детективы'
        collector.books_genre['The clue'] = 'Детективы'
        genre = 'Детективы'
        books_list = collector.get_books_with_specific_genre(genre)
        assert len(books_list) == 2 and 'The clue' in books_list and 'Puaro' in books_list

    books = [
        ['Fairytale', 'Сказки'],
        ['Puaro2', 'Детективы'],
        ['The clue2', 'Боевик'],
        ['Duhless', ''],
        ['', 'Комедии']

    ]

    @pytest.mark.parametrize('name,genre', books)
    def test_get_books_with_specific_genre_genre_not_in_list_get_not_list(self, name, genre, collector):

        collector.books_genre['Fairytale'] = 'Ужасы'
        collector.books_genre['Puaro'] = 'Детективы'
        collector.books_genre['The clue'] = 'Детективы'


        books_list = collector.get_books_with_specific_genre(genre)
        assert name not  in books_list

    def test_get_books_with_specific_genre_by_add_new_book_get_not_list(self, collector):
        collector.add_new_book('Fairytale')
        books_list = collector.get_books_with_specific_genre('')
        assert 'Fairytale' not in books_list



    def test_get_books_genre_after_add_new_book_get_collection(self, collector):
        collector.add_new_book('Bible')
        books_collection = collector.books_genre

        assert type(books_collection) is dict and books_collection.get('Bible') == ''

    def test_get_books_genre_after_set_book_ganre_get_collection(self, collector):
        collector.add_new_book('Puaro')
        collector.set_book_genre('Puaro', 'Детективы')
        books_collection = collector.books_genre
        assert books_collection.get('Puaro') == 'Детективы' and len(books_collection) == 1 and type(books_collection) is dict

    books_3 = [['Fairytale', 'Ужасы'],['Puaro', 'Детективы'],['The clue', 'Комедии'],['Shrek', 'Мультфильмы'],['Good omens', 'Фантастика']]


    def test_get_books_for_children_after_add_new_book_set_ganre_get_list(self, collector):
        books_3 = [['Fairytale', 'Ужасы'], ['Puaro', 'Детективы'], ['The clue', 'Комедии'], ['Shrek', 'Мультфильмы'],['Good omens', 'Фантастика']]
        for i in books_3:
            collector.add_new_book(i[0])
            collector.set_book_genre(i[0], i[1])
        books_list = collector.get_books_for_children()

        assert 'Puaro' not in books_list and 'Fairytale' not in books_list

    def test_add_book_in_favorites_book_in_book_genre_add_in_favorites(self, collector):
        name = 'Puaro'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        list_favorites = collector.favorites
        assert name in list_favorites and len(list_favorites) == 1

    def test_delete_book_from_favorites_delete_book_list_empty(self, collector):
        name = 'Puaro'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        favorites_list = collector.favorites
        assert len(favorites_list) == 0

    def test_get_list_of_favorites_books_one_book_get_list(self, collector):
        name = 'Puaro'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        list_favorites = collector.favorites
        assert list_favorites == ['Puaro']




















