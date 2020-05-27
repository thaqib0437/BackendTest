from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length = 20)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)

class activity_periods(models.Model):
    User = models.ForeignKey(User, related_name='activity_periods', on_delete=models.CASCADE)
    start_time = models.CharField(max_length = 30)
    end_time = models.CharField(max_length = 30)
    def __str__(self):
        return '%s: %s' % (self.start_time, self.end_time)