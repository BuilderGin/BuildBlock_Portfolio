from django.contrib import admin
from .models import Contact, CompanyInformation, Testimonial, Portfolio, Services, ServicesLogos


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message', 'contact_date')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'email', )
    search_fields = ('name', 'email', 'phone', 'contact_date',)
    list_per_page = 25


class CompanyInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'adres', 'completed_projects', 'perspectief_clients', 'happy_clients')
    list_display_links = ('id', 'name')
    list_editable = ('completed_projects', 'perspectief_clients', 'happy_clients',)
    list_per_page = 25


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'person_name', 'person_function', 'message', 'upload_date')
    list_display_links = ('id', 'person_name')
    list_filter = ('person_name', 'person_function', )
    search_fields = ('person_name', 'person_function',)
    list_per_page = 25


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','category', 'upload_date', 'website_link')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'website_link', 'category',)
    search_fields = ('title', 'website_link',)
    list_per_page = 25

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_date')
    list_display_links = ('id', 'title')
    list_filter = ('title', )
    search_fields = ('title',)
    list_per_page = 25

class ServicesLogosAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_date')
    list_display_links = ('id', 'title')
    list_filter = ('title', )
    search_fields = ('title',)
    list_per_page = 25



admin.site.register(Contact, ContactAdmin)
admin.site.register(CompanyInformation, CompanyInformationAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesLogos, ServicesLogosAdmin)