from django.contrib import admin
from models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	list_filter = ('publication_date',)
	#date_hierarchy = 'publication_date'//Doesn' support in django-nonrel
	ordering = ('-publication_date',)
	#fields = ('title', 'authors', 'publisher',)//We can include but now I want to show up each option
	#filter_horizontal = ('authors',)
	raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

