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
            return max_index

        else:
            # search the lowest index
            for index, queue in enumerate(self.queues):
                for person in queue:
                    if person < index:
                        return person
        return None

    def remove_duplicates(self, floor_list):
        seen = set()
        seen_add = seen.add
        return [x for x in floor_list if not (x in seen or seen_add(x))]


    def theLift(self):
        output = [0]
        target_floor = self.get_target_floor()
        while target_floor is not None:
            visited_floors = []

            if self.current_direction == 'UP':
                for floor in range(self.current_floor, target_floor + 1):
                    stopped = False

                    # people get off first.
                    if len(self.current_users) > 0:
                        lift_user_index = len(self.current_users) - 1
                        while lift_user_index >= 0:
                            if self.current_users[lift_user_index] == floor:
                                self.current_users.pop(lift_user_index)
                                stopped = True
                            lift_user_index -= 1

                    # then they get in
                    # todo I'm not respecting queue orders because I'm reading them from the back, need to be from front
                    if len(self.queues[floor]) > 0:
                        queue_index = len(self.queues[floor]) - 1
                        while queue_index >= 0:
                            if self.queues[floor][queue_index] > floor and len(self.current_users) < self.capacity:
                                self.current_users.append(self.queues[floor][queue_index])
                                self.queues[floor].pop(queue_index)
                                stopped = True

                            queue_index -= 1

                    if stopped:
                        visited_floors.append(floor)
            else:
                for floor in range(self.current_floor, target_floor - 1, -1):
                    stopped = False

                    # people get off first.
                    if len(self.current_users) > 0:
                        lift_user_index = len(self.current_users) - 1
                        while lift_user_index >= 0:
                            if self.current_users[lift_user_index] == floor:
                                self.current_users.pop(lift_user_index)
                                stopped = True
                            lift_user_index -= 1

                    # then they get in
                    if len(self.queues[floor]) > 0:
                        queue_index = len(self.queues[floor]) - 1
                        while queue_index >= 0:
                            if self.queues[floor][queue_index] < floor and len(self.current_users) < self.capacity:
                                self.current_users.append(self.queues[floor][queue_index])
                                self.queues[floor].pop(queue_index)
                                stopped = True
                            queue_index -= 1

                    if stopped:
                        visited_floors.append(floor)

            output.extend(self.remove_duplicates(visited_floors))

            # after reaching target floor, change direction.
            self.current_floor = floor
            self.current_direction = 'DOWN' if self.current_direction == 'UP' else 'UP'
            target_floor = self.get_target_floor()

        if output[len(output) - 1] != 0:
            output.append(0)
        return output


# Floors:    G     1      2        3     4      5      6         Answers:
# tests = [[((), (), (5, 5, 5), (), (), (), ()), [0, 2, 5, 0]],
#          [((), (), (1, 1), (), (), (), ()), [0, 2, 1, 0]],
#          [((), (3,), (4,), (), (5,), (), ()), [0, 1, 2, 3, 4, 5, 0]],
#          [((), (0,), (), (), (2,), (3,), ()), [0, 5, 4, 3, 2, 1, 0]]]
#
# for queues, answer in tests:
#     lift = Dinglemouse(queues, 5)
#     a = lift.theLift()
#     print(a, answer)


queues = ((2, 10, 2, 2), (4, 4), (), (8, 7, 4, 11), (3, 2, 0, 11, 3), (10, 3, 0, 10, 3), (3, 7, 2, 11, 9), (), (6, 7, 5), (3, 7, 1, 2, 2), (3, 7, 12, 0, 7), (9, 0), (6, 0, 0, 8))
capacity = 3
lift = Dinglemouse(queues, capacity)
a = lift.theLift()
print(a)
