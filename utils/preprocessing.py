

def get_organic_search_results(path_list):

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
    


def get_titles(dic):

    title_dic = {}
