import json

# List of locations
locations = open("locations.txt",'r')
loc_list = [location.strip('\n') for location in locations]

# List of Queries
queries = open("queries.txt",'r')
query_list = [query.strip('\n') for query in queries]


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


def create_path(location,query):
    
    path_list = []
    for location in loc_list:
        for query in query_list:
           
            path = location + "/" + query
            file_path = f"../Data/{path}.json"
            path_list.append(file_path)
    
    return path_list



def all_json_file(path_list):

    combined = {query:{} for query in query_list}
 
    for query in query_list:

        combined[query] = {}

        for location in loc_list:
            path = location+"/"+query+".json"
            path = f'../Data/{path}'
            if path in path_list:
                
                with open(path,'r') as f:
                    data = json.load(f)
                data = data['organic_results']

                data = {location : data}

                combined[query].update(data)
        
    return combined
    


if __name__ == "__main__":

    paths = create_path(loc_list,query_list)

    combined = all_json_file(paths)


    with open('../Data/merged.json','w') as file:
        json.dump( combined , file , indent=4)    
    print("File Stored successsfully!!!")

    metadata_dic = get_search_metadata(a,csv=True) 
