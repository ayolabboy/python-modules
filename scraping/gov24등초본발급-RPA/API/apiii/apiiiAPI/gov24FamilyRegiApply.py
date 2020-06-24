from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from .commons.BrowserConfig import chromeConfig
from .commons.defineUrl import gov24Url
from .commons.defineTag import gov24Tag
from .commons.commonFunction import *

from .commons.dao import logInsert

## index
def index(request) :
    
    ## 데이터 저장
    PostData = sampleData() ## 추후 getData()와 연동

    ## 전달값 저장
    LoginData = PostData['LoginData']
    Option1 =  PostData['Option1']   
    Option2 =  PostData['Option2']   
    Option3 =  PostData['Option3']   

    for i in range (3) : ## 애러 발생 대비 3회 실행
        result = govFamilyRegiApply(LoginData,Option1,Option2,Option3)

        ## 프로세스 정상 실행 시 결과 전송 및 종료 
        if result == "ok" : 
            return JsonResponse({'result':result})  

    ## 실패 결과 전송
    result = 'err'
    return JsonResponse({'result':result})  

## 등초본 신청 프로세스
def govFamilyRegiApply(LoginData,Option1,Option2,Option3) : 

    try :             
        ## Browser Excute
        driver = chromeConfig()

        ## 로그인, 인증 
        driver.get(gov24Url['loginUrl']) 
        fixedDelay(1)

        driver.find_element_by_xpath(gov24Tag['loginButton']).click() 
        fixedDelay(1)

        driver.find_element_by_id(gov24Tag['pwInput']).send_keys(LoginData['gonginPw']) 
        driver.find_element_by_xpath(gov24Tag['OkButton']).click() 
        fixedDelay(1)
        
        ## 민원 신청 페이지 이동
        driver.get(gov24Url['FamilyCopiUrl']) 
        fixedDelay(1)

        ## 동의 클릭
        driver.find_element_by_xpath(gov24Tag['applyFCStep1']).click() 
        fixedDelay(7)

        ## 등본신청 
        result = 'err'
        if Option1['IsAbstract'] == False : 
            ## 주소 xpath 저장
            stateCode = Option1['state']
            cityCode = Option1['city']
            stateXPath = AddressSetting(stateCode,cityCode)[0]        
            cityXPath = AddressSetting(stateCode,cityCode)[1]
            driver.find_element_by_xpath(stateXPath).click()
            driver.find_element_by_xpath(cityXPath).click() 

            ## 기본신청 
            if Option1['IsOption'] == False :     
                pass

            ## 선택 발급 
            else : 
                driver.find_element_by_xpath(gov24Tag['agree02']).click()     
                if Option2['IsSelect1'] == True :                 
                    driver.find_element_by_xpath(gov24Tag['IsSelect1']).click() 
                    if Option3['SelectOpt1_2'] == True :
                        driver.find_element_by_xpath(gov24Tag['SelectOpt1_2']).click()             
                
                if Option2['IsSelect2'] == True : 
                    driver.find_element_by_xpath(gov24Tag['IsSelect2']).click()   
                    if Option3['SelectOpt2_1'] == False :                    
                        driver.find_element_by_xpath(gov24Tag['SelectOpt2_1']).click()
                    if Option3['SelectOpt2_2'] == False :                    
                        driver.find_element_by_xpath(gov24Tag['SelectOpt2_2']).click()
                    if Option3['SelectOpt2_3'] == False :                    
                        driver.find_element_by_xpath(gov24Tag['SelectOpt2_3']).click()

                if Option2['IsSelect3'] == True : 
                    driver.find_element_by_xpath(gov24Tag['IsSelect3']).click() 
                    if Option3['SelectOpt3_1'] == False :                    
                        driver.find_element_by_xpath(gov24Tag['SelectOpt3_1']).click()
                    if Option3['SelectOpt3_2'] == False :                    
                        driver.find_element_by_xpath(gov24Tag['SelectOpt3_2']).click()
                    if Option3['SelectOpt3_3'] == False :                    
                        driver.find_element_by_xpath(gov24Tag['SelectOpt3_3']).click()
                    if Option3['SelectOpt3_4'] == False :                    
                        driver.find_element_by_xpath(gov24Tag['SelectOpt3_4']).click()
                    if Option3['SelectOpt3_5'] == False :                    
                        driver.find_element_by_xpath(gov24Tag['SelectOpt3_5']).click()

                if Option2['IsSelect4'] == True : 
                    driver.find_element_by_xpath(gov24Tag['IsSelect4']).click() 
                    if Option3['SelectOpt4_1'] == False :                    
                        driver.find_element_by_xpath(gov24Tag['SelectOpt4_1']).click()
                    if Option3['SelectOpt4_2'] == False :                    
                        driver.find_element_by_xpath(gov24Tag['SelectOpt4_2']).click()

            ## 민원 신청          
            driver.find_element_by_xpath(gov24Tag['applyFCStep2']).click() 

            ## 로그 저장 및 결과 전달
            #logInsert('sucess')
            result = 'ok'
                    
        ## 초본신청, 추후 개발
        else :
           pass

    except : 
        result = 'err'
        driver.quit()

    return result

## 주소 Xpath 반환 
def AddressSetting(stateCode,cityCode):

    stateXPath = ''
    cityXPath = ''    
    if stateCode == 2 :
        stateXPath = gov24Tag['address2']
    elif stateCode == 3 :
        stateXPath = gov24Tag['address3']
    elif stateCode == 4 :
        stateXPath = gov24Tag['address4']
    elif stateCode == 5 :
        stateXPath = gov24Tag['address5']
    elif stateCode == 6 :
        stateXPath = gov24Tag['address6']
    elif stateCode == 7 :
        stateXPath = gov24Tag['address7']
    elif stateCode == 8 :
        stateXPath = gov24Tag['address8']        
    elif stateCode == 9 :
        stateXPath = gov24Tag['address9']
    elif stateCode == 10 :
        stateXPath = gov24Tag['address10']
    elif stateCode == 11 :
        stateXPath = gov24Tag['address11']  
    elif stateCode == 12 :
        stateXPath = gov24Tag['address12']
    elif stateCode == 13 :
        stateXPath = gov24Tag['address13']
    elif stateCode == 14 :
        stateXPath = gov24Tag['address14']  
    elif stateCode == 15 :
        stateXPath = gov24Tag['address15']
    elif stateCode == 16 :
        stateXPath = gov24Tag['address16']
    elif stateCode == 17 :
        stateXPath = gov24Tag['address17']  
    else :
        stateXPath = False        

    if cityCode == 2 :
        cityXPath = gov24Tag['city2']
    elif cityCode == 3 :
        cityXPath = gov24Tag['city3']
    elif cityCode == 4 :
        cityXPath = gov24Tag['city4']
    elif cityCode == 5 :
        cityXPath = gov24Tag['city5']
    elif cityCode == 6 :
        cityXPath = gov24Tag['city6']
    elif cityCode == 7 :
        cityXPath = gov24Tag['city7']
    elif cityCode == 8 :
        cityXPath = gov24Tag['city8']        
    elif cityCode == 9 :
        cityXPath = gov24Tag['city9']
    elif cityCode == 10 :
        cityXPath = gov24Tag['city10']
    elif cityCode == 11 :
        cityXPath = gov24Tag['city11']  
    elif cityCode == 12 :
        cityXPath = gov24Tag['city12']
    elif cityCode == 13 :
        cityXPath = gov24Tag['city13']
    elif cityCode == 14 :
        cityXPath = gov24Tag['city14']  
    elif cityCode == 15 :
        cityXPath = gov24Tag['city15']
    elif cityCode == 16 :
        cityXPath = gov24Tag['city16']
    elif cityCode == 17 :
        cityXPath = gov24Tag['city17']  
    elif cityCode == 18 :
        cityXPath = gov24Tag['city18']
    elif cityCode == 19 :
        cityXPath = gov24Tag['city19']
    elif cityCode == 20 :
        cityXPath = gov24Tag['city20']  
    else :
        cityXPath = False      

    result = [stateXPath,cityXPath]
    return result














## 샘플 데이터
def sampleData() :

    ############################# sample data #############################################
    Option1 = {                             # 공통 
        'IsAbstract' : False,               # True >> 초본, False 등본         
        'lan' : 'kor',                      # kor,eng  
        'IsOption' : True,                  # True >>, 선택사항 입력,  False >> 기본신청,   
        'IsSelected' : True,                # 선택발급                
        'state' : 9,                        # '도' 코드넘버
        'city' : 13,                        # '시' 코드넘버
    }    
    Option2 = {
        "agree02"   : True,                      ## 선택발급
        "IsSelect1" : True,                      ## 선택정보 1 
        "IsSelect2" : True,                      ## 선택정보 2
        "IsSelect3" : True,                      ## 선택정보 3
        "IsSelect4" : True,                      ## 선택정보 
    }
    Option3 = {
        "SelectOpt1_1" : False,                 ## 과거주소 최근5년 
        "SelectOpt1_2" : True,                  ## 과거주소 전체포함   
        "SelectOpt1_3" : False,                 ## 과거주소 세대주 (초본 only)
        "SelectOpt1_4" : False,                 ## 과거주소 발생/ 신고일 (초본 only)
        "SelectOpt1_5" : False,                 ## 과거주소 변동사유 (초본 only)

        "SelectOpt2_1" : True,                 ## 세대구성 사유 
        "SelectOpt2_2" : True,                 ## 세대구성 일자
        "SelectOpt2_3" : True,                 ## 변동사유    

        "SelectOpt3_1" : True,                 ## 세대주와의 관계 (등) // 주민등록번호 뒷자리 (초)
        "SelectOpt3_2" : True,                 ## 동거인 (등) // 국내 거소신고번호/ 외국인등록번호 (초)
        "SelectOpt3_3" : True,                 ## 변동사유
        "SelectOpt3_4" : True,                 ## 발생일/ 신고일
        "SelectOpt3_5" : True,                 ## 교부대상자 외 세대주·세대원·외국인 등의 이름

        "SelectOpt4_1" : True,                 ## 주민등록번호 뒷자리 본인 (등) // 입영, 전역일자 (초)
        "SelectOpt4_2" : True,                 ## 주민등록번호 뒷자리 세대원 (등) // 전체 (초)
    }

    LoginData = {                              ## 로그인 데이터
        'id': 'sdi654321',
        'pw': 'ehddlr0901$',
        'gonginPw' : 'ehddlr0901$' ,
    }
    PostData = {                          
        'LoginData' : LoginData,
        'Option1' : Option1,
        'Option2' : Option2,
        'Option3' : Option3,
        'Option4' : '',
    }
    return PostData