
class Dto:
    DTO_PROPERTY_CODE = r"""[DbValue("@@snake_property@@")]\r\n\t\tpublic sting @@property@@ { get; set; }"""

    def __init__(self, namespace: str, physical_name: str, logical_name: str, properties: list[str]) -> None:
        self.namespace = namespace
        self.physical_name = physical_name
        self.logical_name = logical_name
        self.properties = properties
        self.filepath = f"{namespace.replace('.', '/')}/{physical_name}"

    def a():
        pass
