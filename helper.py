'''
1)Настройка вертуального окружения
python3 -m venv venv # создание вертуального окружения

source venv/bin/activate - активировать вертуальное окружение

pip freeze - показывает все установлиные библиотеки

deactivate - отключение вертуального окружения выйти из окружения

#####################################################################
2) Установка библиотек и фраймворков
requirements.txt
    django
    djangorestframework

pip install -r requirements.txt


№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

3) django-admin startpoject name-project . - создаем главное приложение нашего прроекта

#########################################################


4) django-admin startapp name_app - создаем определенное прилодение

    ./manage.py startapp name_app - второй способ создание приложения

5) 

./manage.py makemigrations - создает миграцию
./manage.py migrate - применяет ее

    /.manage.py runserver - запускаем сервер


6)
./manage.py createsuperuser - создает супер юзера



7) подключение к БД PostgreSQL

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', - изменить на postgresql
        'NAME': 'music_app', - тфзвание БД
        'USER': 'tahir', - имя через кого создается 
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': 5432
    }
}







'''