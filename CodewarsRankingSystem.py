RANK_LIST = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

class User:
    def __init__(self, rank=-8):
        self.rank = rank
        self.progress = 0

    def inc_progress(self, task_rank):
        if task_rank not in RANK_LIST:
            raise Exception("Error!")
        value = self.get_task_value(task_rank)
        self.apply_progress(value)

    def get_difference_levels(self, task_rank):
        user_index = RANK_LIST.index(self.rank)
        task_index = RANK_LIST.index(task_rank)
        return task_index- user_index

    def get_task_value(self, task_rank):
        value = 0
        if self.rank == task_rank:
            value += 3
        elif self.rank == task_rank + 1:
            value += 1
        elif task_rank > self.rank:
            difference = self.get_difference_levels(task_rank)
            value += 10 * (difference ** 2)
        return value

    def apply_progress(self, progress):
        self.progress += progress
        while self.progress > 99 and self.rank < 8:
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:
                self.rank += 1


user = User(rank=-1)
user.inc_progress(1)
print(user.progress, 10)