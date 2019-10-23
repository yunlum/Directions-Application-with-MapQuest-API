# YUNLU MA ID: 28072206

import P3_url
import P3_class
import urllib.error


def _get_data(minnumber:int) -> list:
    '''
    Get the data that user input which follows the typical format and return a list
    Could be used as build the list of positions and commands
    
    '''
    data_list=[]
    
    while True:
        n=int(input())
        if n >= minnumber:
            break
        else:
            print("Please enter an integer greater than or equal to " + str(minnumber))
    for i in range(n):
        while True:
            d=input()
            if d!="":
                break
        data_list.append(d)
                
        
    return data_list
    
                           
def _build_output_generator(commands:list,positions:list) -> list:
    '''
    Match the commands that the user inputted with the output generators which were imported from module P3_class
    And build a list of them
    
    '''
    output_generator_list = []
    
    for cmd in commands:
        if cmd == "LATLONG":
            output_generator_list.append(P3_class.LATLONG())
        elif cmd == "TOTALTIME":
            output_generator_list.append(P3_class.TOTALTIME())
        elif cmd == "STEPS":
            output_generator_list.append(P3_class.STEPS())
        elif cmd == "TOTALDISTANCE":
            output_generator_list.append(P3_class.TOTALDISTANCE())
        elif cmd == "ELEVATION":
            for i in range(len(positions)):
                output_generator_list.append(P3_class.ELEVATION())
    return output_generator_list

def _print_output_generator(output_generator_list:list,route:dict,elevation_profile_list:list):
    '''
    Print the outputs which are built by different output generators in the list
    
    '''
    count=0
    for output_generator in output_generator_list:
        if type(output_generator) == P3_class.ELEVATION:
            
            if count == 0:
                print("\nELEVATIONS")
            data_base = elevation_profile_list[count]
            count+=1
        else:
            data_base = route

        final_list = output_generator.output(data_base)
        for ans in final_list:
            print(ans)
            
            
def _is_there_elevation(commands:list) -> bool:
    '''
    Use to check whether the command is ELEVATION or not

    '''
    for cmd in commands:
        if cmd == "ELEVATION":
            return True

def _get_latLngCollection(route:dict) -> list:
    '''
    Get the collection of latLng which would be uses to build the URL of ELEVATION

    '''
    
    data_base = route
    latLngCollection=[]
    s = P3_class.LATLONG()
    s.get_latlong(data_base)
    for i in range(len(s._lng)):
        latLngCollection.append([s._lat[i],s._lng[i]])


    return latLngCollection

    


def user_interface():
    '''
    The MAIN function combines the all processes of the project 3 including get data, get URLs and parsing JSON responses from P3_url
    and finally, print the output from the output generators in P3_class.
    And different ERROR messages will show up when there is an ERROR
    
    '''
    
    try: 
        positions = _get_data(2)
        commands = _get_data(1)
        route = P3_url.get_route(positions)
        elevation_profile_list = []
        
        if _is_there_elevation(commands):  # ELEVATION needs different URL 
            latLngCollection = _get_latLngCollection(route)
            elevation_profile_list = P3_url.get_elevation_profile_list(latLngCollection)
        output_generator_list = _build_output_generator(commands,positions)
        _print_output_generator(output_generator_list,route,elevation_profile_list)
        
        
        print()
        print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")
        

    except KeyError:
        print()
        print("NO ROUTE FOUND")
    except urllib.error.URLError:
        print()
        print("MAPQUEST ERROR")
            
       

if __name__=="__main__":
    user_interface()





    
    
