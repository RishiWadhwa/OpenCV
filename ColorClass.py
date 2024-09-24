import numpy as np

class Color:
    m_low_hue = 0
    m_high_hue = 0
    
    m_low_saturation = 0
    m_high_saturation = 0

    m_low_value = 0
    m_high_value = 0

    m_color_name = ""

    def __init__(self, hueL: int, saturationL: int, valueL: int, hueH: int, saturationH: int, valueH: int, name: str) -> None:
        self.m_low_hue = hueL
        self.m_low_saturation = saturationL
        self.m_low_value = valueL
        
        self.m_high_hue = hueH
        self.m_high_saturation = saturationH
        self.m_high_value = valueH

        self.m_color_name = name
    
    def getLowRange(self):
        return np.array([self.m_low_hue, self.m_low_saturation, self.m_low_value], np.uint8)

    def getHighRange(self):
        return np.array([self.m_high_hue, self.m_high_saturation, self.m_high_value], np.uint8)
    
    def getName(self):
        return self.m_color_name