from django.http import HttpResponse
import logging


def my_view(request):
    logger = logging.getLogger(__name__)

    try:
        # Код, который может вызвать ошибку
        result = 1 / 0
    except ZeroDivisionError:
        # Логирование ошибки
        logger.exception("Ошибка деления на ноль")

    return HttpResponse("Готово")




