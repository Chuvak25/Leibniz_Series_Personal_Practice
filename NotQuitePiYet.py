Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
>>> x = 1
>>> _sum = set()
>>> _sum.add(x)
>>> c = 0
>>> while True:
	i = input()
	x += 2
	y = x
	y = 1/x
	c = len(_sum)
	if c % 2 == 0:
		_sum.add(y)
	if c % 2 == 1:
		y = -y
		_sum.add(y)
	pi = 4 * sum(_sum)
	print("X value: " + str(x) + " approaching pi: " + str(pi))
	time.sleep(4.5)
	if i == "stop":
		break

	

X value: 3 approaching pi: 2.666666666666667




X value: 5 approaching pi: 3.466666666666667
X value: 7 approaching pi: 2.8952380952380956
X value: 9 approaching pi: 3.3396825396825403
X value: 11 approaching pi: 2.9760461760461765

X value: 13 approaching pi: 3.2837384837384844

X value: 15 approaching pi: 3.017071817071818

X value: 17 approaching pi: 3.2523659347188767

X value: 19 approaching pi: 3.0418396189294032

X value: 21 approaching pi: 3.232315809405594

X value: 23 approaching pi: 3.058402765927333

X value: 25 approaching pi: 3.2184027659273333

X value: 27 approaching pi: 3.0702546177791854

X value: 29 approaching pi: 3.2081856522619434

X value: 31 approaching pi: 3.0791533941974274

X value: 33 approaching pi: 3.2003655154095485

X value: 35 approaching pi: 3.086079801123834


X value: 37 approaching pi: 3.194187909231942
X value: 39 approaching pi: 3.0916238066678394

X value: 41 approaching pi: 3.1891847822775956
