f1 = open("/home/adi/Downloads/zed-yolo-master/x1.txt", "r")
f2 = open("/home/adi/Downloads/zed-yolo-master/xo.txt", "r")
for line1 in f1:
    string1 = ".jpg"
    if string1 in line1:
        line_image = line1.replace(string1, "")
    for line2 in f2:
        string2 = ".png"
        if string2 in line2:
            line_new = line2.replace(string2,"")
            if line_image == line_new:
                print("\n")
            else:
                print(line_image)

f1.close()
f2.close()
