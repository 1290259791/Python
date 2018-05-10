from urllib import request
import json
geturl = json.load(request.urlopen('http://172.16.154.130:8800/site/captcha?refresh=1&_=1524368423294'))
imageurl = 'http://172.16.154.130:8800' + geturl['url']
getimage = request.urlopen(imageurl)
imagefile = open('image.png','wb')
imagefile.write(getimage.read())
imagefile.close()

