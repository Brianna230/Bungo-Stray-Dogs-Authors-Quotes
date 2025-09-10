import random
from tkinter import *
import requests
from PIL import Image, ImageTk
import io




quotes =[{
    "author" : "Dazai Osamu",
    "quote" :"For someone like myself in whom the ability to trust others is so cracked and broken that I am wretchedly timid and am forever trying to read the expression on people's faces.",
    "book" :"No Longer Human",
    "image_url":"https://64.media.tumblr.com/ed6e37ce0558f32094fe01fc12fdb804/0712480756c63da5-af/s540x810/8283447160ca8a8d580d0a0afee6113ba8d1ba3e.png"
},{
    "author" : "Chuuya Nakahara",
    "quote":"Upon the tainted sorrow, no hope nor want of anything. Upon the tainted sorrow, to idly dream of death",
    "book":"Upon the Tainted Sorrow",
    "image_url":"https://i.pinimg.com/736x/3a/07/8c/3a078c3f68d49e6cbfa3d5490e11ee53.jpg"
},{
    "author":"Atsushi Nakajima",
    "quote":"Perhaps soon, my inner beast will overcome my human nature,like the ancient palace slowly sinking into the sands. I am scared I am not a valuable gem, but at the same time, I still believe I am valuable. I do not want to be mediocre, but my fear of trying has led me to alienate the world, feeding my growing sense of indignity and shame, and fueling my weakened self-esteem",
    "book":"The Moon Over the Mountain",
    "image_url":"https://64.media.tumblr.com/eea3320f43010fc7949c6aeb242c2b85/92c55185694af48b-6e/s1280x1920/745f4f1b9609a5ef56c6b0d6316192a5f27f6f2d.png"

},{
    "author":"Ryunosuke Akutagawa",
    "quote":"A man sometimes devotes his life to a desire which he is not sure will ever be fulfilled. Those who laugh at this folly are, after all, no more than mere spectators of life.",
    "book": "Rashomon and Other Stories",
    "image_url":"https://www.lemon8-app.com/seo/image?item_id=7446849058595078702&index=1&sign=aace23a05d5c8c04a9f69711c5469ec4"
,},{
    "author":"Yosono Akiko",
    "quote":"O my young brother, I cry for you. \n Don't you understand you must not die! You who were born the last of all \n Command a special store of parents' love \n Would parents place a blade in children's hands \n Teaching them to murder other men \n Teaching them to kill and then to die? \n Have you so learned and grown to twenty-four? \n O my brother, you must not die! \n Could it be the Emperor His Grace Exposeth not to jeopardy of war \n But urgeth men to spilling human blood \n And dying in the way of wild beasts, \n Calling such death the path to glory? \n If his Grace possesseth noble heart \n What must be the thoughts that linger true?",
    "book":"O My Brother, You Must Not Die",
    "image_url" :"https://64.media.tumblr.com/b46be43ade2798369cc389aa9137aa51/3157b52cd797dfd4-f0/s640x960/dbdb8ff92f03b87928b43a65a9737f7b15a66843.jpg"                                           

}]
window = Tk()

imagelabel = Label(window)
imagelabel.pack()

def get_random_quote():
    quote = random.choice(quotes)
    quotelabel.config(text=f"{quote['author']} ({quote['book']}): {quote['quote']}")

    response = requests.get(quote["image_url"])
    images_data = response.content
    image = Image.open(io.BytesIO(images_data))
    image = image.resize((200,200))
    tk_image = ImageTk.PhotoImage(image)

    imagelabel.config(image= tk_image)
    imagelabel.image =tk_image

    


# random_quote = get_random_quote()
# print(f"{random_quote['author']} ({random_quote['book']}): {random_quote['quote']}")
# print(random_quote['image_url'])
window.title("Bungo Stray Dogs Authors Quotes")
window.geometry("420x420")
quotelabel = Label(window, text="Click to get a quote", wraplength=400, justify="left")
quotelabel.pack()
button = Button(window,
                text= "Get Quotes",
                command=get_random_quote)
button.pack()

window.mainloop()