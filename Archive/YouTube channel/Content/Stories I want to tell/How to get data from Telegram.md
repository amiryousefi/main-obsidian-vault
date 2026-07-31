---
status: in-progress
base: "[[Stories I want to tell.base]]"
---

### See the results

To look into these JSON files you can use online JSON viewers. These are lists of message objects which include the message itself, date, media objects, and other details.

Also, you can go through Telethon API documentation here and look into each object's details.

On this site, you can go through any object and see what properties each object has. Like for Message object you can see its details.

But to use these saved JSON files properly, it's better to go through this list in a Python loop and extract each property you need. This way you can save your necessary part or even write it to a database or send it somewhere else like a WordPress site via an API call.

### Introducing Github Repo

You can find the source code for this project in my Github profile. To use this code, you can download it as a zip file or if you are familiar with git, you can pull it via this link here.

If you are looking into this page, don't forget to give a star to my repository or fork it to make use of it for yourself.

If you find out any improvement I'll appreciate your pull requests.

### Looking into source code

### Answering to comments

Ruben: every message comes with it’s sender but for channels you may just get the channel admin. for groups that if Telegram provides the data which it does for publicly available data, yes you could see the user.

by the way I like this kind of collaboartion

bulk message: this script is not about it but generally, yes you could do so by Telegram API and a propper python script, of course Telegram may limit you based on your message rates.

donyor: it may be related to your connection or sometimes it’s Telegram that prevent you to call it’s API by a lot in a short time. Telegram has another API for search which you can use that in a Python script.

Maxim: thanks

Aboubakr: Every message has a media object, you need to obtain that and you can use Telegram media object to download it. but for every wedensday part you may need more modification to search based on a date or hashtag.

Regi: just make sure to pull the latest code from Github and run this in Python3.

l3m0nrock: this is pretty wired to me too. you may clear dot files that created by Telegram client when you run this script or do everything over in a new folder and see if you get any new result.

Crypto: you either need to implement search API or when you go through downloaded messages in the JSON file have some if statement that do this job for you.

Thinnakorn: Sure, there’s a lot of code examples in nodejs as well.

gokhan: make sure to get he latest code and have the configuration file properly

guto: you can use a break.

Juan: if only you are joined to a channel.

florian: yes. everything Telegram provided.

Alpha6: yeah.

Wecare4u: data privacy, telegram API access, public private.

n bamek: this wil download all messages.

nico: real time requires bot.

