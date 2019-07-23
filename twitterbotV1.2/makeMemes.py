from PIL import Image, ImageDraw, ImageFont
import random
import os
print("****Making memes****")
subjectWords = [line.rstrip('\n') for line in open('subjects.txt', 'r')]
subjectX = [line.rstrip('\n') for line in open('aggwords.txt', 'r')]
counter = 0

for i in range(100):
    ranNumber = random.randint(0,10)
    ranNumber2 = random.randint(0,50)
    ranNumber3 = random.randint(0,50)
    ranNumberR = random.randint(0,255)
    ranNumberG = random.randint(0,255)
    ranNumberB = random.randint(0,255)
    try:
        
        subjectNumber = random.randint(1,20)
        imageName = subjectWords[subjectNumber]+'/'+subjectWords[subjectNumber]+'-'+str(ranNumber)+'.jpg'
        newImageName = str(i)+'.jpg'
        image = Image.open(imageName)
        fontType = ImageFont.truetype('impact.ttf',50)
        draw = ImageDraw.Draw(image)
        width,height = image.size
        newWidth = ((width/2)-(width/7))
        newHeight = (height-(height/9))-10
        draw.text(xy=(newWidth,20),text=subjectX[ranNumber2],fill=(ranNumberR,ranNumberG,ranNumberB),font=fontType)
        draw.text(xy=(newWidth,newHeight),text=subjectX[ranNumber3],fill=(ranNumberR,ranNumberG,ranNumberB),font=fontType)
        if (width >= 200)and(height >= 200):
            os.chdir('memes')
            image.save(newImageName)
            
            os.chdir('..')
    except:
        pass
    


