import csv

from django.core.management.base import BaseCommand, CommandError

from rental.management.commands._populate_tools import headers, model_mapped_names
from rental.models import Car, CarMark, CarClass, CarCondition, Driver


MODELS = {
    'CarMark': CarMark,
    'CarClass': CarClass,
    'CarCondition': CarCondition,
}


class Command(BaseCommand):
    help = 'Populate DB with data from CSV files'

    def _car_model_handler(self, field_name: list, values_list: list, do_flush: bool):
        if do_flush:
            Car.objects.all().delete()
        for line in values_list:
            content = {}
            for value, name in zip(line, field_name):
                content[name] = value
                if name == 'car_condition':
                    try:
                        condition = CarCondition.objects.get(condition=value)
                    except CarCondition.DoesNotExist:
                        condition = CarCondition(condition=value)
                        condition.save()
                    content[name] = condition
                if name == 'car_mark':
                    try:
                        mark = CarMark.objects.get(title=value)
                    except CarMark.DoesNotExist:
                        mark = CarMark(title=value)
                        mark.save()
                    content[name] = mark
                if name == 'car_class':
                    try:
                        class_ = CarClass.objects.get(title=value)
                    except CarMark.DoesNotExist:
                        class_ = CarClass(title=value)
                        class_.save()
                    content[name] = class_
            db_model = Car(**content)
            db_model.save()

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            help='Input file name. Data from it will be ued to populate existing DB.'
        )
        parser.add_argument(
            'table_name',
            help='Choose table name'
        )
        parser.add_argument(
            '--do_flush',
            default=False,
            action='store_true',
            help='Flag that says do flushing DB before populating or just adding data to it.'
        )

    def handle(self, *args, **options):
        filepath: str = options['filename']
        model_name: str = options['table_name']
        do_flush: bool = options['do_flush']
        fields_content = []
        fields_names = []
        with open(f'{filepath}', 'r', newline='') as csv_file:
            filename = filepath[filepath.rfind('/') + 1:].split('.')[0]
            file_headers = headers[filename]
            reader = csv.DictReader(csv_file)
            for row in reader:
                fields_content.append([row[header] for header in file_headers])
        file_model_name = filename[filename.rfind('/') + 1:].split('.')[0]
        if do_flush and model_name != 'Car':
            MODELS[model_name].objects.all().delete()
        for name in file_headers:
            fields_names.append(model_mapped_names[file_model_name][name])
        if model_name != 'Car':
            for line in fields_content:
                content = {field_name: value for field_name, value in zip(fields_names, line)}
                db_model = MODELS[model_name](**content)
                db_model.save()
        else:
            self._car_model_handler(fields_names, fields_content, do_flush)
