
class Model:
	PHYSICAL_NAME = "physical_name"
	PROPERTIES = "properties"
	def __init__(self, model:dict):
		self.__model = model
		self.__properties = [Model(x) for x in model.get(self.PROPERTIES, [])]

	def get_physical_name(self) -> str:
		return self.__model.get("physical_name", "UnnamedClass")
	
	def has_properties(self) -> bool:
		return True if len(self.__properties) > 0 else False
	
	def get_properties(self) -> list : return self.__properties