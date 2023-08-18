# 필수 세팅
#-*- coding: utf-8 -*-

try:
    from typing import List, Tuple
except:
    ImportError

import math

import Rhino.Geometry as rg  # type: ignore
import scriptcontext as sc  # type: ignore

# 인풋
plan = None        # 평면 : rg.Polyline
usage = -1       # 용도 : int
fur_List = None    # 가구 : [rg.Brep]

# 가구 클래스
class Furniture:
    def __init__(self,Model=rg.GeometryBase):
        self.model = Model
        self.bbox = Model.GetBoundingBox(rg.Plane.WorldXY)
        self.area = self.get_area()
        self.height = self.get_height()
        self.width,self.depth = self.get_width()
        self.position = self.get_center()

    def get_area(self):
        
        '''
        가구의 바닥 면적을 폴리라인으로 도출하는 함수
        '''
        
        bbox = self.bbox
        points = []
        floor = min(bbox.GetCorners(),key=lambda x: x.Z).Z
        for corner in bbox.GetCorners():
            if (corner.Z == floor):
                points.append(corner)
        points.append(points[0])
        area = rg.PolylineCurve(points)

        return area
    
    def get_center(self):
        return self.area.ToPolyline().CenterPoint()
    
    def get_height(self):
        
        '''
        가구의 높이를 도출하는 함수
        '''
        bbox = self.bbox
        corners = bbox.GetCorners()
        maxPt = max(corners,key=lambda x: x.Z)
        minPt = min(corners,key=lambda x: x.Z)
        
        return maxPt.Z - minPt.Z
    
    def get_width(self):
        '''
        가구의 너비와 깊이를 도출하는 함수
        '''
        area = self.area.ToPolyline()
        lines = area.GetSegments()
        width = max(lines,key=lambda x:x.Length).Length
        depth = min(lines,key=lambda x:x.Length).Length
        return width,depth
    
class Table(Furniture):
    def __init__(self,Model=rg.GeometryBase,Type="탁자"):
        Furniture.__init__(self,Model)
        self.type = Type

class Chair(Furniture):
    def __init__(self,Model=rg.GeometryBase,Type="의자"):
        Furniture.__init__(self,Model)
        self.type = Type
        
class Shelf(Furniture):
    def __init__(self,Model=rg.GeometryBase,Type="선반"):
        Furniture.__init__(self,Model)
        self.type = Type

class Bed(Furniture):
    def __init__(self,Model=rg.GeometryBase,Type="침대"):
        Furniture.__init__(self,Model)
        self.type = Type

# 방 클래스   
class Room:
    def __init__(self,plan=rg.Polyline):
        self.plan = plan
        self.door = rg.Line(plan.First,plan.Last)
        return
    
    def get_area(self):
        return
    
    def set_roomtype(self,usage):
        
        if( usage == 1 ):
            room_type = "거실"
            room = LivingRoom(self.plan,room_type)

        elif( usage == 2 ):
            room_type = "침실"
            room = BedRoom(self.plan,room_type)

        elif( usage == 3 ):
            room_type = "주방"
            room = Kitchen(self.plan,room_type)

        elif( usage == 4 ):
            room_type = "화장실"
            room = BathRoom(self.plan,room_type)

        return  room
    
    def get_shape(self):
        lines = self.plan.GetSegments()
        return lines
        
class LivingRoom(Room):
    def __init__(self,Plan=rg.Polyline,Type=str):
        Room.__init__(self,Plan)
        self.type = Type
        
class BedRoom(Room):
    def __init__(self,Plan=rg.Polyline,Type=str):
        Room.__init__(self,Plan)
        self.type = Type
        
class Kitchen(Room):
    def __init__(self,Plan=rg.Polyline,Type=str):
        Room.__init__(self,Plan)
        self.type = Type
        
class BathRoom(Room):
    def __init__(self,Plan=rg.Polyline,Type=str):
        Room.__init__(self,Plan)
        self.type = Type

# 인풋 저장
def set_room(plan,usage):
    
    room = Room(plan)
    typeroom = room.set_roomtype(usage)
    
    return typeroom

