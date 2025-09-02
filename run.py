#from serpapi import GoogleSearch

# List of locations
locations = open("locations.txt",'r')
loc_list = [location.strip('\n') for location in locations]

# List of Queries
queries = open("queries.txt",'r')
query_list = [query.strip('\n') for query in queries]



if __name__ == "__main__":

    print(loc_list)
    print(query_list)
