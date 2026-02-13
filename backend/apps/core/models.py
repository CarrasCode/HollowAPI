import uuid
from typing import override

from django.conf import settings
from django.db import models

user = settings.AUTH_USER_MODEL


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False)
    user = models.ForeignKey(user, models.CASCADE)

    @override
    def __str__(self):
        return self.name
