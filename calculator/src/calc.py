class Calculator:
    """
    Core calculator logic class.
    Stores operands, operator, and builds a string-based expression
    that is later evaluated to produce a result.
    """

    def __init__(self):
        """
        Initialize calculator state.
        Attributes:
            first_operand (str | None): First operand
            second_operand (str | None): Second operand
            operator (str | None): Current operator
            point (str | None): Decimal point character
            collected (str): Full expression string
        """
        self.first_operand = None
        self.second_operand = None
        self.operator = None
        self.point = None
        self.collected = ''


    def clear(self):
        """
        Reset calculator state and clear all stored values.
        """
        self.first_operand = None
        self.second_operand = None
        self.operator = None
        self.point = None
        self.collected = ''


    def set_variable(self, value):
        """
        Add a numeric value to the current expression.
        Determines whether the value belongs to the first or second operand.
        Args:
            value (int | str): Digit input from the user.
        """
        if self.first_operand is None or self.operator is None:
            self.set_first_operand(value)
        else:
            self.set_second_operand(value)
        self.collected += str(value)


    def clear_last_variable(self):
        """
        Remove the last character from the current expression string.
        """
        self.collected = self.collected[:-1]


    def set_first_operand(self, value):
        """
        Append a digit to the first operand.
        Args:
            value (int | str): Digit input.
        """
        if self.first_operand is None:
            self.first_operand = str(value)
        else:
            self.first_operand += str(value)


    def set_second_operand(self, value):
        """
        Append a digit to the second operand.
        Args:
            value (int | str): Digit input.
        """
        if self.second_operand is None:
            self.second_operand = str(value)
        else:
            self.second_operand += str(value)


    def set_operator(self, oper):
        """
        Set the arithmetic operator and update the expression string.
        Args:
            oper (str): Operator symbol (+, -, *, /, %, √, etc.)
        """
        self.operator = oper
        self.collected += self.operator


    def set_point(self, pt):
        """
        Add a decimal point to the current number if not already present.
        Args:
            pt (str): Decimal point character.
        """
        self.point = pt
        last_number = self.collected.split(self.operator)[-1] if self.operator else self.collected

        if self.point not in last_number:
            self.collected += self.point


    def calculate(self):
        """
        Evaluate the current expression and return the result.
        Supports:
        - Direct evaluation using eval()
        - Manual fallback for basic operations if eval fails
        - Square root operation
        Returns:
            float | int: Computed result
        """
        result = 0
        result_temp = 0

        if self.operator == '√':
                result = float(self.first_operand) ** 0.5
                self.collected = str(result)
                return result

        try:
            result = eval(self.collected)
            self.collected = str(result)
        except Exception:
            if self.operator == '+':
                result_temp += float(self.first_operand) + float(self.second_operand)
            elif self.operator == '-':
                result_temp += float(self.first_operand) - float(self.second_operand)
            elif self.operator == ':':
                result_temp += float(self.first_operand) / float(self.second_operand)
            elif self.operator == '*':
                result_temp += float(self.first_operand) * float(self.second_operand)
            elif self.operator == '%':
                result_temp += float(self.first_operand) % float(self.second_operand)

        return result