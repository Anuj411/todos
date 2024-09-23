from django.db import models
from app_modules.base.models import BaseModel
from app_modules.users.models import User

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
    created_by = models.ForeignKey(User, related_name="task_set", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    