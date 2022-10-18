from django.contrib.auth import logout as logouts
from django.db.models import Avg, Max, Min, Sum, Count
from django.http import HttpResponse
from django.shortcuts import render

from .models import BooksModel
from .models import Datastore
from .models import Question
from .models import Quiz
from .models import Simplebook
from .models import Textbook


# Create your views here.
def index(request):
    return HttpResponse("App")


def books(request):
    books = BooksModel.objects.all()
    # return render(request, "book.html", {"books": books})
    # return render(request, "forpractice.html", {"books": books})
    return render(request, "forpractice1.html", {"books": books})


def filterbybookname(request):
    name = "physics"
    textbook = Textbook.objects.filter(bookname=name)
    return render(request, "textbook.html", {"textbook": textbook, "title": name + " Books"})


def all(request):
    textbook = Textbook.objects.all()
    return render(request, "textbook.html", {"textbook": textbook, "title": "All Books"})


def filterbyprice(request):
    fr = 0
    to = 0
    if request.POST:
        fr = int(request.POST["from"])
        to = int(request.POST["to"])
    textbook = Textbook.objects.filter(price__gte=fr) & Textbook.objects.filter(price__lte=to)

    return render(request, "filterbyprice.html", {"from": fr, "to": to, "books": textbook})


def simplebook(request):
    simple = Simplebook.objects.all()
    return render(request, "simplebook.html")


def searchbooks(request):
    data = BooksModel.objects.filter(subject="c")
    avr = BooksModel.objects.filter(subject="c").aggregate(Avg('price'), Max('price'), Min('price'))
    print(avr)
    print(data)
    return render(request, "allbooks.html", {"books": data, "average": avr})


def aggregates(request):
    # data = (BooksModel.objects.filter(subject="2") | BooksModel.objects.filter(subject="1")).aggregate(Avg('price'))
    data = BooksModel.objects.aggregate(Avg('price'), Max('price'), Min('price'), Sum('price'), Count('price'))
    # print(data['price__avg'])
    return render(request, "aggregates.html", {'books': data, "title": "Aggregates"})


def header(request):
    return render(request, "head.html")


def bookapp(request):
    return render(request, "bookapp.html")

# ---------------------------quiz app and question model are used in below functions ---------


def quiz(request):
    data = Quiz.objects.all()

    n = len(data)
    # print(type(data))
    # print(data[0])
    data2 = []
    for i in range(1, n, 2):
        data2.append([data[i - 1], data[i]])
    # if n%2==1:
    #     data2.append([data[n-1]])
    return render(request, "quizdes.html", {'alldata': data2})


def htmlquestion(request):
    queno = 1
    cmd = ""
    option = ""
    list = []
    # session = request.session
    # list = session.get("list")
    if list == None:
        list = []
    print("List = ", list)
    # session["list"] = list

    if request.GET:
        cmd = request.GET['CMD']
        if cmd == "NEXT":
            queno = int(request.GET['queno']) + 1
            option = request.GET['option']
            print("Submitted option is ", option)
            list.append(option)
        if cmd == "PREVIOUS":
            queno = int(request.GET['queno']) - 1
    # if request.GET:
    #     PREVIOUS = request.GET['PREVIOUS']
    #     queno = int(request.GET['queno']) - 1

    data = Question.objects.get(id=queno)
    max_ques = Question.objects.aggregate(Max('id'))
    session = request.session
    return render(request, "htmlquestion.html",
                  {'alldata': data, 'queno': queno, 'option': option, 'list': list, 'session': session,
                   'max_ques': max_ques})


def session(request):
    submit = ""
    key = ""
    value = ""
    if request.GET:
        submit = request.GET["submit"]
        key = request.GET["key"]
        value = request.GET["value"]
    session = request.session
    session[key] = value
    return render(request, "session.html", {"session": session, "key": key, "value": value})


def result(request):
    option = ""
    list = []
    if request.GET:
        option = request.GET['option']
        list = request.GET['list']
        list.append(option)
    print(list)
    return render(request, "result.html", {'list': list})


def login(request):
    uname = ""
    pa = ""
    if request.GET:
        uname = request.GET["uname"]
        session = request.session
        session["name"] = uname
        # pa = request.GET["pass"]

        submit = request.GET["submit"]
    return render(request, "login.html", {"user_name": uname})


def home(request):
    session = request.session
    uname = session.get("name")
    return render(request, "home.html", {"name": uname})


def logout(request):
    if request.GET:
        session = request.session
        session.delete("name")
        logouts(request)
    return render(request, "logout.html")


def datastore(request):
    return render(request, "datastorehome.html")

# --------------------------------------------------------------------------------------------------- save and delete data

def simpledesign(request):
    data = []
    delete = []
    task = []
    # return HttpResponse("Hello")
    if request.GET:
        cmd = request.GET["cmd"]
        task = int(request.GET["task_number"])
        # task_n = request.GET["task_name"]
        # details = request.GET["details"]
        # status = request.GET["status"]
        # value = Datastore(task_number=task, task_name=task_n, detail=details, status=status)
        # value.save()
        # id = request.GET["id"]
        print(cmd)
        if cmd == "EDIT":
            data = Datastore.objects.get(id=task)
        if cmd == "DELETE":
            data = Datastore.objects.all()

    # delete = Datastore.objects.get(id=task)

    print(data)

    return render(request, "simpledesign.html", {"datass": data})


def simpledesign_d(request):
    data = []
    # id = 0
    task = []
    if request.GET:
        cmd = request.GET["cmd"]
        task =int(request.GET["task_number"])
        print(cmd)
        print(task)
        data = Datastore.objects.get(id=task)
        if data != None:
            data.delete()
    data = Datastore.objects.all()
    return render(request, "simpledesign_d.html", {"datas": data})


def savedata(request):
    if request.GET:
        task = int(request.GET["task"])
        task_n = request.GET["task_name"]
        details = request.GET["details"]
        status = request.GET["status"]
        value = Datastore(task_number=task, task_name=task_n, detail=details, status=status)
        value.save()
    return render(request, "checksave.html")


def delete(request):
    return render(request, "simpledesign.html")
