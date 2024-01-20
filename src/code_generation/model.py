from pyutil.util import case_conversion as cc

class Model:
	NAMESPACE = "namespace"
	PHYSICAL_NAME = "physical_name"
	LOGICAL_NAME = "logical_name"
	INITIALIZATION = "init"
	PROPERTIES = "properties"
	DB_MAPPING_VALUE = "dto_mapping"
	
	def __init__(self, model: dict):
		""" for root model """
		self.__model = model
		self.__properties = [Model(x, self.get_physical_name()) for x in model.get(self.PROPERTIES, [])]
		self.__parent_model_namespace = None
		self.namespace = self.get_physical_name()

	def __init__(self, model: dict, parent_model_namespace: str):
		self.__model = model
		properties = [Model(x, self.namespace) for x in model.get(self.PROPERTIES, [])]
		namespace = f"{parent_model_namespace}.{self.get_physical_name()}" if len(properties) > 0 else parent_model_namespace
		self.__properties = properties
		self.__parent_model_namespace = parent_model_namespace
		self.namespace = namespace
	
	def has_properties(self) -> bool: return True if len(self.__properties) > 0 else False

	def has_parent_model(self) -> bool: return True if self.__parent_model_namespace != None else False

	def get_physical_name(self) -> str:
		return self.__model.get(self.PHYSICAL_NAME, "UnnamedClass")
	
	def get_logical_name(self) -> str:
		return self.__model.get(self.LOGICAL_NAME, "UnnamedClass")
	
	def get_namespace(self) -> str:
		return self.__model.get(self.NAMESPACE, "")
	
	def get_db_mapping_value(self) -> str:
		return self.__model.get(self.DB_MAPPING_VALUE, cc.to_lower_snake_from_pascal(self.get_physical_name()))
	
	def get_properties(self) -> list : return self.__properties