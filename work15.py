pupils = [
    {
        "name": "sardor",
        "payment_date": "01-02-2021",
        "paid_date": "03-02-2021"
    }, {
        "name": "akmal",
        "payment_date": "20-02-2021",
        "paid_date": "18-02-2021"
    }, {
        "name": "sherali",
        "payment_date": "03-01-2021",
        "paid_date": "10-01-2021"
    },
    {
        "name": "jurabel",
        "payment_date": "17-02-2021",
        "paid_date": "25-02-2021"
    },
    {
        "name": "jamshid",
        "payment_date": "02-01-2021",
        "paid_date": "11-02-2021"
    }
]
buyurtmalar = [
    {
        "driver": 1,
        "summa": 10000,
        "date": "01-02-2021"
    },
    {
        "driver": 3,
        "summa": 40000,
        "date": "03-02-2021"
    },
    {
        "driver": 2,
        "summa": 12000,
        "date": "01-02-2021"
    },
    {
        "driver": 1,
        "summa": 10000,
        "date": "01-02-2021"
    },
    {
        "driver": 3,
        "summa": 10000,
        "date": "19-02-2021"
    },
    {
        "driver": 2,
        "summa": 13000,
        "date": "10-01-2021"
    },
    {
        "driver": 1,
        "summa": 11000,
        "date": "10-01-2021"
    },
    {
        "driver": 2,
        "summa": 19700,
        "date": "10-01-2021"
    },
]
driverlar = [
    {
        "id": 1,
        "name": "jamshid"
    },
    {
        "id": 2,
        "name": "doston"
    },
    {
        "id": 3,
        "name": "rustam"
    },
    {
        "id": 4,
        "name": "jurabek"
    }
]
import datetime


def date_func(numbers):
    date_result = datetime.datetime.strptime(numbers, "%d-%m-%Y").date()
    return date_result
dict={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
nomlock_dict = {
    0 : "p",
    1 : "q",
    2 : "t",
    3 : "g",
    4 : "o",
    5 : "b",
    6 : "n",
    7 : "v",
    8 : "m",
    9 : "x",
    "q" : '1',
    "w" : '2',
    "e" : '3',
    "r" : '4',
    "t" : '5',
    "y" : '6',
    "u" : '7',
    "i" : '8',
    "o" : '9',
    "p" : '0',
    "a" : "#",
    "s" : "$",
    "d" : "%",
    "f" : "&",
    "g" : "*",
    "h" : "<",
    "j" : ">",
    "k" : "/",
    "l" : "~",
    "z" : "\\",
    "x" : "{",
    "c" : "}",
    "v" : "[",
    "b" : "]",
    "n" : "(",
    "m" : ")",
    " " : "@"
}
