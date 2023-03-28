from src.com.python.Authentication.main.SignUp import SignUp
from src.com.python.Authentication.main.SignIn import SignIn
from src.com.python.Authentication.main.Home import Home

class Main:

    @staticmethod
    def main():
        while True:
            print("=====<< Python Auth >>=====")
            print("1. 로그인")
            print("2. 회원가입")
            print("q. 프로그램 종료")
            print("===========================")
            select = input("Menu Selected!! >>> ")

            if select == 'q':
                break;
            elif select == '1':
                if SignIn.signIn():
                    Home.home()
                else:
                    print("사용자의 정보를 확인해주세요. 계정이 없다면 회원가입해주세요.")
            elif select == '2':
                SignUp.signUp()
            else:
                print("다시 입력하세요.")
            print("===========================")
            print()

if __name__ == "__main__":
    Main.main()
