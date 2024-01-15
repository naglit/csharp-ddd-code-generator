
class Template:
    PROPERTIES_TAG = "@@properties@@"
    PROPERTY_TAG = "@@property@@"
    DTO_PROPERTY_CODE = r"""public sting @@property@@ { get; set; }"""
    def __init__(self, lines: list[str]) -> None:
        self.__original_lines = lines
        self.__bound_lines = lines
    
    def bind_properties(self, properties: list[str]):
        property_codes = []
        for p in properties:
            property_codes.append(self.DTO_PROPERTY_CODE.replace(self.PROPERTY_TAG, p))
        property_codes_in_string = "\r\n\t\t".join(property_codes)
        
        new_lines = []
        for line in self.__bound_lines:
            if self.PROPERTIES_TAG not in line:
                new_lines.append(line)
                continue
            
            new_lines.append(line.replace(self.PROPERTIES_TAG, property_codes_in_string))
            break
        self.__bound_lines = new_lines
        print(self.__bound_lines)