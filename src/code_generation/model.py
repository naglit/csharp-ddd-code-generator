from pyutil.util import case_conversion as cc
from code_generation.dto import Dto

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

	def __init__(self, model: dict, namespace: str = None):
		self.__model = model
		self.namespace = namespace
		physical_name = model.get(self.PHYSICAL_NAME, "UnnamedClass")
		child_namespace = f"{namespace}.{physical_name}"
		properties = [Model(x, child_namespace) for x in model.get(self.PROPERTIES, [])]
		self.__properties = properties		
	
	def has_properties(self) -> bool: return True if len(self.__properties) > 0 else False

	def has_parent_model(self) -> bool: return True if self.__parent_model_namespace != None else False

	def convert_into_dto(self) -> Dto:
		return Dto(self.namespace, self.get_physical_name(), self.get_logical_name(), self.get_db_mapping_values)

	# def __get_dto_models(self) -> list[list[str]]:
	# 	get_db_mapping_models = [self.get_db_mapping_value(model) for model in models]
	# 	for model in models:
	# 		__get_db_mapping_values(model)

	def get_db_mapping_values(self) -> list[str]:
		""" Recusively get db mapping value """
		values = [p.get_db_mapping_values() for p in self.__properties]
		values.append(self.__get_db_mapping_value())
		return values
	
	def __get_db_mapping_value(self) -> str:
		return self.__model.get(self.DB_MAPPING_VALUE, cc.to_lower_snake_from_pascal(self.get_physical_name()))

	def get_physical_name(self) -> str:
		return self.__model.get(self.PHYSICAL_NAME, "UnnamedClass")
	
	def get_logical_name(self) -> str:
		return self.__model.get(self.LOGICAL_NAME, "UnnamedClass")
	
	def get_namespace(self) -> str:
		return self.__model.get(self.NAMESPACE, "")
	
	def get_properties(self) -> list : return self.__properties