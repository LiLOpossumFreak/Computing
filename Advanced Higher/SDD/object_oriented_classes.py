class customer:
	def _init_(self):
		self.name = ''
		self.member = 'False'
		self.seat = 0
		self.screen = 0

	def setName(self, Name):
		self.name = Name

	def setMember(self, member_status):
		self.member = member_status

	def setSeat(self, Seat):
		self.seat = Seat

	def setScreen(self, Screen):
		self.screen = Screen

	def GET(self):
		string = self.name + ' ' + self.member + ' ' + str(self.seat) + ' ' + str(self.screen)
		return string


customerS = [customer() for index in range(5)]


customerS[0].setName('John Cinema')
customerS[0].setMember('True')
customerS[0].setSeat(69)
customerS[0].setScreen(10000000000000000000000000000)

print(customerS[0].GET())