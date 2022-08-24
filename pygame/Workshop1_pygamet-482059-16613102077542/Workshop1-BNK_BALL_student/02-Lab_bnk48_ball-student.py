# Lab_BNK48 
import pygame as pg

# TODO 1 : กำหนด width : 1000 , height : 600 และ FPS : 60
width = 
height = 
FPS = 

# TODO 2 : กำหนดค่าสีดังนี้ pink : (197,142,195) , white : (255,255,255)
pink = 
white = 

# TODO 3 : กำหนดความเร็วให้กับ member แต่ละคน [ 3 member ]
ball1_speed = [2,2]
    # [-3,4]
    # [3,-2]

# TODO 4 : initialize pygame variable and create clock
pg.
clock = pg.time.Clock()
running =

# TODO 5 : create screen [pygame.display.set_mode] 
# and set caption [pygame.display.set_caption] => "BNK_BALL (Heavy Collision)"
screen = 

# TODO 6
#Load sound [change your sound filepath according to your computer]
pg.mixer.init()
pg.mixer.music.load("/Users/mix_tera/Desktop/Workshop1-BNK_BALL/source/sound.mp3")
pg.mixer.music.play(-1, 0.0)

# ใช้คำสั่ง soundeffect.play() เพื่อเล่นเสียง effect ตอนลูกบอลชนกัน
soundeffect = pg.mixer.Sound("/Users/mix_tera/Desktop/Workshop1-BNK_BALL/source/effect.wav")

# Choose 3 members from BNK48 and create pygame object from  get_rect
# [ load , resize , get_rect ]

# Member 1 [size : (150 , 150) , center : (500 , 250) ]
ball1_img = pg.image.load("source/BNK48/Wee_cc.png").convert_alpha()
ball1_img = pg.transform.scale(ball1_img, (150, 150))
ball1_rect = ball1_img.get_rect(center=(500,250))

# TODO 7 : create object with attribute in each comment
# Member 2 [size : (100 , 100) , center : (250 , 120)]




# Member 3 [size : (120 , 120) , center : (800 , 400)]




while running:
    # TODO 8 : set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม [clock.tick(...)]
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
            pg.quit()

    if running:
        # TODO 9 :ใส่สี background สีชมพู (screen.fill(...))
        

        # TODO 10 : ให้ member ทั้ง 3 คนเคลื่อนที่ตามทิศทางและความเร็วเป็นไปตาม speed ของแต่ละคน
        ball1_rect = ball1_rect.move(ball1_speed)
        

        
        # TODO 11 : วาด text คำว่า "Heavy Collision" [size : 150 , center :(width/2 , height/3), สีขาว]
        font_name = pg.font.match_font('arial')  # กำหนดชื่อ Font
        font = pg.font.Font(font_name, 150)  # กำหนดขนาด font
        




        # TODO 12 : วาด text รหัสนิสิต ลงไป ข้างใต้คำว่า "Heavy Collision" [size : 100 ,center :(width/2 , height/1.5), สีขาว]
        # [ขนาดและตำแหน่งสามารถปรับได้ตามความเหมาะสม]
        font = pg.font.Font(font_name, 100)
        text_surface = font.render(




        # TODO 13 : เขียนเงื่อนไขไม่ให้ตกกรอบทุกด้านให้กับ member ทั้ง 3 คน
        if ball1_rect.left < 0 or ball1_rect.right > width:
            ball1_speed[0] = -ball1_speed[0]
        if ball1_rect.top < 0 or ball1_rect.bottom > height:
            ball1_speed[1] = -ball1_speed[1]

        





        

        # Special point ทำให้ลูกบอลชนกันแล้วเด้งในทิศตรงกันข้าม
    









        ################################################

        # TODO 14 : เอาภาพของ member แต่ละคนใส่ลงใน object ของตนเอง
        screen.blit(ball1_img, ball1_rect)
        


        ##########################################################

        pg.display.flip()