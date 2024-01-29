from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contract(models.Model):
    contract_id = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.contract_id)

class CreditRequest(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='credit_request')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Credit Request #{self.id}"


class CreditRequestProduct(models.Model):
    credit_request = models.ForeignKey(CreditRequest, on_delete=models.CASCADE, related_name='products')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='credit_request_product')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product {self.product.name} for Request #{self.credit_request.id}"