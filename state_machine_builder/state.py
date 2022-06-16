class State:
    RUN_TASK_TYPE = 0
    BEFORE_RUN_TASK_TYPE = 1

    def __init__(self, identification: str, value=None):
        self.id = identification
        self.value = value
        self.task = None
        self.before_task = None
        self.is_first_time = True

    def run(self):

        if self.is_first_time:
            self.before_task = False
            if callable(self.before_task):
                self.before_task()

        if callable(self.task):
            print("Running state task")
            self.task()
        else:
            print("Callback isn't assigned")

    def setTask(self, callback):
        if callable(callback):
            self.task = callback
        else:
            raise Exception("Not callable parameter")

    def setBeforeTask(self, callback):
        if callable(callback):
            print('running before task')
            self.before_task = callback
        else:
            raise Exception("Not callable parameter")

    def reset_flags(self):
        self.is_first_time = True
