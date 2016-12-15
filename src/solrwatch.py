import json
import pprint
from datetime import datetime
from mbeans_metrics import *
from admin_metrics import *
from luke_metrics import *
from swes import *

class SolrWatch:
    def __init__(self):
        self.conf_data = self.get_config()
        self.swes = SWES(self.conf_data)

    def get_config(self):
        with open('../conf/app.conf') as json_data_file:
            conf_data = json.load(json_data_file)    
            return conf_data

    def run(self):
        
        #pp = pprint.PrettyPrinter(indent=4)
        metrics = self.get_all_metrics()
        #pp.pprint(metrics)
        
        # Insert into elasticsearch
        self.swes.insert(metrics)
        
    def get_all_metrics(self):
        
        # Fetch last indexed metrics document from elasticsearch
        # For delta calculations
        # e.g. throughput, response time etc.
        last_doc = self.swes.get_last_document()
        
        # Fetch metrics for MBeans, Admin and Luke 
        mbeans_metrics = MBeansMetrics(self.conf_data)
        admin_metrics = AdminMetrics(self.conf_data)
        luke_metrics = LukeMetrics(self.conf_data)

        # Merge all metrics
        solrwatch_metrics = {}
        solrwatch_metrics.update(mbeans_metrics.get_metrics(last_doc))
        solrwatch_metrics.update(admin_metrics.get_metrics())
        solrwatch_metrics.update(luke_metrics.get_metrics())

        # Add time
        now = datetime.utcnow()
        solrwatch_metrics['DATETIME'] = now.strftime("%Y-%m-%dT%H:%M:00Z")
        
        return solrwatch_metrics
