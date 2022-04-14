class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', "a+") as file:
            file.write(msg)
            file.write('\n')

    def log_info(self, msg):
        self.write('INFO: {}'.format(msg))

    def log_error(self, msg):
        self.write('ERRO: {}'.format(msg))
