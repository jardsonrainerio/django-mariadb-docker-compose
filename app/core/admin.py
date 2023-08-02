from django.contrib import admin
from .models import State, City, Customer, Sale, Company, Service, ReturnPayload


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'modified_at']
    list_per_page = 10
    search_fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'modified_at']
    list_per_page = 10
    search_fields = ['name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'modified_at']
    list_per_page = 10
    search_fields = ['name']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'modified_at']
    list_per_page = 10
    search_fields = ['name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'modified_at']
    list_per_page = 10
    search_fields = ['name']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_customer', 'service', 'get_price', 'active', 'modified_at']
    list_per_page = 10
    search_fields = ['service']

    def get_customer(self, obj):
        return obj.customer.name

    def get_price(self, obj):
        return obj.service.sale_price

    get_customer.short_description = 'Customer'
    get_price.short_description = 'Price'


@admin.register(ReturnPayload)
class ReturnPayloadAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'modified_at']
    list_per_page = 10
    search_fields = ['name']
