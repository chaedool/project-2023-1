# -*- encoding: utf-8 -*-
from zipfile import ZipFile
from enum import Enum
from os import path
import pandas as pd
import geopandas as gpd
from app_operator import Operator

'''
#TODO : Replace this with a proper docstring

Process
1. Zip -> Shp + shx + ...
2. ->BuildingBase, ContourBase, VegetBase,RoadBase
BuildingBase -> Extruder, Parapetter+채원누나st
ContourBase -> Surfacer -> Drape and Contour
VegetBase -> return Point Layer + Random Picture
RoadBase -> CurveBoolean All -> split by Contour Curve -> project onto ContourBaseBuilt -> planarSrf -> Join -> offsetSrf <Thickness>
App(BuildingType : 층수 or 높이 , 파라펫 여부, Contourbase : 콘타 or 면 , VegetBase : Pic or Ensc)
Model_App : 콘타 두께, 스케일 -> App Argument로 변환
'''

# 1 | Enums
class BuildingType(Enum):
        HEIGHT = 0
        FLOOR = 1
    
class VegetationType(Enum):
        PICTURE = 0
        ENSCAPE = 1
        POINT = 2

class ContourType(Enum):
        CONTOURE = 0
        SURFACE = 1


        
# 2 | Site Modeling Automation Application - Main Class
class SMAApp:
        '''
        Site Modeling Automation Application
        
        properties
        - Input : unzip_dir
        - Options : building_type, parapet, contour_type, vegetation_type
        
        methods
        TODO: ABSTRACTION
        '''
        # 2.0 | Constants
        __unzip_dir_name = '\\.temp'
        
        # 2.1 | Constructor
        def __init__(self
                     ,target_file_path:str
                     ,building_type:BuildingType = BuildingType.FLOOR
                     ,doParapet:bool = False 
                     ,contour_type:ContourType = ContourType.CONTOURE 
                     ,vegetation_type:VegetationType = VegetationType.POINT):
                
                self.zip_file = ZipFile(target_file_path)
                self.building_type = building_type
                self.doParapet = doParapet
                self.contour_type = contour_type
                self.vegetation_type = vegetation_type

        # 2.2 | Operate Method : do all the series of operations
        def operate(self):
                operator = Operator(self.zip_file)
                operator.unzip()
                operator.find_elements()

        def get_result(self):
                pass
        
        # 2.3 | Operations
        # def __unzip_target(self):
        #         self.unzip_dir = path.dirname(self.zip_file.filename) + SMAApp.__unzip_dir_name
        #         self.zip_file.extractall(self.unzip_dir)
        
        # def __read_shps_to_json(self):
        #         file_names = self.__filter_shps(self.zip_file.namelist())
                
        #         building_filename = [name for name in file_names if 'B001' in name][0]
        #         self.building_json = gpd.read_file(self.unzip_dir + '\\' + building_filename, encoding='euc-kr').to_dict(orient='records')
                
        #         print(self.building_json)
        #         # [print(i) for i in self.building_json]
                
        # def __filter_shps(self,names:list):
        #         return [name for name in names if name.endswith('.shp')]        
        
                
        
                
                

