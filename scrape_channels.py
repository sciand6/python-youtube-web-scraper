from selenium import webdriver
import csv
import os

def createDriver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    return browser

def getVideoGrid(driver, url):
    driver.get(url)
    grid = driver.find_elements_by_tag_name('ytd-grid-video-renderer')
    return grid

def getVideoTitle(grid, index):
    title = grid[index].find_element_by_id('video-title').get_attribute('innerHTML')
    return title

def getVideoUrl(grid, index):
    href = grid[index].find_element_by_id('video-title').get_attribute('href')
    return href

def getVideoUploadDate(grid, index):
    uploadDateParent = grid[index].find_element_by_id('metadata-line')
    uploadDate = uploadDateParent.find_elements_by_tag_name('span')[1].get_attribute('innerHTML')
    return uploadDate

def scrapeVideos(browser, url, limit, arr):
    grid = getVideoGrid(browser, url)
    for i in range(limit):
        title = getVideoTitle(grid, i)
        uploadDate = getVideoUploadDate(grid, i)
        href = getVideoUrl(grid, i)
        video = [title, uploadDate, href]
        arr.append(video)

def writeVideosToCsv(videos):
    with open('videos.csv', mode='w', encoding='utf-8') as video_file:
        for video in videos:
            title = video[0]
            uploadDate = video[1]
            href = video[2]
            video_file.write(title + "," + uploadDate + "," + href + "\n")

def writeVideosToHTML(videos):
    l = 0
    # Generate intitial HTML
    html = """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl"
            crossorigin="anonymous"
            />
            <title>Recent Uploads</title>
        </head>
        <body>
        <div class="container">
            <div class="d-flex justify-content-center mb-4">
                <h1>Recent Uploads</h1>
            </div>
    """
    with open('index.html', mode='w', encoding='utf-8') as html_file:
        html_file.write(html)
        for video in videos:
            l = l + 1
            title = video[0]
            uploadDate = video[1]
            href = video[2]
            videoCard = f"""
            <div class="card mt-4">
                <div class="card-body">
                <h4 class="card-title">{title}</h4>
                <div class="card-subtitle text-muted mb-2">{uploadDate}</div>
                <a href="{href}" class="btn btn-primary"
                    >{href}</a
                >
                </div>
            </div>
            """
            html_file.write(videoCard)
        footer = """
                </div>
            </div>
        </body>
        </html>
        """
        html_file.write(footer)
        html_file.close()
        
# Sorting
def getLevel(uploadDate):
    if uploadDate == "minute":
        return 0
    elif uploadDate == "minutes":
        return 1
    elif uploadDate == "hour":
        return 2
    elif uploadDate == "hours":
        return 3
    elif uploadDate == "day":
        return 4
    elif uploadDate == "days":
        return 5
    elif uploadDate == "week":
        return 6
    elif uploadDate == "weeks":
        return 7
    elif uploadDate == "month":
        return 8
    elif uploadDate == "months":
        return 9
    elif uploadDate == "year":
        return 10
    elif uploadDate == "years":
        return 11

def bubbleSortVideos(array):
    n = len(array)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            doSwap = False
            uploadDate1Split = array[j][1].split(" ")
            uploadDate2Split = array[j + 1][1].split(" ")
            if getLevel(uploadDate1Split[1]) == getLevel(uploadDate2Split[1]):
                if int(uploadDate1Split[0]) > int(uploadDate2Split[0]):
                    doSwap = True
            elif getLevel(uploadDate1Split[1]) > getLevel(uploadDate2Split[1]):
                doSwap = True
            
            if doSwap:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array

videos = []

# Get user input
videoCount = int(input("Enter how many videos you want to scrape per channel: "))

# Create browser
browser = createDriver()

# Operation for getting the data of multiple artists
with open("channels.txt") as artistFile:
    # Open the CSV
    csv_reader = csv.reader(artistFile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # Skip the headers line
        if line_count == 0:
            line_count += 1
        else:
            # Get the url
            channelURL = row[1]
            # Scrape the videos
            scrapeVideos(browser, channelURL, videoCount, videos)

bubbleSortVideos(videos)
writeVideosToCsv(videos)
writeVideosToHTML(videos)

os.system("index.html")

# Exit
browser.quit()

