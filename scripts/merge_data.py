import json

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from project_utils.preprocessing import get_organic_search_results, get_titles , get_links , get_snippets

from project_utils.metadata import get_search_metadata

from project_utils.metrics import jaccard_matrix

# List of locations
locations = open("locations.txt",'r')
loc_list = [location.strip('\n') for location in locations]

# List of Queries
queries = open("queries.txt",'r')
query_list = [query.strip('\n') for query in queries]


def create_path(location,query):
    
    path_list = []
    for location in loc_list:
        for query in query_list:
           
            path = location + "/" + query
            file_path = f"../Data/{path}.json"
            path_list.append(file_path)
    
    return path_list



if __name__ == "__main__":

    paths = create_path(loc_list,query_list)

    combined = get_organic_search_results(paths,query_list,loc_list)

    title_dic = get_titles(combined)

    title_jaccard = jaccard_matrix(title_dic)
    print(title_jaccard)

"""

    with open('../Data/merged.json','w') as file:
        json.dump( combined , file , indent=4)    
    print("File Stored successsfully!!!")

    metadata_dic = get_search_metadata(a,csv=True) """
