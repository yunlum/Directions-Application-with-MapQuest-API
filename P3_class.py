# YUNLU MA ID: 28072206

class LATLONG:
    '''
    This class is used to get the useful data of LATLONG from the dictionary named "data_base"
    and make some adjustments to let the data match the format of output requirements.
    Finally, return a list of required data
    
    '''
    def __init__(self):
        '''
        Build four lists in the class self
        
        '''
        self._lng=[]
        self._lat=[]
        self._print_lng=[]
        self._print_lat=[]
        
    def get_latlong(self,data_base:dict):
        '''
        Find the sub-dictionary with the key "locations" in the dictionary named "data_base"
        Divide the dictionary named "locations" by the keys and match the key "latLng" in the sub-dictionaries.
        Add the data in the sub-key named "lng" / "lat" to the list self._lng / self._lat

        '''
        locations=data_base["locations"]
        for Dict in locations:
            for key in Dict:
                if key=="latLng":
                    for i in Dict[key]:
                        if i=="lng":
                            self._lng.append(Dict[key][i])
                        elif i=="lat":
                            self._lat.append(Dict[key][i])

    def adjust_latlng(list1:list, string1:str, string2:str, list2:list):
        '''
        Make some adjustments of the data in self._lng and self._lat by keeping two decimal places
        and add "W", "E", "S", "N" to the end
        Finally, add the new data to the list self._print_lng / self._print_lat

        '''
        for i in list1:
            x=str('{:.02f}'.format(round(i,2)))
            if x[0]=="-":
                list2.append(x[1:]+string1)
            else:
                list2.append(x+string2)

    def output(self,data_base:dict) -> list:
        '''
        Return the output list of LATLONG by adding the title "LATLONGS" and the adjusted data from the list self._lng and self._lat
        
        '''
        output_list=[]
        LATLONG.get_latlong(self,data_base)
        LATLONG.adjust_latlng(self._lng,"W","E",self._print_lng)
        LATLONG.adjust_latlng(self._lat,"S","N",self._print_lat)
        output_list.append("\nLATLONGS")
        for i in range(len(self._print_lng)):
            output_list.append(str(self._print_lat[i]+" "+self._print_lng[i]))
        return output_list


class STEPS:
    '''
    This class is used to get the useful directions of STEPS from the dictionary named "data_base"
    Finally, return a list of required directions
    
    '''
    def __init__(self):
        '''
        Build a list in the class self
        
        '''
        self._steps=[]
        
    def get_steps(self,data_base:dict):
        '''
        Find the sub-dictionary with the key "legs" in the dictionary named "data_base"  
        Divide the dictionary "legs" by the keys and match the key "maneuvers" in the sub-dictionaries .
        Add the directions in the sub-key named "narrative" to the list self._steps

        '''
        legs=data_base["legs"]
        for Dict in legs:
            for key in Dict:
                if key == "maneuvers":
                    Mane=Dict[key]
                    for Dict in Mane:
                        for key in Dict:
                            if key == "narrative":
                                self._steps.append(Dict[key])
                                
    def output(self,data_base:dict) -> list:
        '''
        Return the output list of STEPS by adding the title "DIRECTIONS" and directions from the list self._steps
        
        '''
        output_list=[]
        STEPS.get_steps(self,data_base)
        output_list.append("\nDIRECTIONS")
        for i in self._steps:
            output_list.append(i)
        return output_list


class TOTALTIME:
    '''
    This class is used to get the useful datum of TOTALTIME from the dictionary named "data_base"
    and make some adjustments to let the datum match the format of output requirements.
    Finally, return a list of required datum
    
    '''
    def __init__(self):
        '''
        Build two variables in the class self
        
        '''
        self._datum=0
        self._time=''

    def get_adjust_time(self,data_base:dict):
        '''
        Add the datum to the self._data in the key "time" of the dictionary named "data_base"
        And adjust the datum with unit conversion, rounding, and add the unit

        '''
        self._datum = data_base["time"]
        self._time = str(round(self._datum/60))+ " minutes"
        

    def output(self,data_base:dict):
        '''
        Return the output list of TOTALTIME by adding the title "TOTAL TIME" and the adjusted datum(str) from the self._time
        
        ''' 
        output_list=[]
        TOTALTIME.get_adjust_time(self,data_base)
        output_list.append("\nTOTAL TIME: "+ self._time)
        return output_list
    

class TOTALDISTANCE:
    '''
    This class is used to get the useful datum of TOTALDISTANCE from the dictionary named "data_base"
    and make some adjustments to let the datum match the format of output requirements.
    Finally, return a list of required datum
    
    '''
    def __init__(self):
        '''
        Build two variables in the class self
        
        '''
        self._data=0
        self._distance=''
        
    def get_adjust_distance(self,data_base:dict):
        '''
        Add the datum to the self._data in the key "distance" of the dictionary named "data_base"
        And adjust the datum with rounding, and add the unit

        '''
        self._data=data_base["distance"]
        self._distance=str(round(self._data)) + " miles"
        
    def output(self,data_base:dict):
        '''
        Return the output list of TOTALDISTANCE by adding the title "TOTAL DISTANCE" and the adjusted datum(str) from the self._distance
        
        ''' 
        output_list=[]
        TOTALDISTANCE.get_adjust_distance(self,data_base)
        output_list.append("\nTOTAL DISTANCE: "+ self._distance)
        return output_list
    

class ELEVATION:
    '''
    This class is used to get the useful datum of ELEVATION from the dictionary named "data_base"
    and make some adjustments to let the datum match the format of output requirements.
    Finally, return a list of required datum
    
    '''
    def __init__(self):
        '''
        Build two variables in the class self
        
        '''
        self._height = 0
        self._elevation = 0
        
    def get_height(self,data_base:dict):
        '''
        Add the datum in the key "height" of the sub-dictionary of the dictionary named "data_base" to the self._height
        
        '''
        for Dict in data_base:
            for key in Dict:
                if key == "height":
                    self._height = Dict[key]
                    
    def adjust_elevation(self):
        '''
        Adjust the datum in the self._height with unit conversion and rounding
        Add it to the self._elevation

        '''
        elevation = round(int(self._height)*3.2808399)
        self._elevation = elevation
    
    
    def output(self,data_base:dict):
        '''
        Return the output list of ELEVATION by adding the adjusted datum from the self._elevation
        
        ''' 
        output_list=[]
        ELEVATION.get_height(self,data_base)
        ELEVATION.adjust_elevation(self)
        output_list.append(self._elevation)
        return output_list
        
    

        
        
    
