from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QWidget

style = """
QLineEdit {{
    border: {borderSize}px solid {borderColor};
    border-radius: {borderRadius}px;
    color: {color};
    padding-left: {paddingSize}px;
    padding-right: {paddingSize}px;
    background-color: {bgColor};
}}
QLineEdit:hover {{
    border: {borderSize}px solid {borderColorHover};
}}
QLineEdit:focus {{
    border: {borderSize}px solid {borderColorFocus};
    background-color: {bgColorFocus};
}}
"""


class CustomLineEdit(QLineEdit):
    def __init__(self, parent):
        """
        Initialize lide edit component
        :param parent: Reference of the component to which the window belongs
        :type parent: QWidget
        """
        super(CustomLineEdit, self).__init__(parent)
        self.setAlignment(Qt.AlignCenter)

    def setLineEditStyle(self,
                         borderSize=2,
                         borderColor="rgb(37, 39, 48)",
                         borderRadius=10,
                         color="rgb(226, 226, 226)",
                         paddingSize=10,
                         bgColor="#1e2229",
                         borderColorHover="rgb(48, 50, 62)",
                         borderColorFocus="#E47900",
                         bgColorFocus="rgb(43, 45, 56)"
                         ):
        """
        Set line edit style
        :param borderSize: Border Size
        :type borderSize: int
        :param borderColor: Border color
        :type borderColor: str
        :param borderRadius: Border radius
        :type borderRadius: int
        :param color: Text color
        :type color: str
        :param paddingSize: Padding size
        :type paddingSize: int
        :param bgColor: Background color
        :type bgColor: str
        :param borderColorHover: Border Color hover
        :type borderColorHover: str
        :param borderColorFocus: Border Color Focus
        :type borderColorFocus: str
        :param bgColorFocus: Background color focus
        :type bgColorFocus: str
        """
        adjustedStyle = style.format(
            borderSize=borderSize,
            borderColor=borderColor,
            borderRadius=borderRadius,
            color=color,
            paddingSize=paddingSize,
            bgColor=bgColor,
            borderColorHover=borderColorHover,
            borderColorFocus=borderColorFocus,
            bgColorFocus=bgColorFocus
        )
        self.setStyleSheet(adjustedStyle)
