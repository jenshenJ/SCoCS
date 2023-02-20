from container import UniqueContainer

container = UniqueContainer()

login = input("Enter username: ")
container.login(login)
container.remove("Элемент1")
container.save()
