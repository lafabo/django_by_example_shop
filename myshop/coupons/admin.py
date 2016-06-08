from django.contrib import admin
from .models import Coupon


# Register your models here.
class CouponAdmin(admin.ModelAdmin):
	list_display = ['code', 'valide_from', 'valide_to', 'discount', 'active']
	list_filter = ['active', 'valide_from', 'valide_to']
	search_fields = ['code']

admin.site.register(Coupon, CouponAdmin)