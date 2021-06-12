from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название проекта')
    count = models.SmallIntegerField(verbose_name='количество выполненых проектов')
    image = models.ImageField(upload_to='media/images/projects/%Y/%m/')

    class Meta:
        db_table = 'project'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class Customer(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    heading = models.CharField(max_length=128)
    description = models.TextField()

    class Meta:
        db_table = 'customer'
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return f'Заказчик {self.name} | {self.heading}'
