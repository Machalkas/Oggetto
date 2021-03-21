from django.contrib import admin
from .models import Stream

# Register your models here.
class StreamAdmin(admin.ModelAdmin):
    model=Stream
    list_display=('id','title','streamKey', 'date')
    fieldsets=(
        (None,{'fields':('title','streamKey','url', 'is_active', 'shop')}),
    )
admin.site.register(Stream,StreamAdmin)