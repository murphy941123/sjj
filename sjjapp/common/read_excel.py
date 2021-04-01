import os
import xlrd
class ReadExcel():
    def __init__(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))  #获取基准路径，就是当前路径的父路径
        print(base_path)
        self.DataList = [] # 准备一个空列表，用于当前目录下的所有Excel表，这里包含全部路径
        self.ExcelList = []  #准备一个空列表，用来收集所有Excel的文件名，这里仅包含文件名字
        for file_path,dir_name,file_name in os.walk(base_path):
            # 使用os内置方法将路径拆分为文件路径、文件夹名字、文件名字
            for file in file_name:  # 做文件名字的循环
                if file[-5:] in '.xlsx':  # 如果文件的后五位是.xlsx的
                    self.ExcelList.append(file)  #将符合if条件的文件名装进列表内
                    xlsxfile = os.path.join(base_path,file)  # 做完整路径拼接
                    self.DataList.append(xlsxfile) # 将完整路径拼接好的excel文件放入列表内
    def GetExcel(self,file_name):  # 传入你具体要做操作的excel表
        for j in self.ExcelList: # 循环 所有excel文件名
            if j == file_name:  #   如果某一个文件名与我传入的文件名对应
                for i in self.DataList: # 继续做循环完整文件路径
                    if j in i:   # 如果我传入的文件名字在某一个完整文件路径中
                        self.Excelfile = i  # 那就就把他在类里声明一个变量
    def ReadExcelSetType(self):  # 做数据处理，将其整理成{}字典状态，有键和值
        import xlrd  # 导入模块
        work = xlrd.open_workbook(self.Excelfile)  # 打开一个xlsx
        Datalist = []  # 准备一个空列表，用于接收全部的表数据
        sheets = work.sheet_names() # 获取表的所有扉页
        for sheet in sheets:  # 循环每一个扉页
            sheet = work.sheet_by_name(sheet)
            hang = sheet.nrows # 拿到每一个sheet页的行数
            for i in range(0,hang): #  用行数来做循环
                values = sheet.row_values(i)  # 拿到每一行的数据
                Datalist.append(values) # 将每一行的数据装进列表

        title_ = Datalist[0]  # 拿到列表中的标题，也就是excel的第一行
        content_ = Datalist[1:] # 拿到除了第一行以外的全部数据
        new = [] # 准备一个空列表，用于返回数据
        for c in content_: # 循环全部数据除了第一行
            dic = {}  # 准备一个空字典
            for i in range(len(c)): # 已全部内容的行数为循环次数做循环
                try:
                    dic[title_[i]] = int(c[i])  # 尝试将数据转化为int，因为excel默认的纯数字为浮点型
                except:
                    dic[title_[i]] = c[i]  # 如果不是int   就把他正常传入字典中
            new.append(dic)  # 将有键和值的字典传入新列表
        return new  # 返回列表
# ReadExcel()