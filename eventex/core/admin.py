from django.contrib import admin
from eventex.core.models import Speaker, Contact, Talk, Course


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return '<a href="{0}">{0}</a>'.format(obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'website'

    def photo_img(self, obj):
        return '<img width="32px" src="{0}">'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'


class ActivityModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'start', 'get_speakers']

    def get_speakers(self, obj):
        return ', '.join([speaker.name for speaker in obj.speakers.all()])

    get_speakers.short_description = 'palestrante(s)'


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk, ActivityModelAdmin)
admin.site.register(Course, ActivityModelAdmin)