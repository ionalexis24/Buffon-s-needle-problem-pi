l=120
L=2*l
k=0
s=0

def setup():
    background(0)
    size(3*L,3*L)
    stroke(255)
    line(0,L,width,L)
    line(0,2*L,width,2*L)
    
def hit(x1,y1,x2,y2,x3,y3,x4,y4):
    uA=((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
    uB=((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
    if uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1 :
        
        intersectionX = x1 + (uA * (x2-x1))
        intersectionY = y1 + (uA * (y2-y1))
        fill(255,0,0);
        noStroke();
        ellipse(intersectionX,intersectionY, 5,5)
        
        return 1
    else:
        return 0
    
def draw():    
    global k
    global s
    x1=random(0,3*L)
    y1=random(0,3*L)
    fi=random(0,TWO_PI)
    x2=x1+l*cos(fi)
    y2=y1+l*sin(fi)
    #culori
    stroke(map(x1,0,3*L,0,255), map(y1,0,3*L,0,255), map(fi,0,TWO_PI,0,255))
    #stroke(map(fi,0,TWO_PI,0,255),0,0)
    #stroke(150)
    
    if hit(x1,y1,x2,y2, 0,L,width,L) == 1:
        s=s+1.0
        stroke(255,0,0)
        line(x1,y1,x2,y2)
    elif hit(x1,y1,x2,y2, 0,2*L,width,2*L) == 1:
        s=s+1.0
        stroke(255,0,0)
        line(x1,y1,x2,y2)
    else:
        stroke(255)
        line(x1,y1,x2,y2)
    
    k=k+1.0
    
    if s>0:
        print(s,k,k/s)
        
    delay(250)
