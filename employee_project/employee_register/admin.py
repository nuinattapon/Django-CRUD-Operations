from django.contrib import admin
from .models import Position, Employee


# Register your models here.


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position']
    readonly_fields = ['created_at', 'updated_at']
