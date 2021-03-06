from PySide import QtCore
from cdatgui.bases import StaticDockWidget
from cdatgui.toolbars import AddEditRemoveToolbar
from vcs_gm_list import GraphicsMethodList


class GraphicsMethodWidget(StaticDockWidget):

    def __init__(self, parent=None, flags=0):
        super(GraphicsMethodWidget, self).__init__("Graphics Methods", parent=parent, flags=flags)
        self.allowed_sides = [QtCore.Qt.DockWidgetArea.LeftDockWidgetArea]
        self.setTitleBarWidget(AddEditRemoveToolbar("Graphics Methods",
                                                    self,
                                                    self.add_gm,
                                                    self.edit_gm,
                                                    self.remove_gm))
        self.list = GraphicsMethodList()
        self.setWidget(self.list)

    def selection_change(self):
        selected = self.list.get_selected()
        if selected is None:
            return
        self.selectedGraphicsMethod.emit(selected)

    def add_gm(self):
        pass

    def edit_gm(self):
        pass

    def remove_gm(self):
        pass
