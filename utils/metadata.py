def curate_metadata(data):
    
    metadata_dic = {}
    metadata = data['search_metadata']
    
    metadata_dic['id'] = metadata["id"]
    metadata_dic["created_at"] = metadata["created_at"]
    metadata_dic["processed_at"] = metadata["processed_at"]
    metadata_dic["time_taken"] = metadata["total_time_taken"]

    metadata = data["search_parameters"]
    
    metadata_dic["location"] = metadata["location_used"]
    metadata_dic["query"] = metadata["q"]
    metadata_dic["search_engine"] = metadata['engine']
    
    return metadata_dic


def get_search_metadata(path_list, csv:bool=False):
    
    search_metadata_dic = {}
    for path in path_list:

        with open(path,'r') as f:
            data = json.load(f)

        data = curate_metadata(data)        
        search_metadata_dic[path] = data

    if csv:
        import pandas as pd
        df = pd.DataFrame(search_metadata_dic)
        df = df.transpose()

        df.to_csv("../Data/metadata.csv",index=False)
    
        print("Metadata csv created!!!")

    return search_metadata_dic
