from django.urls import path
from main.views import show_main, show_json, show_json_by_id, show_xml, show_xml_by_id, add_product, see_details

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add_product/', add_product, name='add_product'),
    path('product/<str:id>', see_details, name='product_details'),
    path('xml/', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
    path('xml/<str:products_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:products_id>/', show_json_by_id, name='show_json_by_id'),
]