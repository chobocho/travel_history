import wx
from wx.lib import sized_controls

class MemoDialog(sized_controls.SizedDialog):

    def __init__(self, *args, _config, **kwargs):
        super(MemoDialog, self).__init__(*args, **kwargs)
        pane = self.GetContentsPane()
        self.config = _config

        self.lblRegion = wx.StaticText(pane, label = "Region" ,style = wx.ALIGN_CENTRE)
        self.region = wx.ComboBox(pane, size=(600, 30), choices=self.config.getRegionList())
        self.region.Bind(wx.EVT_COMBOBOX, self.__OnChooseRegion)

        self.lblCountry = wx.StaticText(pane, label="Country", style=wx.ALIGN_CENTRE)
        self.country = wx.ComboBox(pane, size=(600, 30), choices=[])
        self.lblCountry = wx.StaticText(pane, label="Mno", style=wx.ALIGN_CENTRE)
        self.mno = wx.TextCtrl(pane, size=(600, 30))
        self.lblCountry = wx.StaticText(pane, label="Network", style=wx.ALIGN_CENTRE)
        self.network = wx.ComboBox(pane, size=(600, 30), choices=self.config.getNetworkList())
        self.lblDate = wx.StaticText(pane, label="Date", style=wx.ALIGN_CENTRE)
        self.date = wx.TextCtrl(pane, size=(600, 30))
        self.lblMemo = wx.StaticText(pane, label="Memo", style=wx.ALIGN_CENTRE)
        self.text = wx.TextCtrl(pane, style = wx.TE_MULTILINE,size=(600,50))
        self.text.SetValue("")
        font = wx.Font(14, wx.FONTFAMILY_TELETYPE, wx.NORMAL, wx.NORMAL)
        self.text.SetFont(font)

        static_line = wx.StaticLine(pane, style=wx.LI_HORIZONTAL)
        static_line.SetSizerProps(border=(('all', 0)), expand=True)

        pane_btns = sized_controls.SizedPanel(pane)
        pane_btns.SetSizerType('horizontal')
        pane_btns.SetSizerProps(align='center')

        button_ok = wx.Button(pane_btns, wx.ID_OK, label='OK')
        button_ok.Bind(wx.EVT_BUTTON, self.on_button)

        button_ok = wx.Button(pane_btns, wx.ID_CANCEL, label='Cancel')
        button_ok.Bind(wx.EVT_BUTTON, self.on_button)

        self.Fit()

    def __OnChooseRegion(self, event):
        region = self.region.GetValue()
        if region not in self.config.getRegionList():
            self.region.SetValue("")
            return
        self.country.SetItems(self.config.getCountryList(region))

    def on_button(self, event):
        if self.IsModal():
            self.EndModal(event.EventObject.Id)
        else:
            self.Close()

    def GetValue(self):
        result = {}
        region = self.region.GetValue()
        if region not in self.config.getRegionList():
            self.region.SetValue("")
            region = ""
        result['region'] = self.region.GetValue()

        country = self.country.GetValue()
        if country not in self.config.getCountryList(region):
            self.country.SetValue("")
        result['country'] = self.country.GetValue()
        result['mno'] = self.mno.GetValue()

        network = self.network.GetValue()
        if network not in self.config.getNetworkList():
            self.network.SetValue("")
        result['network'] = self.network.GetValue()
        result['date'] = self.date.GetValue()
        result['memo'] = self.text.GetValue()
        return result

    def SetValue(self, memo):
        self.region.SetValue(memo['region'])
        self.mno.SetValue(memo['mno'])
        self.network.SetValue(memo['network'])
        self.date.SetValue(memo['date'])
        self.text.SetValue(memo['memo'])

        region = self.region.GetValue()
        if len(region) > 0:
            self.country.SetItems(self.config.getCountryList(region))
        self.country.SetValue(memo['country'])

    def GetTopic(self):
        return self.region.GetValue() + " : " + self.country.GetValue()

    def SetTopic(self, topic):
        return ""