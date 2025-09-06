from serpapi import GoogleSearch
import json

# List of locations
locations = open("locations.txt",'r')
loc_list = [location.strip('\n') for location in locations]

# List of Queries
queries = open("queries.txt",'r')
query_list = [query.strip('\n') for query in queries]


def search_web(query,location,num):

    params = {
            'q' : query,
            'location': location,
            'google_domain': 'google.com',
            'num' : num,
            'output' : 'json',
            'api_key' : "API_KEY"
            }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results



if __name__ == "__main__":

    num = 50

    for location in loc_list:
        for query in query_list:
            
            results = search_web(query,location,num)
            
            path = location + "/" + query 
            file_path = f"../Data/{path}.json"
            
            with open(file_path,'w') as file:
                json.dump(results,file,indent=4)
            print(f"File Saved at {file_path}")


