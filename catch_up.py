from pygame import *

#создай окно игры
display.set_caption('bybygaga')
window = display.set_mode((800, 600))
#задай фон сцены
background = transform.scale(image.load("background.png"), (800, 600))
sprite1= transform.scale(image.load('sprite1.png'), (50, 50))
sprite2 = transform.scale(image.load('sprite2.png'), (50, 50))

x1 = 100
y1 = 100
x2 = 200
y2 = 200 
FPS = 60

clock = time.Clock()


game = True 
while game:   
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    # clock.tick(FPS)
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP]:
        y1 -= 10
    if keys_pressed[K_DOWN]:
        y1 += 10
    if keys_pressed[K_RIGHT]:
        x1 += 10
    if keys_pressed[K_LEFT]:
        x1 -= 10
    if keys_pressed[K_w]:
        y2 -= 10
    if keys_pressed[K_s]:
        y2 += 10
    if keys_pressed[K_d]:
        x2 += 10
    if keys_pressed[K_a]:
        x2 -= 10

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
#создай 2 спрайта и размести их на сцене




#обработай событие «клик по кнопке "Закрыть окно"»