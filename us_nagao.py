#coding:utf-8
from jpype import *  
import os.path  
jarpath = os.path.join(os.path.abspath('.'), 'D:/GitHub/NagaoAlgorithm/JavaSource/')  
startJVM("D:/Program Files/Java/jdk1.8.0_91/jre/bin/client/jvm.dll","-ea", "-Djava.class.path=%s" % (jarpath + 'nagao.jar'))  
#ubuntu 中startJVM("/home/geek/Android/jdk1.6.0_43/jre/lib/i386/server/libjvm.so","-ea", "-Djava.class.path=%s" % (jarpath + 'XXX.jar'))  
JDClass = JClass("com.algo.word.Main")  
jd = Main()  
#jd = JPackage("jpype").JpypeDemo() #两种创建jd的方法  
jprint = java.lang.System.out.println  
jprint(jd.sayHello("waw"))  

shutdownJVM()  