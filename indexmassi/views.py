from django.shortcuts import render


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def weight_index(request):
    if request.method == "POST":
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        if not isint(weight) or not isint(height):
            description = "Ты ввёл вообще не цифры!"
            return render(request, 'htmls/index.html', {"pic": "static/img/0.png", "description": description})
        elif int(height) == 0 or (300 < int(height) < 100) or (500 < int(weight) < 20):
            description = "Делишь на ноль?"
            return render(request, 'htmls/index.html', {"pic": "static/img/0.png", "description": description})
        elif 300 < int(height) or 100 > int(height) or 500 < int(weight) or int(weight) < 20:
            description = "Диапазон неверный!"
            return render(request, 'htmls/index.html', {"pic": "static/img/0.png", "description": description})
        im = round(int(weight)/(int(height)*int(height)/10000), 1)
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
        return render(request, 'htmls/index.html', {"message": format(im), 
                                                         "your_index_description": "Ваш индекс массы тела = ", 
                                                         "description": description, "pic": pic, "weight": weight, 
                                                         "height": height})
    pic = "static/img/0.png"
    return render(request, 'htmls/index.html',  {"pic": pic})

