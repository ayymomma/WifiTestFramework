from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit

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
    def __init__(self, container):
        super(CustomLineEdit, self).__init__(container)
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
