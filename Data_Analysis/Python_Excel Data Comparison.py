#Demands：
    #判断一个Excel表中的两列是否一致，匹配率是多少
    #编程语言：Python

#Idea_one：
    #判断一个Excel表中的两列是否一致：
      import xlrd
      import xlwt
      import xlutils
      
      workbook = xlrd.open_workbook('test.xlsx')
      sheet = workboot.sheets()[0]
      list_a = sheet.col_values(1)
      list_b = sheet.col_values(2)
      n = int(sheet.nrows)
      
      for i in range(n):
        if list_a[i] == list_b[i]L
          print('ok')
        else:
          print('ng')
    #注释：只能判断是否一致，不能获得匹配率。pass
#Idea_two:    
    #判断两个变量是否一致
      #注释：因为其中的数据存在中文、英文、标点符号等。具体结果于上方类似，同样不能获得匹配率。pass
      
#Idea_three：
    #判断两个列中的元素是否一致
        a = list(str(123456))
        b = list(str(214365))
        cmp = [val for val in a if val in b]
        a_number = len(a)
        cmp_number = len(cmp)
        print('%.2f%%' %(cmp_number/a_number*100))
    #注释：虽然可以获取匹配率，也能对比文件内容是否一致，但该方法的对比方式不对（b[0]对比a[0:6],b[1]对比a[0:6],也就是b列表中的元素会先对比a列表的所有元素不是一一对应的进行对比的）pass
    
#Idea_four:
    #模拟论文查重的方法，初步判断可行，使用模块为difflib
    import difflib
    a = "道可道，非常道。"
    b = "名可名，非常名。"
    print(difflib.SequenceMatcher(None, a, b).quick_ratio())
    # 结果为0.625
    # 注释：虽然其结果不错，但在对比逗号，句号等标点符号时，误差较大。
    
# Idea_five:
    # 寻找到另一个对比库，Levenshtein
    from Levenshtein import *
    a = "道可道也，非常道也。"
    b = "名非名也、非名是也。"
    print(ratio(u"%s"%a, u"%s"%b))
    # 其结果为 0.4
    # 注释：结果满意，且对比标点符号时，也可得出结果，其结果暂未发现误差。
