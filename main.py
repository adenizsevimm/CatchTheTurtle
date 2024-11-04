import turtle
import random

#Ekran
sc = turtle.Screen()
sc.bgcolor("light blue")
sc.title("Catch The Turtle")
sc.setup(width=600, height=600)

#Skor Değişkeni ve Skor Tablosu
score=0
score_board = turtle.Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(-250,250)
score_board.write(f"Score: {score}", font=("Arial", 16, "normal"))

#Süre limiti ve süre göstergesi
second=30
time_text = turtle.Turtle()
time_text.hideturtle()
time_text.penup()
time_text.goto(200,250)
time_text.write(f"Time: {second}", font=("Arial", 16, "normal"))

#Kaplumbağa
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()

#Hareket Etme Fonksiyonu
def move():
    if second > 0:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        t.goto(x, y)
        # Her 1 saniyede bir hareket etmesini sağlıyoruz
        sc.ontimer(move,100)

#Kaplumbağaya tıklandığında skoru artıran fonksiyon
def increase_score(x,y):
    global score
    score += 1
    score_board.clear()
    score_board.write(f"Skor: {score}", font=("Arial", 16, "normal"))

#Süreyi geri saydıran fonksiyon
def time_reduction():
    global second
    if second > 0 :
        second -= 1
        time_text.clear()
        time_text.write(f"Time: {second}", font=("Arial", 16, "normal"))
        sc.ontimer(time_reduction,1000)

    else:
        t.hideturtle()
        score_board.clear()
        score_board.write(f"Game Over! Score: {score}", font=("Arial", 16, "normal"))

#Tıklama olayını kaplumbağaya bağlama
t.onclick(increase_score)
#Oyunu Başlatma
move()
time_reduction()
turtle.mainloop()