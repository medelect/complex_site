from django.contrib import admin

from .models import Event, Contact, Stripe


#class StripeInline(admin.StackedInline):
#    model = Stripe
#    extra = 1


#class ContactInline(admin.StackedInline):
#    model = Contact
#    extra = 1

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['type_event', 'describe_event']}),
            ('Time', {'fields': ['start_time', 'limit']}),
            ('Contact', {'fields': ['contact']}),
            ('Other', {'fields': ['status', 'importance']}),
            ]
#    inlines = [ContactInline]
#    inlines = [StripeInline]

admin.site.register(Event, EventAdmin)
admin.site.register(Contact)
admin.site.register(Stripe)

