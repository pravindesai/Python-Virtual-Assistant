# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:17:35 2019

@author: BATMAN
"""
import wx
import wolframalpha
import wikipedia

app_id='7XRWVG-YJ2WE8L35P'
client=wolframalpha.Client(app_id)


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Python Assistant")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Python virtual Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,100))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        Que = self.txt.GetValue()
        Que = Que.lower()
        try:
            result=client.query(Que)
            print('RESULT FOR ', Que,'\n',next(result.results).text)
        except:
            wikipedia.set_lang('en')
            print('RESULT FOR ', Que,'\n',wikipedia.summary(Que,sentences=5))
        


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()