from PyQt5.QtWidgets import QCheckBox

style = """
QCheckBox::indicator{
}
"""


class CustomCheckBox(QCheckBox):

    def __init__(self, container):
        super(CustomCheckBox, self).__init__(container)

    def setCheckBoxStyle(self):
        self.setStyleSheet(style)
