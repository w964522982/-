#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :use.py
@说明    :《动物餐厅》修改代码，因为进行过整合，不能确保能不能正确运行，可以自行测试
@时间    :2020/08/07 14:27:53
@作者    :DanceDJ
@微信公众号    :给我一碗炒饭
@版本    :1.0
'''

import json,requests
import hashlib

def encode(key,value):
    i=602
    n=int(value)+100+i
    globalKey="twgame_rj32io"
    data=str(n)+globalKey+key
    res=hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    enres="t"+res[17]+res[3]+res[27]+res[11]+res[23]+str(i)+value
    print(key+" ------"+enres)
    return enres

def check(key,value,i,md5):
	#n=value+str(100+int(i))
	n=int(value)+int(100+int(i))
	globalKey="twgame_rj32io"
	globalKey="oe6z64rTGm0k2f8WjqcF2gNjPxCM"
	data=str(n)+globalKey+key
	res=hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
	checkmd5=res[17]+res[3]+res[27]+res[11]+res[23]
	enres="t"+checkmd5+str(i)+value
	#print("计算值 %s" %(enres))
	if(checkmd5==md5):
		return "YES"
	else:
		return "NO"


def checkSign2(record,openid):
    '''
    efc2f553
    var i = h.MD5("32roiFEI" + e.record + n.openid).toString();
    e.checkSign2 = i.charAt(8) + i.charAt(3) + i.charAt(21) + i.charAt(10) + i.charAt(16) + i.charAt(9) + i.charAt(11) + i.charAt(23), 
    '''
    globalKey="32roiFEI"
    data=globalKey+record+openid
    res=hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    checkmd5=res[8]+res[3]+res[21]+res[10]+res[16]+res[9]+res[11]+res[23]
    print("checkmd5 ------ "+checkmd5)
    return checkmd5

def record(enopenid,code):
    url="https://dsa-restaurant-beijing.twomiles.cn/uploadRecord"
    record='{"lastServerId":"tb89b99082","openid":"{\\"openid\\":\\"oe6z64rTGm0k2f8WjqcF2gNjPxCM\\",\\"serverId\\":399}","signupTime":"t594ff8091596429246903","version":"t40faa20535","theme_theme_outdoor_group":"t8ec873808","theme_theme_diningRoom_group":"t6d2741422","theme_theme_kitchRoom_group":"tfac909292","theme_theme_buffetRoom_group":"ta17ef4932","cookbook_unlock_food_10":"tbf8b78181","fixDlg_p2":"t45eef5451","building_lv_building_1_group":"td91a49222","customer_unlock_customer_2":"t343e06561","building_lv_building_24_group":"tbda5b2402","freeAdCount":"t44adb1731","customerComingCount":"tac28b88214","building_lv_building_2_group":"tacde12202","cookbook_unlock_food_49":"t87c962601","customer_unlock_customer_54":"t8831b8311","barrage_8":"tb85fb5421","building_lv_building_25_group":"ta8ae56822","tutorials_progress_two":"tb8ab43935","customer_unlock_customer_40":"t6e2572391","building_lv_building_3_group":"t15dc58252","cookbook_unlock_food_50":"t8d9c77711","barrage_3":"tda49d8051","building_lv_building_8_group":"tc38af6152","tipSum":"tb85236210","cookbook_unlock_food_32":"tc56572941","recommendAppVersion":"tea2a53551","guide_task_progress":"tf36d84438","shareTimes":"t95a0f5450","resetTimestamp":"t5cf823601596516549468","capsuleFreeTimes":"tfe81a7440","PondUserDataKey":"[{\\"boothID\\":1,\\"owner\\":-1,\\"state\\":1,\\"constructionEndTime\\":-1,\\"hiringStartTime\\":-1,\\"hiringEndTime\\":-1,\\"hiringOutputTimes\\":[],\\"caseReadyFishTag\\":-1,\\"caseReadyFishID\\":-1,\\"rentingEndTime\\":-1,\\"rentingResult\\":null,\\"rentingLifeLeftTime\\":-1,\\"rentingFishID\\":-1,\\"offlineOutputTimes\\":-1,\\"offlineOwner\\":-1},{\\"boothID\\":2,\\"owner\\":-1,\\"state\\":1,\\"constructionEndTime\\":-1,\\"hiringStartTime\\":-1,\\"hiringEndTime\\":-1,\\"hiringOutputTimes\\":[],\\"caseReadyFishTag\\":-1,\\"caseReadyFishID\\":-1,\\"rentingEndTime\\":-1,\\"rentingResult\\":null,\\"rentingLifeLeftTime\\":-1,\\"rentingFishID\\":-1,\\"offlineOutputTimes\\":-1,\\"offlineOwner\\":-1},{\\"boothID\\":3,\\"owner\\":-1,\\"state\\":1,\\"constructionEndTime\\":-1,\\"hiringStartTime\\":-1,\\"hiringEndTime\\":-1,\\"hiringOutputTimes\\":[],\\"caseReadyFishTag\\":-1,\\"caseReadyFishID\\":-1,\\"rentingEndTime\\":-1,\\"rentingResult\\":null,\\"rentingLifeLeftTime\\":-1,\\"rentingFishID\\":-1,\\"offlineOutputTimes\\":-1,\\"offlineOwner\\":-1},{\\"boothID\\":4,\\"owner\\":-1,\\"state\\":1,\\"constructionEndTime\\":-1,\\"hiringStartTime\\":-1,\\"hiringEndTime\\":-1,\\"hiringOutputTimes\\":[],\\"caseReadyFishTag\\":-1,\\"caseReadyFishID\\":-1,\\"rentingEndTime\\":-1,\\"rentingResult\\":null,\\"rentingLifeLeftTime\\":-1,\\"rentingFishID\\":-1,\\"offlineOutputTimes\\":-1,\\"offlineOwner\\":-1},{\\"boothID\\":5,\\"owner\\":-1,\\"state\\":1,\\"constructionEndTime\\":-1,\\"hiringStartTime\\":-1,\\"hiringEndTime\\":-1,\\"hiringOutputTimes\\":[],\\"caseReadyFishTag\\":-1,\\"caseReadyFishID\\":-1,\\"rentingEndTime\\":-1,\\"rentingResult\\":null,\\"rentingLifeLeftTime\\":-1,\\"rentingFishID\\":-1,\\"offlineOutputTimes\\":-1,\\"offlineOwner\\":-1},{\\"boothID\\":6,\\"owner\\":-1,\\"state\\":1,\\"constructionEndTime\\":-1,\\"hiringStartTime\\":-1,\\"hiringEndTime\\":-1,\\"hiringOutputTimes\\":[],\\"caseReadyFishTag\\":-1,\\"caseReadyFishID\\":-1,\\"rentingEndTime\\":-1,\\"rentingResult\\":null,\\"rentingLifeLeftTime\\":-1,\\"rentingFishID\\":-1,\\"offlineOutputTimes\\":-1,\\"offlineOwner\\":-1}]","barrage_6":"t4faf91091","barrage_10":"ta7f338261","barrage_13":"t1f37b4291","building_lv_building_26_group":"t795d35272","npcInitStep":"t19aad5681","lastCreateNpcTime":"tae7263341596516672801","customer_unlock_npc_3":"t6eb305251","building_lv_building_14_group":"t7f74e2362","daily_task_list_id_0":"t3332289827","daily_task_list_id_1":"te339a37030","daily_task_list_id_2":"t4010423013","daily_task_list_id_3":"tc56b24939","daily_task_list_id_4":"tcaa6e7462","daily_task_list_id_5":"t563a818328","daily_end_time":"t817f74071596516773417","tutorials_progress":"t8451e4418","noticeRedDotTime":"{\\"noticeRedDotTime\\":\\"2020-7-28-0\\"}","hasSubscribeOrder":"{\\"subscribeOrder\\":null}","orderMap":"{\\"order_1\\":1596556800000}","building_lv_building_4_group":"tf99e28332","building_lv_building_5_group":"t5e75a3562","building_lv_building_6_group":"t4e56d1492","building_lv_building_27_group":"t9177e1662","lastTimeRecord":"t6d6012831596516924177","daily_total":"tedf975842","dt_daily_cus_count_customer_40customer_40":"t17f193951","dt_daily_cus_count_customer_2customer_2":"t390876291","playTime":"t91a20555601417","building_lv_building_28_group":"t287313162","cumulative_ad":"tfa8c9421618","daily_cumulative_ad":"t4b079285186","cumulative_sendAd":"t432434702","advertiseAdCount":"tbdff11511","customer_unlock_customer_21":"tab3643741","cumulative_food_food_32":"t6fd3d4129","tipTimestamp":"t7f5846551596517038692","daily_cus_count_customer_2":"t5068d39217","cumulative_food_food_10":"td9dc767045","cumulative_customer_customer_2":"t9f21215345","cumulative_customer_customer_54":"td65fb99342","daily_cus_count_customer_40":"tbcae449315","cumulative_customer":"t3c3c0499118","daily_cumulative_customer":"tfabbe30458","recordCustomer":"[]","cumulative_food_food_50":"tb5a0c26237","cumulative_customer_customer_40":"tc72ea17624","cumulative_food_food_49":"t8606d87327","cumulative_customer_customer_21":"tebc9e7787","recordItemBag":"{\\"coin\\":{},\\"checkSign\\":\\"bf5f3\\"}","money":"te330014913503","cumulative_money":"t33c9285345903","daily_cumulative_money":"t6cdc998314219","first_watch_ad":"td65a41750"}'
    recordjson=json.loads(record)
    #这里来修改游戏数据，格式如下
    recordjson['money']=encode("money","90000000")
    #键值不要写错哦
    record=json.dumps(recordjson)
    #这里的openid在record中寻找未加密的数据
    openid="oe6z64rTGm0k2f8WjqcF2gNjPxCM"
    checkSign=checkSign2(record,openid)
    '''
    提交的数据格式如下，其中openid是加密格式，code需要拦截获取（需要未使用过的），startSum（星星）money（钱），可以直接修改
    data={
        "openid": "YsUc5BPW5aAQMTlyMSoKMEttbdo/GzjC/x4QY40qjdISt/DybBzIZgNxQMtjuq6vXBGKlzlHNoYQLQULGGQIOg==",
        "starSum": 6000,
        "playTime": 601417,
        "record":record,
        "code": "0915A4000BMB3K1gXX000QZsmZ05A40e",
        "type": "wx",
        "checkSign2": checkSign,
        "money": 13506,
        "plate": 0
    }
    '''
    data={
        "openid": enopenid,
        "starSum": 6000,
        "playTime": 601417,
        "record":record,
        "code": code,
        "type": "wx",
        "checkSign2": checkSign,
        "money": 13506,
        "plate": 0
    }
    res=requests.post(url,json=data)
    print(res.text)

if __name__ == "__main__":
    enopenid="加密后的openid 在抓到的包中获取"
    code="未使用的code 拦截获取"
    record(enopenid,code)