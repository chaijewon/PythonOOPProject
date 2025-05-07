# 데이터베이스 CRUD => sqlite
"""
   프로그램 : 데이터를 모아서 관리
            => 변수
   파이썬 클래스 구성 요소
      class class명:
        -----------
          멤버변수 영역
            name : public
            _name : protected
            __name : private
        -----------
          생성자
          def __init__(self):
          소멸자
          def __del__(self):
          ** self => this
        -----------
          함수정의
          => 매개변수에는 self를 포함하고 있다
        -----------

        상속 : 수정후에 재사용
        포함 : 변경없이 있는 그대로 사용
"""
import sqlite3
from _overlapped import NULL
class StudentVO:
    hakbun=0
    name=''
    kor=0
    eng=0
    math=0
    """
    def setHakbun(self,hakbun):
        self.hakbun=hakbun
    def getHakbun(self):
        return self.hakbun
    """
class StudentDAO:
    conn=NULL
    cursor=NULL

