car_headers = ['title', 'price_per_hour_usd', 'color', 'description', 'condition', 'mark', 'class', 'layout']
car_mark_headers = ['mark']
car_cond_headers = ['condition']
car_class_headers = ['class']

headers = {
    'car': car_headers,
    'car_mark': car_mark_headers,
    'car_cond': car_cond_headers,
    'car_class': car_class_headers,
}

model_mapped_names = {
    'car': {
        'title': 'title',
        'price_per_hour_usd': 'price_per_hour_usd',
        'color': 'color',
        'description': 'description',
        'condition': 'car_condition',
        'mark': 'car_mark',
        'class': 'car_class',
        'layout': 'layout'
    },
    'car_mark': {'mark': 'title'},
    'car_cond': {'condition': 'condition'},
    'car_class': {'class': 'title'},
}
