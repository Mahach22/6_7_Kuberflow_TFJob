# Используем официальный базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем Python-скрипт в контейнер
COPY fashion_mnist_train.py /app/fashion_mnist_train.py

# Устанавливаем необходимые библиотеки
RUN pip install --no-cache-dir tensorflow numpy

# Указываем команду по умолчанию для запуска скрипта
CMD ["python", "/app/fashion_mnist_train.py"]

