x = 1
def setup():
    size(1000,1000)
    background(224, 255, 255)
def draw():
    global x
    push()
    fill(128, 128, 128)
    rect(1,200,500,100)
    rect(400,250,80,80)
    pop()
    push()
    rect(600,100,300,500)
    pop()
    push()
    fill(0)
    rect(650,200,200,300)
    pop()
    push()
    fill(0, 255, 255)
    ellipse(450,400,80,80)
    ellipse(450,450,80,80)
    ellipse(450,500,80,80)
    ellipse(450,550,80,80)
    ellipse(450,600,80,80)
    ellipse(450,650,80,80)
    pop()    
    push()
    fill(128, 128, 128)
    rect(250,900,500,500)
    pop()
    x +=1
    
    
