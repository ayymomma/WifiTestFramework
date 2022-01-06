from PyQt5.QtWidgets import QSlider

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
    def __init__(self, container):
        super(CustomSlider, self).__init__(container)

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
