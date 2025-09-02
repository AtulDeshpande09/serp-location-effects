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

    file_path = "test.json"
    
    l = "India"
    q = "Coffee"
    num = 10
    results = search_web(q,l,num)
    print("Results : ",results)
    print()
    print("Type ",type(results))
    
    with open(file_path,'w') as file:
        json.dump(results,file,indent=4)
    print("File Saved Succefully!!!")
    
