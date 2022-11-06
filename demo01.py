''' [demo01.py] file created at 2022/11/6 12:27 '''
import os

from git import GitCommandError

import main
import git

'''
如何使用 python 操作 git 程序 ?
1. 参考: https://mp.weixin.qq.com/s?src=11&timestamp=1667707002&ver=
4149&signature=98rGaFou-HJ28QizmK8XSFOEelEz0KfQR-PyVBX6Hi0wM2h4b2ZD
EvyTiS6jXQVd07P-BDVcXruFEe6xbPps1lMvzOBAvV0QzBqEmm0XqtWvr*mNv9N
a-dO*DFhGcjoH&new=1 (如何使用 Python 操作 Git 代码？GitPython 入门介绍)


'''


class GitController(object):

    def __init__(self, local_repo_path: str):
        # 在本地创建 .git 仓库,如果已经存在则直接使用之前的仓库
        # 在指定的 path 路径执行 git init 命令
        # repo = git.Repo.init(path='.')
        # 配合 with 语句使用的写法
        self.repo = git.Repo.init(path=local_repo_path)
        self.remote = None

    def get_repo(self):
        return self.repo

    def add_file(self, file_path_list: list):
        self.repo.index.add(items=file_path_list)

    def commit_file(self, commit_info: str = 'you commit a few file.'):
        print(self.repo.index.commit(commit_info))
        print('缓冲区文件提交成功!')

    def check_status(self, status):
        print('[info] now all files of have not add to buffer are : ', self.repo.untracked_files)

    def clone_remote_rpeo_to_local(self, local_repo_path, remote_repo_url: str = None):
        return git.Repo.clone_from(url=remote_repo_url, to_path=local_repo_path)

    def link_remote_repo(self, remote_repo_url, remote_name: str = 'common-link'):
        if self.remote is None:
            try:
                remote_temp = self.repo.create_remote(name=remote_name, url=remote_repo_url)
            except GitCommandError as err:
                print(err)
        self.remote = self.repo.remote(remote_name)
        # print('remote=',self.remote)

    def pull(self):
        print(self.remote.pull())

    def push(self):
        print(os.system('git push -u origin master'))
        # print(self.remote.push())

    def fetch(self):
        print(self.remote.fetch())

    def delete_remote(self, remote_name: str):
        print(self.repo.delete_remote(remote_name))



@main.main_call(call_path=__file__)
def test():
    '''
    测试使用 GitPython 操作 git
    :return:
    '''
    repo_url = 'git@github.com:coding-man666/learngit.git'
    # 创建 git 本地仓库对象,需要指定本地仓库路径
    repo = GitController('.')
    repo.check_status('')
    repo.add_file(repo.get_repo().untracked_files)
    # repo.commit_file()
    # repo.link_remote_repo(repo_url)
    # repo.push()
    #
    # local_repo = repo.get_repo()
    # # print(local_repo.head)

    # from excute_system_commands.demo01 import execute_system_command
    # execute_system_command('git init')


if __name__ == '__main__':
    test()
    # pass
