# CPT-U11
this U11 computer science CPT
group members:
      Yingchen Ma
       Simon Li(Zimo)
topic: Vision calculator

Vision calculator:
    Using camera to get user input( hard point: how to identification different word. If input is not standard writing. )

functions

User manual [说明书]
--------------------------------------------------------------------------
The compiled language for this program is python3
[这个程序的编译语言为python3(version 3.7.3)] 

library we use:
      PIL
      tesseract 
      open CV
      numpy
      math
      re
      
      (Before you run our code Please install these libraries correctly.Otherwise there is a risk of a program crash. For the safety of you and others, please install these libraries correctly.)
      [在您使用我们的程序之前，请您正确的安装这些库，否则有可能会出现程序崩溃的风险。为了您和他人的人身和财产安全，请您正确的安装这些库。]
      (Please download all the folders, the only way to start the program correctly)
      [请您下载全部的文件夹，只有这样才能正确的开始程序]
      (The first interface is the login interface. There are two QR codes on this interface. You need to pay us the license fee to purchase a genuine license. The use of pirated licenses is unethical and is not permitted by law.)
      [第一个界面为 登陆界面，在这个界面有两个二维码，您需要向我们支付许可证费用，去购买正版许可证。使用盗版许可证是不道德的，同时也不被法律允许。]
      (The second interface is the welcome interface, welcome to our program, hello world.)
      [第二个界面为欢迎界面，欢迎来到我们的程序，你好世界。]
      (The third interface is the camera selection. You need to enter your camera port number to call the camera correctly. This interface is for the user to experience freedom. (When the input value is not understandable, we will use the No. 0 camera by default))
      [第三个界面为相机选择，您需要输入您的相机端口号码来正确的调用相机，这个界面是为了让用户体验到自由。(当输入值不可理解时，我们将默认使用0号摄像头)]   
      （The fourth interface is the camera interface. The performance of each computer is different, so the running time will be different. You need to wait patiently for a while to wait for the camera interface to start. Please point the camera at the subject. The button 'Q' is the shutter. button. When you press the button 'Q', the frame will be recorded and sent for identification.）
      [第四个界面为拍照界面，每个电脑的性能不同所以运行时间也会不一样，您需要耐心等待一会去等待拍照界面启动，请您将摄像头对准被摄物体，按键‘q’是快门按键。当您按下按键‘Q’,这帧画面将被记录下来，并送去识别]
      
      (The fiveth interface is the result output button, you will see the result of the operation on this page. If the result is NONE, it means the recognition failed, the input picture does not contain, or contains illegal characters, you can exit the program by pressing the exit button. Thank you for using the VC vision calculator made by the SM team, I hope you can have a perfect experience. The next time we see it in the program. "江湖路远，有缘再见")
      [第五个界面为结果输出按键，您将会在这页看到运算结果，如果结果为NONE 这表明识别失败，输入图片中不包含，或含有非法字符，您可以通过按exit按钮来退出程序。感谢您使用SM团队制作的VC视觉计算器，希望您可以拥有一个完美的使用体验。我们下一次，程序里见。江湖路远，有缘再见。]
      
      When you use 1080P or 4K camra to take the user input,the Success rate is 98%, But when you useing 720P or 480p camra to take input. The Success rate is 20%. When the light is insufficient and the ambient light is very complicated, the recognition rate will decrease.
      
Files in the folder:
      Main program
      test image folder(Have 5 test image inside)
      A few of image that program need.
      After you run first time have two image will be make. Do not worry about it! it's nomal and also this is a way you can check where the error come from.
      DO NOT DELETE THEM!!!!!! YOU ONLY NEED TO RUN THE vc_from Team SM.PY
     
算法部分 functions：
def take_picture(camra_choose)
def count_main(letter)
def identification()
Def test()
Def main()

GUI 部分 functions：
def zeropg()
def firstpg()
def secondpg()
def campg(cram_choose)[这个为GUI和算法的端口]
def fourthpg(answer)[这个为算法到GUI的输出端口]


Acknowledgement： Google (For Google OCR) 
                  intel(Open CV)
                  Github
                  CSDN
                  China Jiangsu Tianyi High school Artificial Intelligence Club
