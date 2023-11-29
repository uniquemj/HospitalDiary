from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORIES = [
    ('Mental Health', 'Mental Health'),
    ('Heart Disease', 'Heart Disease'),
    ('Covid19', 'Covid19'),
    ('Immunization', 'Immunization'),
]
    

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/post/")
    category = models.CharField(max_length=100, choices=CATEGORIES)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
    
    @staticmethod
    def get_draft_post(user):
        return BlogPost.objects.filter(author=user, is_draft = True)
    
    @staticmethod
    def get_uploaded_post(user):
        return BlogPost.objects.filter(author=user, is_draft = False)