from enum import Enum


class Model:
    def __init__(self):
        pass

    def add_parameter(self):
        pass

    def set_liklihood_function(self, function):
        pass

    def get_liklihood_function(self):
        pass


class ModelParameters:
    def __init__(self, name, symbol, param_type):
        if not isinstance(param_type, ParameterType):
            raise TypeError('param_type must be an instance \
                             of ParameterType Enum')
        self.name = name
        self.type = type
        self.symbol = symbol

    def define_parameter(self, formula, *params):
        pass

    def set_value(self, value):
        pass

    def get_value(self):
        pass

    def get_symbol(self):
        pass

    def get_symbol_in_latex():
        pass


class ParameterType(Enum):
    INPUT = 0,
    MODELPARAM = 1
