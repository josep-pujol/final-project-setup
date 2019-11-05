from django.db import models


class UserInfo(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=254)
    notes = models.TextField()
    registered = models.DateTimeField('date registered')

    def __str__(self):
        return self.email_address


class Department(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name



# class Task(models.Model):
#     user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     category = models.CharField
#     votes = models.IntegerField(default=0)
