# taigiGameDB

1. 請確定python2.x已經有裝Django套件，假如不確定，執行 pip install Django -U 或 sudo pip install Django -U
2. 要啟動server，只要在專案根目錄下執行 python manage.py runserver 即可
3. 到 http://127.0.0.1:8000/hello/ 看一下有沒有成功啟動
4. 想要到管理界面，就到 http://127.0.0.1:8000/admin/ 然後帳密皆為noel
5. 進到界面之後，可以點選不同的app (queryChineseWords, queryPronounces)的資料庫，然後可以進行更改
6. [2015.05.05 新功能]
  1. http://127.0.0.1:8000/q/chinese_word/水母/ 將會回傳 水母(存在的話)，與 水母 的發音
  2. http://127.0.0.1:8000/q/chinese_word/水/ 會回傳符合 水 的字與它的發音，但不包含 水母
  3. http://127.0.0.1:8000/q/chinese_word/大中天/ 會因為無結果，會回傳 No results
  3. http://127.0.0.1:8000/q/close_pronounce/liāng/ 會回傳接近 liāng 的發音(會排序)，與對應的中文字們
  4. http://127.0.0.1:8000/q/close_pronounce/l/ 會因為query太短，會回傳 Query is too short
  5. http://127.0.0.1:8000/q/close_pronounce/xxx/ 會因為無結果，會回傳 No results
7. [2015.06.09 新功能]
  1. 現在，只要瀏覽 http://127.0.0.1:8000/game/index.html 就可以開始玩遊戲啦! 用本機的速度! Badaboom!
