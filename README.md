#Hypodrical
##Podcasting app, named hypodrical because... names.

This isn't a reusable app because I'm not really sure how much I want to seperate the whole site from the podcasting element (and because this is my first stab at running multiple sites from the same code base). For now it will be the entire site, probably seperated into branches for [animpolitepodcast.com](http://www.animpolitepodcast.com), [hypotheticalpodcast.com](http://www.hypotheticalpodcast.com) and [theunreliablespodcast.com](http://www.theunreliablespodcast.com/). 


###Getting started

    git clone git@github.com:stickwithjosh/hypodrical.git
    virtualenv --no-site-packges env
    pip install -r requirements.txt
    ./manage.py syncdb
    ./manage.py runserver
    ./manage.py migrate
    

That'll get you rocking locally. If you want to push to heroku it should just be a matter of:

1. Setting config variables for SECRET_KEY, AWS_SECRET_KEY and PRODUCTION (set to True).
2. Update settings.py to use your AWS_ACCESS_KEY_ID, AWS_STORAGE_BUCKET_NAME, and AWS_S3_CUSTOM_DOMAIN to be accurate for your deal.
3. You'll probably also want to take a pass throgh the templates and lose the site specific language (particuarly in base.html and feeds.html!) At some point I'll try to get the master branch clean enough so you wouldn't have to worry with this or feeding from the DB maybe so that it's a little less finicky.


### Thanks

Huge thanks to [Anthony Kolber](http://aestheticallyloyal.com/) for [audio.js](http://kolber.github.com/audiojs/) which is included in this project for ease of deployment.

###License

Hypodrical is released under a [MIT license](http://opensource.org/licenses/mit-license.php)