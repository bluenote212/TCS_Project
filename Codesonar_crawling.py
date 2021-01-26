from urllib import request
import pandas as pd

url = 'http://192.168.1.162:7340/sql.csv?sql=select%20id%2Ccreated%2Cname_xml%2Cproject_id%2Cfinished%2Cwarning_count%20from%20cs_analysis%20order%20by%20id%20desc'
request.urlretrieve(url,'C:/Users/B180093/Downloads/Codesonar_result.csv')

result = pd.read_csv('C:/Users/B180093/Downloads/Codesonar_result.csv')


result1 = result.dropna(axis=0)
result1 = result.reset_index()
result2 = result.drop_duplicates(['project_id'], keep='first')

#result2.to_csv('C:/Users/B180093/Downloads/Codesonar_result_완료.csv') #중복 제거 후 원본과 비교해보기 위한 코드