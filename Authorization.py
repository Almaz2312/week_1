login = input("Login: ")
password = input("Password: ")
repeat_login = input("Repeat login: ")
repeat_password = input("Repeat password: ")
if login == repeat_login and password == repeat_password:
    print("Вы успешно вошли в систему")
else:
    print("Неправильный логин или пароль")