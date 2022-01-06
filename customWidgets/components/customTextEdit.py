from PyQt5.QtWidgets import QTextEdit

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
    def __init__(self, container):
        super(CustomTextEdit, self).__init__(container)

    def setTextStyle(self,
                     bgColor="#1e2229",
                     paddingTop=5,
                     color="rgb(226, 226, 226)",
                     borderColor="#E47900"
                     ):
        adjustedStyle = style.format(
            bgColor=bgColor,
            paddingTop=paddingTop,
            color=color,
            borderColor=borderColor
        )
        self.setStyleSheet(adjustedStyle)
        self.setReadOnly(True)
        self.setText("Console")
