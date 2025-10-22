from django.conf import settings
from django.urls import reverse
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Текст статьи")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="Статья"
    )
    comment = models.CharField(max_length=140, verbose_name="комментарий")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def get_absolute_url(self):
        return reverse("article_list")
