# fabrique

Для разворачивания приложения в папке с Dockerfile ввести следующие команды:

sudo docker build .

docker run -it -p 8002:8002 imageid

Административная панель доступна по адресу 127.0.0.1:8002/admin, name=fabriq, password=fab

127.0.0.1:8002/api/survey/ - получение списка опросов<br>
127.0.0.1:8002/api/survey/<int:pk>/ - получение детальной информации об опросе<br> 
127.0.0.1:8002/api/response/ - создание нового ответа<br>
127.0.0.1:8002/api/get-responses/ - получение ответов пользователя (идентификация по ip)
