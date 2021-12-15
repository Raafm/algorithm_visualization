import pygame,time, math, random, string
from graph.color import *


pygame.init()
screen_width,screen_height = 1200,700
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(Black)
font = pygame.font.Font('freesansbold.ttf',15)


def random_vector_char(length):
   letters = 'ACTG'#string.ascii_lowercase
   return list(random.choice(letters) for i in range(length))

def bad_word(length):
    k = len('AAAAAAAACAGTAAAATCGTACTCC')
    word = list(c for c in 'AAAAAAAACAGTAAAATCGTACTCC')
    if length < 20: return word
    
    
    bigWord  = []
    for _ in range(n//k-1):
        if len(bigWord) >= n:
            return bigWord[0:n]
        
        bigWord += random_vector_char(random.randint(0,(length-len(bigWord))//2))    
        
        bigWord += list(word[0:random.randint(8, k-5)])
        

    bigWord += random_vector_char(length-len(bigWord))
    
    return bigWord[0:n]



d = dict()
d['A'] = 0
d['C'] = 1
d['U'] = 2
d['T'] = 2
d['G'] = 3
def convert(letter):
    return d[letter]

def Hash(word,i,f):
    H = 0
    x = i
    while x < f:
        H = ((H<<2) + convert(word[x]))%10000
        x+=1
    
    return H%1000

def display_calculation(word,key):
    word = ''.join(word)
    pygame.draw.rect(screen,Black,(screen_width//2-50,0,screen_width,80)) 
    #font = pygame.font.Font('freesansbold.ttf',15)
    #text = font.render("h(",True,Cyan)                   
    #screen.blit(text,text.get_rect(center = (screen_width//2,50)))
    text = font.render(word ,True,White)                   
    screen.blit(text,text.get_rect(center = (screen_width//2+120,50)))
    #text = font.render(") = ",True,Cyan)                   
    #screen.blit(text,text.get_rect(center = (screen_width//2+ 250,50)))
    text = font.render( str(key),True,Dark_yellow)                   
    screen.blit(text,text.get_rect(center = (screen_width//2  + 280,50)))
    pygame.display.update()



def display_word(words,position = (80,150),erase_screen = True, show = True):   
    if erase_screen: pygame.draw.rect(screen,Black,(0,0,screen_width,screen_height))

    font = pygame.font.Font('freesansbold.ttf',15)
    x,y = position
    
    for j,word in enumerate(words): 
        for i,c in enumerate(word):
            text = font.render(c ,True, White)                   
            screen.blit(text,text.get_rect(center =(10*i+x,j*20+y)))
        
    if show: pygame.display.update()

def display_info(i,k,n):
    if (i)%n + k < n: 
        palavra = Haystack[(i)//n][(i)%n:(i+k)%n]
        
    else:
        palavra = Haystack[(i)//n][(i)%n : n]
        
        l = n - (i)%n
        if i//n < lines-1:
            palavra = palavra + Haystack[i//n+1][0:k-l]

    pygame.draw.rect(screen,Black,(screen_width//2-100,0,screen_width,100))
    display_word(['check: ',palavra],position = (screen_width//2 ,70),erase_screen = False)


def display_square(i,show=True,color=Blue):
    pygame.draw.rect(screen,color,( 10*((i)%n) + 73,  20*((i)//n) + 140,  15,20))
    if show: pygame.display.update()


def display_window(i,k,n,color = Cyan,show = True):
    for index in range(k):
        pygame.draw.rect(screen,color,( 10*((i + index)%n) + 73,  20*((i+index)//n) + 140,  15,20))
        
    if show: pygame.display.update()

def strcomp(i,k,n):
    f = 0
    #time.sleep(0.001)
    display_info(i,k,n)
    while f < k and Needle[f] == Haystack[(i+f)//n][(i+f)%n]:
        display_square(f+i,color = Yellow)
        #time.sleep(0.001)
        display_info(i,k,n)
        f += 1

    
    if f == k:
        display_window(i,k,n,color=Lime)
        time.sleep(1)
        return True
    return False



lines = 29
n = 111
k = 25

#Haystack = list(random_vector_char(n) for _ in range(lines))
#Needle =  random_vector_char(k)

Haystack = list(bad_word(n) for i in range(lines))
Needle   =  'AAAAAAAACAGTAAAATCGTACTCC'
print("len = ",len(Needle))
HashNum    = Hash(Haystack[0][0:k], 0 , k)
HashNeedle = Hash(Needle       , 0 , k)


display_window(n-k+1,k,n)

display_word(["Needle: ",Needle],position = (80,50))
display_word(["Haystack: "],position = (100,130),erase_screen = False)
display_word( Haystack,erase_screen = False)

time.sleep(2.5)


brute = True
rabin = False

#brute,rabin = rabin,brute

i = 0  #S + n*(lines)-k
running =  True
while running :

    # pygame stuff:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   #exit pygame,
            running = False                          #exit() program    
    
    if i == n*(lines)-k:
        if rabin: continue
        else:
            time.sleep(1)
            rabin = True
            brute = False
            i = 0

            pygame.draw.rect(screen,Black,(0,0,1500,1500))
            font = pygame.font.Font('freesansbold.ttf',50)
            text = font.render("Rabin-Karp",True,White)                         
            screen.blit(text,text.get_rect(center = ((screen_width-100)//2,screen_height//2   - 100)))
            
            pygame.display.update()
            time.sleep(1.5)
            display_word(Haystack,erase_screen = True)
            
            
            font = pygame.font.Font('freesansbold.ttf',15)
            text = font.render("h(",True,Cyan)                   
            screen.blit(text,(40,40))
            text = font.render(''.join(Needle) ,True,Lime)                   
            screen.blit(text,(60,40))
            text = font.render(") = ",True,Cyan)                   
            screen.blit(text,(330,40))
            text = font.render( str(Hash(Needle,0,k)),True,Dark_yellow)                   
            screen.blit(text,(400,40))
            pygame.display.update()

            time.sleep(1)

            for index in range(k):
                display_square(index,color = Cyan)



    if brute:
        if strcomp(i,k,n):
            time.sleep(1)
            i = n*lines - k
            continue
        
        display_window(i,k,n,Red,show=False)

        
        
        if i == n*lines//2:
            i = n*(lines)-k
            continue
        
    if rabin:
        display_square(i+k, color  = Cyan, show = False)
        display_square(i  , color  = Navy, show = False)
        
        # for the animation:
        if (i)%n + k < n: 
            palavra = Haystack[(i)//n][(i)%n:(i+k)%n]
            
        else:
            palavra = Haystack[(i)//n][(i)%n : n]
            
            l = n - (i)%n
            if i//n < lines-1:
                palavra = palavra + Haystack[i//n+1][0:k-l]
        
        #back to the algorithm:
        HashNum = ( HashNum<<2 + convert(Haystack[(i+k)//n][(i+k)%n]))%10000
        display_calculation(palavra,HashNum)
        pygame.display.update()
        #time.sleep(0.001)
        if HashNum == HashNeedle:
            display_window(i,k,n,color=Yellow)
            if strcomp(i,k,n):
                i = n*(lines)-k
                time.sleep(1)
                continue

    i += 1
    
