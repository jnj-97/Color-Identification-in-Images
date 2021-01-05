
from PIL import Image
path=input(str("Please Enter the path of your Image"))
img=Image.open(path)
tuple_list=img.convert('RGB').getcolors(148279)
hex_list=[]
for tuples in tuple_list:
    tuple_actual=tuples[-1]
    tuple_actual='#%02x%02x%02x' % (tuple_actual[0], tuple_actual[1],tuple_actual[2])
    hex_list.append(tuple_actual)
f=open("color.txt","at")
f.write("Please Check the colors mentioned below in any this website\nhttps://www.colorhexa.com/\n")
hex_list=set(hex_list)
for things in hex_list:
    f.write(things+"\n")
    print("The Colors have been saved in a text file within the same direcory of this script. Thank you for using this Program")

