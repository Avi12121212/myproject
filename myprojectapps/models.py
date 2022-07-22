

from django.db import models


# Create your models here.
from django.utils import timezone


class Avi(models.Model):
    aviname = models.CharField(max_length=100)
    aviprofession = models.CharField(max_length=100)
    aviage = models.IntegerField()

    class Meta:
        db_table = "Avitable"


class BooksModel(models.Model):
    bookname = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return "BookName={0},Booksubject= {1},Bookprice = {2}".format(self.bookname, self.subject, self.price)

    class Meta:
        db_table = "books"


class Simplebook(models.Model):
    bookname = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return "bookname= {0},subject= {1}, price= {2}".format(self.bookname, self.subject, self.price)

    class Meta:
        db_table = "simplebook"


class Textbook(models.Model):
    bookname = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return "Bookname={0},Price={1}".format(self.bookname, self.price)

    class Meta:
        db_table = "textbook"


class Quiz(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100, default="name")
    description = models.CharField(max_length=500)

    def __str__(self):
        return "number={0}, name={1}, description={2}".format(self.number, self.name, self.description)

    class Meta:
        db_table = "quiz"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    option_a = models.CharField(max_length=50)
    option_b = models.CharField(max_length=50)
    option_c = models.CharField(max_length=50)
    option_d = models.CharField(max_length=50)
    correct = models.IntegerField()

    def __str__(self):
        return "question ={0}, option_a={1},option_b={2},option_c={3},option_d={4},correct={5}".format \
            (self.question, self.option_a, self.option_b, self.option_c, self.option_d, self.correct)

    class Meta:
        db_table = "question"


class Datastore(models.Model):
    task_number = models.IntegerField()
    task_name = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return "task_number={0},task_name= {1},deatil = {2},status = {3}".format \
            (self.task_number, self.task_name, self.detail, self.status)

    class Meta:
        db_table = "datastore"


class Weather(models.Model):
    city = models.CharField(max_length=50)
    tempreture = models.FloatField()
    feel = models.FloatField()
    country = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)
    wind_speed = models.CharField(max_length=200)
    # time = models.TimeField(default=timezone.now)
    time = models.CharField(max_length=200)

    def __str__(self):
        return "city={0},tempreture = {1},feel = {2},country= {3},weather= {4},wind_speed={5},time={6}".format \
            (self.city, self.tempreture, self.feel, self.country, self.weather, self.wind_speed,self.time )

    class Meta:
        db_table = "weather"
