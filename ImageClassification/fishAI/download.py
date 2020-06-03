from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
from tqdm import tqdm
import os, time, sys

# APIキーの情報

key = "4790622ca19ec3c6aac84ffce4ce8a95"
secret = "a108c90fa6953a51"
wait_time = 1

# 保存フォルダの指定

animalname = 'Brown-lined puffer'
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
	text = animalname,
	per_page = 500,
	media = 'photos',
	sort = 'relevance',
	safe_search = 1,
	extras = 'url_q, licence'
) 

photos = result['photos']
# pprint(photos)

for i, photo in tqdm(enumerate(photos['photo'])):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
