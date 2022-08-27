#!/usr/bin/python3

import math
import os
import re
import sys

import pandas as pd
from pandas import DataFrame, Series
from pandas._typing import AggFuncType

# CONSTANTS
ALFA = 0.602
A = 80000


def read_csv(file_name: str) -> DataFrame:
    path = os.path.join(os.getcwd(), file_name)
    return pd.read_csv(path)


def read_excel(file_name: str) -> DataFrame:
    path = os.path.join(os.getcwd(), file_name)
    return pd.read_excel(path)


def calc_c(value: float) -> float:
    exp = (math.log10(A) - math.log10(value)) / ALFA
    return math.pow(10, exp)


def calculate(stator: DataFrame, func: AggFuncType) -> Series:
    return stator.apply(func)


def filter_keys(keys: list, exp: str):
    r = re.compile(exp)
    return list(filter(r.match, keys))


def save_excel(data_frame: DataFrame, file_name: str) -> None:
    name = re.split(r'\\|/|\.', file_name)[-2]
    data_frame.to_excel(f"{name}.xlsx")


def run(file_path: str, extension_file: str, extension: str) -> None:
    print(f'Started analysis of {file_path} file')

    if extension_file == 'csv':
        df = read_csv(file_path)
    else:
        df = read_excel(file_path)

    df2 = DataFrame()
    for key in df:
        df2[key] = df[key]
        if "MOX" in key:
            result = calculate(df[key], calc_c)
            df2['C['+key+']'] = result

    save_excel(df2, file_path)
    print(f'Finished...')


if __name__ == '__main__':
    try:
        __file_path = sys.argv[sys.argv.index('-p') + 1]
        __extension = sys.argv[sys.argv.index('-e') + 1].lower()
        __extension_file = re.split(r'\.', __file_path)[1].lower()

        if __extension in ['csv', 'xlsx'] and __extension_file in ['csv', 'xlsx']:
            run(__file_path, __extension_file, __extension)
        else:
            raise ValueError('Pay attention to the correct way to start the application.\nPython main.py -p [path]/['
                             'file_name].[xlsx, csv] -e [xlsx, csv]')

    except Exception as err:
        print(err)
