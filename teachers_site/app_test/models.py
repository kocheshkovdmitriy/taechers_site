from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=1000, verbose_name='Условие')
    answer = models.CharField(max_length=100, verbose_name='Правильный ответ')
    section = models.ForeignKey('Section', on_delete=models.CASCADE, verbose_name='Раздел', related_name='tasks')

    def __str__(self):
        return 'Задание №:{num}, раздел {section}'.format(
            section=self.section,
            num=self.pk
        )


class Test(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема теста')
    tasks_list = models.ManyToManyField('Task', related_name='tasks')

    def __str__(self):
        return 'Тема: {title}, количесво задани {cnt_task}'.format(
            title=self.title,
            cnt_task=len(self.tasks_list.all())
        )


class Section(models.Model):
    title = models.CharField(max_length=200, verbose_name='Раздел')

    def __str__(self):
        return self.title