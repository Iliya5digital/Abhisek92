def isLeft(line,point):
    delta=1.0*(((line[1][0]-line[0][0])*(point[1]-line[0][1]))-((point[0]-line[0][0])*(line[1][1]-line[0][1])))
    if delta>0:
        return 1
    elif delta<0:
        return -1
    else:
        return 0

def getWindingNumber(point,polygon):
    winding_number=0
    for i in range(1,len(polygon)):
        if polygon[i-1][1] <= point[1]:
            if polygon[i][1] > point[1]:
                if isLeft([polygon[i-1],polygon[i]],point)==1:
                    winding_number=winding_number+1
        else:
            if polygon[i][1] <= point[1]:
                if isLeft([polygon[i-1],polygon[1]],point)==-1:
                    winding_number=winding_number-1
    return winding_number