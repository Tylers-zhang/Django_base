from django.contrib import admin

# Register your models here.
from book.models import BookInfo, PeopleInfo
# register models class
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
# rebuild django
