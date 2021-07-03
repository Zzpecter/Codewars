class Automaton(object):

    def __init__(self):
        self.states = {
            'q1': True,
            'q2': False,
            'q3': False
        }

    def get_current_state(self):
        for state, is_active in self.states.items():
            if is_active:
                return state

    def make_transition(self, command):
        state = self.get_current_state()
        if state == 'q1':
            if command == '1':
                self.states.update({state: False})
                self.states.update({'q2': True})
        elif state == 'q2':
            if command == '0':
                self.states.update({state: False})
                self.states.update({'q3': True})
        else:
            self.states.update({state: False})
            self.states.update({'q2': True})

    def read_commands(self, commands):
        for command in commands:
            self.make_transition(command)
        return self.states['q2']


my_automaton = Automaton()
print(my_automaton.read_commands(["1", "0", "0", "1"]))