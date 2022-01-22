Проект контейнер к api_yamdb
в файле infra_sp2/infra/.env пропишите ваши переменный окружения
Запускать так: в тереминале переходим в папку infra_sp2/infra,
потом в тереминале набираем команду docker-compose up
после этого выполняем миграции командой: docker-compose exec web python manage.py migrate
создаем суперпользователя командой: docker-compose exec web python manage.py createsuperuser
собираем статику командой: docker-compose exec web python manage.py collectstatic --no-input
в браузере набираем localhost
