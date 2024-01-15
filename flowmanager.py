import scene1 
import scene2

def Login(a):
    if scene1.render(a):
        if scene2.start(scene1.getuname())=='Logout':scene1.render(a)

        
    

