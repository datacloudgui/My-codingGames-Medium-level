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
                if h_lines[i][j+1]=='0':
                    line.append(j+1)
                    line.append(i)
                else:
                    line.append(-1)
                    line.append(-1)
            else:
                line.append(-1)
                line.append(-1)
            if i+1<height:
                if h_lines[i+1][j]=='0':
                    line.append(j)
                    line.append(i+1)
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

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# Three coordinates: a node, its right neighbor, its bottom neighbor
#print("0 0 1 0 0 1")
