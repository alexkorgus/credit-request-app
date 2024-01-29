from django.shortcuts import render
from credit.models import Contract, CreditRequest, Product, CreditRequestProduct, Producer

def create_sample_data(request):
    contract1 = Contract.objects.create(contract_id=32812)
    contract2 = Contract.objects.create(contract_id=12354)
    
    credit_request1 = CreditRequest.objects.create(contract=contract1)
    credit_request2 = CreditRequest.objects.create(contract=contract2)

    producer1 = Producer.objects.create(name='Coca Cola Company')
    producer2 = Producer.objects.create(name='Nestle')
    producer3 = Producer.objects.create(name='Lays')

    product1 = Product.objects.create(name='Cola', producer=producer1)
    product2 = Product.objects.create(name='Fanta', producer=producer1)
    product3 = Product.objects.create(name='Sprite', producer=producer1)
    product4 = Product.objects.create(name='Cereals', producer=producer2)
    product5 = Product.objects.create(name='Chocolate Bar', producer=producer2)
    product6 = Product.objects.create(name='Lays Crab', producer=producer3)
    product7 = Product.objects.create(name='Lays Cream', producer=producer3)

    CreditRequestProduct.objects.create(
        credit_request=credit_request1, product=product1
    )
    CreditRequestProduct.objects.create(
        credit_request=credit_request1, product=product4
    )
    CreditRequestProduct.objects.create(
        credit_request=credit_request1, product=product5
    )
    CreditRequestProduct.objects.create(
        credit_request=credit_request1, product=product6
    )
    CreditRequestProduct.objects.create(
        credit_request=credit_request2, product=product2
    )
    CreditRequestProduct.objects.create(
        credit_request=credit_request2, product=product3
    )
    CreditRequestProduct.objects.create(
        credit_request=credit_request2, product=product7
    )
    return render(request, 'sample_data_created.html')

def get_producer_ids(request, contract_id):
    try:
        credit_request = CreditRequest.objects.prefetch_related(
                'products__product__producer'
            ).get(contract__contract_id=contract_id)

        producer_ids = set(product.product.producer.id for product in credit_request.products.all())

        return render(request, 'producer_ids.html', {'producer_ids': producer_ids})
    
    except CreditRequest.DoesNotExist:
        return render(request, 'contract_not_found.html')
