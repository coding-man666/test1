''' [demo01.py] file created at 2022/11/6 12:27 '''
import os

from excute_system_commands.demo01 import execute_system_command
import main

'''
如何使用 python 操作 git 程序 ?
1. 参考: https://mp.weixin.qq.com/s?src=11&timestamp=1667707002&ver=
4149&signature=98rGaFou-HJ28QizmK8XSFOEelEz0KfQR-PyVBX6Hi0wM2h4b2ZD
EvyTiS6jXQVd07P-BDVcXruFEe6xbPps1lMvzOBAvV0QzBqEmm0XqtWvr*mNv9N
a-dO*DFhGcjoH&new=1 (如何使用 Python 操作 Git 代码？GitPython 入门介绍)


'''

# 两个自定义异常类
class GitError(Exception):
    pass


class GitNoneInitError(GitError):
    pass


def git_push(local_repo_path: str, commit_message: str = 'a common commit'):
    '''
    功能: 调用系统接口,执行 git 命令,最终将本地文件 push 到远程仓库
    :param local_repo_path: 指定的 .git 的上一级目录
    :param commit_message: 指定此次 commit 的提交信息
    :return:
    '''
    print('[warning] Before using this program to commit a resource file to git, '
          'initialize the git local repository and successfully push the remote repository once.')
    # 如果指定的路径不是一个目录或者该目录下没有 .git 目录,则该路径无效,抛出相应的异常
    if not os.path.isdir(local_repo_path):
        raise FileNotFoundError('Directory not found, please initialize the directory first!')
    if not os.path.isdir(local_repo_path + '/.git'):
        raise GitNoneInitError('This directory is not managed by git. Perform git init first!')
    print('[info] 即将执行 git 命令 ~~')
    # 需要将传入的路径修改为绝对路径
    abs_path = ''
    # if not os.path.isabs(local_repo_path):
    abs_path = os.path.abspath(local_repo_path)
    print('abs path = ', abs_path)
    # 构造需要执行的 cmd 命令
    # 这里的 git 命令是固定的,如果相关的 git 配置不同,程序将出错
    git_command = abs_path[:1] + ': & cd ' + abs_path + ' & git add . & git commit -m "' \
                  + commit_message + '" & git push origin master'
    # print('git command = ', git_command)
    # 执行构造好的 cmd 命令,若执行成功,则完成整个 git 的 push 操作
    result = os.system(git_command)
    if result == 0:
        print('[info] The submission was successful, located at ', abs_path,
              'All files in the directory are committed to the remote repository!')
    else:
        print('[error] The submission was not successful!')


@main.main_call(call_path=__file__)
def test():
    '''
    测试使用 GitPython 操作 git
    :return:
    '''
    git_push(r'.')


if __name__ == '__main__':
    test()
    # pass
