class JustCounter:
	__secretCount = 0 # private var->"__varName"
	
	def count(self):
		self.__secretCount +=1
		print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
#ERROR print counter.__secretCount
print counter._JustCounter__secretCount