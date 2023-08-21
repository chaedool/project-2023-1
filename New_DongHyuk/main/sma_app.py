from constants.options import *
from zipfile import ZipFile
from operator_ import Operator


class SMA:
    '''
    class SMA (Object)
    SMA : Site Modeling Automation
    this class is an application for site modeling automation
    
    Operations
    1. set options and file
    2. operate by Operator Object
    3. get result and save on local storage
    '''
    #0 | Properties
    def __init__(self):
        self.options = {}
        self.zip_file = None
        self.operator = Operator()

    #1 | Methods
    
    #1 -1 | Set Methods
    def set_options(
        self,
        building_type: BuildingType = BuildingType.NATURAL,
        detail_type: DetailType = DetailType.MASS,
        vegetation_type: VegetationType = VegetationType.POINT,
        contour_type: ContourType = ContourType.CONTOUR,
    ):
        self.options = {
            "building_type": building_type,
            "detailType": detail_type,
            "vegetation_type": vegetation_type,
            "contour_type": contour_type,
        }

    def set_file(self, zip_file: ZipFile):
        self.zip_file = zip_file
    
    #1 -2 | Operate
    def operate(self):
        try:
            self.operator.set_zip_file(self.zip_file)
            self.operator.unzip()
            self.operator.find_elements("BUILDING")
            self.operator.bake_elements_tojson()
        except Exception as e:
            raise e
        finally:
            self.operator.remove_unzipped()
        
    #1 -3 | Get Result
    def get_result(self):
        pass
    
    