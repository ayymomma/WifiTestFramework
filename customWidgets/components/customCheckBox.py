from PyQt5.QtWidgets import QCheckBox, QWidget

style = """
QCheckBox::indicator{
}
"""


class CustomCheckBox(QCheckBox):

    def __init__(self, parent):
        """
        Initialize checkbox component\n
        :param parent: Reference of the component to which the window belongs
        :type parent: QWidget
        """
        super(CustomCheckBox, self).__init__(parent)

    def setCheckBoxStyle(self):
        """
        Set component style
        """
        self.setStyleSheet(style)
