from datetime import timedelta, datetime

class Recorder():
    def __init__(self):
        self.start_time = None
        self.stop_time = None
        self.running = False

    def start(self):
        assert(not self.running)
        self.start_time = datetime.now()
        self.running = True

    def stop(self):
        assert(self.running)
        self.stop_time = datetime.now()
        self.running = False

    def get_elapsed(self):
        return self.stop_time - self.start_time

class Chronometer():
    def __init__(self, id_=0, name="Chronometer", own_time=timedelta(0)):
        self.id_ = id_
        self.name = name
        self.own_time = own_time
        self.recorder = Recorder()

    def start(self):
        self.recorder.start()

    def stop(self):
        self.recorder.stop()
        self.own_time += self.recorder.get_elapsed()

    def __str__(self):
        return "{}: {}".format(self.name, self.own_time)

class ChronometerWithChilds(Chronometer):
    def __init__(self, id_=0, name="Chronometer", own_time=timedelta(0)):
       self.childs = list()
       self.total_time = 0
       super().__init__(id_=id_, name=name, own_time=own_time) 

    def update_total_time(self):
        self.total_time = self._get_cumul_time_of_childs(self) + self.own_time

    def _get_cumul_time_of_childs(self, parent, cumul=timedelta(0)):
        for child in parent.childs:
            if len(child.childs) > 0:
                cumul = self._get_cumul_time_of_childs(child, cumul)
            cumul += child.own_time
        return cumul

    def __str__(self):
        return "{}: {} (CUMUL : {})".format(self.name, self.own_time, self.total_time)
