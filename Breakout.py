from tkinter import *
import random
from tkinter import messagebox

#-----------------------------------    

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

#-----------------------------------    

class GameObject:
    
    def __init__(self, pos):
        self.position = Vector(pos[0], pos[1])
    
    def isCollidingWith(self, otherGameObject):  # Checks collosion between itself
        global x
        global y
        #############################            #   and another game object. Returns
        #   INSERT YOUR CODE HERE                #   True if they are colliding,
                                                 #   False otherwise.
        
        
        a = Game.canvas.bbox(self.ball.box)
        b = Game.canvas.bbox(otherGameObject.box)
        if otherGameObject == self.back:
            if not a[2] in range(b[0], b[2]):
                self.xState = False
                return True
            elif not a[0] in range(b[0], b[2]):
                self.xState = True
                return True
            elif not a[1] in range(b[1], b[3]):
                self.yState = True
                return True
            elif a[3] >= b[3]:
                x=300
                y=300
                self.paddle.lives-=1
                self.ball.updatePos([x,y])
                
                return True
        else:
            if a[2] in range(b[0], b[2]) and a[3] in range(b[1], b[3]):
                self.yState = False
                return True
            elif a[0] in range(b[0], b[2]) and a[1] in range(b[1], b[3]):
                self.yState = True
                return True
            elif a[1] in range(b[1], b[3]) and a[0] in range(b[0], b[2]):
                self.xState = True
                return True
            elif a[3] in range(b[1], b[3]) and a[2] in range(b[0], b[2]):
                self.xState = False
                return True
            else:
                return False
            
        
        #############################
    
    def Draw(self):                                 # This function MUST be overidden by all 
         raise     #   sub-classes !!!
        
        

#-----------------------------------

class Background(GameObject):
    def __init__(self):
        #############################
        #   INSERT YOUR CODE HERE
        super().__init__([320, 240])
        
        self.back = PhotoImage(file = 'assets\\bg.gif')
        self.Draw()
        #############################
    
    def Draw(self):
        #############################
        #   INSERT YOUR CODE HERE
        self.box = Game.canvas.create_image(self.position.x, self.position.y, image = self.back)
        
        
        #############################
        

#-----------------------------------
    
class Brick(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self):
        self.y=80
        self.x=100
        self.Line1=[]
        self.Line2=[]
        self.Line3=[]
        self.Line4=[]
        for i in range(8):
            r=random.randint(1,20)
            if r==1:
                self.Line1.append(ExplodingBrick(self.x,self.y))
            else:
                self.Line1.append(MetalBrick(self.x,self.y))
            self.x=self.x+65
        self.y=self.y+30
        self.x=100
        for i in range(8):
            r=random.randint(1,20)
            if r==1:
                self.Line2.append(ExplodingBrick(self.x,self.y))
            else:
                self.Line2.append(NormalBrick(self.x,self.y))
            self.x=self.x+65
        self.y=self.y+30
        self.x=100
        for i in range(8):
            r=random.randint(1,20)
            if r==1:
                self.Line3.append(ExplodingBrick(self.x,self.y))
            else:
                self.Line3.append(NormalBrick(self.x,self.y))
            self.x=self.x+65
        self.y=self.y+30
        self.x=100
        for i in range(8):
            r=random.randint(1,20)
            if r==1:
                self.Line4.append(ExplodingBrick(self.x,self.y))
            else:
                self.Line4.append(GlassBrick(self.x,self.y))
            self.x=self.x+65
    def Draw(self):
        for i in self.Line1:
            if i=="":
                pass
            else:
                i.Draw()
        
        for i in self.Line2:
            if i=="":
                pass
            else:
                i.Draw()
        for i in self.Line3:
            if i=="":
                pass
            else:
                i.Draw()
        for i in self.Line4:
            if i=="":
                pass
            else:
                i.Draw()
                

        

    #############################

class GlassBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,x=100,y=80):
        self.type='glass'
        self.health=1
        self.position=Vector(x,y)
        self.b=PhotoImage(file = 'assets\\glassbrick.gif')


    def Draw(self):
        self.box= Game.canvas.create_image(self.position.x, self.position.y, image = self.b)



class NormalBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,x,y):
        self.type='normal'
        self.health=2
        self.position=Vector(x,y)
        self.b=PhotoImage(file = 'assets\\normalbrick.gif')

    def Draw(self):
        self.box = Game.canvas.create_image(self.position.x, self.position.y, image = self.b)

    #############################

    
class MetalBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,x,y):
        self.type='metal'
        self.health=7
        self.position=Vector(x,y)
        self.b=PhotoImage(file = 'assets\\metalbrick.gif')

    def Draw(self):
        self.box = Game.canvas.create_image(self.position.x, self.position.y, image = self.b)

    #############################

    
class ExplodingBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,x,y):
        self.type='explosive'
        self.health=4
        self.position=Vector(x,y)
        self.b=PhotoImage(file = 'assets\\explodingbrick.gif')
    def Draw(self):
        self.box = Game.canvas.create_image(self.position.x, self.position.y, image = self.b)

    #############################


#-----------------------------------
    
class Ball(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self, pos):
        super().__init__(pos)
        self.ball = PhotoImage(file = 'assets\\ballBlue.png')
        self.vel = 2

    def Draw(self):
        self.box = Game.canvas.create_image(self.position.x, self.position.y, image = self.ball)

    def updatePos(self, pos):
        super().__init__(pos)

    #############################

    
#-----------------------------------


class Powerup(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,xlimits):
        self.x=random.randrange(xlimits[1], xlimits[3])
        self.y=10
        
        self.r=random.randint(1, 3)
        

    def Draw(self):
        if self.r==1:
            self.drawnPower = Life(self.x,self.y)
            self.drawnPower.Draw()
            self.a = 1
            
        elif self.r==2:
            self.drawnPower=FastPaddle(self.x,self.y)
            self.drawnPower.Draw()
            self.a = 2
        else:
            self.drawnPower=CrazyBall(self.x,self.y)
            self.drawnPower.Draw()
            self.a = 3

    def updatePos(self, pos):
        super().__init__(pos)
        
    #############################

    
class Life(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,x,y):
        self.position=Vector(x,y)
        self.i=PhotoImage(file = 'assets\\life.gif')
    def Draw(self):
        self.box = Game.canvas.create_image(self.position.x, self.position.y, image = self.i)

    #############################

    
class FastPaddle(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,x,y):
        self.position=Vector(x,y)
        self.i=PhotoImage(file = 'assets\\fastpaddle.gif')
    def Draw(self):
        self.box = Game.canvas.create_image(self.position.x, self.position.y, image = self.i)
        pass
    #############################


class CrazyBall(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,x,y):
        self.position=Vector(x,y)
        self.i=PhotoImage(file = 'assets\\crazyball.gif')
    def Draw(self):
        self.box = Game.canvas.create_image(self.position.x, self.position.y, image = self.i)

        pass
    #############################


#-----------------------------------

class Player(GameObject):
    def __init__(self, game, pos, vel):
        #############################
        #   INSERT YOUR CODE HERE
        super().__init__(pos)
        self.p = PhotoImage(file = 'assets\\paddleBlu.gif')
        self.velocity = vel
        self.lives=3
        #############################


    def Draw(self):
        #############################
        #   INSERT YOUR CODE HERE
        self.box = Game.canvas.create_image(self.position.x, self.position.y, image = self.p)
        #############################

        
    
#-----------------------------------

class Game:
    canvas = None
    def __init__(self, canvas):
        global x
        global y

        self.yState = True
        self.xState = True
        self.score = 0
        
        Game.canvas = canvas           # Save canvas for future use
        x = 300
        y = 240
        self.back = Background()
        self.paddle = Player(self, [300, 400], 5)
        self.ball = Ball([x, y])
        self.brick = Brick()
        self.power=""
        self.gameObjects = [self.back, self.paddle, self.ball, self.brick]# A list of ALL game objects in the game

    
        #############################
        #   INSERT YOUR CODE HERE
        pass
        #############################

                
    def Draw(self):                    # This function draws ALL of the things
        
        global secCount
        
        Game.canvas.delete(ALL)        # First clear the screen 
        
        
        for obj in self.gameObjects:   # Now the objects draw THEMSELVES one by one
            obj.Draw()
        if secCount % 20 == 0 and self.power=="":
            self.power = Powerup(Game.canvas.bbox(self.back.box))
        if self.power=="":
            pass
        else:
            self.power.Draw()
            
            a = Game.canvas.bbox(self.power.drawnPower.box)
            b = Game.canvas.bbox(self.back.box)
            c = Game.canvas.bbox(self.paddle.box)
            if a[3] in range(b[1], b[3]):
                self.power.y += 3
                Game.canvas.delete(obj)
                self.power.updatePos([self.power.x, self.power.y])
            elif a[2] in range(c[0], c[2]) and a[3] in range(c[1], c[3]):
                if self.power.a == 1:
                    self.paddle.lives += 1
                    self.power = ''                            
                elif self.power.a == 2:
                    self.paddle.velocity = 10
                    self.power = ''
                    if secCount % 5 == 0:
                        self.paddle.velocity = 5
                else:
                    self.ball.vel = 5
                    self.power = ''
                    if secCount % 5 == 0:
                        self.ball.vel = 2
            elif a[0] in range(c[0], c[2]) and a[1] in range(c[1], c[3]):
                if self.power.a == 1:
                    self.paddle.lives += 1
                    self.power = ''                            
                elif self.power.a == 2:
                    self.paddle.velocity = 10
                    self.power = ''
                    if secCount % 5 == 0:
                        self.paddle.velocity = 5
                else:
                    self.ball.vel = 5
                    self.power = ''
                    if secCount % 5 == 0:
                        self.ball.vel = 2                        
            else:
                self.power = ''
            
        self.textScore = 'Score:'+str(self.score)
        self.textLife = 'Lives:'+str(self.paddle.lives)
        self.showLives = Game.canvas.create_text(50, 15, text = self.textLife, fill = 'white', font = 'Times 20 bold')
        self.showScore = Game.canvas.create_text(550, 15, text = self.textScore, fill = 'white', font = 'Times 20 bold')

        if self.checkWin():
            GameWindow.ShowWinMessage()
        elif self.paddle.lives == 0:
            GameWindow.ShowLoseMessage()
        self.BounceBall()
        
    def LeftKeyPressed(self):        
        #############################
        #   INSERT YOUR CODE HERE
        
        self.paddle.position.x -= self.paddle.velocity
        #############################

    
    def RightKeyPressed(self):        
        #############################
        #   INSERT YOUR CODE HERE
        self.paddle.position.x += self.paddle.velocity
        #############################

            
    def Update(self):                   # You can add all of your game logic here
        #############################   #   for example collision between game objects,
        #   INSERT YOUR CODE HERE       #   updating the state of the objects based
                                        #   on decisions or logic etc...
        if GameObject.isCollidingWith(self, self.back):
            self.BounceBall()

        if GameObject.isCollidingWith(self, self.paddle):
            self.BounceBall()
        for i in range(len(self.brick.Line1)):
            if self.brick.Line1[i]=="":
                pass
            else:
                if GameObject.isCollidingWith(self, self.brick.Line1[i]):
                    if self.brick.Line1[i].health-1==0:
                        if self.brick.Line1[i].type=='explosive':
                            if i>0:
                                self.brick.Line1[i-1]=""
                                self.brick.Line2[i-1]=""
                                self.score += 700
                                
                            if i<7:
                                self.brick.Line1[i+1]=""
                                self.brick.Line2[i+1]=""
                                self.score += 700
                                
                            self.brick.Line2[i]=""
                            self.score += 200
                            
                        self.brick.Line1[i]=""
                        self.score += 500
                        self.BounceBall()
                    else:
                        self.brick.Line1[i].health-=1
        for i in range(len(self.brick.Line2)): 
            if self.brick.Line2[i]=="":
                pass
            else:
                if GameObject.isCollidingWith(self, self.brick.Line2[i]):
                    if self.brick.Line2[i].health-1==0:
                        if self.brick.Line2[i].type=='explosive':
                            if i>0:
                                self.brick.Line1[i-1]=""
                                self.brick.Line2[i-1]=""
                                self.brick.Line3[i-1]=""
                                self.score += 800
                            if i<7:
                                self.brick.Line1[i+1]=""
                                self.brick.Line2[i+1]=""
                                self.brick.Line3[i+1]=""
                                self.score += 800
                                
                            self.brick.Line1[i]=""
                            self.brick.Line3[i]=""
                            self.score += 600
                        self.brick.Line2[i]=""
                        self.score += 200
                        self.BounceBall()
                    else:
                        self.brick.Line2[i].health-=1
        for i in range(len(self.brick.Line3)): 
            if self.brick.Line3[i]=="":
                pass
            else:
                if GameObject.isCollidingWith(self, self.brick.Line3[i]):
                    if self.brick.Line3[i].health-1==0:
                        if self.brick.Line3[i].type=='explosive':
                            if i>0:
                                self.brick.Line2[i-1]=""
                                self.brick.Line3[i-1]=""
                                self.brick.Line4[i-1]=""
                                self.score += 500
                            if i<7:
                                self.brick.Line2[i+1]=""
                                self.brick.Line3[i+1]=""
                                self.brick.Line4[i+1]=""
                                self.score += 500
                            self.brick.Line2[i]=""
                            self.brick.Line4[i]=""
                            self.score += 300
                            
                        self.brick.Line3[i]=""
                        self.score += 200
                        self.BounceBall()
                    else:
                        self.brick.Line3[i].health-=1
        for i in range(len(self.brick.Line4)):
            if self.brick.Line4[i]=="":
                pass
            else:
                if GameObject.isCollidingWith(self, self.brick.Line4[i]):
                    if self.brick.Line4[i].health-1==0:
                        if self.brick.Line4[i].type=='explosive':
                            if i>0:
                                self.brick.Line4[i-1]=""
                                self.brick.Line3[i-1]=""
                                self.score += 300
                            if i<7:
                                self.brick.Line3[i+1]=""
                                self.brick.Line4[i+1]=""
                                self.score += 300
                            self.brick.Line3[i]=""
                        self.brick.Line4[i]=""
                        self.score += 100
                        self.BounceBall()
                    else:
                        self.brick.Line4[i].health -=1

    def checkWin(self):
        for i in self.brick.Line1:
            if not(i ==""):
                return False
        for i in self.brick.Line2:
            if not(i==""):
                return False
        for i in self.brick.Line3:
            if not(i==""):
                return False
        for i in self.brick.Line3:
            if not(i==""):
                return False
        if self.paddle.lives == 0:
            return False
        return True     
        
        
        #############################
    def BounceBall(self):
        global x
        global y
        if self.yState and self.xState:
            x += self.ball.vel
            y += self.ball.vel
        if not self.yState and self.xState:
            x += self.ball.vel
            y -= self.ball.vel
        if not self.xState and self.yState:
            x -= self.ball.vel
            y += self.ball.vel
        if not self.xState and not self.yState:
            x -= self.ball.vel
            y -= self.ball.vel
        self.ball.updatePos([x, y])
        if self.paddle.lives<=0:
            Game.canvas.delete(ALL)

#-----------------------------------


class GameWindow:
    def __init__(self):
        global secCount
        self.root = Tk()
        self.root.title("Project 2 -- Breakout Game")
        self.root.geometry('640x480')

        secCount = 0

        self.canvas = Canvas(self.root, width = 640, height = 480)
        self.canvas.grid(column=0, row=0)

        self.canvas.after(1, self.OneSecTimer)
        self.canvas.bind("<Key>", self.KeyPressed)
        self.canvas.focus_set()
        

        self.game = Game(self.canvas)    
        self.root.after(1, self.GameLoop)

        
        self.root.mainloop()
    
    def KeyPressed(self, event):
        c = str(event.char)
        if c == 'a':
            self.game.LeftKeyPressed()
        if c == 'd':
            self.game.RightKeyPressed()

    
    def GameLoop(self):
        self.game.Draw()
        self.game.Update()
        
        self.root.after(1000//10, self.GameLoop)

    def OneSecTimer(self):
        global secCount
        print(secCount)
        secCount += 1
        self.canvas.after(1000, self.OneSecTimer)

    def ShowWinMessage():
        messagebox.showinfo('Congrats', 'You Win!')
        self.root.destroy
    def ShowLoseMessage():
        messagebox.showinfo('Hard luck', 'You lose!')
        self.root.destroy
#-----------------------------------


game = GameWindow()


