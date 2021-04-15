from watchlist import Scraper, Writer

sc = Scraper('channels.txt', 5)
vids = sc.scrapeVideos()

for vid in vids:
    print(vid)

wr = Writer(vids)
wr.writeVideosToCsv('vids.csv')
wr.writeVideosToHTML('test.html')