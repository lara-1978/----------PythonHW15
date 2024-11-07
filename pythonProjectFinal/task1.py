# Задание 1. Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='debug_info.log', encoding='utf-8', level=logging.DEBUG)
debug_info_Handler = logging.FileHandler('debug_info.log', encoding='utf -8')
debug_info_Handler.setLevel(logging.DEBUG)
debug_info_Handler.setFormatter(formatter)


warnings_errors_Handler = logging.FileHandler('warnings_errors.log', encoding='utf 8')
warnings_errors_Handler.setLevel(logging.WARNING)
warnings_errors_Handler.setFormatter(formatter)

logger.addHandler(debug_info_Handler)
logger.addHandler(warnings_errors_Handler)

logger.debug('Cообщение  DEBUGa.')
logger.info('Полезная ин-ция!')
logger.warning('Внимание! Смотри в оба!')
logger.error('Поймали ошибку в коде!')
logger.critical(' Уровень критический! На этом всё!')







