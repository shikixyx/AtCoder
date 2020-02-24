import os
import shutil

s_select_type = '''Please Select Contest Type
1.ABC 2.ARC 3.CDF 4.etc'''
print(s_select_type)
TYPE = int(input())

if TYPE == 1 or TYPE == 2 or TYPE == 3:
    s_select_num = '''Please Input Contest Number'''
    print(s_select_num)
    NUM = input()

    s_select_prob_num = '''Please Input Problem Number'''
    print(s_select_prob_num)
    PROB_NUM = int(input())

    if TYPE == 1:
        PARENT_DIR = 'ABC'
    elif TYPE == 2:
        PARENT_DIR = 'ARC'
    elif TYPE == 3:
        PARENT_DIR = 'CDF'

    CHILD_DIR = PARENT_DIR + '/' + NUM
    os.mkdir(CHILD_DIR)

    for i in range(65, 65 + PROB_NUM):
        FILE_PATH = CHILD_DIR + '/' + NUM + '_' + chr(i) + '.py'
        shutil.copyfile('template.py', FILE_PATH)


exit(0)
