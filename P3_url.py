# YUNLU MA ID: 28072206

import json
import urllib.parse
import urllib.request
import urllib.error


Consumer_API_Key = "J4LAhmqkNJjkn4zfS7KmRhQfNnuisOdx"
Base_Map_URL = "http://open.mapquestapi.com/directions/v2/route"
Elevation_Profile_URL = "http://open.mapquestapi.com/elevation/v1/profile"



def get_route(positions:list) -> dict:
    '''
    Get a dictionary which contains the useful information of the commands LATLONG, STEPS, TOTALTIME, and TOTALDISTANCE
    from a dictionary of the parsing JSON response 
    
    '''
    base_map_url = _build_base_map_url(positions)
    base_map_result = _get_result(base_map_url)
    route = base_map_result["route"]
    return route

def get_elevation_profile_list(latLngCollection:list) -> list:
    '''
    Get a list of dictionaries which contains the useful information of the command ELEVATION
    from a dictionary of the parsing JSON response

    '''
    elevation_profile_list = []
    elevation_url_list = _build_elevation_url(latLngCollection)
    for elevation_url in elevation_url_list:
        elevation_result = _get_result(elevation_url)
        elevation_profile_list.append(elevation_result['elevationProfile'])
    return elevation_profile_list

#Private Function#

def _build_base_map_url(positions:list) -> str:
    '''
    Use positions in the list from the user's input and build the URL for the commands LATLONG, STEPS, TOTALTIME, and TOTALDISTANCE
    
    '''
    query_parameters = [('key',Consumer_API_Key),('from',positions[0])]
    for i in range(1,len(positions)):
        query_parameters.append(('to',positions[i]))
    return Base_Map_URL + '?' + urllib.parse.urlencode(query_parameters)

def _build_elevation_url(latLngCollection:list) -> list:
    '''
    Use latLng data of positions in the list from the user's input and build a list of URLs for the command ELEVATION

    '''   
    elevation_url_list = []
    query_parameters = [('key',Consumer_API_Key),('shapeFormat','raw')]
    for lst in latLngCollection:
        elevation_url_list.append(Elevation_Profile_URL + "?" + urllib.parse.urlencode(query_parameters) + "&latLngCollection=" +str(lst)[1:-1].replace(" ",""))
        
    return elevation_url_list
    
    
def _get_result(url:str) -> dict:
    '''
    Use the URL to send HTTP request in order to get JSON response and finally, parse it and return a dictionary
    
    '''
    response=None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()



