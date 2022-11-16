# MLOps. Домашнее задание 1
Будем работать с этим [датасетом](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci).

## Запуск
1. Создаем окружение и клонируем репозиторий
```
python -m venv mlops1
source mlops1/bin/activate
выберите Python 3.7.x
cd ml_project
pip install -r requirements.txt
pip install -e .
```
разархивированный датасет кладем в `data/heart_cleveland_upload.csv`

2. EDA
Можно посмотреть в `notebooks/EDA.ipynb`.

3. Обучение модели
```
python3 src/train.py config/train_config_logreg.yaml
или
python3 src/train.py config/train_config_rf.yaml
```
или создайте свой конфиг


4. Инференс
```
python3 src/predict.py config/predict_config_logreg.yaml
или
python3 src/predict.py config/predict_config_rf.yaml
```
укажите в конфиге путь до данных.
