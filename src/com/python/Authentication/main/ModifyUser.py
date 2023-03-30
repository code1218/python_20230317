from src.com.python.Authentication.security.PrincipalUser import PrincipalUser
from src.com.python.Authentication.repository.UserRepository import UserRepository
from src.com.python.Authentication.entity.User import User
from src.com.python.Authentication.entity.UserDetail import UserDetail

class ModifyUser:

    @staticmethod
    def modifyUser():
        select = input("회원정보 수정에 동의 하십니까? 계속하려면 (Y/y)입력, 취소하려면 아무키나 입력")
        if select != 'Y' and select != 'y':
            return

        checkPassword = input("기존 password를 입력하세요 >>> ")
        if PrincipalUser.session.get("password") != checkPassword:
            print("비밀번호를 다시 확인해 주세요.")
            return

        while True:
            print("=====<< ModifyUser >>=====")
            print("1. 기본정보 수정")
            print("2. 비밀번호 수정")
            print("3. 상세정보 수정")
            print("b. 뒤로가기")
            print("====================")
            select = input("Menu Selected!! >>> ")
            if select == "b":
                break;
            elif select == "1":
                ModifyUser.updateBasicInformation()
            elif select == "2":
                ModifyUser.updatePassword()
            elif select == "3":
                ModifyUser.updateDetailInformation()
            else:
                print("다시 입력하세요.")
            print("===========================")
            print()

    @staticmethod
    def updateBasicInformation():
        print("수정하지 않으려면 빈값으로 enter를 눌러주세요.")
        name = input("name >>> ")
        email = input("email >>> ")

        if len(name.replace(' ', '') + email.replace(' ', '')) == 0:
            print("수정사항이 없습니다.")
            return

        userDict = PrincipalUser.session;
        user = User(
            userDict.get("username"),
            userDict.get("password"),
            name if len(name.replace(' ', '')) > 0 else userDict.get("name"),
            email if len(email.replace(' ', '')) > 0 else userDict.get("email")
        )

        UserRepository.updateUser(user)
        PrincipalUser.setSession(UserRepository.findUserByUsername(user.username))
        print("회원 정보가 수정되었습니다.")

    @staticmethod
    def updatePassword():
        select = input("비밀번호 변경에 동의 하십니까? 계속하려면 (Y/y)입력, 취소하려면 아무키나 입력")
        if select != 'Y' and select != 'y':
            return

        newPassword = None
        while True:
            newPassword = input("newPassword >>> ")
            if len(newPassword) < 8:
                print("비밀번호는 8자 이상이어야합니다.")
                continue
            if PrincipalUser.session.get("password") == newPassword:
                print("기존 비밀번호와 동일한 비밀번호는 사용할 수 없습니다.")
                continue
            checkPassword = input("checkPassword >>> ")
            if checkPassword != newPassword:
                print("비밀번호가 일치하지 않습니다. 비밀번호를 다시 입력해주세요.")
                continue

            userDict = PrincipalUser.session
            user = User(
                userDict.get("username"),
                newPassword,
                userDict.get("name"),
                userDict.get("email")
            )
            UserRepository.updateUser(user)
            PrincipalUser.setSession(UserRepository.findUserByUsername(user.username))
            print("비밀번호 변경 완료되었습니다.")
            return
        '''
        newPassword 새로운 비밀번호 입력
        비밀번호가 8자 이상인지 확인
        기존의 비밀번호와 다른지 확인
        두 조건이 성립되지 않으면 다시 newPassword를 입력받도록 한다.
        
        checkPassword 새로운 비밀번호 확인 입력
        newPassword와 일치하는 확인
        일치하지 않으면 다시 newPassword를 입력하도록 한다.
        
        모든 조건이 성립되면 updateUser를 호출하여 새로운 비밀번호를 commit한다.
        update된 정보를 다시 principal에 저장한다.
        비밀번호 변경 완료되었습니다. 메세지 출력
        '''

    @staticmethod
    def updateDetailInformation():
        print("수정하지 않으려면 빈값으로 enter를 눌러주세요.")
        phone = input("phone >>> ")
        address = input("address >>> ")
        gender = input("gender >>> ")

        if len(phone.replace(' ', '') + address.replace(' ', '') + gender.replace(' ', '')) == 0:
            print("수정사항이 없습니다.")
            return

        userDict = PrincipalUser.session;
        userDetail = UserDetail(
            userDict.get("user_id"),
            phone if len(phone.replace(' ', '')) > 0 else userDict.get("phone"),
            address if len(address.replace(' ', '')) > 0 else userDict.get("address"),
            gender if len(gender.replace(' ', '')) > 0 else userDict.get("gender")
        )

        UserRepository.updateUserDetail(userDetail)
        PrincipalUser.setSession(UserRepository.findUserByUsername(userDict.get("username")))
        print("회원 정보가 수정되었습니다.")




