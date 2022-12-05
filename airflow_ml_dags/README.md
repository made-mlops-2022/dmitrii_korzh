Запуск
```
docker-compose up -d --build
docker-compose start 
```

Остановка
```
sudo docker-compose down 
```

Открывается на `http://localhost:8080`, логин `admin`,  пароль `admin`. Нажимаем последовательно на trigger-docker для `make_data`, `train`, `predict`.

Можно предварительно удалить все в `data`: `rm -r .\data\*`