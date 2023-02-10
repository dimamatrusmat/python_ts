from django.shortcuts import render
import pymorphy3
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests as req


def get_fior_s(fio1, fio2, fio3):
    ua = UserAgent()

    lastname = fio1.strip()
    name = fio2.strip()
    middlename = fio3.strip()

    url = 'https://surnameonline.ru/inflect.php'

    context = {
        'surname': lastname,
        'name': name,
        'patronymic': middlename
    }

    h = ua.random
    headers = {'User-Agent': h}

    resp = req.post(url, context, headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    try:
        text = soup.html.body.ul.find_all('li')

    except:
        text = False

    return text


def pager(request):

    if request.method == "GET":
        context = {}
    else:
        surname = request.POST.get('lastname')
        name = request.POST.get('name')
        fname = request.POST.get('fname')

        fios = get_fior_s(surname, name, fname)

        if fios:
            fio_ps = []

            for fio in fios:
                fio_ps.append(fio.text[5:])
        else:
            fio_ps = ["Не пропадежевировалось"]

        context = {
            "fio_ps": fio_ps
        }






    return render(request=request, template_name="fioget/index.html", context=context)

