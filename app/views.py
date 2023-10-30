from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.


def near_hundred(request: HttpRequest, n: int) -> HttpResponse:
    return HttpResponse(abs(n - 100) <= 10 or abs(n - 200) <= 10)


def string_splosion(request: HttpRequest, string: str) -> HttpResponse:
    sploded_string = ""
    for i in range(len(string)):
        sploded_string = sploded_string + string[: i + 1]
    return HttpResponse(sploded_string)


def cat_dog(request: HttpRequest, string: str) -> HttpResponse:
    cats = 0
    dogs = 0
    while "cat" in string or "dog" in string:
        if "cat" in string:
            cats += 1
            string = string.replace("cat", "", 1)
        elif "dog" in string:
            dogs += 1
            string = string.replace("dog", "", 1)

    return HttpResponse(cats == dogs)


def lone_sum(request: HttpRequest, a: int, b: int, c: int) -> HttpResponse:
    sum = 0
    if a != b and a != c:
        sum += a
    if b != a and b != c:
        sum += b
    if c != a and c != b:
        sum += c
    return HttpResponse(sum)
