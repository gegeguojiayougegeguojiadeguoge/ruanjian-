print('hello world')
print(31802314)

ph=open('D:/text.txt','a+')#使用文件输出，使用file=变量  2.a+：如果不存在就创建，存在直接输出
print('hello word',file=ph)
ph.close()

print('hello\nword') #换行\n;\t水平制表符；\r覆盖字符\b回退一个字符
#如果想要在输出一个引号只需要打上转义字符\；双引号也一样
#如果不信望其中的转移字符不起作用只需要在前面打上一个R或者r；注意最后一个字符不能是反斜杠,也被称为原始字符串
print('老师说：\'大家好\'')

#可以使用ord函数输出一个字符的十进制标号
print(ord('乘'))

#使用id加变量输出变量所在位置；使用type加变量输出变量的类型
name='辰宇'
print(id(name))
print(type(name))
print('\n')
#input 输入；字符串直接相加就可以拼接
#temp=input("我可以输入：")
#print('\n')
#rint(temp)