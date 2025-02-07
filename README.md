# qa_python
MacBook-Air-Elena:qa_python elena$ pytest -v tests.py
====================================================================================== test session starts ======================================================================================
platform darwin -- Python 3.7.0, pytest-7.4.4, pluggy-1.2.0 -- /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/elena/qa_python
plugins: cov-4.1.0
collected 29 items

tests.py::TestBooksCollector::test_add_new_books_books_genre_is_empty_str PASSED                                                                                                          [  3%]
tests.py::TestBooksCollector::test_add_new_book_valid_name_book_added[ ] PASSED                                                                                                           [  6%]
tests.py::TestBooksCollector::test_add_new_book_valid_name_book_added[R] PASSED                                                                                                           [ 10%]
tests.py::TestBooksCollector::test_add_new_book_valid_name_book_added[\u0414\u0430] PASSED                                                                                                [ 13%]
tests.py::TestBooksCollector::test_add_new_book_valid_name_book_added[\u0414\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441] PASSED [ 17%]
tests.py::TestBooksCollector::test_add_new_book_valid_name_book_added[\u0414\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043b] PASSED [ 20%]
tests.py::TestBooksCollector::test_add_new_book_ivalid_name_book_not_added[] PASSED                                                                                                       [ 24%]
tests.py::TestBooksCollector::test_add_new_book_ivalid_name_book_not_added[\u0414\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043b\u043e] PASSED [ 27%]
tests.py::TestBooksCollector::test_add_new_book_ivalid_name_book_not_added[\u0414\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043b\u043e\u0432] PASSED [ 31%]
tests.py::TestBooksCollector::test_add_new_book_ivalid_name_book_not_added[\u0414\u0430\u043d\u043d\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u043f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043b\u043e\u0432, \u0441\u043e\u0441\u0442\u043e\u044f\u0449\u0438\u0445 \u0438\u0437 \u0431\u0443\u043a\u0432] PASSED [ 34%]
tests.py::TestBooksCollector::test_add_new_book_same_book_not_added_twice PASSED                                                                                                          [ 37%]
tests.py::TestBooksCollector::test_set_book_genre_name_and_genre_in_list_genre_setted PASSED                                                                                              [ 41%]
tests.py::TestBooksCollector::test_set_book_genre_or_name_not_in_list_genre_not_setted[\u041f\u0443\u0430\u0440\u043e-\u0417\u0430\u043f\u0443\u0442\u0430\u043d\u043d\u044b\u0439] PASSED [ 44%]
tests.py::TestBooksCollector::test_set_book_genre_or_name_not_in_list_genre_not_setted[\u0418\u0434\u0438\u043e\u0442-\u041c\u0443\u043b\u044c\u0442\u0444\u0438\u043b\u044c\u043c\u044b] PASSED [ 48%]
tests.py::TestBooksCollector::test_set_book_genre_or_name_not_in_list_genre_not_setted[\u041a\u0430\u043a \u044f \u0441\u044a\u0435\u043b \u0441\u043e\u0431\u0430\u043a\u0443-\u0410\u0443\u0434\u0438\u043e\u0441\u043f\u0435\u043a\u0442\u0430\u043a\u043b\u044c] PASSED [ 51%]
tests.py::TestBooksCollector::test_get_book_genre_name_in_collection_gengre_getted PASSED                                                                                                 [ 55%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_name_and_genre_in_list_get_names_list PASSED                                                                             [ 58%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_genre_not_in_list_get_not_list[Fairytale-\u0421\u043a\u0430\u0437\u043a\u0438] PASSED                                    [ 62%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_genre_not_in_list_get_not_list[Puaro2-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED                     [ 65%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_genre_not_in_list_get_not_list[The clue2-\u0411\u043e\u0435\u0432\u0438\u043a] PASSED                                    [ 68%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_genre_not_in_list_get_not_list[Duhless-] PASSED                                                                          [ 72%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_genre_not_in_list_get_not_list[-\u041a\u043e\u043c\u0435\u0434\u0438\u0438] PASSED                                       [ 75%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_by_add_new_book_get_not_list PASSED                                                                                      [ 79%]
tests.py::TestBooksCollector::test_get_books_genre_after_add_new_book_get_collection PASSED                                                                                               [ 82%]
tests.py::TestBooksCollector::test_get_books_genre_after_set_book_ganre_get_collection PASSED                                                                                             [ 86%]
tests.py::TestBooksCollector::test_get_books_for_children_after_add_new_book_set_ganre_get_list PASSED                                                                                    [ 89%]
tests.py::TestBooksCollector::test_add_book_in_favorites_book_in_book_genre_add_in_favorites PASSED                                                                                       [ 93%]
tests.py::TestBooksCollector::test_delete_book_from_favorites_delete_book_list_empty PASSED                                                                                               [ 96%]
tests.py::TestBooksCollector::test_get_list_of_favorites_books_one_book_get_list PASSED
