from commandLine import Argument

class VarInput(object):
    def __init__(self, invalid_handler=None):
        if invalid_handler is not None: self.invalidHandler = invalid_handler
        else: self.invalidHandler = self.__default_handler

    def input(self, message: str, argument: Argument):
        input_str = input(message)

        try:
            input_val = argument.get_type()(input_str)

        except ValueError:
            return self.invalidHandler(input_str, [message, argument], True)

        if not argument.get_validity_function()(input_val):
            return self.invalidHandler(input_str, [message, argument], False)

        return input_val

    def __default_handler(self, value, params, value_error):
        print("Value Invalid!")
        return self.input(*params)
