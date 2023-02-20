from container import UniqueContainer

container = UniqueContainer()

login = input("Enter username: ")
container.login(login)
container.find(['123', '458', '789'])
container.load('user2')
container.add(['elem'])
container.load('user3')
container.save()
