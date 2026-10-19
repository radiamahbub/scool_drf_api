from django.db import models


class CourseModel(models.Model):
    category_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
            return f'{self.category_name}'


class SubjectModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(
        CourseModel,
        on_delete=models.SET_NULL,
        related_name='cat_sub',
        null=True
        )
    teacher_name = models.CharField(max_length=100, null=True)
    credit = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}'

