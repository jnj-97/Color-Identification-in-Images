import cv2
from PIL import Image
i_v=int(input("Enter 1 for Image or 2 for Video\n"))
def image_color(path):
    img=Image.open(path)
    tuple_list=img.convert('RGB').getcolors(148279)
    hex_list=[]
    for tuples in tuple_list:
        tuple_actual=tuples[-1]
        tuple_actual='#%02x%02x%02x' % (tuple_actual[0], tuple_actual[1],tuple_actual[2])
        hex_list.append(tuple_actual)
    f=open("color.txt","at")
    f.write("Please Check the colors mentioned below on this website\nhttps://www.colorhexa.com/\n")
    hex_list=set(hex_list)
    for things in hex_list:
        f.write(things+"\n")
    print("The Colors have been saved in a text file within the same direcory of this script. Thank you for using this Program")
if i_v==1:
    path=str(input("Enter the path of your image\n"))
    print(path)
    print(type(path))
    image_color(path)
elif i_v==2:
    hex_list=[]
    path=str(input("Enter the path of your video\n"))
    vidcap = cv2.VideoCapture(path)
    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            cv2.imwrite("A:\Projects\Frames/image"+str(count)+".jpg", image)    
        return hasFrames
    frameRate=int(input("Enter the time interval at which colors are taken (in seconds)\n\n"))
    sec = 0
    count=1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)
    f=open("color.txt","at")
    f.write("Please Check the colors mentioned below in any this website\nhttps://www.colorhexa.com/\n")
    for numbers in range(1,count-1):
        img=Image.open("A:\Projects\Frames\image"+str(numbers)+".jpg")
        tuple_list=img.convert('RGB').getcolors(17000000)
        for tuples in tuple_list:
            tuple_actual=tuples[-1]
            tuple_actual='#%02x%02x%02x' % (tuple_actual[0], tuple_actual[1],tuple_actual[2])
            hex_list.append(tuple_actual)
    hex_list=set(hex_list)
    for things in hex_list:
        f.write(things+"\n")
    print("The Colors have been saved in a text file within the same direcory of this script. Thank you for using this Program")
    
        
    
        
   