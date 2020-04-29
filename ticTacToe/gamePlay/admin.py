from django.contrib import admin

from .models import Move, Game


# visit https://docs.djangoproject.com/en/1.11/ref/contrib/admin/ for doc.

# admin.site.register(Game)
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # to set which fields you want to see per game
    list_display = ('id', 'first_player', 'second_player', 'status')
    # makes status editable and make sure to make it a tuple
    list_editable = ('status',)


admin.site.register(Move)
