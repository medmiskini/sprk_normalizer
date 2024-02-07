from rest_framework import serializers
from sprk_normalizer.products.utils import parse_unicode
from django.forms.models import model_to_dict

class ProductSerializer(serializers.Serializer):
    def to_internal_value(self, data):
        clean_data = [self.clean_product(data_entry) for data_entry in data.get('amounts')]
        
        merged_clean_data = {}
        for item in clean_data:
            code = item['code']
            if code in merged_clean_data:
                if merged_clean_data[code].get('type') is None:
                    merged_clean_data[code]['type'] = item.get('type')
                merged_clean_data[code]['amount'] = merged_clean_data[code].get('amount', 0) + item['amount']
            else:
                merged_clean_data[code] = {key: item[key] for key in item.keys() if (key != 'amount')}
                merged_clean_data[code]['amount'] = item['amount']

        return {'products':list(merged_clean_data.values())}
    
    def create(self, validated_data):
        return validated_data

    def clean_product(self, data_entry):
        item = data_entry.get('item')
        clean_entry = {}
        if(item):
            clean_entry = {
                'code': 
                    self.clean_code(item.get('code')),
                'type': 
                    item.get('type'),
                'trade_item_unit_descriptor': 
                    parse_unicode(item.get('trade_item_unit_descriptor')) if item.get('trade_item_unit_descriptor') else parse_unicode(item.get('trade_item_descriptor')),
                'trade_item_unit_descriptor_name': 
                    parse_unicode(item.get('trade_item_unit_descriptor_name')) ,
                'amount': 
                    self.clean_amount(data_entry.get('amount'), item.get('amount_multiplier')),
                'brand': 
                    parse_unicode(item.get('brand')),
                'description':
                    parse_unicode(item.get('description')),
                'has_edeka_article_number':
                    self.clean_has_edeka_article_number(item.get('edeka_article_number')),
                'edeka_article_number':
                    self.clean_edeka_article_number(item.get('edeka_article_number')),
                'gross_weight':
                    self.clean_weight_amount(item.get('gross_weight')),
                'net_weight':
                    self.clean_weight_amount(item.get('net_weight')),
                'validation_status':
                    item.get('validation_status'),
                'packaging':
                    parse_unicode(item.get('packaging')),
                'unit_name':
                    parse_unicode(item.get('unit_name'))
            }
        return clean_entry
    
    def clean_code(self, code):
        return code.lstrip('0') if code else None
    
    def clean_amount(self, amount, amount_multiplier):
        return amount * amount_multiplier if amount>0 and amount_multiplier else amount
    
    def clean_weight_amount(self, weight):
        if isinstance(weight, dict):
            return weight['amount']
        else:
            return weight
        
    def clean_has_edeka_article_number(self, edeka_article_number):
        if isinstance(edeka_article_number, bool):
            return edeka_article_number
        elif edeka_article_number:
            return True
        return False
        
    def clean_edeka_article_number(self, edeka_article_number):
        if not isinstance(edeka_article_number, bool):
            return edeka_article_number
        return None

    def to_representation(self, instance):
        return model_to_dict(instance)