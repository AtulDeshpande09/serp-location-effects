import json

def get_organic_search_results(path_list,query_list,loc_list):
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
    """
    input : dict
    format :
    {"query" : {"location" : [res1,res2]}
    """
    title_dic = {}

    for query in dic.keys():
        
        title_dic[query] = {}

        for location, result_list in dic[query].items():
            title_list = []
            for result in result_list:
                title = result["title"]
                title_list.append(title)

            data = { location : title_list }
            title_dic[query].update(data)

    return title_dic



def get_links(dic):
    """
    input : dict
    format :
    {"query" : {"location" : [res1,res2]}
    """
    link_dic = {}

    for query in dic.keys():
        
        link_dic[query] = {}

        for location, result_list in dic[query].items():
            link_list = []
            for result in result_list:
                link = result["link"]
                link_list.append(snippet)

            data = { location : link_list }
            link_dic[query].update(data)

    return link_dic




def get_positions(dic):
    """
    input : dict
    format :
    {"query" : {"location" : [res1,res2]}
    """
    pos_dic = {}

    for query in dic.keys():
        
        pos_dic[query] = {}

        for location, result_list in dic[query].items():
            pos_list = []
            for result in result_list:
                pos = result["position"]
                pos_list.append(pos)

            data = { location : pos_list }
            pos_dic[query].update(data)

    return pos_dic



def get_snippets(dic):
    """
    input : dict
    format :
    {"query" : {"location" : [res1,res2]}
    """
    snippet_dic = {}

    for query in dic.keys():
        
        snippet_dic[query] = {}

        for location, result_list in dic[query].items():
            snipp_list = []
            for result in result_list:
                snippet = result["snippet"]
                snipp_list.append(snippet)

            data = { location : snipp_list }
            snippet_dic[query].update(data)

    return snippet_dic








