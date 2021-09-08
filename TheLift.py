class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = [list(queue) for queue in queues]
        self.capacity = capacity
        self.current_floor = 0
        self.current_direction = 'UP'
        self.current_users = []

    def get_target_floor(self):
        #search for the highest floor with a person wanting to go up
        if self.current_direction == 'UP':
            # search for the highest index
            max_index = 0
            for index, queue in enumerate(self.queues):
                if len(queue) > 0:
                    if max(queue) > max_index:
                        max_index = max(queue)
                    if index > max_index:
                        max_index = index
            for index, queue in enumerate(self.current_users):
                if len(queue) > 0:
                    if max(queue) > max_index:
                        max_index = max(queue)
            return max_index

        else:
            # search the lowest index
            min_index = len(self.queues)
            for index, queue in enumerate(self.queues):
                for person in queue:
                    if person < index:
                        min_index = person
            if min(self.current_users) < min_index:
                min_index = min(self.current_users)
            return min_index

    def remove_duplicates(self, floor_list):
        seen = set()
        seen_add = seen.add
        return [x for x in floor_list if not (x in seen or seen_add(x))]

    def check_queues(self):
        for queue in self.queues:
            if queue:
                return True
        return False

    def theLift(self):
        output = []
        first = True

        while self.check_queues():
            if first:
                visited_floors = [0]
                first = False
            else:
                visited_floors = []

            if self.current_direction == 'UP':
                for floor in range(self.current_floor, len(self.queues)):
                    stopped = False

                    # people get off first.
                    pop_indexes = []
                    for index, lift_user in enumerate(self.current_users):
                        if lift_user == floor:
                            pop_indexes.append(index)
                            stopped = True

                    for index in reversed(pop_indexes):
                        self.current_users.pop(index)

                    # then they get in
                    pop_indexes = []
                    additional_people = 0
                    for index, lift_user in enumerate(self.queues[floor]):
                        if lift_user > floor:
                            stopped = True
                        if lift_user > floor and (len(self.current_users) + additional_people) < self.capacity:
                            pop_indexes.append(index)
                            additional_people += 1
                            stopped = True

                    for index in reversed(pop_indexes):
                        self.current_users.append(self.queues[floor].pop(index))

                    if stopped:
                        visited_floors.append(floor)
            else:
                for floor in range(self.current_floor, -1, -1):
                    stopped = False

                    # people get off first.
                    pop_indexes = []
                    for index, lift_user in enumerate(self.current_users):
                        if lift_user == floor:
                            pop_indexes.append(index)
                            stopped = True

                    for index in reversed(pop_indexes):
                        self.current_users.pop(index)

                    # then they get in
                    pop_indexes = []
                    additional_people = 0
                    for index, lift_user in enumerate(self.queues[floor]):
                        if lift_user < floor:
                            stopped = True
                        if lift_user < floor and (len(self.current_users) + additional_people) < self.capacity:
                            pop_indexes.append(index)
                            additional_people += 1

                    for index in reversed(pop_indexes):
                        self.current_users.append(self.queues[floor].pop(index))

                    if stopped:
                        visited_floors.append(floor)
            no_dupes = self.remove_duplicates(visited_floors)
            if output and no_dupes:
                if output[len(output) - 1] == no_dupes[0]:
                    no_dupes.pop(0)
            output.extend(no_dupes)

            # after reaching target floor, change direction.
            self.current_floor = floor
            self.current_direction = 'DOWN' if self.current_direction == 'UP' else 'UP'

        if output and output[len(output) - 1] != 0:
            output.append(0)
        return output if output else [0]


# #Floors:    G     1      2        3     4      5      6         Answers:
# tests = [[((), (), (5, 5, 5), (), (), (), ()), [0, 2, 5, 0]],
#          [((), (), (1, 1), (), (), (), ()), [0, 2, 1, 0]],
#          [((), (3,), (4,), (), (5,), (), ()), [0, 1, 2, 3, 4, 5, 0]],
#          [((), (0,), (), (), (2,), (3,), ()), [0, 5, 4, 3, 2, 1, 0]]]
#
# for queues, answer in tests:
#     lift = Dinglemouse(queues, 5)
#     a = lift.theLift()
#     print(a, answer)


queues = ((), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))
capacity = 5
lift = Dinglemouse(queues, capacity)
a = lift.theLift()
print(a)
