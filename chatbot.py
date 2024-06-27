from instabot import Bot
bot=Bot()
bot.login(username="_being._.strong_",password="bijepo")
bot.follow("space_coderr")
bot.unfollow("")
bot.send_message("I Love.....",["space_coderr"])
bot.upload_photo()
followers=bot.get_user_followers("")
for follower in followers:
    print(bot.get_user_info)("follower")
following=bot.get_user_following("")
for follows in following:
    print(bot.get_user_info("follows"))
bot.upload_photo()
bot.upload_story_photo()
bot.upload_video()
