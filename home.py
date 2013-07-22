
''' Home screen for a car pc based on a raspberry pi '''

import wx

class home(wx.Frame):

	def __init__(self, parent, id):
		# Set a frame(window) the same size as the display
		# Can also be called in fullscreen mode
		wx.Frame.__init__(self, parent, id, 'Home Screen', size=(800, 480))
		panel=wx.Panel(self)
		# Buttons
		button1=wx.Button(panel, label='Exit', pos=(30, 10), size=(350, 130))
		button2=wx.Button(panel, label='button2', pos=(420, 10), size=(350, 130))
		button3=wx.Button(panel, label='Button3', pos=(30, 175), size=(350, 130))
		button4=wx.Button(panel, label='Button4', pos=(420, 175), size=(350, 130))
		button5=wx.Button(panel, label='Button5', pos=(30, 340), size=(350, 130))
		button6=wx.Button(panel, label='Button6', pos=(420, 340), size=(350, 130))

		# functions to bind to buttons
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
