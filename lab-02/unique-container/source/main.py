from app import App

def main():
    app = App()
    
    try:
        app.start_app()

    except KeyboardInterrupt:
        print('See you later!')
        exit(0)

if __name__ == '__main__':
    main()