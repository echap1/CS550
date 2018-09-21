class VarInput(object):
    def __init__(self, invalid_handler=None):
        if invalid_handler is not None: self.invalidHandler = invalid_handler
        else: self.invalidHandler = self.__default_handler

    def input(self, message, var_type: type, validity_function=lambda x: True):
        input_str = input(message)

        try:
            input_val = var_type(input_str)

        except ValueError:
            self.invalidHandler(input_str, [message, var_type, validity_function], True)
            return None

        if not validity_function(input_val):
            self.invalidHandler(input_str, [message, var_type, validity_function], False)
            return None

        return input_val

    def __default_handler(self, value, params, valueError):
        print("Value Invalid!")
        return self.input(*params)
