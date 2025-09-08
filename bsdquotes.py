import random
import webbrowser

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
    "quote":"Perhaps soon, my inner beast will overcome my human nature, like the ancient palace slowly sinking into the sands. I am scared I am not a valuable gem, but at the same time, I still believe I am valuable. I do not want to be mediocre, but my fear of trying has led me to alienate the world, feeding my growing sense of indignity and shame, and fueling my weakened self-esteem",
    "book":"The Moon Over the Mountain",
    "image_url":"https://64.media.tumblr.com/eea3320f43010fc7949c6aeb242c2b85/92c55185694af48b-6e/s1280x1920/745f4f1b9609a5ef56c6b0d6316192a5f27f6f2d.png"

},{
    "author":"Ryunosuke Akutagawa",
    "quote":"A man sometimes devotes his life to a desire which he is not sure will ever be fulfilled. Those who laugh at this folly are, after all, no more than mere spectators of life.",
    "book": "Rashomon and Other Stories",
    "image_url":"https://www.lemon8-app.com/seo/image?item_id=7446849058595078702&index=1&sign=aace23a05d5c8c04a9f69711c5469ec4"
}]

def get_random_quote():
    quote = random.choice(quotes)
    return quote

random_quote = get_random_quote()
print(f"{random_quote['author']} ({random_quote['book']}): {random_quote['quote']}")
print(random_quote['image_url'])
webbrowser.open(random_quote['image_url'])