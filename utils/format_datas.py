import os
import sys

sys.path.append(os.getcwd())

from flask import json
import datetime
from decimal import Decimal

from models.repository import RepositoryAnime


class Encoder:
    def default(self, o):
        if isinstance(o, datetime.datetime):
            if o.tzinfo:
                # eg: '2015-09-25T23:14:42.588601+00:00'
                return o.isoformat("T")
            else:
                # No timezone present - assume UTC.
                # eg: '2015-09-25T23:14:42.588601Z'
                return o.isoformat("T") + "Z"

        if isinstance(o, datetime.date):
            return o.isoformat()

        if isinstance(o, Decimal):
            return float(o)

        if isinstance(o, set):
            return list(o)

        return o


def convert(lis: list) -> list:
    __lista: list = []

    for dic in lis:
        __dic: dict = {}

        for (key, value) in dic.items():

            if isinstance(value, datetime.datetime):
                __dic[key] = value.strftime("%Y-%m-%d %H:%m:%s")
            elif isinstance(value, datetime.date):
                __dic[key] = value.strftime("%Y-%m-%d")
            else:
                __dic[key] = value

        __lista.append(__dic)
    return __lista


if __name__ == "__main__":

    data = RepositoryAnime().read()
    print(data[0])
