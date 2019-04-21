# 成人網站爬蟲

[demo.jpg](https://github.com/sunrimii/porn-crawler/blob/master/demo.jpg?raw=true)

經深入爬取各大成人網站的首頁

整合所有原始影片檔與標題以新的網站呈現

因此無廣告且可供下載(除部份使用串流影片的網站)

並有搜尋功能 一次搜尋各大網站

# 使用知識

- 網頁爬蟲
- 多行程
- 後端

# 執行步驟

安裝相關套件`pip install -r requirements.txt`

若首次執行須先配置資料庫欄位`python manage.py migrate`

保持執行爬蟲主程式`python crawler.py`

再以另一終端機

保持執行網頁伺服器`python manage.py runserver`

最後可於[網頁](http://127.0.0.1:8000)查看架設成果

# 補充說明

因應網頁不斷更新 爬蟲無法永久有效

於`crawler.py`可改善爬取規則
