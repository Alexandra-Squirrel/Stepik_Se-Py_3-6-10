# Задание: запуск автотестов для разных языков интерфейса

## Состав файлов
### Файл conftest.py:
- содержит обработчик, который считывает из командной строки параметры language и browser_nm (pytest_addoption)
- браузер объявляется в фикстуре browser и передается в тесты как параметр. Содержит логику запуска браузера с указанным языком пользователя и браузером.
### Файл test_items.py:
- содержит тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.
- проверяется товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/

## Запуск
- тест должен запускаться и проходить успешно с параметром --language следующей командой:
 ```
pytest --language=es test_items.py
```
- тест может запускаться и проходить успешно с параметром --browser_nm (chrome or firefox)  следующей командой:
```
pytest --browser_nm=firefox test_items.py
```

## Значения по умолчанию
- browser_nm=chrome
- language=ru

## Примечание
Если при запуске вы получаете ошибку вроде: 
```
raise ValueError("option names %s already added" % conflict)
ValueError: option names {'--language'} already added
```
Перепроверьте, что у вас нет своего conftest.py в директории выше

