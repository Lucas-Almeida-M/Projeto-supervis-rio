#from ast import Str
from xml.dom.minidom import CharacterData
from db import Base
from sqlalchemy import Column, Integer,Float, DateTime, String

class DadoCLP(Base):
    """
    Modelo dos dados do CLP
    """
    __tablename__='dadosclp'
    id = Column(Integer,primary_key=True,autoincrement=True)
    timestamp = Column(DateTime)
    FT_001 = Column(Float)
    FT_002 = Column(Float)
    PT_001 = Column(Float)
    PT_002 = Column(Float)
    PT_003 = Column(Float)
    PT_004 = Column(Float)
    TE_001 = Column(Float)
    TE_002 = Column(Float)
    TE_003 = Column(Float)
    TT_001 = Column(Float)
    TT_002 = Column(Float)
    TT_003 = Column(Float)
    FZ_003 = Column(Float)
    FZ_001 = Column(Float)
    FZ_002 = Column(Float)
    SV_001 = Column(Integer)
    SV_002 = Column(Integer)
    SV_003 = Column(Integer)
    SV_004 = Column(Integer)
    SV_005 = Column(Integer)
    SV_006 = Column(Integer)
    SV_007 = Column(Integer)
    SV_008 = Column(Integer)
    LSH_001 = Column(Integer)
    LSL_001 = Column(Integer)
    LSL_002 = Column(Integer)
    BY_001 = Column(Integer)
    FY_001 = Column(Integer)
    FY_002 = Column(Integer)
    FY_003 = Column(Integer)
    EE_101 = Column(Float)
    EE_102 = Column(Float)
    EE_103 = Column(Float)
    IE_101 = Column(Float)
    IE_102 = Column(Float) 
    IE_103 = Column(Float)
    TE_101 = Column(Float)
    SE_101 = Column(Float)
    EE_201 = Column(Float)
    EE_202 = Column(Float)
    IE_201 = Column(Float)
    TE_201 = Column(Float)
    TE_202 = Column(Float)
    EE_301 = Column(Float)
    EE_302 = Column(Float)
    EE_303 = Column(Float)
    IE_301 = Column(Float)
    IE_302 = Column(Float)
    IE_303 = Column(Float)
    TE_301 = Column(Float)
    ST_301 = Column(Float)
    WT_401 = Column(Float)
    TE_401 = Column(Float)
    WT_402 = Column(Float)
    TE_402 = Column(Float)
    falhas = Column(String)
   
    

    def dadoDicionario(self):
        
            dic = {'timestamp':self.timestamp,
            'FT_001':self.FT_001,
            'FT_002': self.FT_002,
            'PT_001': self.PT_001,
            'PT_002':self.PT_002,
            'PT_003': self.PT_003,
            'PT_004':self.PT_004,
            'TE_001': self.TE_001,
            'TE_002': self.TE_002,
            'TE_003': self.TE_003,
            'TT_001': self.TT_001,
            'TT_002': self.TT_002,
            'TT_003': self.TT_003,
            'FZ_003':self.FZ_003,
            'FZ_001': self.FZ_001,
            'FZ_002':self.FZ_002,
            'SV_001': self.SV_001,
            'SV_002': self.SV_002,
            'SV_003': self.SV_003,
            'SV_004': self.SV_004,
            'SV_005': self.SV_005,
            'SV_006': self.SV_006,
            'SV_007': self.SV_007,
            'SV_008': self.SV_008,
            'LSH_001': self.LSH_001,
            'LSL_001': self.LSL_001,
            'LSL_002': self.LSL_002,
            'BY_001': self.BY_001,
            'FY_001': self.FY_001,
            'FY_002': self.FY_002,
            'FY_003': self.FY_003,
            'EE_101': self.EE_101,
            'EE_102': self.EE_102,
            'EE_103': self.EE_103,
            'IE_101': self.IE_101,
            'IE_102': self.IE_102,
            'IE_103': self.IE_103,
            'TE_101': self.TE_101,
            'SE_101': self.SE_101,
            'EE_201': self.EE_201,
            'EE_202': self.EE_202,
            'IE_201': self.IE_201,
            'TE_201': self.TE_201,
            'TE_202': self.TE_202,
            'EE_301': self.EE_301,
            'EE_302': self.EE_302,
            'EE_303': self.EE_303,
            'IE_301': self.IE_301,
            'IE_302': self.IE_302,
            'IE_303': self.IE_303,
            'TE_301': self.TE_301,
            'ST_301': self.ST_301,
            'WT_401': self.WT_401,
            'TE_401': self.TE_401,
            'WT_402': self.WT_402,
            'TE_402': self.TE_402,
            'falhas': self.falhas
            }
            return dic