1. установить pycharm: https://www.jetbrains.com/ru-ru/pycharm/download/
2. скачать и установить python: https://www.python.org/downloads/
3. скачать и установить git: https://git-scm.com/download1. 
4. в консоли windows выполнить: 
 cd c:\Users\Olga\AppData\Local\Programs\Python\Python38-32\; 
 python -m pip install --upgrade pip; 
 cd Scripts; 
 pip3 install selenium; 
5. Открыть pycharm > Get from version control > вставить ссылку на репозиторий https://github.com/okaekhtina/consultantTests.git
6. В папке с питоном установить вебдрайвер для браузера хром https://chromedriver.chromium.org/downloads

Для корректного запуска автотестов (типовые проблемы при запуске) необходимо:
* Проверить подключение к интернету на машине, с которой будут запускаться тесты;
* Проверить версию скаченного вебдрайвера для хрома (на сайте есть подсказки https://chromedriver.chromium.org/downloads)
* Разорхивировать и поместить вебдрайвер именно в папку, где лежит питон
* Настроить параметры запуска через pytest: в pycharm открыть edit run/debug configueation > add new configuration > python test > pytest > указать путь до исполняемого файла PycharmProjects/consultantTests/tests/test_search.py > выбрать python interpreter (путь до python.exe)
* Данная инструкция предназначена для запуска тестов на ОС windows с использованием браузера chrome (на других ОС пути для установки могут отличаться)
