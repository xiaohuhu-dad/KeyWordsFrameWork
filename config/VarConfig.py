#encoding = utf-8
import os

chromeDriverFilePath = "D:\Python36\chromedriver"
firefoxDriverFilePath = "D:\Python36\geckodriver"

parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
screenPicturesDir = parentDirPath + "\\exceptionpictures\\"
dataFilePath = parentDirPath + "\\testData\\126邮箱联系人.xlsx"

testCase_testCaseName=2
testCase_testStepSheetName=4
testCase_isExecute=5
testCase_runTime=6
testCase_testResult=7

testStep_testStepDescribe=2
testStep_keyWords=3
testStep_locationType=4
testStep_locatorExpression=5
testStep_operateValue=6
testStep_runTime=7
testStep_testResult=8
testStep_errorInfo=9
testStep_errorPic=10
