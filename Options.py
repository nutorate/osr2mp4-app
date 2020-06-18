from Parents import Button

class Options(Button):
	def __init__(self, parent):
		super(Options, self).__init__(parent)

		self.default_x = 20
		self.default_y = 400
		self.default_size = 3.5

		self.img_idle = "res/Options_Idle.png"
		self.img_hover = "res/options_hover.png"
		self.img_click = "res/Options_Click.png"
		self.img_shadow = "res/Options_Shadow.png"
		self.parent = parent
		super().setup()

	def mouseclicked(self):
		self.parent.settingspage.show()
		self.parent.settingspage.settingsarea.scrollArea.show()




