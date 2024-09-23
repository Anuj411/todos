from django.db import models
from app_modules.base.models import BaseModel


class Task(BaseModel):
    PENDING = "pending"
    COMPLETED = "completed"

    STATUSES = (
        (PENDING, "Pending"),
        (COMPLETED, "Completed"),
    )

    title = models.CharField("Title", max_length=200)
    description = models.TextField("Description", null=True, blank=True)
    due_date = models.DateField("Due Date", null=True, blank=True)
    status = models.CharField("Status", choices=STATUSES, max_length=100, default=PENDING)

    def __str__(self):
        return self.title

    