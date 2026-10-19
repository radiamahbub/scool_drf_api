from django.contrib import admin
from scool.models import *

admin.site.register([CourseModel, SubjectModel])