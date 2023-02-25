# speech-recognition-and-translation-service

  1. Клонировать репозиторий
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

  2. Создайте .env файл в корневой директории проекта, в котором должны содержаться следующие переменные:
  ```
  DEEPL_KEY = {Ваш ключ}
  ```

  3. Перейдите в директорию src/ и выполните команду для запуска сервиса.
  ```
  python run.py
  ```
