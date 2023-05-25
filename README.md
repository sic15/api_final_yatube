Описание:
Проект позволяет создавать посты. Свои посты можно редактировать и удалять. Кроме того есть возможность оставлять колмментарии и подписываться на авторов. Есть возможность опредления поста в какую-то из заранее известных групп (возможности создавать и изменять группы у пользователей нет).


Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:sic15/api_final_yatube.git

2. Перейти в папку yatube_api:

cd yatube_api

3. Cоздать и активировать виртуальное окружение:

python -m venv venv
source venv/scripts/activate

4. Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt

5. Выполнить миграции:

python manage.py migrate

6. Запустить проект:

python manage.py runserver

