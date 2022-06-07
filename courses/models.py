from django.db import models


class Course(models.Model):
    title = models.CharField('Название курса', max_length=50)
    sphere = models.CharField('Сфера', max_length=50)
    description = models.TextField('Описание курса')
    learningHours = models.IntegerField('Время изучения')
    blokInfo1 = models.TextField('Блок с информацией 1', default='')
    blokInfo2 = models.TextField('Блок с информацией 2', default='')
    blokInfo3 = models.TextField('Блок с информацией 3', default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

