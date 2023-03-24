from src.com.python.Authentication.entity.User import User
from src.com.python.Authentication.repository.UserRepository import UserRepository

class SignUp:

    @staticmethod
    def signUp():

        while True:
            select = input("회원가입에 동의 하십니까? 계속하려면 (Y/y)입력, 취소하려면 아무키나 입력")
            if select == 'Y' or select == 'y':
                break
            else:
                return

        username = None
        password = None
        name = None
        email = None

        ############ Validation(유효성) 검사
        while True:
            username = input("username >>> ")
            if len(username) > 2:
                if UserRepository.findUserByUsername(username) == None:
                    break
                else:
                    print("이미 가입된 사용자이름입니다.")
            else:
                print("사용자이름은 3글자 이상이어야 합니다.")

        ############ 비밀번호 8자 이상입력시에 넘어갈 수 있게 설정
        while True:
            password = input("password >>> ")
            if len(password) > 7:
                break
            else:
                print("비밀번호는 8자 이상이어야 합니다.")

        while True:
            checkPassword = input("check password >>> ")
            if password == checkPassword:
                break
            else:
                print("비밀번호가 일치하지 않습니다.")

        name = input("name >>> ")
        email = input("email >>> ")

        newUser = User(username, password, name, email)
        UserRepository.saveUser(newUser)
        print("회원가입이 완료되었습니다. 환영합니다.")







