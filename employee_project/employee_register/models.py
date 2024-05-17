from django.db import models

# Create your models here.


class TimeStampMixin(models.Model):
    """
    TimeStampMixin abstract model
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """ meta """
        abstract = True


class Position(TimeStampMixin):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.title}"


class Employee(TimeStampMixin):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
