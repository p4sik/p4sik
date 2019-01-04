import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Catego(models.Model):
    """No kategorie w ktorych beda posty np nie wiem obiad hehe albo kolacja hehe xdd"""
    name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Catego, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    # image = models.ImageField(upload_to='MEDIA_ROOT') TODO: niew wiem jak to zrobic, sciezke doadc itp
    created_on = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(user, on_delete=models.CASCADE) TODO: potem trzeba dodac usera nowa apke i wpisac go

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(user, on_delete=models.CASCADE) TODO: potem trzeba dodac usera nowa apke i wpisac go
    def __str__(self):
        """Zwraca reprezentacje modelu w postaci ciągu tekstowego."""
        return self.text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text