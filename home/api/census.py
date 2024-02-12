import cellxgene_census
from  asgiref.sync import sync_to_async

def fetchFilteringFields():
    census = cellxgene_census.open_soma()
    result =  list(census["census_data"]["homo_sapiens"].obs.keys())
    return result

    
    

