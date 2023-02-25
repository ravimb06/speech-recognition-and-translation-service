# speech-recognition-and-translation-service

## Для локального запуска:

  Клонировать репозиторий
  ```
  git clone https://github.com/ravimb06/speech-recognition-and-translation-service.git
  ```
  ```
  cd speech-recognition-and-translation-service/
  ```
  Cоздать и активировать виртуальное окружение:
  ```
  python -m venv venv
  ```
  ```
  source venv/scripts/activate
  ```
  ```
  python -m pip install --upgrade pip
  ```
  Установить зависимости из файла requirements.txt:
  ```
  pip install -r requirements.txt
  ```

  Создайте .env файл в корневой директории проекта, в котором должны содержаться следующие переменные:
  ```
  DEEPL_KEY = {Ваш ключ}
  ```

  Перейдите в директорию src/ и выполните команду для запуска сервиса.
  ```
  python run.py
  ```

## Запуск в Docker:
  
  Находясь в корневой директории проекта где находится DockerFile
  ```
  docker build -t {название образа} .
  ```
  После сборки образа запускаем проект
  ```
  docker run -p 80:80 {имя образа который создали выше}
  ```
