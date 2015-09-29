from PySide import QtGui, QtCore
from cdatgui.bases import RangeWidget
from cdatgui.utils import header_label
from cdatgui.cdat.axis import axis_values, selector_value
from functools import partial
import genutil


class AxisBoundsChooser(QtGui.QWidget):
    boundsEdited = QtCore.Signal(object)

    def __init__(self, axis, source_axis=None, parent=None):
        super(AxisBoundsChooser, self).__init__(parent=parent)
        if source_axis is not None:
            self.axis = source_axis
        else:
            self.axis = axis
        l = QtGui.QVBoxLayout()
        l.addWidget(header_label(axis.id))

        if source_axis is not None:
            minimum, maximum = (float(num) for num in genutil.minmax(source_axis))
            bottom, top = (float(num) for num in genutil.minmax(axis))
            for i, v in enumerate(source_axis):
                if v == bottom:
                    bot_ind = i
                if v == top:
                    top_ind = i
            self.range = RangeWidget(axis_values(source_axis), bottom=bot_ind, top=top_ind)
        else:
            minimum, maximum = (float(num) for num in genutil.minmax(axis))
            self.range = RangeWidget(axis_values(axis))

        l.addWidget(self.range)
        self.setLayout(l)

        emitter = partial(self.boundsEdited.emit, self.axis)

        self.range.boundsEdited.connect(emitter)

    def getSelector(self):
        lower, upper = self.range.getBounds()
        lower = selector_value(lower, self.axis)
        upper = selector_value(upper, self.axis)
        return self.axis.id, (lower, upper)
