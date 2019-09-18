;ControlFocus("title","text",controlId) Edit1=Edit instance 1
ControlFocus("打开","","Edit1")

; Wait 10 seconds for the Upload windown to appear
WinWait("[CLASS:#32770]","",10)

; Set the File name text on the edit field
ControlSetText("打开","","Edit1","C:\Users\fir\Desktop\上传文件\自动化验证文档\插入的图片.png")
Sleep(2000)

; click on the open button
ControlClick("打开","","Button1")