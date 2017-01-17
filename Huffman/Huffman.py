import sys
import bisect
from collections import Counter
class HuffmanTreeNode(object):
	CharText = ''
	Frequency = 0
	Left = None
	Right = None
	def __init__(self, CharText = '\0', Frequency = 0):
		self.CharText = CharText
		self.Frequency = Frequency
	def __lt__(self, other):
		return self.Frequency < other.Frequency
	def __str__(self):
		return str(self.CharText) + " " + str(self.Frequency)

def Encode( Str, EncTable ):
	RetStr = ""
	for Text in Str:
		RetStr += EncTable[Text]
	return RetStr

def Decode( Str, CodeTree ):
	DecodedStr = ""
	CurrentNode = CodeTree
	for Bit in Str:
		if '0' == Bit:
			CurrentNode = CurrentNode.Left
		else:
			CurrentNode = CurrentNode.Right
		if '\0' != CurrentNode.CharText:
			DecodedStr += CurrentNode.CharText
			CurrentNode = CodeTree		
	return DecodedStr

def CreatePriorityQueue( Str ):
	TextCountDic = Counter(Str)
	print TextCountDic
	PriorityQueue = list( (HuffmanTreeNode( Text, Freq ) for (Text, Freq) in TextCountDic.iteritems()) )
	PriorityQueue.sort(key=lambda Node:Node.Frequency)
	#for Node in PriorityQueue:
	#	print Node.CharText
	return PriorityQueue

def CreateEncodingTree( TextQueue ):
	while 1 < len(TextQueue):
		LeftNode = TextQueue.pop(0)
		RightNode = TextQueue.pop(0)
		NewRoot = HuffmanTreeNode( '\0', LeftNode.Frequency+RightNode.Frequency )
		NewRoot.Left = LeftNode
		NewRoot.Right = RightNode
		bisect.insort( TextQueue, NewRoot )
	return TextQueue[0]

def TraverseTree( Root ):
	if None == Root:
		return 0
	TraverseTree(Root.Left)
	if '\0' != Root.CharText:
		print str(Root)
	TraverseTree(Root.Right)

def CreateCodeTable( EncodingTree, Path = "", CodeTable = {} ):
	if None != EncodingTree.Left:
		CreateCodeTable( EncodingTree.Left, Path+"0", CodeTable )
	if None != EncodingTree.Right:
		CreateCodeTable( EncodingTree.Right, Path+"1", CodeTable )
	else:
		CodeTable[EncodingTree.CharText] = Path
	#return CodeTable
		
if 2 > len( sys.argv ):
	print "No content to be encoded\n"
	exit()
TargetText = sys.argv[1]
PrioQueueForTree = CreatePriorityQueue( TargetText )
EncodingTree = CreateEncodingTree( PrioQueueForTree )
#TraverseTree( EncodingTree ) #Only for debugging
CodeTable = {}
CreateCodeTable( EncodingTree, "", CodeTable )
print CodeTable
CompressedStr = Encode( TargetText, CodeTable )
print CompressedStr
DecodedStr = ""
if 3 == len( sys.argv ):
	DecodedStr = Decode( sys.argv[2], EncodingTree )
else:
	DecodedStr = Decode( CompressedStr, EncodingTree )
print "Decoded str = %s" % DecodedStr
