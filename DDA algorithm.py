from matplotlib import pyplot as plt

X = [] #create a emply list for store X values

#iterating till the range
for i in range(0,2):
    value = int(input())
    X.append(value) #adding the value in X list
Y = [] #create a emply list for store X values

#iterating till the range
for i in range(0,2):
    values = int(input())
    Y.append(values) #adding the value in X list
print(X)
print(Y)

dx = X[1]-X[0]
dy = Y[1]-Y[0]

if(abs(dx)>abs(dy)):
    step = abs(dx)
else:
    step = abs(dy)

#increment for drawing a line
Xinc = dx/step
Yinc = dy/step

#ploting for line using two points
for i in range(0, step):
    plt.plot(X[0],Y[0], color = 'r', label = 'DDA Line', marker='o')
    X[0]= X[0]+Xinc
    Y[0]= Y[0]+Yinc

plt.xlabel('X Axes') #labeling the X axes
plt.ylabel('Y Axes') #labeling the X axes
plt.title('DDA Algorithm for Line drawing') #Title fo the figure
plt.legend('o')

plt.show()
