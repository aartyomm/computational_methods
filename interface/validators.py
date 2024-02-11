from PyQt6 import QtGui
from PyQt6 import QtCore


class Int_1_1000_Validator(QtGui.QRegularExpressionValidator):
    regular = QtCore.QRegularExpression('([1-9]\\d{0,2})|1000')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Int_1_1000_Validator, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super(Int_1_1000_Validator, self).__init__(self.regular)


class Double_0_1_Validator(QtGui.QRegularExpressionValidator):
    regular = QtCore.QRegularExpression('(0(\\.\\d{1,5})?)|1')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Double_0_1_Validator, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super(Double_0_1_Validator, self).__init__(self.regular)


class Double_0_1000_Validator(QtGui.QRegularExpressionValidator):
    regular = QtCore.QRegularExpression('(\\d{1,3}(\\.\\d{1,5})?)|1000')

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Double_0_1000_Validator, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        super(Double_0_1000_Validator, self).__init__(self.regular)
