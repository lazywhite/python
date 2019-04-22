import subprocess

# 不需要输出
subprocess.call(["ls", "-al"], shell=False)
subprocess.call("ls -al", shell=True)
# 需要返回输出
output = subprocess.check_output("ls -al", shell=True)
