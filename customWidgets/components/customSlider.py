from PyQt5.QtWidgets import QSlider, QWidget

style = """
QSlider {{ 
    margin: {margin}px;
    border-style: none;
}}
QSlider::groove:horizontal {{
    border-radius: {bgRadius}px;
    height: {bgSize}px;
    background-color: {bgColor};
}}
QSlider::groove:horizontal:hover {{ background-color: {bgColorHover}; }}
QSlider::handle:horizontal {{
    border: none;
    height: {handleSize}px;
    width: {handleSize}px;
    margin: {handleMargin}px;
    border-radius: {handleRadius}px;
    background-color: {handleColor};
}}
QSlider::handle:horizontal:hover {{ background-color: {handleColorHover}; }}
QSlider::handle:horizontal:pressed {{ background-color: {handleColorPressed}; }}
"""


class CustomSlider(QSlider):
    def __init__(self, parent):
        """
        Initialize slider component\n
        :param parent: Reference of the component to which the window belongs
        :type parent: QWidget
        """
        super(CustomSlider, self).__init__(parent)
        self.setMaximum(250)

    def setSliderStyle(self, margin=0,
                       bgSize=20,
                       bgRadius=10,
                       bgColor="#1e2229",
                       bgColorHover="rgb(181, 181, 181)",
                       handleMargin=2,
                       handleSize=16,
                       handleRadius=8,
                       handleColor="#E47900",
                       handleColorHover="#FF9C2B",
                       handleColorPressed="#A57947"
                       ):
        """
        Set Slider style\n
        :param margin: Margin of slider
        :type margin: int
        :param bgSize: Background size ( Height )
        :type bgSize: int
        :param bgRadius: Background radius
        :type bgRadius: int
        :param bgColor: Background color
        :type bgColor: str
        :param bgColorHover: Background hover color
        :type bgColorHover: str
        :param handleMargin: Handler margin
        :type handleMargin: int
        :param handleSize: Handler size
        :type handleSize: int
        :param handleRadius: Handler radius
        :type handleRadius: int
        :param handleColor: Handler color
        :type handleColor: str
        :param handleColorHover: Handler hover color
        :type handleColorHover: str
        :param handleColorPressed: Handler pressed color
        :type handleColorPressed: str
        """
        adjustedStyle = style.format(
            margin=margin,
            bgSize=bgSize,
            bgRadius=bgRadius,
            bgColor=bgColor,
            bgColorHover=bgColorHover,
            handleMargin=handleMargin,
            handleSize=handleSize,
            handleRadius=handleRadius,
            handleColor=handleColor,
            handleColorHover=handleColorHover,
            handleColorPressed=handleColorPressed
        )
        self.setStyleSheet(adjustedStyle)

    def getValue(self):
        """
        Get slider value\n
        :return: Slider value in raport with motor speed
        :rtype: int
        """
        return int((self.value() * 13000) / 250)
