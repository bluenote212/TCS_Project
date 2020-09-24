from urllib import request

#Codesonar sql "select id,created,name_xml,project_id,warning_count from cs_analysis where created > '2020-09-16' AND created < '2020-09-17'"
url = 'http://192.168.1.162:7340/sql.csv?sql=select%20id%2Ccreated%2Cname_xml%2Cproject_id%2Cwarning_count%20from%20cs_analysis%20where%20created%20%3E%20%272020-09-16%27%20AND%20created%20%3C%20%272020-09-17%27'
request.urlretrieve(url,'C:/Users/B180093/Downloads/project.csv')
