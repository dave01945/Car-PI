
''' Home screen for a car pc based on a raspberry pi '''

import wx

###############################################################################

# craete home menu

class home(wx.Panel):

	def __init__(self, parent):

		# Create panel
		wx.Panel.__init__(self, parent=parent)
		# Buttons
		button1=wx.Button(self, label='Exit', pos=(30, 10), size=(350, 130))
		button2=wx.Button(self, label='MP3', pos=(420, 10), size=(350, 130))
		button3=wx.Button(self, label='Button3', pos=(30, 175), size=(350, 130))
		button4=wx.Button(self, label='Button4', pos=(420, 175), size=(350, 130))
		button5=wx.Button(self, label='Button5', pos=(30, 340), size=(350, 130))
		button6=wx.Button(self, label='Button6', pos=(420, 340), size=(350, 130))

		# functions to bind to buttons
		self.Bind(wx.EVT_BUTTON, self.closebutton, button1) # event for pushing button
		self.Bind(wx.EVT_CLOSE, self.closewindow) # event for pushing x on window
		self.Bind(wx.EVT_BUTTON, self.openaudio, button2) # Event for pushing mp3
		
	def closebutton(self, event):
		self.Close(True)

	def closewindow(self, event):
		self.Destroy()

	def openaudio(self, event):
		self.homepanel.Hide()
		self.audiopanel.Show()

###############################################################################

# Audio class used for displayeing audio files on internal or external storage

class audio(wx.Panel):

	def __init__(self, parent):
		
# Create panel
		wx.Panel.__init__(self, parent=parent)
# Back to home button mainly to test
		button=wx.Button(self, label='Home', pos=(720, 10), size=(60, 60))

# Bind event to the button
		self.Bind(wx.EVT_BUTTON, self.gohome, button)

	def gohome(self, event): # Changes back to home screen
		self.audiopanel.Hide()
		self.homepanel.Show()


##########################################################################

# Frame subclass

class mainframe(wx.Frame):

	def __init__(self):

		wx.Frame.__init__(self, None, wx.ID_ANY, size=(800, 480))

		self.homepanel=home(self)
#		self.audiopanel=audio(self)
#		self.audiopanel.Hide()

###############################################################################

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=mainframe()
	frame.Show()
	app.MainLoop()
