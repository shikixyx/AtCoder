import os
import shutil

# Contest Type
s_select_type = """Please Select Contest Type
1.ABC 2.ARC 3.Enterprise 4.CDF 5.yukicoder 6.etc"""
print(s_select_type)
TYPE = int(input())

# IF Enterprise Contest
if TYPE == 3:
    s_enterprise_name = """Please Input Enterprise Name"""
    print(s_enterprise_name)
    ENTERPRISE = input()

# Contest Number
s_select_num = """Please Input Contest Number"""
print(s_select_num)
NUM = input()

# Problem Number
s_select_prob_num = """Please Input Problem Number"""
print(s_select_prob_num)
PROB_NUM = int(input())

PARENT_DIR = "/Users/hiroaki/Documents/34_AtCoder/"

if TYPE == 1:
    PARENT_DIR += "ABC"
elif TYPE == 2:
    PARENT_DIR += "ARC"
elif TYPE == 3:
    PARENT_DIR += "Enterprise/" + ENTERPRISE
elif TYPE == 4:
    PARENT_DIR = "CDF"
elif TYPE == 5:
    PARENT_DIR = "yukicoder"

CHILD_DIR = PARENT_DIR + "/" + NUM

if not os.path.isdir(CHILD_DIR):
    os.makedirs(CHILD_DIR)

for i in range(65, 65 + PROB_NUM):
    FILE_PATH = CHILD_DIR + "/" + NUM + "_" + chr(i) + ".py"
    shutil.copyfile("template.py", FILE_PATH)


exit(0)
