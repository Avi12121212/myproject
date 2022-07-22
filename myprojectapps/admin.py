from django.contrib import admin
from . models import Avi
from . models import BooksModel
from . models import Simplebook
from . models import Textbook
from . models import Quiz
from .models import Question
from .models import Datastore
from .models import Weather

# Register your models here.
admin.site.register(Avi)
admin.site.register(BooksModel)
admin.site.register(Simplebook)
admin.site.register(Textbook)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Datastore)
admin.site.register(Weather)


