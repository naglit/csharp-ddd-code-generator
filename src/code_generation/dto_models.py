from code_generation.model import Model

class DtoModel:
    def __init__(self, model: Model):
        self.original_model = model
        self.physical_class_name = model.get_physical_name()
        self.logical_class_name = model.get_logical_name()
        self.namespace = model.get_namespace()
        self.initialization = ""
    
        