from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Book(models.Model):
    author = models.CharField(max_length=100, verbose_name='Имя автора')
    email = models.EmailField(max_length=100, verbose_name='Почта автора')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время редактирования")
    status = models.CharField(max_length=200,
                              default=STATUS_CHOICES[0][0],
                              verbose_name='Статус',
                              choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.pk}. {self.author} : {self.email}'

    class Meta:
        db_table = 'Books'
        verbose_name = 'Гостевая книга'
        verbose_name_plural = 'Гостевая книга'