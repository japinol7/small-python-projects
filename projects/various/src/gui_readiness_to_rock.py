import logging
from tkinter import messagebox

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s: %(message)s')
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def main():
    log.info("Starting app gui_readiness_to_rock")
    are_you_ready = messagebox.askyesno(
        title='Rock readiness',
        message='Are you ready to rock?',
        detail='Click Yes if you are awesome'
    )

    if are_you_ready:
        res = 'Ok. You are ready to rock.'
    else:
        res = "Don't worry. You will be ready to rock soon enough."

    log.info(f"Response: {res}")
    log.info("End app")


if __name__ == '__main__':
    main()
