#encoding = utf-8
import win32api
import win32con

class KeyBoardKeys(object):
    VK_CODE={
        'enter':0x0D,
        'ctrl':0x11,
        'v':0x56
    }

    @staticmethod
    def keyDown(keyname):
        win32api.keybd_event(KeyBoardKeys.VK_CODE[keyname],0,0,0)

    @staticmethod
    def keyUp(keyname):
        win32api.keybd_event(KeyBoardKeys.VK_CODE[keyname],0,win32con.KEYEVENTF_KEYUP,0)

    @staticmethod
    def oneKey(key):
        KeyBoardKeys.keyDown(key)
        KeyBoardKeys.keyUp(key)

    def twoKeys(key1,key2):
        KeyBoardKeys.keyDown(key1)
        KeyBoardKeys.keyDown(key2)
        KeyBoardKeys.keyUp(key2)
        KeyBoardKeys.keyUp(key1)
