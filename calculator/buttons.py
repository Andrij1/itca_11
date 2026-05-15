btns_nums = [
    'BTN_0','BTN_1','BTN_2','BTN_3','BTN_4',
    'BTN_5', 'BTN_6', 'BTN_7','BTN_8','BTN_9',
]

for idx, btn_name in enumerate(btns_nums):

    btn = getattr(self.ui, btn_name)

    btn.clicked.connect(lambda checked=False idx: self.on_button(idx))

def on_button(self, value):
    self.ui.Display.setText(str(value))
    self.calc.set_variable(value)
