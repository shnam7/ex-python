# Hanoi tower simulation
import time


class HanoiTower:
    """Hanoi Tower Simulator"""

    def __init__(self, diskCount):
        self.iter = 0
        self.pegs = [list(range(1, diskCount+1)), [], []]

    def move(self, n, source, helper, target, silent=False):
        if n <= 0:
            return

        # move n-1 disks from source peg to target peg
        self.move(n-1, source, target, helper, silent)

        # move disk from source to target
        if self.pegs[source]:
            disk = self.pegs[source].pop(0)
            # if not silent: self.print()
            self.pegs[target].insert(0, disk)
            self.iter += 1
            if not silent:
                self.print()

        # move n-1 disks from helper to target
        self.move(n-1, helper, source, target, silent)

    def run(self, silent=False):
        """
        Move disks from self.peg[0] to self.peg[2] using self.peg[1]
        as helper peg
        """
        self.print()
        self.move(len(self.pegs[0]), 0, 1, 2, silent)
        if silent:
            self.print()     # print last status if silent switch is turned on
        return self.iter

    def print(self):
        print('n={:03d} {!s:^15} {!s:^15} {!s:^15}'.format(
            self.iter, self.pegs[0], self.pegs[1], self.pegs[2]))


hanoi = HanoiTower(5)
tm1 = time.time()
count = hanoi.run(False)
tm2 = time.time()

print('Total iteration={} Elapsed time={}'.format(count, tm2-tm1))
