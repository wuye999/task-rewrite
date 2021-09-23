#编写一个程序，能在指定目录以及指定目录的所有子目录下查找文件名包含指定字符串的文件，并打印出路径。
import os

search_str = 'Fruit'
search_path = '/ql/log'

class Search_files(object):
    def __init__(self, search_str, search_path):
        self.search_str = search_str
        self.search_path = search_path
        self.s_results=[]

    def all_files(self,Search_path):
        dirs=[Search_path+'/'+x for x in os.listdir(Search_path) if os.path.isdir(Search_path+'/'+x)]
        files=[x for x in os.listdir(Search_path) if os.path.isfile(Search_path+'/'+x)]
        print('正在搜索目录： '+Search_path)
        return Search_path, dirs, files

    def judge_file(self,Search_path, files):
        for file_name in files:
            if self.search_str in file_name:
                self.s_results.append(Search_path+'/'+file_name)

    def run_search(self,Search_path):
        Search_path, dirs, files=self.all_files(Search_path)
        self.judge_file(Search_path, files)
        if dirs==[]:
            return
        return list(map(self.run_search, dirs))

if __name__ == '__main__':
    s = Search_files(search_str, search_path)
    s.run_search(s.search_path)
    print(f'\n\n带 {search_str} 的文件有\n')
    for tt in s.s_results:
        print(tt)
