from django.db import models
from babel import Locale
from django.conf import settings

# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título")
    company = models.CharField(max_length=200, verbose_name = "Empresa")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "work")
    datestart = models.DateField(verbose_name = "Fecha de comienzo")
    datefinish = models.DateField(verbose_name = "Fecha de finalización")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Cronomarcador de creación")
    updated = models.DateTimeField(auto_now =True, verbose_name = "Cronomarcador de modificación")

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'
        ordering = ['-datefinish']

    def __str__(self):
        return ( self.title + ' en ' + self.company )

    def date_started(self):
            locale = Locale(settings.LANGUAGE_CODE[:2])
            month = self.datestart.strftime("%m")
            month_localized = locale.months['format']['wide'][int(month)]
            return (str(month_localized.title()) + " " + self.datestart.strftime("%Y"))

    def date_finished(self):
            locale = Locale(settings.LANGUAGE_CODE[:2])
            month = self.datefinish.strftime("%m")
            month_localized = locale.months['format']['wide'][int(month)]
            return (str(month_localized.title()) + " " + self.datefinish.strftime("%Y"))

    def time_worked(self):
        months = ( self.datefinish.year - self.datestart.year) * 12 + self.datefinish.month - self.datestart.month
        years = months // 12
        months = months - ( years * 12 )
       
        if years > 1:
            year_name = ' años' 
        else:
            year_name = ' año'

        if months > 1:
            month_name = ' meses'
        else:
            month_name = ' mes'
        
        if years == 0:
            if months == 1:
                days_diff =  self.datefinish - self.datestart
                if days_diff.days < 30:
                    return('Menos de un mes')     
                else:
                    return(str(months) + month_name)
            else:
                return(str(months) + month_name)    
        else:
            if months == 0: 
                return(str(years) + year_name)
            else:    
                return(str(years) + year_name + ' y ' + str(months) + month_name)

class Client(models.Model):
    client = models.ForeignKey(Work, on_delete=models.CASCADE, verbose_name = "Empresa Cliente")
    company = models.CharField(blank=True, null=True, max_length=200, verbose_name = "Empresa Cliente")
    image = models.ImageField(blank=True, null=True, verbose_name = "Imagen Cliente", upload_to = "work")
    description = models.TextField(blank=True, null=True,verbose_name = "Descripción")
    datestart = models.DateField(verbose_name = "Fecha de comienzo")
    datefinish = models.DateField(verbose_name = "Fecha de finalización")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Cronomarcador de creación")
    updated = models.DateTimeField(auto_now =True, verbose_name = "Cronomarcador de modificación")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-datefinish']

    def date_started(self):
            locale = Locale(settings.LANGUAGE_CODE[:2])
            month = self.datestart.strftime("%m")
            month_localized = locale.months['format']['wide'][int(month)]
            return (str(month_localized.title()) + " " + self.datestart.strftime("%Y"))

    def date_finished(self):
            locale = Locale(settings.LANGUAGE_CODE[:2])
            month = self.datefinish.strftime("%m")
            month_localized = locale.months['format']['wide'][int(month)]
            return (str(month_localized.title()) + " " + self.datefinish.strftime("%Y"))

    def time_worked(self):
        months = ( self.datefinish.year - self.datestart.year) * 12 + self.datefinish.month - self.datestart.month
        years = months // 12
        months = months - ( years * 12 )
       
        if years > 1:
            year_name = ' años' 
        else:
            year_name = ' año'

        if months > 1:
            month_name = ' meses'
        else:
            month_name = ' mes'
        
        if years == 0:
            if months == 1:
                days_diff =  self.datefinish - self.datestart
                if days_diff.days < 30:
                    return('Menos de un mes')     
                else:
                    return(str(months) + month_name)
            else:
                return(str(months) + month_name)    
        else:
            if months == 0: 
                return(str(years) + year_name)
            else:    
                return(str(years) + year_name + ' y ' + str(months) + month_name)
