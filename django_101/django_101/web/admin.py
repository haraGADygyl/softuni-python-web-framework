from django.contrib import admin

# superuser: Jorko
# password: 123

# Register your models here.
from django_101.web.models import Category, Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
