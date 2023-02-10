from django.shortcuts import render
import requests
import math

def get_currs():
    url = "https://api.apilayer.com/currency_data/change"

    headers = {
        "apikey": "LlYmxo3mh36bz3J54YklfREEJEiS96J8"
    }

    response = requests.request("GET", url, headers=headers)

    currencies = response.json().get('quotes')
    currs = []

    for cur in currencies:
        currs.append(cur[3:])

    return currs


def get_amount(amout, to, from1):
    url = f"https://api.apilayer.com/currency_data/convert?to={to}&from={from1}&amount={amout}"

    headers = {
        "apikey": "LlYmxo3mh36bz3J54YklfREEJEiS96J8"
    }

    response = requests.request("GET", url, headers=headers)

    result = response.json()['result']

    return result

def get_flaot_round(str1):

    return str(round(float(str1), 2))

def exchange(request):
    currs = get_currs()

    if request.method == "GET":

        context = {
            'currencies': currs
        }

        return render(request=request, template_name="exchange_v/index.html", context=context)


    else:
        amout = request.POST.get('from-amount')
        to = str(request.POST.get('from-curr'))
        from1 = str(request.POST.get('to-curr'))

        result = get_amount(amout, to, from1)
        print(amout)
        context = {
            'from_curr': from1 + " " + get_flaot_round(amout),
            'to_curr': to,
            'converted_amount': get_flaot_round(result),
            'currencies': currs
        }

        return render(request=request, template_name="exchange_v/index.html", context=context)
