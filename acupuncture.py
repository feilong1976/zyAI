from datetime import datetime
'''
根据疾病情况得出穴位按摩处方

'''


class Acupuncture(object):    
    
    shichen=['子','丑','寅','卯','辰','己','午','未','申','酉','戌','亥']
    jingmai=['足少阳胆经','足厥阴肝经','手太阴肺经','手阳明大肠经','足阳明胃经','足太阴脾经','手少阴心经','手太阳小肠经','足太阳膀胱经','足少阴肾经','心包经','三焦经']
    '''十二井穴用于退热神昏热闭'''
    jinxue=('足窍阴','大敦','少商','商阳','历兑','隐白','少冲','少泽','至阴','涌泉','中冲','关冲')
    '''荥穴用于发烧'''
    yinxue=()
    '''郄穴用于疼痛'''
    xixue=()
    '''经穴'''
    jingxue=()
    '''合穴'''
    hexue=()
    '''原穴'''
    yuanxue=()
    '''俞穴'''
    shuxue=()
    '''募穴'''
    muxue=()
    
    '''
        疼痛部位
    '''
    tenTongBuWei={
        
        
    }
    '''
    经脉主病
    '''
    jingmai_bing={}
    
    '''到百度百科词条的链接
        比如穴位经脉
    '''
    def getBaiduLink(self,data):
        
        return 'https://baike.baidu.com/item/'+data
    
    def getCurrentCtime(self):
        '''
            计算当前天干地支
        
        '''
        current = datetime.now()
        hour = current.hour
        
        if hour <1 or hour>=23 :
            return self.shichen[0]
        elif hour >=1 and hour <3:
            return self.shichen[1]
        elif hour>=3 and hour<5:
            return self.shichen[2]
        elif hour>=5 and hour<7 :
            return self.shichen[3]
        elif hour>=7 and hour<9 :
            return self.shichen[4] 
        elif hour>=9 and hour<11 :
            return self.shichen[5]
        elif hour >=11 and hour <13:
            return self.shichen[6]
        elif hour>=13 and hour<15:
            return self.shichen[7]
        elif hour>=15 and hour<17:
            return self.shichen[8]
        elif hour>=17 and hour<19:
            return self.shichen[9]
        elif hour>=19 and hour<21:
            return self.shichen[10]
        else :
            return self.shichen[11]
         
    '''
        得出当前循行经脉
    '''    
    def getCurrentJinmai(self,sc):
        if not sc or self.shichen.index(sc)==-1:
            sc =self.getCurrentCtime()
        return self.jingmai[self.shichen.index(sc)]        
       
    '''
        得出灵龟八法子午流注开穴
    '''
    def getCurrentPoint(self):
        pass
    
    
    def diseaseRoad(self):
        pass
    
if __name__ =='__main__':
    ac = Acupuncture()
    sc=ac.getCurrentCtime()
    print('现在时辰为：%s' % sc)
    
    print('现在循行经脉为：%s' % ac.getCurrentJinmai(sc))
