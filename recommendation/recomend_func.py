import pandas as pd
import math
 
#标签流行度算法
def TagPopularity(records):
    tagfreq = dict()
    for user,item,tag in records:
        if tag not in tagfreq:
            tagfreq[tag] = 1
        else:
            tagfreq[tag] += 1
    return tagfreq
 
#物品相似度余弦算法
def CosineSim(item_tags,i,j):
    ret  = 0
    for b,wib in item_tags[i].items():
        if b in item_tags[j]:
            ret += wib * item_tags[j][b]
    ni = 0
    nj = 0
    for b,w in item_tags[i].items():
        ni += w * w
    for b,w in item_tags[j].items():
        nj += w * w
    if ret == 0:
        return 0
    return ret / math.sqrt(ni * nj)
 
#推荐物品的多样性算法
def Diversity(item_tags,recommend_items):
    ret = 0
    n = 0
    for i in recommend_items.keys():
        for j in recommend_items.keys():
            if i == j:
                continue
            ret += CosineSim(item_tags,i,j)
            n += 1
    return ret / (n * 1.0)
 
 
def addValueToMat(dicts,index,k,v):
    if index not in dicts:
        dicts[index] = dict()
        dicts[index][k] = v
    else:
        if k not in dicts[index]:
            dicts[index][k] = v
        else:
            dicts[index][k] += v
 
def InitStat(records):
    user_tags.clear() #存储 user_tags[u][b] = n(u,b)
    tag_items.clear() # tag_items[b][i] = n(b,i)
    user_items.clear()
    for user,item,tag in records.items():
        addValueToMat(user_tags,user,tag,1)
        addValueToMat(tag_items,tag,item,1)
        addValueToMat(user_items,user,item,1)
 
 
def Recommend(user):
    recommend_items = dict()
    tagged_items = user_items[user]
    for tag,wut in user_tags[user].items():
        # wut = wut*1.0/math.log(1+len(tag_users[tag])) #TagBasedTFIDF and TagBasedTFIDF++
        for item,wti in tag_items[tag].items():
            # wti = wti*1.0/math.log(1+len(user_items[user])) #TagBasedTFIDF++
            if item in tagged_items:
                continue
            if item not in recommend_items:
                recommend_items[item] = wut * wti
            else:
                recommend_items[item] += wut * wti
    return recommend_items
 
 
if __name__ == "main":
    user_tags = dict()
    user_items = dict()
    tag_items = dict()
 
    records = dict()
    user = '1220'
 
    InitStat(records)
    rec_items = Recommend(user)