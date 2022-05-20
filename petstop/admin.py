from django.contrib import admin
from .models import Item,User_Detail,Pet,Cart,Post
# Register your models here.
admin.site.register(Item)
admin.site.register(Post)
admin.site.register(Cart)
admin.site.register(User_Detail)
admin.site.register(Pet)
