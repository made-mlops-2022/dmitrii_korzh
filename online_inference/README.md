



```
docker build -t marsianin500/mlops:v2 .
docker tag marsianin500/mlops:v2 marsianin500/mlops:v2
docker push marsianin500/mlops:v2
docker pull marsianin500/mlops:v2
```

Чтобы запустить, 
```
docker pull marsianin500/mlops:v2
docker run --name fastapi_app -d -p 8112:8112 marsianin500/mlops:v2
```

```
python make_request.py 
```
To test
```
python -m pytest -v
```

Уменьшили вес контейнера, взяв slimgit, также можно уменьшать вес, убирая лишние зависимости (например, для ноутбуков). Смотрите папку `images`. 