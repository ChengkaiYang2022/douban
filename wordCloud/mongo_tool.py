from pymongo import MongoClient
def write_file(film_id):
    client = MongoClient('localhost', 27017)
    db = client.douban
    collection = db['DoubanShoutComments']
    a = collection.find({"film_id":film_id})
    c_list = list()
    for post in collection.find({"film_id":film_id}):
        # pprint.pprint(post['comment_info'])
        c_list.append(post['comment_info'])
    print(".".join(c_list))
    with open(film_id+".txt","w",encoding="utf-8") as f:
        f.writelines(".".join(c_list))
write_file(str(27191492))
