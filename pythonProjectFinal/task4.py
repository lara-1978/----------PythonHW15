# Задача 4. Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.

import argparse
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    logger.debug("Started main function")

    parser = argparse.ArgumentParser(prog='Options and flags', description='Parsing number str',
                                     epilog='task4, pythonProjectFinal')


    parser.add_argument('number', type=int, metavar='number', help='Number for output')
    parser.add_argument('text', type=str, metavar='text', help='String for output')

    parser.add_argument('--verbose', action='store_true', help='Output information')
    parser.add_argument('--repeat', type=int, default=1, help='Count repeat str')

    try:
        args = parser.parse_args()
        if args.verbose:
            print(f'arg:\nnumber={args.number},\ntext="{args.text}",\nrepeat={args.repeat}')
        print(f'number: {args.number},\nstring: {args.text * args.repeat}')

    except ValueError as e:
        # если ошибки преобразования типов
        logger.error("Value error: %s", e)
        print("Error: Invalid value. Please ensure that all arguments are correct.")

    except argparse.ArgumentTypeError as e:
        # если не правильный тип аргумента
        logger.error("Argument type error: %s", e)
        print("Error: Invalid argument type.")

if __name__ == '__main__':
    main()

#  Результат из терминала:
# DEBUG:__main__:Started main function
# arg:
# number=5,
# text="hello Lora",
# repeat=5
# number: 5,
# string: hello Lorahello Lorahello Lorahello Lorahello Lora
