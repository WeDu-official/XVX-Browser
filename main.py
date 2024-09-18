import os.path
import subprocess
import urllib.parse
import wx
import wx.aui
import wx.lib.platebtn
import wx.html2
import wx.lib.agw.aui.tabart
bg = [254,254,254]
tex = [0,0,0]
bn = [200, 200, 200]
SCHEME = {
    'background': wx.Colour(254, 254, 254),  # Dark gray
    'text': wx.Colour(0,0,0),
    'button_normal': wx.Colour(200, 200, 200),  # Darker buttons
}
LIGHT_SCHEME = {
    'background': wx.Colour(254, 254, 254),  # Dark gray
    'text': wx.Colour(0,0,0),
    'button_normal': wx.Colour(200, 200, 200),  # Darker buttons
}
validurl = False
bookmarks = []
lm = 'False'
sbmc = 'True'
CAD = False
par = None
asasa = None
hisd = 'False'
tko = ""
q1 = 'True'
q2 = 'True'
q3 = 'True'
class themepage(wx.Panel):
    def __init__(self,parent):
        global bg,tex,bn,CAD
        wx.Panel.__init__(self, parent=parent)
        self.parent = parent
        self.frame = wx.GetTopLevelParent(self)
        self.frame.SetBackgroundColour(LIGHT_SCHEME['background'])
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.new = wx.Button(self, label='+', size=(30, 30), style=wx.DOUBLE_BORDER)
        self.new.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        self.new.SetToolTip(wx.ToolTip('Open a new tab'))
        self.new.Bind(wx.EVT_ENTER_WINDOW, self.hovered_new)
        self.new.Bind(wx.EVT_LEAVE_WINDOW, self.leave_new)
        self.new.Bind(wx.EVT_BUTTON, self.tab_new)
        row1_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.label1 = wx.StaticText(self, label="Red")
        self.input1 = wx.TextCtrl(self)
        self.label2 = wx.StaticText(self, label="Green")
        self.input2 = wx.TextCtrl(self)
        self.label3 = wx.StaticText(self, label="Blue")
        self.input3 = wx.TextCtrl(self)
        per1 = wx.StaticText(self, label=f"background({bg[0]},{bg[1]},{bg[2]}),(254,254,254)")
        row1_sizer.Add(self.label1, 0, wx.ALL, 5)
        row1_sizer.Add(self.input1, 0, wx.ALL, 5)
        row1_sizer.Add(self.label2, 0, wx.ALL, 5)
        row1_sizer.Add(self.input2, 0, wx.ALL, 5)
        row1_sizer.Add(self.label3, 0, wx.ALL, 5)
        row1_sizer.Add(self.input3, 0, wx.ALL, 5)
        row1_sizer.Add(per1,0,wx.ALL,5)
        row1_sizer.Add(self.new, 0, wx.ALL, 5)
        self.sizer.Add(row1_sizer, 0, wx.ALL, 5)
        # Create the second row of input places and labels
        row2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.label4 = wx.StaticText(self, label="Red")
        self.input4 = wx.TextCtrl(self)
        self.label5 = wx.StaticText(self, label="Green")
        self.input5 = wx.TextCtrl(self)
        self.label6 = wx.StaticText(self, label="Blue")
        self.input6 = wx.TextCtrl(self)
        self.ch = wx.Button(self, label='check')
        self.ch.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.ch.SetForegroundColour(LIGHT_SCHEME['text'])
        self.ch.SetToolTip(wx.ToolTip('check if you can make a new theme'))
        self.ch.Bind(wx.EVT_ENTER_WINDOW, self.hovered_ch)
        self.ch.Bind(wx.EVT_LEAVE_WINDOW, self.leave_ch)
        self.ch.Bind(wx.EVT_BUTTON, self.check)
        per2 = wx.StaticText(self, label=f"text({tex[0]},{tex[1]},{tex[2]}),(0,0,0)")
        row2_sizer.Add(self.label4, 0, wx.ALL, 5)
        row2_sizer.Add(self.input4, 0, wx.ALL, 5)
        row2_sizer.Add(self.label5, 0, wx.ALL, 5)
        row2_sizer.Add(self.input5, 0, wx.ALL, 5)
        row2_sizer.Add(self.label6, 0, wx.ALL, 5)
        row2_sizer.Add(self.input6, 0, wx.ALL, 5)
        row2_sizer.Add(per2,0,wx.ALL,5)
        row2_sizer.Add(self.ch, 0, wx.ALL, 5)
        self.sizer.Add(row2_sizer, 0, wx.ALL, 5)
        row3_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.label7 = wx.StaticText(self, label="Red")
        self.input7 = wx.TextCtrl(self)
        self.label8 = wx.StaticText(self, label="Green")
        self.input8 = wx.TextCtrl(self)
        self.label9 = wx.StaticText(self, label="Blue")
        self.input9 = wx.TextCtrl(self)
        per3 = wx.StaticText(self, label=f"Buttons({bn[0]},{bn[1]},{bn[2]}),(200,200,200)")
        self.send = wx.Button(self,label='save changes')
        self.send.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.send.SetForegroundColour(LIGHT_SCHEME['text'])
        self.send.SetToolTip(wx.ToolTip('save the new theme'))
        self.send.Bind(wx.EVT_ENTER_WINDOW, self.hovered_send)
        self.send.Bind(wx.EVT_LEAVE_WINDOW, self.leave_send)
        self.send.Bind(wx.EVT_BUTTON,self.doit)
        self.send.Disable()
        row3_sizer.Add(self.label7, 0, wx.ALL, 5)
        row3_sizer.Add(self.input7, 0, wx.ALL, 5)
        row3_sizer.Add(self.label8, 0, wx.ALL, 5)
        row3_sizer.Add(self.input8, 0, wx.ALL, 5)
        row3_sizer.Add(self.label9, 0, wx.ALL, 5)
        row3_sizer.Add(self.input9, 0, wx.ALL, 5)
        row3_sizer.Add(per3, 0, wx.ALL, 10)
        row3_sizer.Add(self.send,0,wx.BOTTOM|wx.CENTER,5)
        self.sizer.Add(row3_sizer, 0, wx.ALL, 5)
        self.SetSizer(self.sizer)
        self.Layout()
    def check(self,event):
        global CAD
        if self.input1.GetValue() != '':
            CAD = True
        if self.input2.GetValue() != '':
            CAD = True
        if self.input3.GetValue() != '':
            CAD = True
        if self.input4.GetValue() != '':
            CAD = True
        if self.input5.GetValue() != '':
            CAD = True
        if self.input6.GetValue() != '':
            CAD = True
        if self.input7.GetValue() != '':
            CAD = True
        if self.input8.GetValue() != '':
            CAD = True
        if self.input9.GetValue() != '':
            CAD = True
        if CAD is True:
            self.send.Enable()
            CAD = False
        event.Skip()
    def doit(self,event):
        global LIGHT_SCHEME,bg,tex,bn,CAD
        if self.input1.GetValue() == '':
            v1=254
        else:
            v1=int(self.input1.GetValue())
        if self.input2.GetValue() == '':
            v2=254
        else:
            v2=int(self.input2.GetValue())
        if self.input3.GetValue() == '':
            v3=254
        else:
            v3=int(self.input3.GetValue())
        if self.input4.GetValue() == '':
            v4=0
        else:
            v4=int(self.input4.GetValue())
        if self.input5.GetValue() == '':
            v5=0
        else:
            v5=int(self.input5.GetValue())
        if self.input6.GetValue() == '':
            v6=0
        else:
            v6=int(self.input6.GetValue())
        if self.input7.GetValue() == '':
            v7=254
        else:
            v7=int(self.input7.GetValue())
        if self.input8.GetValue() == '':
            v8=254
        else:
            v8=int(self.input8.GetValue())
        if self.input9.GetValue() == '':
            v9=254
        else:
            v9=int(self.input9.GetValue())
        LIGHT_SCHEME = {'background':wx.Colour(v1,v2,v3),
'text':wx.Colour(v4,v5,v6),
'button_normal':wx.Colour(v7,v8,v9)}
        bg = [v1,v2,v3]
        tex = [v4,v5,v6]
        bn = [v7,v8,v9]
        self.send.Disable()
        event.Skip()
    def hovered_new(self,event):
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_new(self,event):
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def hovered_ch(self,event):
        self.ch.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_ch(self,event):
        self.ch.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def hovered_send(self,event):
        self.send.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_send(self,event):
        self.send.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def tab_new(self, event):
        page = WebPage(self.parent, [])
        self.parent.AddPage(page, caption="Loading", select=True)
    def on_close(self):
        self.open = False
    def on_select(self):
        self.frame.SetTitle("XVX Browser History")
class HistoryPage(wx.Panel):
    def __init__(self, parent, history_var):
        wx.Panel.__init__(self, parent=parent)
        self.open = True
        self.parent = parent
        self.history_var = history_var
        self.frame = wx.GetTopLevelParent(self)
        self.frame.SetBackgroundColour(LIGHT_SCHEME['background'])
        pagesizer = wx.BoxSizer(wx.VERTICAL)
        self.listbox = listbox = wx.ListBox(self)
        top_bar_container = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, label='Double-click on an item to open it.', style=wx.ST_ELLIPSIZE_END)
        self.new = wx.Button(self, label='+', size=(30, 30), style=wx.DOUBLE_BORDER)
        self.new.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        self.new.Bind(wx.EVT_ENTER_WINDOW, self.hovered_new)
        self.new.Bind(wx.EVT_LEAVE_WINDOW, self.leave_new)
        new_tip = wx.ToolTip('Open a new tab')
        self.new.SetToolTip(new_tip)
        self.delh = wx.Button(self, label='-', size=(30, 30), style=wx.DOUBLE_BORDER)
        self.delh.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.delh.SetForegroundColour(LIGHT_SCHEME['text'])
        self.delh.Bind(wx.EVT_ENTER_WINDOW, self.hovered_delh)
        self.delh.Bind(wx.EVT_LEAVE_WINDOW, self.leave_delh)
        d_tip = wx.ToolTip('delete selected item from history')
        self.delh.SetToolTip(d_tip)
        top_bar_container.Add(label, 1, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        top_bar_container.AddSpacer(30)
        top_bar_container.Add(self.delh, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 5)
        top_bar_container.Add(self.new, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 5)
        pagesizer.Add(top_bar_container, proportion=False, flag=wx.EXPAND)
        pagesizer.Add(listbox, proportion=True, flag=wx.EXPAND)
        self.new.Bind(wx.EVT_BUTTON, self.tab_new)
        self.delh.Bind(wx.EVT_BUTTON, self.deletehis)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.open_link)
        self.SetSizer(pagesizer)
        self.refresh()
    def hovered_delh(self,event):
        self.delh.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_delh(self,event):
        self.delh.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def hovered_new(self,event):
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_new(self,event):
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def refresh(self):
        if self.open:
            try:
                self.listbox.AppendItems(self.history_var[len(self.listbox.GetItems()):])
                wx.CallLater(3000, self.refresh)
            except:
                pass
    def deletehis(self, event):
        index = event.GetSelection()

        # Check if an item is selected
        if index != wx.NOT_FOUND:
            # Get the selected item
            selected_item = self.listbox.GetStringSelection()
            for i, item in enumerate(self.history_var):
                if item == selected_item:
                    try:
                        self.listbox.Delete(i)
                    except (IndexError):
                        pass
                    try:
                        self.history_var.pop(i)
                    except (IndexError):
                        pass
    def open_link(self, event):
        page = WebPage(self.parent, self.history_var, url=event.GetString())
        self.parent.AddPage(page, caption="Loading")
    def tab_new(self, event):
        page = WebPage(self.parent, self.history_var)
        self.parent.AddPage(page, caption="Loading", select=True)
    def on_close(self):
        self.open = False
    def on_select(self):
        self.frame.SetTitle("XVX Browser History")
class SourceCode(wx.Panel):
    def __init__(self, parent, windowname, windowurl, history_var, *args, **kwargs):
        wx.Panel.__init__(self, parent)
        self.name = windowname
        self.parent = parent
        self.history_var = history_var
        self.frame = wx.GetTopLevelParent(self)
        self.frame.SetBackgroundColour(LIGHT_SCHEME['background'])
        pagesizer = wx.BoxSizer(wx.VERTICAL)
        self.source = source = wx.TextCtrl(self, *args, **kwargs)
        top_bar_container = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, label=('Source: ' + windowurl), style=wx.ST_ELLIPSIZE_END)
        self.new = wx.Button(self, label='+', size=(30, 30), style=wx.DOUBLE_BORDER)
        self.new.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        self.new.Bind(wx.EVT_ENTER_WINDOW, self.hovered_new)
        self.new.Bind(wx.EVT_LEAVE_WINDOW, self.leave_new)
        new_tip = wx.ToolTip('Open a new tab')
        self.new.SetToolTip(new_tip)
        top_bar_container.Add(label, 1, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        top_bar_container.AddSpacer(30)
        top_bar_container.Add(self.new, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 5)
        pagesizer.Add(top_bar_container, proportion=False, flag=wx.EXPAND)
        pagesizer.Add(source, proportion=True, flag=wx.EXPAND)
        self.new.Bind(wx.EVT_BUTTON, self.tab_new)
        self.SetSizer(pagesizer)
    def on_select(self):
        self.frame.SetTitle(self.name)
    def tab_new(self, event):
        page = WebPage(self.parent, self.history_var)
        self.parent.AddPage(page, caption="Loading", select=True)
    def hovered_new(self,event):
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_new(self,event):
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def on_close(self):
        pass
class BookmarkPage(wx.Panel):
    def __init__(self, parent, bo1okmarks,bm):
        wx.Panel.__init__(self, parent=parent)
        self.bm = bm
        self.open = True
        self.parent = parent
        self.bookmarks = bo1okmarks
        self.frame = wx.GetTopLevelParent(self)
        self.frame.SetBackgroundColour(LIGHT_SCHEME['background'])
        pagesizer = wx.BoxSizer(wx.VERTICAL)
        self.listbox = listbox = wx.ListBox(self)
        top_bar_container = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, label='Double-click on an item to open it.', style=wx.ST_ELLIPSIZE_END)
        self.new = wx.Button(self, label='+', size=(30, 30), style=wx.DOUBLE_BORDER)
        self.new.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        self.new.Bind(wx.EVT_ENTER_WINDOW, self.hovered_new)
        self.new.Bind(wx.EVT_LEAVE_WINDOW, self.leave_new)
        new_tip = wx.ToolTip('Open a new tab')
        self.new.SetToolTip(new_tip)
        self.delb = wx.Button(self, label='-', size=(30, 30), style=wx.DOUBLE_BORDER)
        self.delb.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.delb.SetForegroundColour(LIGHT_SCHEME['text'])
        self.delb.Bind(wx.EVT_ENTER_WINDOW, self.hovered_delb)
        self.delb.Bind(wx.EVT_LEAVE_WINDOW, self.leave_delb)
        db_tip = wx.ToolTip('delete selected item from bookmarks')
        self.delb.SetToolTip(db_tip)
        top_bar_container.Add(label, 1, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        top_bar_container.AddSpacer(30)
        top_bar_container.Add(self.delb, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 5)
        top_bar_container.Add(self.new, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 5)
        pagesizer.Add(top_bar_container, proportion=False, flag=wx.EXPAND)
        pagesizer.Add(listbox, proportion=True, flag=wx.EXPAND)
        self.delb.Bind(wx.EVT_BUTTON, self.deleteb)
        self.new.Bind(wx.EVT_BUTTON, self.tab_new)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.open_link)
        self.SetSizer(pagesizer)
        self.refresh()
    def hovered_delb(self,event):
        self.delb.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_delb(self,event):
        self.delb.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def hovered_new(self,event):
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_new(self,event):
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def deleteb(self,event):
        index = event.GetSelection()
        # Check if an item is selected
        if index != wx.NOT_FOUND:
            # Get the selected item
            selected_item = self.listbox.GetStringSelection()
            for i, item in enumerate(self.bookmarks):
                if item == selected_item:
                    self.bookmarks.pop(i)
                    try:
                        bookmarks.pop(i)
                    except IndexError:
                        pass
                    self.listbox.Delete(i)
                    for d, item2 in enumerate(self.bm):
                        if item2 == selected_item:
                            self.bm.pop(d)
                    try:
                        try:
                            write = open('bookmarks.txt', 'w')
                            write.write("\n".join(self.bm))
                            write.close()
                        except(OSError, PermissionError):
                            wx.MessageBox('it might be OS or permission problem to write in bookmarks.txt',
                                          'Error with bookmarks',
                                          wx.OK | wx.ICON_ERROR)
                    except FileNotFoundError:
                        open('bookmarks.txt', 'x')
    def refresh(self):
        if self.open:
            try:
                self.listbox.AppendItems(self.bookmarks[len(self.listbox.GetItems()):])
                wx.CallLater(3000, self.refresh)
            except:
                pass
    def open_link(self, event):
        page = WebPage(self.parent, self.bookmarks, url=event.GetString())
        self.parent.AddPage(page, caption="Loading")
    def tab_new(self, event):
        page = WebPage(self.parent, self.bookmarks)
        self.parent.AddPage(page, caption="Loading", select=True)
    def on_close(self):
        self.open = False
    def on_select(self):
        self.frame.SetTitle("XVX Browser History")
class WebPage(wx.Panel):
    def __init__(self, parent, history_var, url=f"file:///{os.path.dirname(os.path.abspath(__file__)).replace('\\','/')}/home.html"):
        global par,asasa
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundColour(LIGHT_SCHEME['background'])
        self.parent = parent
        par = self.parent
        self.visited = history_var
        asasa = self.visited
        self.remember_history = True
        self.frame = wx.GetTopLevelParent(self)
        self.frame.SetBackgroundColour(LIGHT_SCHEME['background'])
        self.pagesizer = pagesizer = wx.BoxSizer(wx.VERTICAL)
        self.top_bar_container = top_bar_container = wx.FlexGridSizer(1, 10, 4, 4)
        self.back = back = wx.Button(self, label='<', size=(30, 30), style=wx.DOUBLE_BORDER)
        self.back.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.back.SetForegroundColour(LIGHT_SCHEME['text'])
        self.back.Bind(wx.EVT_ENTER_WINDOW, self.hovered_back)
        self.back.Bind(wx.EVT_LEAVE_WINDOW, self.leave_back)
        back_tip = wx.ToolTip('Go back one page')
        back.SetToolTip(back_tip)
        self.forward = forward = wx.Button(self, label='>', size=(30, 30), style=wx.DOUBLE_BORDER)
        self.forward.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.forward.SetForegroundColour(LIGHT_SCHEME['text'])
        self.forward.Bind(wx.EVT_ENTER_WINDOW, self.hovered_forward)
        self.forward.Bind(wx.EVT_LEAVE_WINDOW, self.leave_forward)
        forward_tip = wx.ToolTip('Go forward one page')
        forward.SetToolTip(forward_tip)
        self.reload = reload = wx.Button(self, label='⟳', size=(30, 30), style=wx.DOUBLE_BORDER)
        self.reload.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.reload.SetForegroundColour(LIGHT_SCHEME['text'])
        self.reload.Bind(wx.EVT_ENTER_WINDOW, self.hovered_reload)
        self.reload.Bind(wx.EVT_LEAVE_WINDOW, self.leave_reload)
        reload_tip = wx.ToolTip('Reload current page')
        reload.SetToolTip(reload_tip)
        self.url_field = url_field = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.url_field.SetCursor(wx.Cursor(wx.CURSOR_IBEAM))
        geoaka = (400, 15)
        self.url_field.SetMinSize(geoaka)
        self.fulltitle = fulltitle = wx.TextCtrl(self, value="", style=wx.TE_READONLY)
        self.fulltitle.SetCursor(wx.Cursor(wx.CURSOR_IBEAM))
        self.fulltitle.SetMinSize(geoaka)
        self.new = wx.Button(self, label='+', size=(30, 30), style=wx.DOUBLE_BORDER)
        self.new.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        self.new.Bind(wx.EVT_ENTER_WINDOW, self.hovered_new)
        self.new.Bind(wx.EVT_LEAVE_WINDOW, self.leave_new)
        self.new_tip = wx.ToolTip('Open a new tab')
        self.new.SetToolTip(self.new_tip)
        self.buttosn = wx.Button(self, label="☰", size=(30, 30), style=wx.DOUBLE_BORDER)
        self.buttosn.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.buttosn.SetForegroundColour(LIGHT_SCHEME['text'])
        self.buttosn.Bind(wx.EVT_ENTER_WINDOW, self.hovered_op1)
        self.buttosn.Bind(wx.EVT_LEAVE_WINDOW, self.leave_op1)
        self.buttosn.SetToolTip(wx.ToolTip('show menu'))
        self.buttosn2 = wx.Button(self,label="⚙",size=(30, 30), style=wx.DOUBLE_BORDER)
        self.buttosn2.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.buttosn2.SetForegroundColour(LIGHT_SCHEME['text'])
        self.buttosn2.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, 'Consolas'))
        self.buttosn2.Bind(wx.EVT_ENTER_WINDOW, self.hovered_op2)
        self.buttosn2.SetToolTip(wx.ToolTip('General Settings'))
        self.SM = wx.Button(self, label="❃", size=(30, 30), style=wx.DOUBLE_BORDER)
        self.SM.SetBackgroundColour(LIGHT_SCHEME['button_normal'])
        self.SM.SetForegroundColour(LIGHT_SCHEME['text'])
        self.SM.SetFont(wx.Font(19, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, 'Consolas'))
        self.SM.Bind(wx.EVT_ENTER_WINDOW, self.hovered_sm)
        self.SM.Bind(wx.EVT_LEAVE_WINDOW, self.leave_sm)
        self.SM.SetToolTip(wx.ToolTip('show menu'))
        stacked_sizer = wx.BoxSizer(wx.VERTICAL)
        stacked_sizer.Add(self.url_field,1, wx.EXPAND,5)
        stacked_sizer.Add(self.fulltitle,1, wx.EXPAND,5)
        self.html_window = html_window = wx.html2.WebView.New(self,backend=wx.html2.WebViewBackendEdge)
        top_bar_container.AddGrowableCol(4)
        top_bar_container.Add(back, 0, wx.LEFT | wx.BOTTOM | wx.TOP, 5)
        top_bar_container.Add(forward, 0, wx.LEFT | wx.BOTTOM | wx.TOP, 5)
        top_bar_container.Add(reload, 0, wx.LEFT | wx.BOTTOM | wx.TOP, 5)
        top_bar_container.AddSpacer(30)
        self.top_bar_container.Add(stacked_sizer, 0, wx.EXPAND)
        top_bar_container.Add(self.buttosn, 0, wx.RIGHT | wx.BOTTOM | wx.TOP, 5)
        top_bar_container.Add(self.buttosn2, 0, wx.RIGHT | wx.BOTTOM | wx.TOP, 5)
        top_bar_container.Add(self.SM, 0, wx.RIGHT | wx.BOTTOM | wx.TOP, 5)
        top_bar_container.AddSpacer(30)
        top_bar_container.Add(self.new, 0, wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT | wx.TOP, 5)
        self.find_container = find_container = wx.BoxSizer(wx.HORIZONTAL)
        self.find_field = find_field = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        find_next = wx.Button(self, label='>', size=(30, 30))
        find_next_tip = wx.ToolTip('Find next occurance')
        find_next.SetToolTip(find_next_tip)
        self.entire_word = entire_word = wx.CheckBox(self, label='Entire word')
        self.match_case = match_case = wx.CheckBox(self, label='Match case')
        self.highlight_results = highlight_results = wx.CheckBox(self, label='Highlight results')
        find_results_label = wx.StaticText(self)
        find_close = wx.Button(self, label='×', size=(30, 30))
        find_close_tip = wx.ToolTip('Close find bar')
        find_close.SetToolTip(find_close_tip)
        find_container.Add(find_field, 0, wx.EXPAND | wx.LEFT | wx.TOP | wx.BOTTOM, 5)
        find_container.Add(find_next, 0, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 5)
        find_container.Add(entire_word, 0, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 5)
        find_container.Add(match_case, 0, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 5)
        find_container.Add(highlight_results, 0, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 5)
        find_container.AddSpacer(30)
        find_container.Add(find_results_label, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 5)
        find_container.Add(find_close, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 5)
        self.zoom_container = zoom_container = wx.BoxSizer(wx.HORIZONTAL)
        self.zoom_slider = zoom_slider = wx.Slider(self, value=3, minValue=1, maxValue=5)
        zoom_close = wx.Button(self, label='×', size=(30, 30))
        zoom_close_tip = wx.ToolTip('Close zoom bar')
        zoom_close.SetToolTip(zoom_close_tip)
        zoom_container.Add(zoom_slider, 1, wx.EXPAND | wx.LEFT | wx.TOP | wx.BOTTOM, 5)
        zoom_container.AddSpacer(30)
        zoom_container.Add(zoom_close, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 5)
        pagesizer.Add(top_bar_container, proportion=False, flag=wx.EXPAND)
        pagesizer.Add(html_window, proportion=True, flag=wx.EXPAND)
        pagesizer.Add(find_container, proportion=False, flag=wx.EXPAND)
        pagesizer.Add(zoom_container, proportion=False, flag=wx.EXPAND)
        pagesizer.Hide(find_container)
        pagesizer.Hide(zoom_container)
        find_field.Bind(wx.EVT_TEXT_ENTER, self.continue_find)
        find_next.Bind(wx.EVT_BUTTON, lambda event, goprev=True: self.continue_find(event, goprev))
        entire_word.Bind(wx.EVT_CHECKBOX, self.continue_find)
        match_case.Bind(wx.EVT_CHECKBOX, self.continue_find)
        highlight_results.Bind(wx.EVT_CHECKBOX, self.continue_find)
        find_field.Bind(wx.EVT_TEXT, self.continue_find)
        find_close.Bind(wx.EVT_BUTTON, self.close_find)
        zoom_close.Bind(wx.EVT_BUTTON, self.close_zoom)
        zoom_slider.Bind(wx.EVT_COMMAND_SCROLL, self.zoom_slider_change)
        back.Bind(wx.EVT_BUTTON, self.tab_back)
        forward.Bind(wx.EVT_BUTTON, self.tab_foward)
        reload.Bind(wx.EVT_BUTTON, self.tab_reload)
        self.new.Bind(wx.EVT_BUTTON, self.tab_new)
        url_field.Bind(wx.EVT_TEXT_ENTER, self.loadpage)
        url_field.Bind(wx.EVT_SET_FOCUS, self.click_on_url_field)
        html_window.Bind(wx.html2.EVT_WEBVIEW_LOADED, self.post_load_config)
        html_window.Bind(wx.html2.EVT_WEBVIEW_NEWWINDOW, self.open_in_new_tab)
        self.html_window.Bind(wx.html2.EVT_WEBVIEW_TITLE_CHANGED, self.change_title)
        self.load_url(url)
        url_field.SetValue(url)
        settings_menu = wx.Menu()
        self.sm_menu = wx.Menu()
        self.menu_sm1 = menu_sm1 = wx.MenuItem(self.sm_menu, 0, "make a server")
        self.menu_sm2 = menu_sm2 = wx.MenuItem(self.sm_menu, 1, "join a server")
        self.sm_menu.Append(self.menu_sm1)
        self.sm_menu.AppendSeparator()
        self.sm_menu.Append(self.menu_sm2)
        self.optional_menu = wx.Menu()
        self.menu_dbookmarks = menu_dbookmarks = wx.MenuItem(self.optional_menu, 0, "Store bookmarks: " + sbmc)
        self.menu_lm = menu_lm = wx.MenuItem(self.optional_menu, 1, "Literal mode: " + lm)
        self.menu_dish = menu_dish = wx.MenuItem(self.optional_menu, 2, "Disable history: " + hisd)
        self.optional_menu.Append(self.menu_dbookmarks)
        self.optional_menu.AppendSeparator()
        self.optional_menu.Append(self.menu_lm)
        self.optional_menu.Append(self.menu_dish)
        self.page_menu = wx.Menu()
        menu_zoom = wx.MenuItem(settings_menu, 10, "Change zoom")
        self.menu_contextmenu = menu_contextmenu = wx.MenuItem(settings_menu, 11, "Enable context menu: " + q2)
        self.menu_historyenabled = menu_historyenabled = wx.MenuItem(settings_menu, 12, "Page forever lock")
        menu_source = wx.MenuItem(self.page_menu, 0, "Show source")
        menu_history = wx.MenuItem(self.page_menu, 1, "Show history")
        menu_print = wx.MenuItem(self.page_menu, 2, "Print this page")
        menu_find = wx.MenuItem(self.page_menu, 3, "Find in page")
        menu_dhistory = wx.MenuItem(self.page_menu, 4, "Delete history")
        menu_downloads = wx.MenuItem(self.page_menu, 5, "Show downloads folder")
        menu_bookmarks = wx.MenuItem(self.page_menu, 6, "Show bookmarks page")
        menu_addbookmarks = wx.MenuItem(self.page_menu, 7, "Add this website to bookmarks")
        menu_theme = wx.MenuItem(self.page_menu, 8, "Change Theme")
        menu_dth = wx.MenuItem(self.page_menu, 9, "Turn to default theme")
        settings_menu.Append(menu_zoom)
        settings_menu.AppendSeparator()
        try:
            self.html_window.EnableAccessToDevTools()
            self.menu_devtools = menu_devtools = wx.MenuItem(settings_menu, 12, "Enable access to dev tools: " + q1)
            settings_menu.Append(menu_devtools)
            settings_menu.Bind(wx.EVT_MENU, self.enable_devtools, menu_devtools)
        except:
            pass
        settings_menu.Append(menu_contextmenu)
        settings_menu.AppendSeparator()
        settings_menu.Append(menu_historyenabled)
        self.page_menu.Append(menu_downloads)
        self.page_menu.Append(menu_source)
        self.page_menu.AppendSeparator()
        self.page_menu.Append(menu_theme)
        self.page_menu.Append(menu_dth)
        self.page_menu.AppendSeparator()
        self.page_menu.Append(menu_history)
        self.page_menu.Append(menu_dhistory)
        self.page_menu.AppendSeparator()
        self.page_menu.Append(menu_print)
        self.page_menu.Append(menu_find)
        self.page_menu.AppendSeparator()
        self.page_menu.Append(menu_bookmarks)
        self.page_menu.Append(menu_addbookmarks)
        self.page_menu.AppendSeparator()
        self.page_menu.AppendSubMenu(settings_menu, 'Page Settings')
        self.sm_menu.Bind(wx.EVT_MENU, self.mas, menu_sm1)
        self.sm_menu.Bind(wx.EVT_MENU, self.cts, menu_sm2)
        self.optional_menu.Bind(wx.EVT_MENU, self.csbmc, menu_dbookmarks)
        self.optional_menu.Bind(wx.EVT_MENU, self.clms, menu_lm)
        self.optional_menu.Bind(wx.EVT_MENU, self.eadh, menu_dish)
        settings_menu.Bind(wx.EVT_MENU, self.enable_contextmenu, menu_contextmenu)
        settings_menu.Bind(wx.EVT_MENU, self.enable_historyenabled, menu_historyenabled)
        settings_menu.Bind(wx.EVT_MENU, self.adjust_zoom, menu_zoom)
        self.page_menu.Bind(wx.EVT_MENU, self.show_source, menu_source)
        self.page_menu.Bind(wx.EVT_MENU, self.show_history, menu_history)
        self.page_menu.Bind(wx.EVT_MENU, self.print_page, menu_print)
        self.page_menu.Bind(wx.EVT_MENU, self.find_in_page, menu_find)
        self.page_menu.Bind(wx.EVT_MENU, self.open_theme, menu_theme)
        self.page_menu.Bind(wx.EVT_MENU, self.turnbacktodth, menu_dth)
        self.page_menu.Bind(wx.EVT_MENU, self.dhistory, menu_dhistory)
        self.page_menu.Bind(wx.EVT_MENU, self.downloadsfolder, menu_downloads)
        self.page_menu.Bind(wx.EVT_MENU, self.bookmark_minitab, menu_bookmarks)
        self.page_menu.Bind(wx.EVT_MENU, self.bookmarksadd, menu_addbookmarks)
        self.buttosn.Bind(wx.EVT_BUTTON, self.sshowf)
        self.buttosn2.Bind(wx.EVT_BUTTON, self.sshowf2)
        self.SM.Bind(wx.EVT_BUTTON, self.sshowf3)
        self.k = 0
        self.SetSizer(pagesizer)
    def cts(self,event):
        os.startfile('C:\\XVX_Browser1.4\\app\\app\\chatc.exe')
        event.Skip()
    def mas(self,event):
        os.startfile('C:\\XVX_Browser1.4\\app\\app\\MAS.exe')
        event.Skip()
    def hovered_back(self,event):
        self.back.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_back(self,event):
        self.back.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def hovered_forward(self,event):
        self.forward.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_forward(self,event):
        self.forward.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def hovered_reload(self,event):
        self.reload.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_reload(self,event):
        self.reload.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def hovered_op1(self,event):
        self.buttosn.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_op1(self,event):
        self.buttosn.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def hovered_op2(self,event):
        self.buttosn2.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_op2(self,event):
        self.buttosn2.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def hovered_new(self,event):
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_new(self,event):
        self.new.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def hovered_sm(self,event):
        self.SM.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def leave_sm(self,event):
        self.SM.SetForegroundColour(LIGHT_SCHEME['text'])
        event.Skip()
    def eadh(self,event):
        global hisd
        if hisd == 'True':
            hisd = 'False'
        else:
            hisd = 'True'
        self.menu_dish.SetItemLabel("Disable history: " + hisd)
        event.Skip()
    def csbmc(self,event):
        global sbmc
        if sbmc == 'True':
            sbmc = 'False'
        else:
            sbmc = 'True'
        self.menu_dbookmarks.SetItemLabel("Store bookmarks: " + sbmc)
        event.Skip()
    def sshowf(self,event):
        self.PopupMenu(self.page_menu)
    def sshowf2(self,event):
        self.PopupMenu(self.optional_menu)
    def sshowf3(self,event):
        self.PopupMenu(self.sm_menu)
    def open_theme(self,event):
        theme_tab = themepage(self.parent)
        self.parent.AddPage(theme_tab, caption="XVX Browser theme", select=False)
    def turnbacktodth(self,event):
        global LIGHT_SCHEME,bg,tex,bn
        LIGHT_SCHEME = {
            'background': wx.Colour(254, 254, 254),  # Dark gray
            'text': wx.Colour(0, 0, 0),
            'button_normal': wx.Colour(200, 200, 200),
        }
        bg = [254, 254, 254]
        tex = [0, 0, 0]
        bn = [200, 200, 200]
    def bookmarksadd(self,event):
        if sbmc == 'True':
            try:
                try:
                    f = open('bookmarks.txt', 'r')
                    if self.html_window.GetCurrentURL() in f.read():
                        f.close()
                    else:
                        f.close()
                        write = open('bookmarks.txt','a')
                        write.write(f'{self.html_window.GetCurrentURL()}\n')
                        write.close()
                except(OSError, PermissionError):
                    wx.MessageBox('it might be OS or permission problem to write in bookmarks.txt', 'Error with bookmarks',
                                  wx.OK | wx.ICON_ERROR)
            except FileNotFoundError:
                open('bookmarks.txt','x')
        else:
            bookmarks.append(self.html_window.GetCurrentURL())
    def bookmark_minitab(self,event):
        try:
            try:
                try:
                    with open('bookmarks.txt', 'r') as file:
                        line = file.readlines()
                    line = [lin.strip() for lin in line]
                    lines = list(set(line) | set(bookmarks))
                    bookmark_tab = BookmarkPage(self.parent, lines, line)
                    self.parent.AddPage(bookmark_tab, caption="XVX Bookmarks page", select=False)
                except(OSError,PermissionError):
                    wx.MessageBox('it might be OS or permission problem to read bookmarks.txt', 'Error with bookmarks',
                                  wx.OK | wx.ICON_ERROR)
            except(UnicodeError,UnicodeDecodeError,UnicodeEncodeError):
                wx.MessageBox('the bookmarks.txt might has non ASCII litters', 'Error with bookmarks', wx.OK | wx.ICON_ERROR)
        except FileNotFoundError:
            open('bookmarks.txt','x')
    def downloadsfolder(self,event):
        current_user = os.getlogin()
        subprocess.Popen(f'explorer "C:\\Users\\{current_user}\\Downloads"')
    def on_key_down(self, event):
        key_code = event.GetKeyCode()
        print('d')
        if key_code == ord('N') and event.ControlDown():
            print('C')
    def show_source(self, event):
        title = self.html_window.GetCurrentTitle()
        if title == "":
            title = ("XVX Browser - Source for " + self.html_window.GetCurrentURL())
        else:
            title = ("XVX Browser - Source for " + self.html_window.GetCurrentTitle())
        page = SourceCode(self.parent, windowname=title, windowurl=self.html_window.GetCurrentURL(),
                          history_var=self.visited, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        page.source.SetValue(self.html_window.GetPageSource())
        self.parent.AddPage(page, caption=title, select=False)
    def show_history(self, event):
        history_tab = HistoryPage(self.parent, self.visited)
        self.parent.AddPage(history_tab, caption="XVX Browser History", select=False)
    def dhistory(self,event):
        self.visited.clear()
        event.Skip()
    def adjust_zoom(self, event):
        self.pagesizer.Hide(self.find_container)
        self.pagesizer.Show(self.zoom_container)
        self.pagesizer.Layout()
    def close_zoom(self, event):
        self.pagesizer.Hide(self.zoom_container)
        self.pagesizer.Layout()
    def zoom_slider_change(self, event):
        scalenum = event.GetInt()
        scale_val = None
        if scalenum == 1:
            scale_val = wx.html2.WEBVIEW_ZOOM_TINY
        elif scalenum == 2:
            scale_val = wx.html2.WEBVIEW_ZOOM_SMALL
        elif scalenum == 3:
            scale_val = wx.html2.WEBVIEW_ZOOM_MEDIUM
        elif scalenum == 4:
            scale_val = wx.html2.WEBVIEW_ZOOM_LARGE
        elif scalenum == 5:
            scale_val = wx.html2.WEBVIEW_ZOOM_LARGEST
        self.html_window.SetZoom(scale_val)
    def print_page(self, event):
        self.html_window.Print()
    def find_in_page(self, event):
        self.pagesizer.Hide(self.zoom_container)
        self.pagesizer.Show(self.find_container)
        self.pagesizer.Layout()
    def continue_find(self, event, gonext=False):
        match_case = self.match_case.IsChecked()
        entire_word = self.entire_word.IsChecked()
        highlight_results = self.highlight_results.IsChecked()
        if not gonext:
            self.html_window.Find("")
        if match_case and entire_word and highlight_results:
            self.html_window.Find(self.find_field.GetValue(),
                                  flags=wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD | wx.html2.WEBVIEW_FIND_MATCH_CASE)
        elif match_case and highlight_results:
            self.html_window.Find(self.find_field.GetValue(),
                                  flags=wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_MATCH_CASE)
        elif entire_word and highlight_results:
            self.html_window.Find(self.find_field.GetValue(),
                                  flags=wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT | wx.html2.WEBVIEW_FIND_ENTIRE_WORD)
        elif entire_word and match_case:
            self.html_window.Find(self.find_field.GetValue(),
                                  flags=wx.html2.WEBVIEW_FIND_ENTIRE_WORD | wx.html2.WEBVIEW_FIND_MATCH_CASE)
        elif match_case:
            self.html_window.Find(self.find_field.GetValue(), flags=wx.html2.WEBVIEW_FIND_MATCH_CASE)
        elif entire_word:
            self.html_window.Find(self.find_field.GetValue(), flags=wx.html2.WEBVIEW_FIND_ENTIRE_WORD)
        elif highlight_results:
            self.html_window.Find(self.find_field.GetValue(), flags=wx.html2.WEBVIEW_FIND_HIGHLIGHT_RESULT)
        else:
            self.html_window.Find(self.find_field.GetValue())
    def close_find(self, event):
        self.pagesizer.Hide(self.find_container)
        self.pagesizer.Layout()
    def click_on_url_field(self, event):
        self.url_field.SetInsertionPointEnd()
        self.url_field.SelectAll()
        event.Skip()
    def clms(self,event):
        global lm
        if lm == 'False':
            lm = 'True'
        else:
            lm = 'False'
        self.menu_lm.SetItemLabel("literal mode: " + lm)
        event.Skip()
    def enable_devtools(self, event):
        global q1
        if q1 == 'True':
            q1 = 'False'
        else:
            q1 = 'True'
        self.menu_devtools.SetItemLabel("Enable access to dev tools: " + q1)
        if q1 == 'True':
            self.html_window.EnableAccessToDevTools(True)
        else:
            self.html_window.EnableAccessToDevTools(False)
        event.Skip()
    def enable_contextmenu(self, event):
        global q2
        if q2 == 'True':
            q2 = 'False'
        else:
            q2 = 'True'
        self.menu_contextmenu.SetItemLabel("Enable context menu: " + q2)
        if q2 == 'True':
            self.html_window.EnableContextMenu(True)
        else:
            self.html_window.EnableContextMenu(False)
        event.Skip()
    def enable_historyenabled(self, event):
        global q3
        if q3 == 'True':
            q3 = 'False'
        else:
            q3 = 'True'
        if q3 == 'True':
            history_enabled = True
            self.menu_historyenabled.SetItemLabel("page forever lock")
        else:
            history_enabled = False
            self.menu_historyenabled.SetItemLabel("LOCKED UNCHANGEABLE")
            self.menu_historyenabled.Enable(False)
        self.html_window.EnableHistory(history_enabled)
        self.remember_history = history_enabled
        if self.html_window.CanGoBack():
            self.back.Enable()
        else:
            self.back.Disable()
        if self.html_window.CanGoForward():
            self.forward.Enable()
        else:
            self.forward.Disable()
        event.Skip()
    def load_url(self, url=None):
        if url:
            self.html_window.LoadURL(url)
    def tab_back(self, event):
        if self.html_window.CanGoBack():
            self.load_url()
            self.html_window.GoBack()
    def tab_foward(self, event):
        if self.html_window.CanGoForward():
            self.load_url()
            self.html_window.GoForward()
    def tab_reload(self, event):
        if self.reload.GetLabel() == "×":
            self.html_window.Stop()
            self.post_load_config()
        else:
            self.load_url()
            self.html_window.Reload()
    def tab_new(self, event):
        page = WebPage(self.parent, self.visited)
        page.SetBackgroundColour(LIGHT_SCHEME['background'])
        self.parent.AddPage(page, caption="Loading", select=True)
    def post_load_config(self, event=None):
        global hisd
        url = self.html_window.GetCurrentURL()
        self.url_field.SetValue(url)
        if self.parent.GetSelection() == self.parent.GetPageIndex(self):
            self.on_select()
        if self.html_window.CanGoBack():
            self.back.Enable()
        if self.html_window.CanGoForward():
            self.forward.Enable()
        self.reload.SetLabel("⟳")
        self.url_field.Enable()
        if self.remember_history:
            if hisd == 'False':
                self.visited.append(url)
    def change_title(self, event):
        title = self.html_window.GetCurrentTitle()
        current_page_index = self.parent.GetPageIndex(self)
        if len(title) > 14:
            self.parent.SetPageText(current_page_index, title[:10] + '...')
            self.fulltitle.SetValue(title)
        else:
            self.fulltitle.SetValue(title)
            self.parent.SetPageText(current_page_index, title)
    def on_select(self):
        title = self.html_window.GetCurrentTitle()
        divider = ""
        if title != "":
            divider = " - "
        self.frame.SetTitle("XVX Browser")
    def on_close(self):
        if self.html_window.IsBusy():
            self.html_window.Stop()
    def open_in_new_tab(self, event):
        page = WebPage(self.parent, self.visited, url=event.URL)
        self.parent.AddPage(page, caption="Loading")
    def loadpage(self, event):
        global validurl
        def is_valid_url(url):
            parsed_url = urllib.parse.urlparse(url)
            return bool(parsed_url.scheme and parsed_url.netloc)
        url = self.url_field.GetValue()
        if (not url.startswith("https://") and not url.startswith("http://") and lm == 'False'):
            if url.startswith("s:") or url.startswith("S:"):
                url = "https://duckduckgo.com/" + url[2:]
            else:
                url = "http:/" + url
        if lm == 'True':
            url = self.url_field.GetValue()
        self.load_url(url)
class Browser(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        if os.path.exists('./logo.ico'):
            icone = wx.Icon('./logo.ico', wx.BITMAP_TYPE_ANY)
            self.SetIcon(icone)
            self.Show()
        else:
            pass
        self.SetMinSize((900, 500))
        self.hovered_page = None
        self.hover_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_hover_timer)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.history_closed = []
        self.load_notebook()
    def OnClose(self, event):
        dlg = wx.MessageDialog(self, "Are you sure you want to close?", "Confirmation",
                               wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        if result == wx.ID_NO:
            event.Veto()
        else:
            exit()
    def load_notebook(self):
        self.panel = panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)
        self.notebook = notebook = wx.aui.AuiNotebook(panel, style=wx.aui.AUI_NB_DEFAULT_STYLE)
        box.Add(notebook, proportion=True, flag=wx.EXPAND)
        panel.SetSizer(box)
        notebook.AddPage(WebPage(self.notebook, self.history_closed), caption="Loading", select=True)
        notebook.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.on_page_close)
        notebook.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.on_page_select)
        notebook.Bind(wx.EVT_MOTION, self.on_tab_hover)
        notebook.SetBackgroundColour(LIGHT_SCHEME['background'])
        self.notebook.SetBackgroundColour(LIGHT_SCHEME['background'])
    def on_page_close(self, event):
        event.Skip()
        try:
            page = self.notebook.GetCurrentPage()
            page.on_close()
        except:
            pass
        if self.notebook.GetPageCount() <= 1:
            exit()
    def on_page_select(self, event):
        self.notebook.GetCurrentPage().on_select()
    def on_hover_timer(self, event):
        if self.hovered_page:
            self.hovered_page.DestroyTipWindow()
            self.hovered_page = None
    def on_tab_hover(self, event): pass
def main():
    app = wx.App()
    browser = Browser(None, title='XVX Browser')
    browser.Show()
    app.MainLoop()
if __name__ == '__main__':
    main()