# FastAPI Blog Server

Минимальный блог-сервер на FastAPI + PostgreSQL с автоматическим деплоем.

## Технологии
- Python 3.9 + FastAPI
- PostgreSQL
- Docker + Docker Compose
- GitHub Actions (CI/CD)

## Необходимые секреты в GitHub:

    SSH_PRIVATE_KEY - Приватный ключ для доступа к серверу

    SERVER_USER - SSH пользователь (напр. ubuntu)

    SERVER_HOST - IP сервера или localhost
## Запуск локально 
1. Установите Docker и Docker Compose.
2. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/fastapi-blog.git
cd fastapi-blog
docker-compose up -d
