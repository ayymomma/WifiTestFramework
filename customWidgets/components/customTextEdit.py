from PyQt5.QtWidgets import QTextEdit, QWidget

style = """
QTextEdit {{
    background-color: {bgColor};
    border: none;
    padding-top: {paddingTop}px;
    color: {color};
    border-left: 1px solid {borderColor};
    border-right: 1px solid {borderColor};
    border-bottom: 5px solid {borderColor};
}}
"""


class CustomTextEdit(QTextEdit):
    def __init__(self, parent):
        """
        Initialize text edit component\n
        :param parent: Reference of the component to which the window belongs
        :type parent: QWidget
        """
        super(CustomTextEdit, self).__init__(parent)

    def setTextStyle(self,
                     bgColor="#1e2229",
                     paddingTop=5,
                     color="rgb(226, 226, 226)",
                     borderColor="#E47900"
                     ):
        """
        Set the style of component\n
        :param bgColor: Background color
        :type bgColor: str
        :param paddingTop: Top padding
        :type paddingTop: int
        :param color: Text color
        :type color: str
        :param borderColor: Border color
        :type borderColor: str
        """
        adjustedStyle = style.format(
            bgColor=bgColor,
            paddingTop=paddingTop,
            color=color,
            borderColor=borderColor
        )
        self.setStyleSheet(adjustedStyle)
        self.setReadOnly(True)
