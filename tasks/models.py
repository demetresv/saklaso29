from django.db import models


class Task(models.Model):

    STATUS_CHOICES = {'draft': "Draft",
                      'in_progress':' In Progress',
                      'done': 'Done',
                      'cancelled': 'Cancelled'}

    PRIORITY_CHOICES = {1:'Low',
                        2: 'Medium',
                        3: 'High',
                        4: 'Urgent'}

    name = models.Charfield()
    status = models.Charfield(choices=STATUS_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    description = models.TextField()
    archived = models.BooleanField(default=False)
    assigned_to = models.Charfield()
    create_date = models.DateTimeField(default=datetime.now)
    update_date = models.DateTimeField(default=datetime.now)
    deadline_date = models.DateField()
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self. name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name