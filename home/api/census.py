import cellxgene_census

def fetchFilteringFields():
    census = cellxgene_census.open_soma()
    result =  list(census["census_data"]["homo_sapiens"].obs.keys())
    return result

    
    

