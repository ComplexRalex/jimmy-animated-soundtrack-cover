"""
    This is just an approximation of the soundtrack cover of the game:
    "Jimmy and the Pulsating Mass"

    You should play it!

    My code is (pretty much) spaghetti, so be calm xD...
    in the next days I think I can add some comments on it.
"""

import pygame

long = 250
FPS = 60
velocity = 60/FPS

pygame.init()
pygame.display.set_caption("Fresh.")
font = pygame.font.SysFont("Something", 110)
jimmy = pygame.image.load('./jimmy.png')
screen = pygame.display.set_mode((long, long))
clock = pygame.time.Clock()

y = 21
center = (long//2, long//2-y-12)
num = 10
scale = long//(num-2)
points = []
for x in range(-num//2,num//2):
    points.append([[x*scale],[y],[0]])

run = True
while run:
    clock.tick(FPS)
    screen.fill('#0F0F0F')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(0,len(points)):
        p1 = points[i]

        pair1 = (p1[0][0]+center[0],p1[1][0]+center[1])
        depth = long//10
        pair2 = (p1[0][0]*long+center[0],p1[1][0]*long+center[1])
        pygame.draw.line(screen,'green',pair1,pair2,1)

        if p1[0][0]+velocity <= (num//2)*scale:
            p1[0][0] += velocity
        else:
            p1[0][0] = -(num//2)*scale

    d = -1
    limit = 0
    while limit <= long:
        limit = y//2 + y*2**d+center[1]
        pygame.draw.line(screen,'green',(0,limit),(long,limit),1)
        d += 1

    screen.blit(font.render('Fresh.', False, '#FFFFFF'), (long//2-110,long//2-25))
    screen.blit(jimmy, (long//2-36,long//2-77))

    pygame.display.update()

pygame.quit()
