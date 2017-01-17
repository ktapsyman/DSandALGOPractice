def Qsort(Data, Left, Right):
	if Right <= Left:
		return 0
	Pivot = Data[Right - 1]
	Wall = Left
	CurrentIndex = Left
	while CurrentIndex < Right:
		if Data[CurrentIndex] < Pivot:
			Data[CurrentIndex], Data[Wall] = Data[Wall], Data[CurrentIndex]
			Wall = Wall + 1
		CurrentIndex = CurrentIndex + 1
	Data[Right-1], Data[Wall] = Data[Wall], Data[Right-1]
	Qsort(Data, Left, Wall)
	Qsort(Data, Wall+1, Right)


Data = [ 6,2,5,3,37,93,49,86,32,77 ]
Qsort(Data, 0, len(Data))
for i in Data:
	print str(i)
