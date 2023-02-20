from container import UniqueContainer

container = UniqueContainer()

login = input("Enter username: ")
container.login(login)
container.switch('user3')