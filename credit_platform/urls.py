from django.contrib import admin
from django.urls import path
from credit.views import get_producer_ids, create_sample_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producer_ids/<int:contract_id>/', get_producer_ids, name='get_producer_ids'),
    path('create_sample_data/', create_sample_data, name='create_sample_data'),
]
