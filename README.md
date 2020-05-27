# Foobar

Foobar is a Python library for dealing with word pluralization.


## Models

```python
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
```
## Views
```python 
class userList():

    def get(self, request):
        
        users = User.objects.all().values() #Returns all feilds
        users_list = list(users)  
        for user in users_list:
            print(user)
        return JsonResponse(users_list, safe=False)
        
  
class userListUI(APIView): #For viewing data in APIview
'''Creates a UI view of the JSON file'''
    def get(self, request):
        
        abl1 = User.objects.all()
        sls = UserSerializer(abl1, many = True)
        return Response(sls.data)
        

```

# URLs:
The default URL will return an error page with a list of all sub URLs. 
The URLs in the code are as follows:
```python

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewall/', views.userList.as_view()),
    path('uiview/', views.userListUI.as_view()),

]

```

```https://www.link.com/admin/ ``` This URL will take you to a login page. 
From this page you can add users and usage time for each user. 
```python
username = 'thaqib'
password = '123'
```


```https://www.link.com/viewall/ ``` This URL will return the raw JSON file.  

```https://www.link.com/uiview/ ``` This URL will show the data in a UI view.  


Currently the usage times are strings but can be converted into datetime objects.
   
