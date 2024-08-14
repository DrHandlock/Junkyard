# By Jerry Halflin for [REDACTED]

# Iteration 1.01 of reddit bot: "Portal-Gun-Bot"

# Note to future users of this script: this version has never been tested, or any other versions below it. 


import praw
import random

# Authentication
reddit = praw.Reddit(
    client_id='client_id',
    client_secret='client_secret',
    user_agent='user_agent',
    username='username',
    password='password'
)

# Lists:
link_list = []  # Portal ID mapping
C_link_list = []  # Comment ID mapping
subreddits_list = [ #List of the subreddits that could be randomly chosen
    'AskReddit', 'worldnews', 'funny', 'gaming', 'aww', 'science', 'pics', 'technology', 
    'todayilearned', 'IAmA', 'askscience', 'explainlikeimfive', 'books', 'movies', 
    'television', 'Music', 'DIY', 'space', 'gadgets', 'dataisbeautiful', 'Documentaries', 
    'GetMotivated', 'history', 'UpliftingNews', 'WritingPrompts', 'Food', 'sports', 
    'Art', 'EarthPorn', 'philosophy', 'travel', 'Fitness', 'personalfinance', 
    'lifehacks', 'nosleep', 'OldSchoolCool', 'Futurology', 'Showerthoughts', 
    'nottheonion', 'photoshopbattles', 'tifu', 'Jokes', 'interestingasfuck', 
    'mildlyinteresting', 'wholesomememes', 'creepy', 'listentothis', 'technology', 
    'movies', 'gadgets', 'space', 'nottheonion', 'bestof', 'GetMotivated', 'InternetIsBeautiful', 
    'Documentaries', 'gadgets', 'photoshopbattles', 'Cinemagraphs', 'ExposurePorn', 
    'wallpapers', 'RoomPorn', 'FoodPorn', 'MachinePorn', 'QuotesPorn', 'HistoryPorn', 
    'carporn', 'HousePorn', 'MilitaryPorn', 'BotanicalPorn', 'StarWars', 'FanTheories', 
    'conspiracy', 'TrueReddit', 'bestof', 'changemyview', 'CrazyIdeas', 'technology', 
    'YouShouldKnow', 'LifeProTips', 'IWantToLearn', 'howto', 'DIY', 'LifeHacks', 
    'DoesAnybodyElse', 'explainlikeimfive', 'TodayILearned', 'AskHistorians', 
    'history', 'AskReddit', 'science', 'AskScience', 'askphilosophy', 'philosophy', 
    'politics', 'news', 'worldnews', 'TrueCrime', 'JusticeServed', 'legaladvice', 
    'InternetIsBeautiful', 'food', 'Cooking', 'recipes', 'baking', 'foodhacks', 
    'EatCheapAndHealthy', 'food', 'nutrition', 'MealPrepSunday', 'GetMotivated', 
    'quotes', 'LifeProTips', 'personalfinance', 'investing', 'Frugal', 'financialindependence', 
    'povertyfinance', 'budget', 'StudentLoans', 'Insurance', 'debtfree', 'RealEstate', 
    'homestead', 'financialindependence', 'Frugal', 'careerguidance', 'productivity', 
    'GetDisciplined', 'entrepreneur', 'startups', 'smallbusiness', 'workonline', 
    'freelance', 'business', 'Marketing', 'sales', 'digital_marketing', 'web_design', 
    'graphic_design', 'art', 'Design', 'logos', 'userexperience', 'typography', 
    'crafts', 'DIY', 'woodworking', 'sewing', 'knitting', 'crochet', 'leathercraft', 
    'Ceramics', 'origami', 'gardening', 'bonsai', 'minipainting', 'Embroidery', 
    'modelmakers', 'drawing', 'Illustration', 'calligraphy', 'painting', 'watercolor', 
    'comics', 'comicbooks', 'Marvel', 'DCcomics', 'webcomics', 'manga', 'anime', 
    'movies', 'television', 'Netflix', 'Hulu', 'YouTube', 'Documentaries', 'TrueFilm', 
    'cinematography', 'FilmMaking', 'moviecritic', 'screenwriting', 'books', 
    'WritingPrompts', 'FanFiction', 'booksuggestions', 'bookclub', 'literature', 
    'audiobooks', 'comics', 'comicbooks', 'MangaCollectors', 'noveltranslations', 
    'creepy', 'nosleep', 'horror', 'Thetruthishere', 'UnresolvedMysteries', 
    'conspiracy', 'Paranormal', 'creepypasta', 'Scarymovies', 'ShortScaryStories', 
    'TrueScaryStories', 'Ghosts', 'Glitch_in_the_Matrix', 'Aliens', 'Abductions', 
    'psychology', 'MentalHealth', 'self', 'depression', 'anxiety', 'ADHD', 
    'Fitness', 'bodyweightfitness', 'Running', 'bicycling', 'Swimming', 'Yoga', 
    'Crossfit', 'weightlifting', 'homegym', 'golf', 'tennis', 'squash', 'climbing', 
    'hiking', 'camping', 'survival', 'outdoors', 'Fishing', 'hunting', 'archery', 
    'guns', 'martialarts', 'boxing', 'jiujitsu', 'karate', 'taekwondo', 'wrestling', 
    'Judo', 'fencing', 'Football', 'soccer', 'baseball', 'basketball', 'hockey', 
    'Cricket', 'rugby', 'motorsports', 'racing', 'Nascar', 'F1', 'billiards', 
    'esports', 'gaming', 'boardgames', 'chess', 'poker', 'MagicTCG', 'tabletop', 
    'tabletopgamedesign', 'tabletoprpg', 'dnd', 'DnDBehindTheScreen', 'LARP', 
    'startrek', 'startrekmemes', 'startrekships', 'startrekpic', 'TheExpanse', 
    'HarryPotter', 'Lotr', 'lotrmemes', 'StarWars', 'Marvel', 'marvelmemes', 
    'DCcomics', 'comicbooks', 'Manga', 'anime', 'otaku', 'cosplay', 'cosplaygirls', 
    'cosplayprops', 'cosplayhelp', 'costume', 'steampunk', 'cyberpunk', 'fantasy', 
    'scifi', 'fanfiction', 'writing', 'writers', 'nanowrimo', 'poetry', 'fanart', 
    'deviantart', 'art', 'digitalpainting', 'blender', 'modelmakers', 'photography', 
    'photoshop', 'drawing', 'illustration', 'ArtCrit', 'ArtFundamentals', 'graphic_design', 
    'typography', 'logodesign', 'comics', 'comicbooks', 'IndieDev', 'gamedev', 
    'gameideas', 'Screenwriting', 'filmmakers', 'cinematography', 'videography', 
    'videoeditors', 'animation', 'motiongraphics', 'aftereffects', 'vfx', '3Dmodeling', 
    '3Dprinting', 'blender', 'programming', 'learnprogramming', 'coding', 'compsci', 
    'datascience', 'MachineLearning', 'ArtificialIntelligence', 'bigdata', 'statistics', 
    'math', 'Physics', 'chemistry', 'biology', 'neuroscience', 'space', 'astronomy', 
    'astrophysics', 'engineering', 'robotics', 'electronics', 'arduino', 'raspberry_pi', 
    'computers', 'buildapc', 'mac', 'linux', 'networking', 'sysadmin', 'cloudcomputing', 
    'techsupport', 'android', 'iOS', 'gadgets', 'Smartphones', 'apple', 'windows', 
    'technews', 'programming', 'python', 'javascript', 'webdev', 'web_design', 
    'css', 'html', 'sql', 'nosql', 'database', 'blockchain', 'cryptocurrency', 
    'bitcoin', 'ethereum', 'investing', 'stocks', 'trading', 'forex', 'FinancialIndependence', 
    'Frugal', 'RealEstate', 'PersonalFinance', 'Budget', 'StudentLoans', 'debtfree', 
    'Insurance', 'retirement', 'CreditCards', 'fire', 'LeanFIRE', 'FatFIRE', 'business', 
    'startups', 'Entrepreneur', 'smallbusiness', 'marketing', 'SEO', 'digital_marketing', 
    'socialmedia', 'sales', 'networking', 'investing', 'finance', 'stockmarket', 
    'CryptoCurrency', 'Bitcoin', 'ethereum', 'blockchain', 'programming', 'webdev', 
    'datascience', 'machinelearning', 'engineering', 'electronics', 'robotics', 
    'arduino', 'raspberry_pi', 'diy', 'woodworking', 'gardening', 'homestead', 
    'bicycling', 'Fitness', 'running', 'climbing', 'hiking', 'camping', 'outdoors', 
    'Fishing', 'hunting', 'guns', 'archery', 'martialarts', 'boxing', 'jiujitsu', 
    'taekwondo', 'wrestling', 'Judo', 'Portal', 'ChatGPT', 'MinecraftMemes, PhoenixSC'
    , 'SCP', 'TheLetterH']


def destination_finder():
    for message in reddit.inbox.unread(limit=None):
        if isinstance(message, praw.models.Message):
            if message.body == "!random":
                portal_creation("", True, message.author.name, len(link_list) - 2, "unknown", message.id)
                message.mark_read()
            elif "!goto_" in message.body:
                destination = message.body.replace("!goto_", "")
                portal_creation(destination, False, message.author.name, len(link_list) - 2, "unknown", message.id)
                message.mark_read()
            else:
                message.reply("Sorry, your response could not be accepted. Please use the commands !random or !goto_r/subreddit_name. \n ^(This response was automated by a bot)")
                message.mark_read()

def portal_creation(location, randomness, opener, id_index, start_subr, origin_id):
    num_index = id_index

    if randomness:
        landing = random.choice(subreddits_list)
    else:
        landing = location

    landed_subreddit = reddit.subreddit(landing)
    posts = list(landed_subreddit.top(limit=50))
    landed_post = random.choice(posts)

    C_link_list[num_index + 1] = landed_post.id

    landed_post.reply(
        f"A portal has been created in this post by {opener} from {start_subr} \n"
        f"^(This response is automated by a bot) \n"
        f"[{link_list[num_index]}] [{C_link_list[num_index + 1]}]"
    )

    # Comment on the original post (to verify information back to the opener)
    reddit.comment(origin_id).reply(
        f"The portal has been opened \n Comment ID: {landed_post.id} \n"
        f"^(This response is automated by a bot)"
    )

def manage_link():
    for voice in reddit.inbox.unread(limit=None):
        if isinstance(voice, praw.models.Comment):
            if voice.parent_id in C_link_list:
                vocal_parent_unindexed = voice.parent_id
                if C_link_list[C_link_list.index(vocal_parent_unindexed) + 1] != "UCR":
                    vocal_parent_indexed = C_link_list.index(vocal_parent_unindexed)
                    passthrough(voice, voice.author.name, vocal_parent_indexed)
                voice.mark_read()

def passthrough(echo, echo_owner, index):
    side = index % 2
    side_conversion = 1 if side == 1 else -1
    linked_comment_id = C_link_list[index + side_conversion]
    linked_comment = reddit.comment(linked_comment_id)
    linked_comment.reply(
        f"{echo.body} \n ^(This response was not created by this bot "
        f"\n rather this response was created by a user called {echo_owner})"
        f" btw here is the comment ID of which this reply originated from: {echo.id})"
    )

# Main loop
while True:
    try:
        monitor_comments()
        destination_finder()
        manage_link()
    except Exception as error:
        logging.error(f"An error occurred: {error}")