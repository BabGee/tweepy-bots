# tweepy-bots

**tweepy-bots** is a Twitter Bot in Python with Tweepy, a package that provides a convenient way to use the Twitter API. It contains the following bots:
   
1. The Reply to Mentions Bot(autoreply.py) that automatically replies to tweets mentioning you that match certain criteria e.g containing the words help or support.
2. The Fav & Retweet Bot(favretweet.py) that automatically likes and retweets tweets that match certain criteria e.g containing the words python or django.
3. The Follow Followers Bot(followfollowers.py) that automatically follows anyone who follows you.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites
You will find hereafter what I use to develop and to run the project
* Twitter developer account to use its API
* Python 3.9
* pipenv (not mandatory but highly recommended)

### Installing
Get a local copy of the project directory by cloning "tweepy-bots" from github. `git clone git@github.com:BabGee/tweepy-bots.git` 
I use pipenv for developing this project so I recommend you to create a virtual environment and activate it, `pipenv shell`  and to install the requirements `pip install -r requirements.txt`.

Then follow these steps:
1. Create a `.env` file in the root folder, provide the required app details from your twitter developer portal to the `.env` file (.env.example file is provided to help set this information)
2. Finally, execute the bots
    i. Run `python bots/autoreply.py`
    ii. Run `python bots/favretweet.py`
    iii. Run `python bots/followfollowers.py`


## Built With

* [Python 3](https://www.python.org/downloads/) - Programming language


## Versioning
I use exclusively Github

## License

This is an open source project not under any particular license.
However framework, packages and libraries used are on their own licenses. Be aware of this if you intend to use part of this project for your own project.

