from turtle import *
from random import sample
from time import sleep
level=1
def draw_circle(n , c):
    pu()
    goto(number_to_point(n))
    
    pendown()
    color(c)
    begin_fill()
    circle(25)
    end_fill()
    penup()    
     
def number_to_point(n):
    x = (n % 5 * 50 + 25 ) - 125
    y = (n // 5 * 50 ) - 125
    return x, y

def point_to_number(f, g):
    pu()
    if f<126 and g>-126 and f<126 and g>-126:
        row = (g+ 125) // 50
        col = (f + 125) // 50
        
        n = int(row * 5 + col)
        if userlist[n]==0:
            
            draw_circle(n,'skyblue')
            userlist[n]=1
            print(userlist)
        else:
            draw_circle(n,'beige')
            userlist[n]=0
            print(userlist)
        return n
userlist=[]
userlist=[0]*25
complist= [0]*25
print(userlist)
ht()
penup()
speed(0)
for i in range(25):
    draw_circle(i,'beige')
def r_draw():
    rl=sample(range(25),level)
    print(rl)
    for i in rl:
        draw_circle(i,"limegreen")
        complist[i]=1
    sleep(3)
    for i in rl:
        
        draw_circle(i,"beige")

uslist=[]
cmplist=[]
  
def d_c():
    for i in range(25):
        userlist[i]=0
        draw_circle(i,'beige')

        complist[i]=0

    r_draw()
def complete():
    global level
    wrong=0
    uslist.clear()
    cmplist.clear()
    for i in range(25):
        if complist[i]==1:
            cmplist.append(i)
        else:
            continue
    for i in range(25):
        if userlist[i]==1:
            uslist.append(i)
            
        else:
            continue

    for i in range(level):
        if uslist[i] in cmplist:
            draw_circle(uslist[i],'green')
        else:
            
            draw_circle(uslist[i],'tomato')
            wrong=1
            
    for i in range(level):
        if cmplist[i] in uslist:
            continue
        else:
            draw_circle(cmplist[i],'MediumSeaGreen')
    if wrong==1:
        print('pay more attention')
        level=1
    else:
        print('good job')
        level+=1
        print('level = ',level)
            
        
    
    


    
r_draw()
listen()
speed(0)
onkeypress(complete, "Return")
onscreenclick( point_to_number )
onkeypress(d_c, "space")
