# Task Manager API

Backend-сервис для управления задачами, реализованный на FastAPI.

## Функциональность

- создание задачи
- получение списка задач
- получение задачи по id
- обновление задачи
- удаление задачи
- фильтрация задач по статусу (is_done)

## Стек

- Python
- FastAPI
- SQLAlchemy
- SQLite

## Запуск

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload```

После запуска документация API (Swagger UI) доступна по адресу http://127.0.0.1:8000/docs

## Эндпоинты

| Метод  | Путь               | Описание                                   |
|--------|--------------------|--------------------------------------------|
| GET    | `/`                | Проверка работы сервиса                    |
| POST   | `/tasks`           | Создать задачу                             |
| GET    | `/tasks`           | Список задач (`?is_done=true/false` — фильтр) |
| GET    | `/tasks/{task_id}` | Получить задачу по id                      |
| PUT    | `/tasks/{task_id}` | Обновить задачу                            |
| DELETE | `/tasks/{task_id}` | Удалить задачу                             |

## Структура

```
app/
├── main.py      # FastAPI-приложение и эндпоинты
├── crud.py      # операции с базой данных
├── models.py    # SQLAlchemy-модели
├── schemas.py   # Pydantic-схемы
└── database.py  # подключение к SQLite
```
