from pyutil.util import case_conversion as cc
from code_generation.dto import Dto

class Template:
    NAMESPACE = "@@namespace@@"
    PHYSICAL_NAME = "@@physical_name@@"
    LOGICAL_NAME = "@@logical_name@@"
    PROPERTIES_TAG = "@@properties@@"
    PASCAL_PROPERTY_TAG = "@@property@@"
    SNAKE_PROPERTY_TAG = "@@snake_property@@"
    DTO_PROPERTY_TEMPLATE = r"""[DbValue("@@snake_property@@")]\r\n\t\tpublic sting @@property@@ { get; set; }"""
    
    def __init__(self, lines: list[str]) -> None:
        self.__original_lines = lines
        self.__bound_lines = lines
    
    def bind(self, dto: Dto) -> list[str]:
        new_lines = [self.bind_by_line(line, dto) for line in self.__bound_lines]
        print(new_lines)

    def bind_by_line(self, line: str, dto: Dto) -> str:
        new_line = line\
            .replace(self.NAMESPACE, dto.namespace)\
            .replace(self.PHYSICAL_NAME, dto.physical_name)\
            .replace(self.LOGICAL_NAME, dto.logical_name)\
            .replace(
                self.PROPERTIES_TAG,
                self.generate_property_lines(self.DTO_PROPERTY_TEMPLATE, dto.properties))
        return new_line
    
    def generate_property_lines(self, property_template: str, properties: list[str]) -> str:
        """ Bind Properties """
        property_codes = [self.bind_property(property_template, p) for p in properties]
        return "\r\n\t\t".join(property_codes)

    def bind_property(self, template: str,  p: str) -> str:
        return template.\
            replace(self.PASCAL_PROPERTY_TAG, cc.to_pascal_from_snake(p)).\
            replace(self.SNAKE_PROPERTY_TAG, p)
 