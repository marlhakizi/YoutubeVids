from scraper import  get_channelinfo

def test_results():
    assert(get_channelinfo("UCM5cUUo5Asa-QgFrBu9L7EQ")=={'xwbD6fL5qC8': {'publishedAt': '2020-11-25T21:59:21Z', 'title': 'CUDA Programming', 'statistics': {'viewCount': '10705', 'likeCount': '288', 'favoriteCount': '0', 'commentCount': '13'}}})
    