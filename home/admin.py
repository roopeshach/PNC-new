from django.contrib import admin
from .models import Content, Slider, Description, Message_From_Chief, FAQ, aboutUs , SocialMedia,Campus_Chiefs_to_date, PageImage, Preloader


# Register your models here.
class content(admin.ModelAdmin):
    list_display = ['email', 'phone', 'address']


class sliderContent(admin.ModelAdmin):
    list_display = ['head', 'SliderImage','content']


class descView(admin.ModelAdmin):
    list_display = ['header']


class message(admin.ModelAdmin):
    list_display = ['Image', 'chief_name']


class faq(admin.ModelAdmin):
    list_display = ['question']


class PageImageTabularInline(admin.TabularInline):
    model = PageImage

    class Meta:
        model = aboutUs


class uptoDate(admin.ModelAdmin):
    list_display = ['chief_name','duration']


class about(admin.ModelAdmin):
    inlines = [PageImageTabularInline]


class abtPreloader(admin.ModelAdmin):
    list_display = ['title','Image','is_active']
    list_filter = ['is_active']


class socialMedia(admin.ModelAdmin):
    list_display = ['facebook','twitter','google_plus','linkedin','youtube']


admin.site.register(Content, content)
admin.site.register(Slider, sliderContent)
admin.site.register(Description, descView)
admin.site.register(Message_From_Chief, message)
admin.site.register(FAQ, faq)
admin.site.register(aboutUs,about)
admin.site.register(SocialMedia)
admin.site.register(Campus_Chiefs_to_date, uptoDate)
admin.site.register(Preloader, abtPreloader)