from django.db import models
from datetime import date


class RecordReporting(models.Model):
    bailiff_name = models.CharField(max_length=140)
    court_case_applicants = models.CharField(max_length=140)
    court_case_num = models.IntegerField()
    bailiff_address = models.CharField(max_length=100)
    court_case_date = models.DateField(default=date.today())
    court_case_time = models.TimeField()
    court_case_msg_title = models.CharField(max_length=140)
    court_case_lawyer = models.CharField(max_length=140)
    court_case_agent = models.CharField(max_length=140)
    court_case_defendants = models.CharField(max_length=200)
    court_case_msg_content = models.CharField(max_length=140)

    def __str__(self):
        return self.bailiff_name
