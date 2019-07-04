import pickle
import time
def ConvertTime(k):
	try:
		k=k.replace(',', '').lower()
		k=k.split(' ', 2)
		day=int(k[0])
		month={ 'january' : 1, 'february' : 2, 'march' : 3, 'april' : 4, 'may' : 5, 'june' : 6, 'july' : 7, 'august' : 8, 'september' : 9, 'october' : 10, 'november' : 11, 'december' : 12 }[k[1]]
		year=int(k[2])
		return [day, month, year]
	except:
		raise Exception('nigga wtf')
class kTime:
	def __init__(self, date, user):
		self.user=user
		self.time=ConvertTime(date)
	def say(self):
		print(self.time)
	def difference(self):
		og=[time.localtime().tm_mday, time.localtime().tm_mon, time.localtime().tm_year]
		date=self.time
		diff=og[2]-date[2]-1
		if date[1]<og[1]:
			diff+=1
		if date[1]==og[1]:
			if date[0]<=og[0]:
				diff+=1
		return diff
			
def dumping(*args):
	
	list0=[]
	try:
		list1=pickle.load(open('k.text', 'rb'))
		print('loaded')
	except:
		list1=[]
	for abb in args:
		print(abb.user)
		if not any([abb.user==c.user for c in list1]):
			list1.append(abb)
	pickle.dump(list1, open('k.text','wb'))
def gettingAge(usr):
	list1=pickle.load(open('k.text', 'rb'))
	for i in list1:
		if usr==i.user:
			return str(i.difference())
	return 'not in the archives, use /birthday to record ur birthday u fucking nigger'
