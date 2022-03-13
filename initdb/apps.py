from django.apps import AppConfig
import csv

class InitdbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'initdb'

    def ready(self): # runs on startup
        from django.conf import settings
        self._initDB(settings.BASE_DIR / str(settings.CSV_LOCATION))
    
    def _initDB(self, path: str):
        from .models import Entry

        Entry.objects.all().delete() # clear DB

        entries = []
        with open(path, "r") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            columns = {"Station": "station", "Line": "line", "AdmArea": "admin_area", 
                "District": "district", "Status": "status", "ID": "entryID"}
            
            for row in reader:
                # setup read data
                row_data = {}
                for column_name in columns:
                    key = columns[column_name] # key in DB
                    
                    if column_name in row: # if data exists in the table
                        data = row[column_name] # data by key from csv
                        row_data[key] = data if data != "" else None
                    else:
                        row_data[key] = None
                    
                entries.append(Entry(**row_data))
            
            Entry.objects.bulk_create(entries) # add entries to DB