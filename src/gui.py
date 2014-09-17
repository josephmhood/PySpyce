# -*- coding: utf-8 -*- # ############################################################################ Python code generated with wxFormBuilder (version Sep 12 2010)## http://www.wxformbuilder.org/#### PLEASE DO "NOT" EDIT THIS FILE!###########################################################################import wximport wx.auiimport wx.grid############################################################################# Class MainFrame###########################################################################class MainFrame(wx.Frame):    def __init__(self, parent):        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,                          pos=wx.DefaultPosition, size=wx.Size(500, 300),                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)        self.menu = wx.MenuBar(0)        self.menu_schem = wx.Menu()        self.item_save = wx.MenuItem(self.menu_schem, wx.ID_ANY, u"Save",                                     wx.EmptyString, wx.ITEM_NORMAL)        self.menu_schem.AppendItem(self.item_save)        self.item_save_as = wx.MenuItem(self.menu_schem, wx.ID_ANY, u"Save As",                                        wx.EmptyString, wx.ITEM_NORMAL)        self.menu_schem.AppendItem(self.item_save_as)        self.item_open = wx.MenuItem(self.menu_schem, wx.ID_ANY, u"Open",                                     wx.EmptyString, wx.ITEM_NORMAL)        self.menu_schem.AppendItem(self.item_open)        self.item_new = wx.MenuItem(self.menu_schem, wx.ID_ANY, u"New",                                    wx.EmptyString, wx.ITEM_NORMAL)        self.menu_schem.AppendItem(self.item_new)        self.menu.Append(self.menu_schem, u"Schematic")        self.menu_devices = wx.Menu()        self.sub_elements = wx.Menu()        self.item_groud = wx.MenuItem(self.sub_elements, wx.ID_ANY, u"Ground",                                      wx.EmptyString, wx.ITEM_NORMAL)        self.sub_elements.AppendItem(self.item_groud)        self.item_R = wx.MenuItem(self.sub_elements, wx.ID_ANY,                                  u"R (Resistor)", wx.EmptyString,                                  wx.ITEM_NORMAL)        self.sub_elements.AppendItem(self.item_R)        self.item_L = wx.MenuItem(self.sub_elements, wx.ID_ANY,                                  u"L (Inductor)", wx.EmptyString,                                  wx.ITEM_NORMAL)        self.sub_elements.AppendItem(self.item_L)        self.item_C = wx.MenuItem(self.sub_elements, wx.ID_ANY,                                  u"C (Capacitor)", wx.EmptyString,                                  wx.ITEM_NORMAL)        self.sub_elements.AppendItem(self.item_C)        self.menu_devices.AppendSubMenu(self.sub_elements, u"Elements")        self.sub_sources = wx.Menu()        self.item_V = wx.MenuItem(self.sub_sources, wx.ID_ANY, u"V (DC)",                                  wx.EmptyString, wx.ITEM_NORMAL)        self.sub_sources.AppendItem(self.item_V)        self.item_VSin = wx.MenuItem(self.sub_sources, wx.ID_ANY, u"V (Sine)",                                     wx.EmptyString, wx.ITEM_NORMAL)        self.sub_sources.AppendItem(self.item_VSin)        self.item_VPulse = wx.MenuItem(self.sub_sources, wx.ID_ANY,                                       u"V (Pulse)", wx.EmptyString,                                       wx.ITEM_NORMAL)        self.sub_sources.AppendItem(self.item_VPulse)        self.item_VPwl = wx.MenuItem(self.sub_sources, wx.ID_ANY, u"V (Pwl)",                                     wx.EmptyString, wx.ITEM_NORMAL)        self.sub_sources.AppendItem(self.item_VPwl)        self.item_I = wx.MenuItem(self.sub_sources, wx.ID_ANY, u"I (DC)",                                  wx.EmptyString, wx.ITEM_NORMAL)        self.sub_sources.AppendItem(self.item_I)        self.menu_devices.AppendSubMenu(self.sub_sources, u"Sources")        self.sub_semi = wx.Menu()        self.item_D = wx.MenuItem(self.sub_semi, wx.ID_ANY, u"Diode",                                  wx.EmptyString, wx.ITEM_NORMAL)        self.sub_semi.AppendItem(self.item_D)        self.menu_devices.AppendSubMenu(self.sub_semi, u"Semiconductors")        self.menu.Append(self.menu_devices, u"Devices")        self.menu_gadgets = wx.Menu()        self.item_vscope = wx.MenuItem(self.menu_gadgets, wx.ID_ANY,                                       u"Voltage Scope", wx.EmptyString,                                       wx.ITEM_NORMAL)        self.menu_gadgets.AppendItem(self.item_vscope)        self.item_vscope3 = wx.MenuItem(self.menu_gadgets, wx.ID_ANY,                                       u"Voltage Scope (3ph)", wx.EmptyString,                                       wx.ITEM_NORMAL)        self.menu_gadgets.AppendItem(self.item_vscope3)        self.item_iscope = wx.MenuItem(self.menu_gadgets, wx.ID_ANY,                                       u"Current Scope", wx.EmptyString,                                       wx.ITEM_NORMAL)        self.menu_gadgets.AppendItem(self.item_iscope)        self.menu.Append(self.menu_gadgets, u"Gadgets")        self.menu_run = wx.Menu()        self.item_setup = wx.MenuItem(self.menu_run, wx.ID_ANY, u"Setup",                                      wx.EmptyString, wx.ITEM_NORMAL)        self.menu_run.AppendItem(self.item_setup)        self.item_run = wx.MenuItem(self.menu_run, wx.ID_ANY, u"Run",                                    wx.EmptyString, wx.ITEM_NORMAL)        self.menu_run.AppendItem(self.item_run)        self.menu.Append(self.menu_run, u"Run")        self.SetMenuBar(self.menu)        szr_main = wx.GridSizer(1, 1, 0, 0)        self.ntb_main = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition,                                           wx.DefaultSize,                                           wx.aui.AUI_NB_DEFAULT_STYLE)        szr_main.Add(self.ntb_main, 1, wx.EXPAND, 5)        self.SetSizer(szr_main)        self.Layout()        self.Centre(wx.BOTH)        # Connect Events        self.Bind(wx.EVT_MENU, self.on_save, id=self.item_save.GetId())        self.Bind(wx.EVT_MENU, self.on_save_as, id=self.item_save_as.GetId())        self.Bind(wx.EVT_MENU, self.on_open, id=self.item_open.GetId())        self.Bind(wx.EVT_MENU, self.on_new_schem, id=self.item_new.GetId())        self.Bind(wx.EVT_MENU, self.on_add_ground, id=self.item_groud.GetId())        self.Bind(wx.EVT_MENU, self.on_add_R, id=self.item_R.GetId())        self.Bind(wx.EVT_MENU, self.on_add_L, id=self.item_L.GetId())        self.Bind(wx.EVT_MENU, self.on_add_C, id=self.item_C.GetId())        self.Bind(wx.EVT_MENU, self.on_add_V, id=self.item_V.GetId())        self.Bind(wx.EVT_MENU, self.on_add_VSin, id=self.item_VSin.GetId())        self.Bind(wx.EVT_MENU, self.on_add_VPulse, id=self.item_VPulse.GetId())        self.Bind(wx.EVT_MENU, self.on_add_VPwl, id=self.item_VPwl.GetId())        self.Bind(wx.EVT_MENU, self.on_add_I, id=self.item_I.GetId())        self.Bind(wx.EVT_MENU, self.on_add_D, id=self.item_D.GetId())        self.Bind(wx.EVT_MENU, self.on_add_vscope, id=self.item_vscope.GetId())        self.Bind(wx.EVT_MENU, self.on_add_vscope3, id=self.item_vscope3.GetId())        self.Bind(wx.EVT_MENU, self.on_add_iscope, id=self.item_iscope.GetId())        self.Bind(wx.EVT_MENU, self.on_setup, id=self.item_setup.GetId())        self.Bind(wx.EVT_MENU, self.on_run, id=self.item_run.GetId())        self.ntb_main.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE,                           self.on_page_close)    def __del__(self):        pass    # Virtual event handlers, overide them in your derived class    def on_save(self, event):        event.Skip()    def on_save_as(self, event):        event.Skip()    def on_open(self, event):        event.Skip()    def on_new_schem(self, event):        event.Skip()    def on_add_ground(self, event):        event.Skip()    def on_add_R(self, event):        event.Skip()    def on_add_L(self, event):        event.Skip()    def on_add_C(self, event):        event.Skip()    def on_add_V(self, event):        event.Skip()    def on_add_VSin(self, event):        event.Skip()    def on_add_VPulse(self, event):        event.Skip()    def on_add_VPwl(self, event):        event.Skip()    def on_add_I(self, event):        event.Skip()    def on_add_D(self, event):        event.Skip()    def on_add_vscope(self, event):        event.Skip()    def on_add_vscope3(self, event):        event.Skip()    def on_add_iscope(self, event):        event.Skip()    def on_setup(self, event):        event.Skip()    def on_run(self, event):        event.Skip()    def on_page_close(self, event):        event.Skip()############################################################################# Class PropertyDialog###########################################################################class PropertyDialog(wx.Dialog):    def __init__(self, parent):        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Properties",                           pos=wx.DefaultPosition, size=wx.DefaultSize,                           style=wx.DEFAULT_DIALOG_STYLE)        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)        self.szr_main = wx.BoxSizer(wx.VERTICAL)        self.propgrid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition,                                     wx.DefaultSize, 0)        # Grid        self.propgrid.CreateGrid(0, 1)        self.propgrid.EnableEditing(True)        self.propgrid.EnableGridLines(True)        self.propgrid.EnableDragGridSize(False)        self.propgrid.SetMargins(0, 0)        # Columns        self.propgrid.EnableDragColMove(False)        self.propgrid.EnableDragColSize(True)        self.propgrid.SetColLabelSize(0)        self.propgrid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)        # Rows        self.propgrid.EnableDragRowSize(True)        self.propgrid.SetRowLabelSize(200)        self.propgrid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)        # Label Appearance        # Cell Defaults        self.propgrid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)        self.szr_main.Add(self.propgrid, 0, 0, 5)        dlg_btns = wx.StdDialogButtonSizer()        self.dlg_btnsOK = wx.Button(self, wx.ID_OK)        dlg_btns.AddButton(self.dlg_btnsOK)        self.dlg_btnsCancel = wx.Button(self, wx.ID_CANCEL)        dlg_btns.AddButton(self.dlg_btnsCancel)        dlg_btns.Realize();        self.szr_main.Add(dlg_btns, 1, wx.EXPAND, 5)        self.SetSizer(self.szr_main)        self.Layout()        self.szr_main.Fit(self)        self.Centre(wx.BOTH)        # Connect Events        self.propgrid.Bind(wx.grid.EVT_GRID_CELL_CHANGE, self.on_grid_update)    def __del__(self):        pass    # Virtual event handlers, overide them in your derived class    def on_grid_update(self, event):        event.Skip()	