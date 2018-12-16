import requests

token = 'EAAAAAYsX7TsBAAIT0yKd0gZCtJIXR7hTjzG0m3Bup6f0cjsb0V9pCPGU9n2sSp58ZCC2wdtLzqikd7LioArvoujLXVimzVGBSm4PruzpZCZAoKOQiTHwzUZArx4Tp1Ke0HmzxqJ4F1YqvjeeDfBh7mBBi8JN3cJXw2L2ZCPQbEMgZDZD'
payload = {'method': 'get', 'access_token': token}
group_id = '1425733670814087'

list = []
groups = requests.get('https://graph.facebook.com/' + group_id + '/feed', params=payload).json()
for i in range(0, 5):
    for feed in groups['data']:
        feed_id = feed['id']
        try:
            comments = requests.get('https://graph.facebook.com/' + feed_id + '/comments', params=payload).json()
            for comment in comments['data']:
                user_id = comment['from']['id']
                if user_id not in list:
                    list.append(user_id)
        except KeyError:
            pass
        try:
            reactions = requests.get('https://graph.facebook.com/' + feed_id + '/reactions', params=payload).json()
            for reaction in reactions['data']:
                user_id = reaction['id']
        except KeyError:
            pass
    try:
        next_paging = groups['paging']['next']
        groups = requests.get(next_paging).json()
    except KeyError:
        pass
file = open('listID.txt', 'w')
inputID = ''
for item in list:
    inputID = inputID + item + '\n'
file.write(inputID)
file.close()