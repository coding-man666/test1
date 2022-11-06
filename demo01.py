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


class GitController(object):

    def __init__(self, local_repo_path: str):
        pass

    def pull(self):
        print()


class GitError(Exception):
    pass


class GitNoneInitError(GitError):
    pass


def test01(local_repo_path: str, commit_message: str = 'a common commit'):
    print('[warning] Before using this program to commit a resource file to git, '
          'initialize the git local repository and successfully push the remote repository once.')
    if not os.path.isdir(local_repo_path):
        raise FileNotFoundError('Directory not found, please initialize the directory first!')
    if not os.path.isdir(local_repo_path + '/.git'):
        raise GitNoneInitError('This directory is not managed by git. Perform git init first!')
    print('[info] 即将执行 git 命令 ~~')
    abs_path = ''
    if not os.path.isabs(local_repo_path):
        abs_path = os.path.abspath(local_repo_path)
        print('abs path = ', abs_path)
    git_command = abs_path[:1] + ': & cd ' + abs_path + ' & git add . & git commit -m "' \
                  + commit_message + '" & git push origin master'
    print('git command = ', git_command)
    execute_system_command(git_command)
    print('[info] The submission was successful, located at ', abs_path,
          'All files in the directory are committed to the remote repository!')


def test02():
    # execute_system_command('f:')
    # execute_system_command('dir')
    path = 'E:\qq浏览器\图片'

    os.system('e: & cd E:\qq浏览器\图片 & dir')


@main.main_call(call_path=__file__)
def test():
    '''
    测试使用 GitPython 操作 git
    :return:
    '''
    test01('./')


if __name__ == '__main__':
    test()
    # pass
