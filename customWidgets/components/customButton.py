from PyQt5.QtWidgets import QPushButton, QWidget


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
    def __init__(self, parent, buttonName):
        """
        Initialize button component
        :param parent: Reference of the component to which the window belongs
        :type parent: QWidget
        :param buttonName: Name of button
        :type buttonName: str
        """
        super(CustomButton, self).__init__(parent)
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
        """
        Set component style\n
        :param bgColor: Background color
        :type bgColor: str
        :param paddingTop: Padding  top
        :type paddingTop: int
        :param color: Text color
        :type color: str
        :param borderColor: Border color
        :type borderColor: str
        :param bgColorHover: Background color hover
        :type bgColorHover: str
        :param bgColorPressed: Background color pressed
        :type bgColorPressed: str
        :param borderRadius: Border Radius
        :type borderRadius: int
        """
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
