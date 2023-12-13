from tkinter import messagebox


def main():
    are_you_ready = messagebox.askyesno(
        title='Rock readiness',
        message='Are you ready to rock?',
        detail='Click Yes if you are awesome'
    )

    if are_you_ready:
        res = 'Ok. You are ready to rock.'
    else:
        res = "Don't worry. You will be ready to rock soon enough."

    print(res)


if __name__ == '__main__':
    main()
