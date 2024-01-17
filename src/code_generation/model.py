from pyutil.util import case_conversion as cc

class Model:
	PHYSICAL_NAME = "physical_name"
	LOGICAL_NAME = "logical_name"
	PROPERTIES = "properties"
	DB_MAPPING_VALUE = "dto_mapping"
	
	def __init__(self, model:dict):
		self.__model = model
		self.__properties = [Model(x) for x in model.get(self.PROPERTIES, [])]

	def get_physical_name(self) -> str:
		return self.__model.get(self.PHYSICAL_NAME, "UnnamedClass")
	def get_logical_name(self) -> str:
		return self.__model.get(self.LOGICAL_NAME, "UnnamedClass")
	def get_namespace(self) -> str:
		return self.__model.get(self.NAMESPACE, "")
	
	def has_properties(self) -> bool:
		return True if len(self.__properties) > 0 else False

	def get_db_mapping_value(self) -> str:
		return self.__model.get(self.DB_MAPPING_VALUE, cc.to_lower_snake_from_pascal(self.get_physical_name()))
	
	def get_properties(self) -> list : return self.__properties