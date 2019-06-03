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
            description = "Ты ввёл вообще не цифры!"
            return render(request, 'indexmassi/index.html', {"pic": "static/img/0.png", "description": description})
        elif int(rost) == 0 or (300 < int(rost) < 100) or (500 < int(ves) < 20):
            description = "Делишь на ноль?"
            return render(request, 'indexmassi/index.html', {"pic": "static/img/0.png", "description": description})
        elif 300 < int(rost) or 100 > int(rost) or 500 < int(ves) or int(ves) < 20:
            description = "Диапазон неверный!"
            return render(request, 'indexmassi/index.html', {"pic": "static/img/0.png", "description": description})
        im = round(int(ves)/((int(rost) * int(rost) / 10000)), 1)
        if 1 <= im <= 16:
            description = "Выраженный дефицит массы"
            pic = "static/img/1.png"
        elif 16 < im <= 18.5:
            description = "Недостаточная масса тела"
            pic = "static/img/1.png"
        elif 18.5 < im <= 25:
            description = "Норма"
            pic = "static/img/2.png"
        elif 25 < im <= 30:
            description = "Избыточная масса тела (предожирение)"
            pic = "static/img/3.png"
        elif 30 < im <= 35:
            description = "Ожирение первой степени!"
            pic = "static/img/4.png"
        elif 35 < im < 40:
            description = "Ожирение второй степени!"
            pic = "static/img/5.png"
        elif 500 > im >= 40:
            description = "Ожирение третьей степени!"
            pic = "static/img/6.png"
        else:
            description = "Получен некорректный ИМТ!"
            pic = "static/img/0.png"
        return render(request, 'indexmassi/index.html', {"message": format(im), "vashindexraventext": "Ваш индекс массы тела = ", "description": description, "pic": pic, "ves": ves, "rost": rost})
    pic = "static/img/0.png"
    return render(request, 'indexmassi/index.html',  {"pic": pic})

