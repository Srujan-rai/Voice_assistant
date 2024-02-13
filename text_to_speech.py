from gtts import gTTS
import os
my_text="hi my self srujan"
lan='en'

my_obj=gTTS(text=my_text,lang=lan,slow=False)
my_obj.save('1.mp3')
os.system('1.mp3')