from src.com.python.Authentication.security.PrincipalUser import PrincipalUser

class Home:

    @staticmethod
    def home():
        while True:
            print("=====<< Home >>=====")
            print(f"접속한 사용자이름: {PrincipalUser.session.get('username')}")
            print("====================")
            print("1. 마이페이지")
            print("2. 사용자정보 조회")
            print("3. 로그아웃")
            print("====================")
            select = input("Menu Selected!! >>> ")
            if select == "1":
                pass
            elif select == "2":
                pass
            elif select == "3":
                PrincipalUser.clearSession()
                break
            else:
                print("다시 입력하세요.")
            print("===========================")
            print()
