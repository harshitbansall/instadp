from django.db import models

# Create your models here.

class InstagramUser(models.Model):
    username = models.CharField(max_length=50)
    searched_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'searched_usernames'

    def __str__(self):
        return '{} : {}'.format(self.username, self.searched_at)
