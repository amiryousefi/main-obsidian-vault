---
status: done
created: 2023-03-29
base: "[[Medium.base]]"
---
### Intro

There are lots of YouTube downloader services, free or premium. If you are curious how these services may work or you like to have a YouTube downloader of your own, you can read this article and create a simple YouTube downloader. You can benefit from this for your personal use or use this code to build something more extensive like a YouTube downloader service or any other kind of YouTube integration you may need.

We will use the PyTube package with Flask framework to create a simple web page that makes it easy to download a single video, videos of a playlist, or an entire channel’s videos.

So first thing first, let’s start by installing both Flask and PyTube packages:


```shell
pip install pytube
pip install Flask
```

Don’t forget to use pip3 instead of pip if you needed.

### Introducing PyTube package

Python has many valuable packages that you can use for scraping and downloading files from over the internet. The PyTube package is a lightweight and dependency-free Python package specially designed to download videos from YouTube.

With this package you can have these features:

- Downloading a video
- Downloading all videos of a playlist
- Downloading all videos of a channel
- Downloading captions for a video
- Thumbnail download

So now that you know about this package, let’s see that in action.

### Main code for downloading a video

As mentioned above, we’re going to use the Flask framework to build a YouTube downloader web service. But first let’s take a look at the main code that does the actual job, which is downloading a video.

```python
import os

from flask import Flask, request, render_template
from datetime import datetime
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

def download_video(video_url):
    download_started_at = datetime.now()

    video = YouTube(video_url)
    # video = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)

    file_path = f"downloads/{video.video_id}.mp4"

    try:

        youtube_stream = video.streams.get_highest_resolution()

        youtube_stream.download(output_path='downloads/', filename=f"{video.video_id}.mp4")

    except AgeRestrictedError:
        age_restricted = "yes"

    download_ended_at = datetime.now()

    check_exist = os.path.exists(file_path)

    data = {
        'video': video,
        'download_started_at': download_started_at.strftime("%d/%m/%Y %H:%M:%S"),
        'download_ended_at': download_ended_at.strftime("%d/%m/%Y %H:%M:%S"),
        'downloaded_in': (download_ended_at - download_started_at).seconds

    }

    return data if check_exist else False
```

This code is the core of the YouTube downloader service. Using the PyTube package, we create a `YouTube` object from the video URL we want to download. 

Then it tries to get the highest resolution of the video.

```python
youtube_streams = video.streams.get_highest_resolution()
```

You can filter streams based on the resolution to get a lower quality. For that, you can use a code like this:

```python
youtube_720_stream=video.streams.filter(res="720p")
```

No matter what stream quality you choose, the download code is the same. You can specify a download path and a file name so the file will store at the place you want with your desired name.

```python
youtube_stream.download(output_path='downloads/', filename=f"{video.video_id}.mp4"
```

I save videos with their video Ids which is the hash that you may see in the YouTube links. You can get this information from the `YouTube` object we created first. Video title is also available in the same way: `video.title` which actually translates to `YouTube(video_url).title`.

You can check [PyTube documentation](https://pytube.io/en/latest/api.html#youtube-object) to see what other data you can get from `YouTube` class. There are all data you may need from YouTube such as channel Id and URL, description, keywords, views, etc.

At last, we check if the file exists in the path we saved and return the video object with some extra data like how long it takes to be downloaded.

### Creating a YouTube downloader service

Using Python’s Flask package and having the main downloader code ready, we can create a web service to get a YouTube URL and download the video file.

This simple code will do the job:

```python
@app.route('/video', methods=['GET', "POST"])
def video_downloader():

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':

        video_url = request.form.get('video_url')

        if video_url:

            video = download_video(video_url)

            if video:
                return render_template('index.html', video=video)

            return "DL error", 500

        return "Invalid data", 422
```

This function returns an HTML template when called by `GET` method which has a simple form that users can submit a video URL in it.

When a video URL is submitted `download_vieo` function is called to download the video and return the same template with video data to show the downloaded video.

### YouTube playlist download

The logic is almost the same as downloading entire playlist videos. The only difference is that we get the video URLs from a playlist using PyTube.

PyTube has a `Playlist` class where you can get the playlist details such as all of its video URLs.
Given a playlist URL, we can get the video URLs with this code:

```python
from pytube import Playlist

playlist = Playlist(playlist_url)

playlist_video_urls = playlist.video_urls
```

Then it’s simply a job for our famous `download_video` function to download each video:

```python
downloaded_videos = []

videos_with_error = []

for video_url in playlist_video_urls:

	try:

		video = download_video(video_url)
		downloaded_videos.append(video)

	except Exception as e:

		videos_with_error.append(video_url)

    continue
```

Again, checking PyTube `Playlist` class documentation will give you a clue about the other details that you can get from a playlist, such as title, views, etc.

### YouTube channel download

To download a YouTube channel's entire videos, we’re gonna use the `Channel` class from `PyTube` package. This class provides channel details data alongside video URLs of a channel just like a playlist.

So a small code like this will get the URLs for videos.

```python
from pytube import Channel

channel = Channel(channel_url)

channel_video_urls = channel.video_urls
```

And we can use the same logic to download this list of video URLs

```python
downloaded_videos = []

videos_with_error = []

for video_url in channel_video_urls:

	try:

		video = download_video(video_url)
		downloaded_videos.append(video)

	except Exception as e:

		videos_with_error.append(video_url)

    continue
```

Keep this in mind that this code may take a while to finish, based on the video count in the channel and your connection speed. This code gets the videos from newest to oldest based on publish date, so you can add a break to the codes when you downloaded a number of the videos(like after 100 videos).

### Putting it all together

You can use these code portions separately, but I put it all in one basic Flask app to use these codes as a service.

This is the general structure of the app. You have already been introduced to the codes inside the functions.

```python
import os

from flask import Flask, request, render_template
from datetime import datetime
from pytube import YouTube, Playlist, Channel
from pytube.exceptions import AgeRestrictedError

app = Flask(__name__)


@app.route('/video', methods=['GET', "POST"])
def video_downloader():
	...


@app.route('/playlist', methods=['GET', "POST"])
def playlist_downloader():
	...


@app.route('/channel', methods=['GET', "POST"])
def channel_downloader():
	...


def download_video(video_url):
	...


if __name__ == '__main__':
    app.run()
```

The only other thing in this Flask app is a simple HTML template that has 3 forms, each with a single input to get either video, playlist, or channel URL.

```html
<!DOCTYPE html>
<html lang="en" >
<head>
  <title>YouTube downloader</title>
</head>
<body>
<div>
  <div>
    <h1>Video download</h1>

    <form action="/video" name='video' method='post>

      {% if video is defined %}
      <video width="320" height="240" controls>
        <source src='{{url_for("static", filename=video["video"]["video_id"]+".mp4")}}' type="video/mp4">
      </video>
      {% endif %}

      <input type='text' name='video_url' requiredplaceholder='Enter YouTube video URL'>
      <button>Download video</button>
    </form>
	</div>
    <hr/>
	<div>
    <h1 class='text-center'>Playlist download</h1>

    <form action="/playlist" name='playlist' method='post'>

      {% if downloaded_videos is defined %}

        {% for video in downloaded_videos %}

          <video width="320" height="240" controls>
            <source src='{{url_for("static", filename=video["video"]["video_id"]+".mp4")}}' type="video/mp4">
          </video>

        {% endfor %}

      {% endif %}

      <input type='text' name='playlist_url' required placeholder='Enter playlist URL'>
      <button>Download playlist</button>
    </form>
  </div>
	<hr/>
	<div>
    <h1>Channel download</h1>

    <form action="/channel" name='channel' method='post'>

      {% if channel_downloaded_videos is defined %}

        {% for video in channel_downloaded_videos %}

          <video width="320" height="240" controls>
            <source src='{{url_for("static", filename=video["video"]["video_id"]+".mp4")}}' type="video/mp4">
          </video>

        {% endfor %}

      {% endif %}

      <input type='text' name='channel_url' required placeholder='Enter channel URL'>
      <button>Download channel</button>
    </form>
  </div>
</div>

</body>
</html>
```

### Fixing PyTube problems(If you face any)

Since there are always lots of changes to YouTube it happens from time to time that PyTube does not work as you expected.

In those cases, make sure that you got the latest version of PyTube. Sometimes you need to install it from their Github instead of regular pip installation. For that, you can use this code:

```shell
python -m pip install git+https://github.com/pytube/pytube
```

Sometimes you need to do more. Like editing some files of the PyTube package. For that, you should know that these package files are stored in `site-packages` inside your Python installation just like any other package. Since I’m using `venv` my path for the PyTube package is something like this:

```shell
venv/lib/python3.9/site-packages/pytube
```

For example, I needed to change the entire [`channel.py`](http://channel.py/) file from this path:


```shell
venv/lib/python3.9/site-packages/pytube/contrib/channel.py
```

This[ code from the other fork in GitHub ](https://github.com/pishiko/pytube/blob/fix-channel/pytube/contrib/channel.py)was working fine but the installed code with the package was broken.

Also from my experience, there are always some changes to the `cipher` file in this path:

```shell
venv/lib/python3.9/site-packages/pytube/cipher.py
```

Mostly changes are happening to the regex in this file, like this one:
 https://github.com/pytube/pytube/pull/1698 

The last thing to mention here is not a real problem but something you need to have in mind downloading all types of videos from YouTube.

To download age-restricted videos or anything that needed you to be logged in, you can change this part of the `download_video` function:

```python
video = YouTube(video_url)
```

to this:

```python
video = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)
```

If you do change this, running this code for the first time will ask you on the terminal to go to your Google account and add a code.

![[Screenshot_2023-07-24_at_8.12.45_PM.png]]

By doing this, you can download whatever you see in your YouTube account.

---

I wrote a Flask app to serve a basic HTML template and get a URL, either for a video, playlist, or channel, and download the video or videos from YouTube. You can find the source code on my GitHub.

[https://github.com/amiryousefi/youtube-downloader](https://github.com/amiryousefi/youtube-downloader)

You can use this code as your own YouTube downloader and enhance it by adding progress indicators or a better way to show downloaded videos or any other great idea you may have.

Feel free to do pull requests to this repository and get in touch with me about your ideas.