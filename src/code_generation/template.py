from pyutil.util import case_conversion as cc
from code_generation.dto import Dto

class Template:
    PROPERTIES_TAG = "@@properties@@"
    PASCAL_PROPERTY_TAG = "@@property@@"
    SNAKE_PROPERTY_TAG = "@@snake_property@@"
    DTO_PROPERTY_CODE = r"""[DbValue("@@snake_property@@")]\r\n\t\tpublic sting @@property@@ { get; set; }"""
    
    def __init__(self, lines: list[str]) -> None:
        self.__original_lines = lines
        self.__bound_lines = lines
    
    def bind_properties(self, dto: Dto) -> list[str]:
        new_lines = []
        for line in self.__bound_lines:
            if self.PROPERTIES_TAG not in line:
                new_lines.append(line)
                continue
            new_lines.append(line.replace(self.PROPERTIES_TAG, dto.properties))
            break
        
        self.__bound_lines = new_lines
        print(self.__bound_lines)

    def generate_property_codes(self, properties: list[str]) -> str:
        """ Bind Properties """
        property_codes = []
        for p in properties:
            property_codes.append(self.bind_property(p))
        return "\r\n\t\t".join(property_codes)

    def bind_property(self, p: str) -> str:
        return self.DTO_PROPERTY_CODE.\
            replace(self.PASCAL_PROPERTY_TAG, cc.to_pascal_from_snake(p)).\
            replace(self.SNAKE_PROPERTY_TAG, p)
 