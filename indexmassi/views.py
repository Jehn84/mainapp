from django.shortcuts import render


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def indexmassi(request):
    if request.method == "POST":
        ves = request.POST.get("ves")
        rost = request.POST.get("rost")
        if not isint(ves) or not isint(rost):
            opisanie = "Ты ввёл вообще не цифры, гад!"
            pic = "static/img/0.png"
            return render(request, 'indexmassi/index.html', {"pic": pic, "opisanie": opisanie})
        elif int(rost) == 0 or (300 < int(rost) < 100) or (500 < int(ves) < 20):
            opisanie = "Делишь на ноль, собака?"
            pic = "static/img/0.png"
            return render(request, 'indexmassi/index.html', {"pic": pic, "opisanie": opisanie})
        elif int(rost) < 100 or (500 < int(ves) < 20):
            opisanie = "Диапазон говно!"
            pic = "static/img/0.png"
            return render(request, 'indexmassi/index.html', {"pic": pic, "opisanie": opisanie})
        im = round(int(ves)/((int(rost) * int(rost) / 10000)), 1)
        if 1 <= im < 16:
            opisanie = "Вы дистрофан! Выраженный дефицит массы"
            pic = "static/img/1.png"
        elif 16 < im <= 18.5:
            opisanie = "Вы тощий! Недостаточная масса тела"
            pic = "static/img/1.png"
        elif 18.5 < im <= 25:
            opisanie = "Ура! Вы нормальный"
            pic = "static/img/2.png"
        elif 25 < im <= 30:
            opisanie = "Вы жирноваты! Избыточная масса тела (предожирение)"
            pic = "static/img/3.png"
        elif 30 < im <= 35:
            opisanie = "Вы жирный! Ожирение 1-ой степени!"
            pic = "static/img/4.png"
        elif 35 < im < 40:
            opisanie = "Вы очень жирный! Ожирение 2-ой степени!"
            pic = "static/img/5.png"
        elif 500 > im >= 40:
            opisanie = "Вы супержирный! Ожирение 3-ей степени!"
            pic = "static/img/6.png"
        else:
            opisanie = "Получен некорректный ИМТ!"
            pic = "static/img/0.png"
        return render(request, 'indexmassi/index.html', {"message": format(im), "vashindexraventext": "Ваш индекс массы тела = ", "opisanie": opisanie, "pic": pic, "ves": ves, "rost": rost})
    pic = "static/img/0.png"
    return render(request, 'indexmassi/index.html',  {"pic": pic})

