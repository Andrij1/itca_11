class Calculator:
    def __init__(self):
        self.var1 = None
        self.var2 = None
        self.operator = None
        self.point = None
        self.collected = ''


    def clear(self):
        self.var1 = None
        self.var2 = None
        self.operator = None
        self.point = None
        self.collected = ''


    def set_variable(self, value):
        if self.var1 is None or self.operator is None:
            self.set_var1(value)
        else:
            self.set_var2(value)
        self.collected += str(value)


    def clear_last_variable(self):
        self.collected = self.collected[:-1]


    def set_var1(self, value):
        if self.var1 is None:
            self.var1 = str(value)
        else:
            self.var1 += str(value)


    def set_var2(self, value):
        if self.var2 is None:
            self.var2 = str(value)
        else:
            self.var2 += str(value)


    def set_operator(self, oper):
        self.operator = oper
        self.collected += self.operator


    def set_point(self, pt):
        self.point = pt
        last_number = self.collected.split(self.operator)[-1] if self.operator else self.collected

        if self.point not in last_number:
            self.collected += self.point


    def calculate(self):
        result = 0
        result_temp = 0

        if self.operator == '√':
                result = float(self.var1) ** 0.5
                self.collected = str(result)
                return result

        try:
            result = eval(self.collected)
            self.collected = str(result)
        except Exception:
            if self.operator == '+':
                result_temp += float(self.var1) + float(self.var2)
            elif self.operator == '-':
                result_temp += float(self.var1) - float(self.var2)
            elif self.operator == ':':
                result_temp += float(self.var1) / float(self.var2)
            elif self.operator == '*':
                result_temp += float(self.var1) * float(self.var2)
            elif self.operator == '%':
                result_temp += float(self.var1) % float(self.var2)

        except Exception:
            result = result_temp

        return result
