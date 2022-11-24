

To test
```
python -m pytest -v
```

```
docker build -t marsianin500/mlops:v2 .
docker tag marsianin500/mlops:v2 marsianin500/mlops:v2
docker push marsianin500/mlops:v2
docker pull marsianin500/mlops:v2
```

```
docker run --name fastapi_app -d -p 8112:8112 marsianin500/mlops:v2
```



Уменьшили вес контейнера, взяв slim