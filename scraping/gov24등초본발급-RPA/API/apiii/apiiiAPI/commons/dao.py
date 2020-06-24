from django.db import connection

## select test, should be deleted
def selectTest() :
    antiHacks()
    cursor = connection.cursor()
    query_string = "SELECT * FROM testdb.testtb"
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts =[]
    
    for row in rows:
        dic = {'id':row[0], 'name':row[1]}
        posts.append(dic)
 
    return posts

## 추후 해킹 방어 로직 추가
def antiHacks() :    
    return 0

## 추후 개발
def logInsert(applyResult) :
    cursor = connection.cursor()
    query_string = "INSERT INTO gov24.resultlog ( `bizIdx`, `userIdx`, `serviceIdx`, `result`, `createDate`) VALUES ( '0', '0', '0', '" + applyResult + "', NOW() )"
    result = cursor.execute(query_string)
    return result