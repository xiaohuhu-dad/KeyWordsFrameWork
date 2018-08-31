#encoding = utf-8
from action.PageAction import *
from util.ParseeExcel import ParseExcel
from config.VarConfig import *
import traceback

excelObj=ParseExcel()
excelObj.loadWorkBook(dataFilePath)

def writeTestResult(sheetObj,rowNo,colsNo,testResult,errorInfo=None,picPath=None):
    colorDict={"pass":"green","faild":"red"}
    colsDict={
        "testCase":[testCase_runTime,testCase_testResult],
        "caseStep":[testStep_runTime,testStep_testResult]
    }
    try:
        excelObj.writeCellCurrentTime(sheetObj,rowNo=rowNo,colsNo=colsDict[colsNo][0])
        excelObj.writeCell(sheetObj,content=testResult,rowNo=rowNo,colsNo=colsDict[colsNo][1],style=colorDict[testResult])
        if errorInfo and picPath:
            excelObj.writeCell(sheetObj,content=errorInfo,rowNo=rowNo,colsNo=testStep_errorInfo)
            excelObj.writeCell(sheetObj, content=picPath, rowNo=rowNo, colsNo=testStep_errorPic)
        else:
            excelObj.writeCell(sheetObj,content="",rowNo=rowNo,colsNo=testStep_errorInfo)
            excelObj.writeCell(sheetObj, content="", rowNo=rowNo, colsNo=testStep_errorPic)
    except Exception as e:
        print("写excel出错,",traceback.print_exc())


def TestSendMailWithAttachment():
    # open_browser("chrome")
    # maximize_browser()
    # visit_url("http://mail.126.com")
    # sleep(5)
    #
    # assert_string_in_pagesource("126网易免费邮--你的专业电子邮局")
    #
    # waitFrameToBeAvailableAndSwitchToIt("id", "x-URS-iframe")
    #
    # input_string("xpath","//input[@name='email']","huyixiao2016")
    #
    # input_string("xpath","//input[@name='password']","huyixiao20160514")
    #
    # click("id","dologin")
    #
    # sleep(5)
    # assert_title("网易邮箱")
    #
    # waitVisibilityOfElementLocated("xpath","//span[.='写 信']")
    # click("xpath","//span[.='写 信']")
    #
    # input_string("xpath","//div[contains(@id,'_mail_emailinput')]/input","75750165@qq.com")
    #
    # input_string("xpath","//div[@aria-label='邮件主题输入框，请输入邮件主题']/input","新邮件")
    # click("xpath","//div[@title='点击添加附件' and @class='by0']")
    # sleep(3)
    #
    # paste_string("D:\\a.txt")
    # press_enter_key()
    # waitFrameToBeAvailableAndSwitchToIt("xpath","//iframe[@tabindex=1]")
    # input_string("xpath","/html/body","发给爸爸的一封信")
    # switch_to_default_content()
    #
    # click("xpath","//header//span[.='发送']")
    # time.sleep(3)
    # assert_string_in_pagesource("发送成功")
    # close_browser()

    try:
        caseSheet=excelObj.getSheetByName("测试用例")
        isExecuteColumn = excelObj.getColumn(caseSheet,testCase_isExecute)
        successfulCase=0
        requiredCase=0
        for idx,i in enumerate(isExecuteColumn[1:]):
            if i.value.lower()=="y":
                requiredCase+=1
                caseRow=excelObj.getRow(caseSheet,idx+2)
                caseStepSheetName=caseRow[testCase_testStepSheetName-1].value

                stepSheet = excelObj.getSheetByName(caseStepSheetName)
                stepNum= excelObj.getRowsNumber(stepSheet)
                successfulSteps=0
                print("开始执行用例'%s'" %caseRow[testCase_testCaseName-1].value)
                for step in range(2,stepNum+1):
                    stepRow = excelObj.getRow(stepSheet,step)
                    keyWord = stepRow[testStep_keyWords-1].value
                    locationType = stepRow[testStep_locationType-1].value
                    locatorExpression = stepRow[testStep_locatorExpression-1].value
                    operateValue = stepRow[testStep_operateValue-1].value

                    if isinstance(operateValue,int):
                        operateValue = str(operateValue)

                    expressionStr = ""
                    if keyWord and operateValue and locationType is None and locatorExpression is None:
                        expressionStr = keyWord.strip() + "('" + operateValue + "')"
                    elif keyWord and operateValue is None and locationType is None and locatorExpression is None:
                        expressionStr = keyWord.strip() + "()"
                    elif keyWord and locationType and operateValue and locatorExpression is None:
                        expressionStr = keyWord.strip() + "('" + locationType.strip() + "','" + operateValue+"')"
                    elif keyWord and locationType and locatorExpression and operateValue:
                        expressionStr = keyWord.strip() + "('" + locationType.strip() + "','" + \
                        locatorExpression.replace("'",'"').strip() +"','"+operateValue + "')"
                    elif keyWord and locationType and locatorExpression and operateValue is None:
                        expressionStr = keyWord.strip() + "('" + locationType.strip() + "','" + \
                        locatorExpression.replace("'",'"').strip() + "')"

                    try:
                        eval(expressionStr)
                        excelObj.writeCellCurrentTime(stepSheet,rowNo=step,colsNo=testStep_runTime)
                    except Exception as e:
                        capturePic = capture_screen()
                        errorInfo = traceback.format_exc()
                        writeTestResult(stepSheet,step,"caseStep","faild",errorInfo,capturePic)
                        print("步骤'%s'执行失败！" %stepRow[testStep_testStepDescribe-1].value)
                    else:
                        writeTestResult(stepSheet,step,"caseStep","pass")
                        successfulSteps += 1
                        print("步骤'%s'执行通过！" %stepRow[testStep_testStepDescribe-1].value)
                if successfulSteps == stepNum-1:
                    writeTestResult(caseSheet,idx+2,"testCase","pass")
                    successfulCase +=1
                else:
                    writeTestResult(caseSheet,idx+2,"testCase","faild")
        print("共%d条用例, %d条需要被执行，本次执行通过%d条，" %(len(isExecuteColumn)-1, requiredCase, successfulCase))
    except Exception as e:
        print(traceback.print_exc())

if __name__=='__main__':
    TestSendMailWithAttachment()