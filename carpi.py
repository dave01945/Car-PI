
''' Home screen for a car pc based on a raspberry pi '''

import wx

###############################################################################

# craete home menu

""""""

class home(wx.Panel):

	def __init__(self, parent):

		# Create panel
		wx.Panel.__init__(self, parent=parent, size=(800, 480))
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
		prnt=self.GetParent()
		prnt.Close()

	def closewindow(self, event):
		self.Destroy()

	def openaudio(self, event):
	#	self.audiopanel=audio(self)
	#	self.homepanel=home(self)
		homepanel.Hide()		
		audiopanel.Show()

###############################################################################

# Audio class used for displayeing audio files on internal or external storage

""""""

class audio(wx.Panel):

	def __init__(self, parent):
		
# Create panel
		wx.Panel.__init__(self, parent=parent, size=(800, 480))
# Back to home button mainly to test
		button=wx.Button(self, label='Home', pos=(720, 10), size=(60, 60))

# Bind event to the button
		self.Bind(wx.EVT_BUTTON, self.gohome, button)

	def gohome(self, event): # Changes back to home screen

	#	self.audiopanel=audio(self)
	#	self.homepanel=home(self)
		audiopanel.Hide()
		homepanel.Show()

###############################################################################

# Frame subclass

class mainframe(wx.Frame):

# some declarations here 


	def __init__(self):
		
		displaysize=wx.DisplaySize()

		wx.Frame.__init__(self, None, wx.ID_ANY, size=(displaysize[0]/2, displaysize[1]/2))
		
		global homepanel
		global audiopanel
		homepanel=home(self)
		audiopanel=audio(self)
		audiopanel.Hide()
		
		if debug:
			print 'mainframe'
			print displaysize

###############################################################################

# A class for switching windows

""""""

#class toggle(self, event):

#	def switch_mp3()



###############################################################################
debug=1

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=mainframe()
	frame.Show()
	app.MainLoop()
