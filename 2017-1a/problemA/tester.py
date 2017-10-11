import math
import sys

from subprocess import run, PIPE

"""
A tool used to test the solution.
"""


class Tester:
    """
    Creates a new tester.
    """

    def __init__(self):
        self.tests = []
        self.load_tests()

    """
    Adds a test to this tester.
    """

    def add_test(self, name, input, expected):
        self.tests.append(Test(name, input, expected))

    def load_tests(self):
        with open('tests.txt') as f:
            line = f.readline()
            while (line != ''):
                if (line.startswith('# ')):  # begining of a test
                    name = line[2:].strip()
                    input = self.read_section(f)
                    output = self.read_section(f)
                    self.add_test(name, input, output)
                line = f.readline()

    """
    Reads the next section of the file, where sections are seperated by
    markdown headers.
    """

    def read_section(self, file):
        file.readline()  # consume the section label
        prev_pos = file.tell()  # reverse when we read next section label
        result = ""
        line = file.readline()
        while (line != '' and not line.startswith("#")):
            result += line
            prev_pos = file.tell()
            line = file.readline()

        file.seek(prev_pos)

        if (line == '' and not result.endswith('\n')):  # add newline to end of result
            result += '\n'

        return result

    def format_input(self, arg):
        return " | ".join(str(arg).splitlines())

    """
    Runs all of the tests.
    """

    def run(self):
        success = 0
        failed = 0
        for test in self.tests:
            message = ""
            if (test.run()):
                success += 1
                message += "Test Passed!"
            else:
                failed += 1
                message += "Test Failed!"
            message += f' Name: {test.name}, Input: {self.format_input(test.input)}'
            if (test.expected != test.actual):
                message += f'\n\tExpected: \t{repr(test.expected)}\n\tActual: \t{repr(test.actual)}'
            print(message)
        print()
        if (failed == 0):
            print('All tests passed!')
        else:
            print(f'Test run failed! {success} passed, {failed} failed')


"""
A test that can be run on the solution.
"""


class Test:
    """
    Creates a new test.
    """

    def __init__(self, name, input, expected):
        self.name = name
        self.input = input
        self.expected = expected

    """
    Runs this test.
    """

    def run(self):
        p = run(['python', 'solution.py'], input=self.input,
                stdout=PIPE, encoding='ascii')
        self.actual = p.stdout
        return self.actual == self.expected


"""
Run the algorithm using input from standard input.
"""


def main():
    solution_tester = Tester()
    solution_tester.run()


if __name__ == "__main__":
    main()
