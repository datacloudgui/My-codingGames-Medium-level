import sys
import math

# Don't let the machines win. You are humanity's last hope...
h_lines = []

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line = input()  # width characters, each either 0 or .
    h_lines.append(line)

output_line=[]

for i in range (height):
    for j in range(len(h_lines[i])):
        if h_lines[i][j]=='0':
            line=[]
            line.append(j)
            line.append(i)
            if j+1<len(h_lines[i]):
                h_line_0_validation = h_lines[i].find('0',j+1) #find the next 0 in the line
                if h_line_0_validation != -1:
                    line.append(h_line_0_validation)
                    line.append(i)
                else:
                    line.append(-1)
                    line.append(-1)
            else:
                line.append(-1)
                line.append(-1)
            if i+1<height:
                height_0_index = -1 #To store the index if is a node in the present column
                for k in range(i+1,height):
                    if h_lines[k][j]=='0':
                        height_0_index = k
                        break
                if height_0_index!=-1:
                    line.append(j)
                    line.append(height_0_index)
                else:
                    line.append(-1)
                    line.append(-1)
            else:
                line.append(-1)
                line.append(-1)
            output_line.append(line)
            
for i in range(len(output_line)):
    for j in range(len(output_line[i])):
        print(output_line[i][j],end=' ')
    print('')