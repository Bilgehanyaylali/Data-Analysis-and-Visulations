import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv("supermarket.csv")

# Categorical Variable Visualization #

df['Payment'].value_counts().plot(kind='bar')
plt.show(block=True)

"""Warning: 
If you don't get results when you write (plt.show()) this way,
 you should write (plt.show(block=True)) this way."""

sns.lineplot(x='Branch', y='Gender', data=df)

# Numeric Variable Visualization #

plt.hist(df["Quantity"])
plt.show(block=True)
###########################

plt.boxplot(df["Quantity"])
plt.show(block=True)

# plot #

x = np.array([0, 10])
y = np.array([0, 230])

plt.plot(x, y)
plt.show(block=True)
#####################

x = np.array([2, 9])
y = np.array([5, 13])

plt.plot(x, y)
plt.show(block=True)

# Multiple Points #

x = np.array([2, 4, 6, 7])
y = np.array([3, 9, 3, 12])

plt.plot(x, y, "o")
plt.show(block=True)

# Markers #

"""
You can use the keyword argument marker to emphasize each point with a specified marker:
plt.plot(y, marker = '*')

Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
"""

y = np.array([3, 8, 1, 10])

plt.plot(y, 'o:r')
plt.show(block=True)

# o = markers
# r = color

"""
Color Reference
Color Syntax	Description
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
"""

y = np.array([3, 8, 1, 10])

plt.plot(y, '|:m')
plt.show(block=True)

# Marker Size #

y = np.array([3, 8, 1, 10])

plt.plot(y, marker='o', ms=20)
plt.show(block=True)

# Marker Color #

x = np.array([3, 8, 1, 10])

plt.plot(x, marker='o', color='c', ms=20, mec='k')
plt.show(block=True)

# Line style #

y = np.array([3, 8, 1, 10])

plt.plot(y, linestyle='dotted')
plt.show(block=True)

"""
You can choose any of these styles:

Style	Or
'solid' (default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'	
'None'	'' or ' '
"""

# Line Width #

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth='20.5')
plt.show(block=True)

# Multiple Lines #

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show(block=True)
############################

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show(block=True)

##################################
plt.plot(x1, y1, 'o', x2, y2, 'o')
plt.show(block=True)

# Labels #

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("x axis")
plt.ylabel("y axis")

plt.show(block=True)

#################################

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y, color='y')

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show(block=True)

#################################

plt.plot(x, y, color='y')

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid()
plt.show(block=True)

# Subplots #

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.show(block=True)

# Draw 2 plots on top of each other #

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x, y)

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x, y)

plt.show(block=True)

# Draw 6 plots:

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x, y)

plt.show(block=True)

# Adding title #

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("SALES")

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show(block=True)

# Plots #

# Scatter Plots

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(x, y)
plt.show(block=True)

# Compare Plots #

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x, y)

##########################
x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
plt.scatter(x, y)

plt.show(block=True)

# Color Each Dot #

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array(
    ["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan",
     "magenta"])

plt.scatter(x, y, c=colors)

plt.show(block=True)

# Size #

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, s=sizes)

plt.show(block=True)

# Bars #

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show(block=True)

# Histograms #

x = np.random.normal(170, 10, 250)
print(x)
"""
[166.73522397 181.78595292 169.11375494 180.09203908 183.2405537
 166.99765271 173.67730955 155.00041711 181.95825987 169.02682515
 177.20089478 193.28232243 172.49889424 184.19443894 148.99978079
 161.65681526 167.72082375 174.13304422 175.0587553  180.46019708
 187.62546801 185.97224679 169.18403015 178.49724779 192.38647217
 171.26255135 158.22993194 159.73078353 182.79082578 177.95207779
 174.44947805 176.6741458  164.05532553 156.1536175  158.40299223
 167.53509994 170.95487749 157.55895773 170.585068   183.12330939
 156.0336145  176.4064965  185.07506379 170.72565736 176.14448072
 154.23894509 162.84918045 180.73427706 179.06478638 176.01382604
 170.89212997 165.35971979 164.16688312 158.79797528 174.48074749
 169.02100511 161.23444403 160.03463559 172.26987567 174.98004958
 168.60351131 177.33992234 173.83605148 185.93719009 181.13184098
 174.30247626 158.67918222 145.33723822 191.15696573 184.85861457
 163.97527171 171.79213512 157.07146985 170.07960083 172.54054494
 161.03909825 182.46422305 176.24653919 184.72785704 170.06583922
 168.02718184 157.27874823 168.26150047 170.80558639 178.49082767
 172.52675244 161.09472618 189.85917929 165.32573783 175.31352441
 174.41972001 170.49159979 167.06175457 176.88065112 169.8260739
 180.39333533 177.13065008 175.32359771 170.13361233 163.7953227
 163.91256709 172.50722339 181.77166873 148.19929616 172.03909651
 162.13220209 162.94377489 179.09593822 170.64899828 173.21350504
 160.03751228 168.24736454 159.71555608 171.37951421 170.84281979
 156.58720946 173.71318888 168.35218614 162.17917588 166.20377375
 169.40534118 180.85254693 163.48664137 170.43906159 170.51200816
 176.76918774 163.96735574 160.07474295 163.74787495 174.23874116
 179.02893501 166.31807902 172.74435009 167.24758693 160.56274356
 153.68015866 155.37787046 180.07592995 166.5138826  173.8391845
 177.07627517 167.72911028 174.26216318 188.0079583  155.33250394
 171.13576609 180.29864815 180.88203793 163.72697959 162.5327923
 190.44095956 167.81708429 177.73616336 166.79516243 158.71863456
 158.31957852 172.31200353 156.98986032 170.61757428 167.69611057
 177.48733078 162.23837233 166.90453251 173.89490454 170.61498491
 177.06604681 170.20064066 173.72091393 163.38115928 152.24406156
 181.76144586 165.9923905  192.44018905 158.83132012 180.09269416
 184.56077486 150.8109703  183.40979942 174.01548354 158.58704677
 185.2510001  167.49109685 167.39332967 172.11777068 175.69625582
 158.20236427 178.27364491 177.35515551 171.08756224 164.62096028
 155.52887423 163.78585888 184.37037676 164.52397121 148.71636329
 163.4865931  179.61130553 162.5619085  159.83617799 177.90869754
 168.76215983 164.90986183 173.18683746 174.39981942 172.20831969"""

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show(block=True)

# Pie Charts #

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show(block=True)

##############

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=mylabels)
plt.show(block=True)

# Explode#
 #

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0.5, 0, 0]

plt.pie(y, labels=mylabels, explode=myexplode)
plt.show(block=True)


# SEABORN #

df["City"].value_counts()
sns.countplot(x=df["City"], data=df)
plt.show(block=True)

# I use Matplotlib Library #
df['City'].value_counts().plot(kind='bar')
plt.show(block=True)

# Numeric Variable Visualization #

sns.boxplot(x=df["Total"])
plt.show(block=True)
#########
df["Total"].hist()
plt.show(block=True)

