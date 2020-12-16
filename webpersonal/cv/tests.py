from django.test import TestCase
from django.conf import settings
from .models import Work
import datetime
# Create your tests here.

class WorkModelTests(TestCase):
    def test_date_started_english(self):
        settings.LANGUAGE_CODE = 'en-US'
        test_date = datetime.datetime(2010,1,3)
        work_english = Work(datestart=test_date,title='test_en',company='django')
        self.assertEqual(work_english.date_started(), 'January 2010')

    def test_date_started_german(self):
        settings.LANGUAGE_CODE = 'de-DE'
        test_date = datetime.datetime(1987,12,7)
        work_german = Work(datestart=test_date,title='test_de',company='django')
        self.assertEqual(work_german.date_started(), 'Dezember 1987')

    def test_date_started_italian(self):
        settings.LANGUAGE_CODE = 'it-IT'
        test_date = datetime.datetime(1950,10,11)
        work_italian = Work(datestart=test_date,title='test_it',company='django')
        self.assertEqual(work_italian.date_started(), 'Ottobre 1950')

    def test_date_finished_french(self):
        settings.LANGUAGE_CODE = 'fr-FR'
        test_date = datetime.datetime(2018,2,9)
        work_french = Work(datefinish=test_date,title='test_fr',company='django')
        self.assertEqual(work_french.date_finished(), 'Février 2018')

    def test_date_finished_portuguese(self):
        settings.LANGUAGE_CODE = 'pt-BR'
        test_date = datetime.datetime(1987,11,25)
        work_portuguese = Work(datefinish=test_date,title='test_br',company='django')
        self.assertEqual(work_portuguese.date_finished(), 'Novembro 1987')

    def test_date_finished_greek(self):
        settings.LANGUAGE_CODE = 'el-EL'
        test_date = datetime.datetime(1920,4,15)
        work_greek = Work(datefinish=test_date,title='test_el',company='django')
        self.assertEqual(work_greek.date_finished(), 'Απριλίου 1920')

    def test_dates_time_worked(self):
        test_date_st = datetime.datetime(1920,4,15)
        test_date_fi = datetime.datetime(1940,6,15)
        work_diff = Work(datestart=test_date_st,datefinish=test_date_fi,title='test_diff')
        self.assertEqual(work_diff.time_worked(), '20 años y 2 meses')

    def test_dates_time_worked(self):
        test_date_st = datetime.datetime(1990,4,15)
        test_date_fi = datetime.datetime(1990,5,10)
        work_diff = Work(datestart=test_date_st,datefinish=test_date_fi,title='test_diff')
        self.assertEqual(work_diff.time_worked(), 'Menos de un mes')

    def test_dates_time_worked(self):
        test_date_st = datetime.datetime(1989,12,15)
        test_date_fi = datetime.datetime(1990,1,14)
        work_diff = Work(datestart=test_date_st,datefinish=test_date_fi,title='test_diff')
        self.assertEqual(work_diff.time_worked(), '1 mes')

    def test_dates_time_worked(self):
        test_date_st = datetime.datetime(1989,12,15)
        test_date_fi = datetime.datetime(1990,1,13)
        work_diff = Work(datestart=test_date_st,datefinish=test_date_fi,title='test_diff')
        self.assertEqual(work_diff.time_worked(), 'Menos de un mes')

    def test_dates_time_worked(self):
        test_date_st = datetime.datetime(1980,5,1)
        test_date_fi = datetime.datetime(1981,6,1)
        work_diff = Work(datestart=test_date_st,datefinish=test_date_fi,title='test_diff')
        self.assertEqual(work_diff.time_worked(), '1 año y 1 mes')
