
''' Home screen for a car pc based on a raspberry pi '''

import wx

###############################################################################

# craete home menu

""""""

class home(wx.Panel):

	def __init__(self, parent):

		# Create panel
		wx.Panel.__init__(self, parent=parent, size=(1280, 720))
		# Buttons
		button1=wx.Button(self, label='Exit', pos=(30, 10), size=(590, 210))
		button2=wx.Button(self, label='MP3', pos=(660, 10), size=(590, 210))
		button3=wx.Button(self, label='Button3', pos=(30, 255), size=(590, 210))
		button4=wx.Button(self, label='Button4', pos=(660, 255), size=(590, 210))
		button5=wx.Button(self, label='Button5', pos=(30, 500), size=(590, 210))
		button6=wx.Button(self, label='Button6', pos=(660, 500), size=(590, 210))

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
		audiopanel1.Show()

###############################################################################

# Audio class used for displayeing audio files on internal or external storage

""""""

class audio1(wx.Panel):

	def __init__(self, parent):
		
# Create panel
		wx.Panel.__init__(self, parent=parent, size=(320, 720))
# Back to home button mainly to test
		button1=wx.Button(self, label='button1', pos=(20, 20), size=(280, 155))
		button2=wx.Button(self, label='button2', pos=(20, 195), size=(280, 155))
		button3=wx.Button(self, label='button3', pos=(20, 370), size=(280, 155))
		button4=wx.Button(self, label='Home', pos=(20, 545), size=(280, 155))

# Bind event to the button
		self.Bind(wx.EVT_BUTTON, self.gohome, button4)

	def gohome(self, event): # Changes back to home screen
		audiopanel1.Hide()
		homepanel.Show()

###############################################################################

# Frame subclass

class mainframe(wx.Frame):

# some declarations here 


	def __init__(self):
		
		#displaysize=wx.DisplaySize()

		wx.Frame.__init__(self, None, wx.ID_ANY, size=(1280, 720))
		
		global homepanel
		global audiopanel1
		homepanel=home(self)
		audiopanel1=audio1(self)
		audiopanel1.Hide()
		
		if debug:
			print 'mainframe'
		#	print displaysize

###############################################################################


###############################################################################
debug=1

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=mainframe()
	frame.Show()
	frame.ShowFullScreen(True)
	app.MainLoop()
