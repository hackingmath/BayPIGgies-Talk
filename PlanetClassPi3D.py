import pi3d
from random import random,randint
from math import sin, cos

DISPLAY = pi3d.Display.create()
DISPLAY.set_background(0.0,0.0,0.0,1) #black background

class Planet:
	def __init__(self,size,dist,img):
		self.size = size
		self.dist = dist #distance from Sun
		self.freq = 1/dist #frequency is based on distance
		self.img = pi3d.Texture(img) #declare image
		self.offset = randint(0,1000) #sets it randomly along orbit
		
		self.light = pi3d.Light(is_point = True,
						lightpos=(0,0,0),
						lightcol = (5000,
									5000,
									5000),
						lightamb = (0.05,0.05,0.05))
		self.obj = pi3d.Sphere(light = self.light,
							radius = self.size,
							x = self.dist)
		print(self,"size:",self.size,"dist:",self.dist,
		"freq:",self.freq)
		
	def update(self,t):
		self.obj.position(self.dist*cos(self.freq*(t+self.offset)),
							0,
							self.dist*sin(self.freq*(t+self.offset)))
		self.obj.draw(shader,[self.img])

#create shader
shader = pi3d.Shader('uv_light')
sunimg = pi3d.Texture('sun.jpg')

#create lights:
sunlight = pi3d.Light(lightamb =(1.0,1.0,1.0))


#create our objects
planets = []
sun = pi3d.Sphere(light = sunlight,
				  radius = 15.0,sides = 96)
				  
mercury = Planet(0.5,20,'mercury.jpg')

venus = Planet(0.7,25,'venus.jpg')

earth = Planet(1,30,'earth.jpg')

mars = Planet(0.7,40,'mars.jpg')

jupiter = Planet(3,50,'jupiter.jpg')

uranus = Planet(2,70,'uranus.jpg')

planets += [mercury, venus, earth,mars,jupiter,uranus]

#Create a camera object
CAMERA = pi3d.Camera(eye = (0.0,0.0,-75.0))

#create mouse object
mouse = pi3d.Mouse(restrict=False)
mouse.start()

#listen for keystrokes:
mykeys = pi3d.Keyboard()

#time variable
t = 0

while DISPLAY.loop_running():
	
	#store keystrokes:
	k = mykeys.read()
	
	#if the user presses ESC to quit:
	if k == 27:
		mykeys.close()
		DISPLAY.destroy()
		break #Break out of the infinite loop

	#get coordinates of mouse
	u,v = mouse.position()

	CAMERA.relocate(-u*0.5,v*0.5, #horiz and vert rotation
					[0,0,0], #where camera is pointing
					[-40,-40,-40])
	#draw the planets
	
	for p in planets:
		p.update(t)
		
	sun.draw(shader,[sunimg])
		
	t += 0.5

