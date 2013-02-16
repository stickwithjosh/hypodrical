#Hypodrical
##Podcasting app, named hypodrical because... names.

This isn't a reusable app because I'm not really sure how much I want to seperate the whole site from the podcasting element (and because this is my first stab at running multiple sites from the same code base). For now it will be the entire site, probably seperated into branches for [animpolitepodcast.com](http://www.animpolitepodcast.com), [hypotheticalpodcast.com](http://www.hypotheticalpodcast.com) and [theunreliablespodcast.com](http://www.theunreliablespodcast.com/). 


###Getting started

    git clone git@github.com:stickwithjosh/hypodrical.git
    virtualenv --no-site-packges env
    pip install -r requirements.txt
    ./manage.py syncdb
    ./manage.py runserver
    


### Thanks

Huge thanks to [Anthony Kolber](http://aestheticallyloyal.com/) for [audio.js](http://kolber.github.com/audiojs/) which is included in this project for ease of deployment.

###License

Hypodrical is released under a [MIT license](http://opensource.org/licenses/mit-license.php)