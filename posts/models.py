from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(u'Заголовок', max_length=100)
    content = models.TextField('Текст поста', max_length=300)
    timepublish = models.DateTimeField('Дата публикации', default=timezone.now)

    class Meta:
        verbose_name='Страница'
        verbose_name_plural='Страницы'

    def __str__(self):
        return self.title


class Comments(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    comments_text = models.TextField('Текст комментария')
    comments_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)


class Project(models.Model):
    title = models.CharField(u'Название проекты', max_length=100)
    content = models.TextField('Описание проекта', max_length=500)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title
