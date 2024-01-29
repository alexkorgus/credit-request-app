from django.contrib import admin
from credit.models import Producer, Product, Contract, CreditRequest, CreditRequestProduct

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'producer', 'created_at')

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract_id', 'created_at')

@admin.register(CreditRequest)
class CreditRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract', 'created_at')

@admin.register(CreditRequestProduct)
class CreditRequestProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'credit_request', 'product', 'created_at')