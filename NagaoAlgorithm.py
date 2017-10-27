#coding:utf-8
class NagaoAlgorithm():
	N=5
	leftPTable=[]
	leftLTable=[]
	rightPTable=[]
	rightLTable=[]
	wordNumber=0.0
	wordTFNeighbor={}
	stopwords = "的很了么呢是嘛个都也比还这于不与才上用就好在和对挺去后没说";  
	
	def reverse(self,phrase):
		'''
		反转字符串 
		'''
		print(phrase)
		result=""
		for x in range(len(phrase)):
			result = result + phrase[-(x+1)]
			
		print (result)
		return result
	def coPrefixLength(self,word1,word2):
		'''
		获取两字符串公共长度
		'''
		coPrefixLength =0
		for x in range(min(len(word1),len(word2))):
			if(word1[x]==word2[x]): coPrefixLength+=1
			else: break
		print(coPrefixLength)
		return coPrefixLength

	def addToPTable(self,line):
		'''
		把line 按非中文字符或停止词分割
		分别添加到rightPTable 
		逆序添加到leftPTable
		'''
		import re  
		n= NagaoAlgorithm()
		phrases = re.split("[^\u4E00-\u9FA5]+|["+NagaoAlgorithm.stopwords+"]",line)
		print(phrases)
		for phrase in phrases:
			for i in phrase:
				n.rightPTable.append(i)
			reversePhrase =n.reverse(phrase)
			for i in reversePhrase:
				n.leftPTable.append(i)
			n.wordNumber += len(phrase)
			print(n.wordNumber)

nagao= NagaoAlgorithm()
nagao.addToPTable("祥明说今天天气挺不错的，确实啊！")