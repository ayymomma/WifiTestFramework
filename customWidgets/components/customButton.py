from PyQt5.QtWidgets import QPushButton

style = """
QPushButton {{
    background-color: {bgColor};
    border: none;
    padding-top: {paddingTop}px;
    color: {color};
    border-left: 1px solid {borderColor};
    border-right: 1px solid {borderColor};
    border-bottom: 5px solid {borderColor};
    border-radius: {borderRadius}px;
}}
QPushButton:hover {{
    background-color: {bgColorHover};
    border-left: 1px solid {borderColor};
    border-right: 1px solid {borderColor};
    border-bottom: 5px solid {borderColor};
}}
QPushButton:pressed {{
    background-color: {bgColorPressed};
    border-left: 1px solid {borderColor};
    border-right: 1px solid {borderColor};
    border-bottom: 5px solid {borderColor};   
    padding-top: -{paddingTop}px;
    border-bottom: none;
}}
"""

class CustomButton(QPushButton):
    def __init__(self, container, buttonName):
        super(CustomButton, self).__init__(container)
        self.setText(buttonName)

    def setButtonStyle(self,
                       bgColor="#E47900",
                       paddingTop=3,
                       color="rgb(226, 226, 226)",
                       borderColor="#A57947",
                       bgColorHover="#FF9C2B",
                       bgColorPressed="#FF9C2B",
                       borderRadius=5
                       ):
        adjustedStyle = style.format(
            bgColor=bgColor,
            paddingTop=paddingTop,
            color=color,
            borderColor=borderColor,
            bgColorHover=bgColorHover,
            bgColorPressed=bgColorPressed,
            borderRadius=borderRadius
        )
        self.setStyleSheet(adjustedStyle)
