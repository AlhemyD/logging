# logging

# Как работать
Запускаем сервер командой
`python3 user-service.py`
Запустится сервер, на который теперь из файлов publisher и subscriber можно будет отправлять запросы.

Запускаем прослушку командой в отдельном окне
`python3 subscriber.py`

Прослушка запустилась
Теперь запускаем генерацию случайных тестовых сообщений в Publisher командой:

`python3 publisher.py`

Ожидаемый результат:

Логи записываются в файл и выводятся в консоль.
Логи показывают, что publisher публикует сообщения, а subscriber их принимает.

Для проверки логов выполняем команду 
`python3 log-check.py`
Если порядок вывода логов верный, выведет что все логи правильные. Иначе выведет название приложения, в котором логи ошибаются

Пример логов в файле my-app.log
