from OpenGL.GL import *
from OpenGL.GLU import *

def render(obj, pos=[0,0,0], rot=[0,0,0], scale=[1,1,1]):
    glPushMatrix()
    glTranslate(pos[0], pos[1], pos[2])
    glScale(scale[0], scale[1], scale[2])
    glRotate(rot[0], 1, 0, 0)
    glRotate(rot[1], 0, 1, 0)
    glRotate(rot[2], 0, 0, 1)
    glCallList(obj.gl_list)
    glPopMatrix()
 
def get_vertices(obj):
    vector = []
    for x in obj.vertices:
    	vector.append([ x[0]+obj.pos[0], x[1]+obj.pos[1], x[2]+obj.pos[2] ])
    return vector

def get_vert(obj):
	vertices = []
	for v in obj.vertices:
		vertices.append(v)
	return vertices
 
def check_box_collision(box1, box2):
    """
    Check Collision of 2 box colliders
    """
    #print('\nCollision check:')
 
    x_max = max([e[0] for e in box1])
    x_min = min([e[0] for e in box1])
    y_max = max([e[1] for e in box1])
    y_min = min([e[1] for e in box1])
    z_max = max([e[2] for e in box1])
    z_min = min([e[2] for e in box1])
    #print('Box1 min %.2f, %.2f, %.2f' % (x_min, y_min, z_min))
    #print('Box1 max %.2f, %.2f, %.2f' % (x_max, y_max, z_max))    
     
    x_max2 = max([e[0] for e in box2])
    x_min2 = min([e[0] for e in box2])
    y_max2 = max([e[1] for e in box2])
    y_min2 = min([e[1] for e in box2])
    z_max2 = max([e[2] for e in box2])
    z_min2 = min([e[2] for e in box2])
    #print('Box2 min %.2f, %.2f, %.2f' % (x_min2, y_min2, z_min2))
    #print('Box2 max %.2f, %.2f, %.2f' % (x_max2, y_max2, z_max2))        
     
    ''' 
    isColliding = ((x_max >= x_min2 and x_max <= x_max2) or (x_min <= x_max2 and x_min >= x_min2)) \
                    
                    and ((y_max >= y_min2 and y_max <= y_max2) or (y_min <= y_max2 and y_min >= y_min2)) \
                    
                    and ((z_max >= z_min2 and z_max <= z_max2) or (z_min <= z_max2 and z_min >= z_min2))
    '''
    isColliding = []

    if(x_max >= x_min2 and x_max <= x_max2): isColliding.append(True)
    else: isColliding.append(False)

    if(x_min <= x_max2 and x_min >= x_min2): isColliding.append(True)
    else: isColliding.append(False)

    if(y_max >= y_min2 and y_max <= y_max2): isColliding.append(True)
    else: isColliding.append(False)

    if(y_min <= y_max2 and y_min >= y_min2): isColliding.append(True)
    else: isColliding.append(False)

    if(z_max >= z_min2 and z_max <= z_max2): isColliding.append(True)
    else: isColliding.append(False) 

    if(z_min <= z_max2 and z_min >= z_min2): isColliding.append(True)
    else: isColliding.append(False)  

    #if isColliding:
    #    print('Colliding!')
         
    return isColliding

def chek_collisions(player, collisionMask=[]):
    allcolisions = { 'left':0, 'right':0, 'up':0,'down':0 }
    for collider in collisionMask:
        a = check_box_collision(get_vertices(player),get_vertices(collider))
        #colisoes no eixo x
        if a[0] and (a[4] or a[5]): allcolisions['down'] += 1
        if a[1] and (a[4] or a[5]): allcolisions['up']   += 1
        #colisoes no eixo z
        if a[4] and (a[0] or a[1]): allcolisions['left'] += 1
        if a[5] and (a[0] or a[1]): allcolisions['right']   += 1

    return allcolisions
