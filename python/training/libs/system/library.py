import os
import typing
import pathlib


class System:
    @staticmethod
    def get_files(parent_dir: pathlib.Path, pattern: typing.List[str]) -> typing.Generator:
        '''
        사용자가 지정한 부모 디렉토리로부터 모든 하위 디렉토리를 검색하여
        특정 확장자를 가진 파일들을 반환하는 제네레이터
        :return: 파일 경로 <generator>
        '''
        for f in parent_dir.glob('**/*'):
            if not f.is_file():
                continue
            if '*' in pattern:
                yield f
            else:
                if f.suffix in pattern:
                    yield f

    @staticmethod
    def get_files_lst(parent_dir: pathlib.Path, pattern: typing.List[str]) -> typing.List[pathlib.Path]:
        '''
        사용자가 지정한 부모 디렉토리로부터 모든 하위 디렉토리를 검색하여
        특정 확장자를 가진 파일들을 반환하는 메서드
        :return: 파일 경로 <list>
        '''
        lst = list()
        for f in parent_dir.glob('**/*'):
            if not f.is_file():
                continue
            if '*' in pattern:
                lst.append(f)
            else:
                if f.suffix in pattern:
                    lst.append(f)
        return lst

    @staticmethod
    def get_files_recursion(dpath: str, pattern: typing.List[str], depth: int = 0) -> typing.Generator:
        '''
        :param dpath: 부모 디렉토리
        :param depth: 깊이 값
        :return: file path generator
        '''
        lst = list()
        file_lst = os.listdir(dpath)
        for f in file_lst:
            # fullpath => '/home/rapa/workspace/usd/sdr/api.h'
            # fullpath => '/home/rapa/workspace/usd/sdr/testenv'
            fullpath = os.path.join(dpath, f)
            if os.path.isdir(fullpath):
                lst += System.get_files_recursion(fullpath, pattern, depth+1)
            else:
                if os.path.isfile(fullpath):
                    if '*' in pattern:
                        lst.append(fullpath)
                    else:
                        ext = f'.{fullpath.split(".")[-1]}'
                        if ext in pattern:
                            lst.append(fullpath)
        yield from lst

