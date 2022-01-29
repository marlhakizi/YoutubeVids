from googleapiclient.discovery import build


youtubeAPIkey = "AIzaSyBYSq3ka4lcC3sdOt6t0jfKYBw3C9JA00o"
youtube = build("youtube", "v3", developerKey=youtubeAPIkey)

def get_channelinfo(chanid):
    results = youtube.channels().list(part="contentDetails", id=chanid).execute()
    #return (results)
    playlistid = results["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    allvideos = []
    next_Page_Token = None
    while 1:
        videocontent = (
            youtube.playlistItems()
            .list(
                part="contentDetails",
                playlistId=playlistid,
                maxResults=50,
                pageToken=next_Page_Token,
            )
            .execute()
        )
        # print(videocontent)
        for item in videocontent["items"]:
            allvideos.append(item["contentDetails"]["videoId"])

        next_Page_Token = videocontent.get("nextPageToken")

        if next_Page_Token is None:
            break
    max = -1
    vidid = 0
    # videoid = "revn4n2v8-U"
    # infovid = youtube.videos().list(part="statistics", id=videoid).execute()
    for i in allvideos:
        infovid = youtube.videos().list(part="statistics", id=i).execute()
        for item in infovid["items"]:
            if max < int(item["statistics"]["viewCount"]):
                max = int(item["statistics"]["viewCount"])
                vidid = i
    infovidsnippet = youtube.videos().list(part="snippet", id=vidid).execute()
    infovidinfo = youtube.videos().list(part="statistics", id=vidid).execute()
    information = ["publishedAt", "title", "statistics"]
    time = infovidsnippet["items"][0]["snippet"]["publishedAt"]
    title = infovidsnippet["items"][0]["snippet"]["title"]
    stats = infovidinfo["items"][0]["statistics"]
    videodictinfo = dict(zip(information, [time, title, stats]))

    return dict(zip([vidid], [videodictinfo]))