# YouTube Channel Scraper

This is a script that will get the latest videos from a spreadsheet of YouTube channels.

# Installation

```bash
pip install selenium
```

# Usage

1. Create a CSV file that looks like this:

   Name,Channel <br />
   FreeCodeCamp,https://www.youtube.com/c/Freecodecamp/videos <br />
   Today,https://www.youtube.com/c/TODAY/videos <br />
   TechWithTim,https://www.youtube.com/c/TechWithTim/videos <br />

2. Video scraping

```python
from watchlist import Scraper

sc = Scraper('channels.txt', 5)
vids = sc.scrapeVideos()

for vid in vids:
    print(vid)
```

Scraper takes 2 parameters. The first one is the CSV file containing the channels to be scraped. The second is the amount of videos to be scraped for each channel starting with the most recent upload.

Each video in vids has 3 properties. Those are the title, uploadDate and url of the video.

3. Writing videos to CSV files

```python
from watchlist import Scraper, Writer

sc = Scraper('channels.txt', 5)
vids = sc.scrapeVideos()

for vid in vids:
    print(vid)

wr = Writer(vids)
wr.writeVideosToCsv('vids.csv')
```

Writer takes one parameter. That is the videos array we obtained from sc.scrapeVideos().

The writeVideosToCsv function takes 1 parameter. That is the name of the CSV file which will store the videos.

4. Writing videos to HTML

```python
from watchlist import Scraper, Writer

sc = Scraper('channels.txt', 5)
vids = sc.scrapeVideos()

for vid in vids:
    print(vid)

wr = Writer(vids)
wr.writeVideosToCsv('vids.csv')
wr.writeVideosToHTML('test.html')
```

The writeVideosToHTML function takes 1 parameter. That is the name of the HTML file which will display the videos.

Your output should look similar to this image:
![Example Output](https://github.com/sciand6/python-youtube-web-scraper/blob/main/example_output.png?raw=true)

# Add as many channels as you wish

Add your favorite youtube channels using the format listed in step 1, and continue growing your watchlist.