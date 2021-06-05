from django.contrib import admin
from resources import models
# Register your models here.


admin.site.register([

    models.Topic,
    models.SubTopic,
    models.Subscription,
    models.Request
])