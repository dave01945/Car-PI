
''' Home screen for a car pc based on a raspberry pi '''

import wx

class home(wx.Frame):

	def __init__(self, parent, id):

		wx.Frame.__init__(self, parent, id, 'Home Screen', size=(800, 480))
		panel=wx.Panel(self)
		button1=wx.Button(panel, label='Exit', pos=(20, 10), size=(60, 60))
		self.Bind(wx.EVT_BUTTON, self.closebutton, button1) # event for pushing button
		self.Bind(wx.EVT_CLOSE, self.closewindow) # event for pushing x on window

	def closebutton(self, event):
		self.Close(True)

	def closewindow(self, event):
		self.Destroy()

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=home(parent=None, id=-1)
	frame.Show()
	app.MainLoop()
