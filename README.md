# pipe_project
# Flask 網頁版
## Before
![](https://i.imgur.com/cHcK6Yh.png)
## After
![](https://i.imgur.com/fMNU3J5.png)

# tkinter 應用程式(exe)版
下載 資料夾 pipe_tkinter 後 進去
打上 

pyinstaller -F -w -i [icon 絕/對/路/徑]/pyi_icon.ico cal_pipe_gui.py

將原始檔案包裝成 應用程式 EXE 檔來使用

## 執行畫面
![](https://i.imgur.com/MMf1GZL.png)

##最新版本(網頁版)執行畫面
添加關聯式下拉表單
![](https://i.imgur.com/DAFdlWb.png)

## 將 Flask 版本 用 PYINSTALLER 包裝成 EXE 檔
指令:
pyinstaller -F -i pyi_icon.ico --add-data="templates;templates"  app.py

## 更新 pipe tkinter 程式
簡化介面，把資料內化到程式中

## Deploy on Heroku at 2022.8.16
https://afternoon-reef-38149.herokuapp.com/