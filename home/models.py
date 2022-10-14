from django.db import models
from datetime import datetime
from django.utils.dateformat import DateFormat

class Today(models.model):
    today = DateFormat(datetime.now()).format('Ymd')
