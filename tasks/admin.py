from django.contrib import admin

from tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
    #cols to display in the list view
    list_display = ('id', 'title', 'completed', 'created_at', 'updated_at' )

    #added filters in sidebar for quick filtering
    list_filter = ('completed', 'created_at', 'updated_at')

    #Added search box for title and description
    search_fields = ('title', 'description')

    #order by latest updated task first
    ordering = ('-updated_at',)

    #make "completed" directly editable in list view
    list_editable = ('completed',)
# Register your models here.
admin.site.register(Task, TaskAdmin)
