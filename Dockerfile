# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app
# Копируем файлы приложения в контейнер
COPY . app/

RUN pip install --no-cache-dir flask pytest
# Устанавливаем зависимости
#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install pytest
# Открываем порт, на котором будет работать приложение
EXPOSE 5000
ENV PYTHONPATH=/app
# Запускаем приложение
CMD ["python3", "app/run.py"]
