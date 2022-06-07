from django.db import models


class Course(models.Model):
    title = models.CharField('Название курса', max_length=50)
    sphere = models.CharField('Сфера', max_length=50)
    description = models.TextField('Описание курса')
    learningHours = models.IntegerField('Время изучения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

