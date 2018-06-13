#encoding = utf-8
import win32clipboard as w
import win32con,time

class Clipboard(object):
    @staticmethod
    def getText():
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
        return d

    @staticmethod
    def setText(aString):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
        w.CloseClipboard()

if __name__ == "__main__":
    content = "xiaohuhu"
    Clipboard.setText(content)
    time.sleep(3)  #一定一定要加暂停，要不然会提示pywintypes.error: (1418, 'GetClipboardData',线程没有打开的剪贴板)
    a = Clipboard.getText()
    print(a)