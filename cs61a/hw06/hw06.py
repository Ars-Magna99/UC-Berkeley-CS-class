passphrase = '*** PASSPHRASE HERE ***'


def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()


class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        next_fib = Fib()

        # start case where the current value is 0.
        if self.value == 0:
            next_fib.value = 1
        else:
            next_fib.value = self.value + self.previous
        next_fib.previous = self.value
        return next_fib

    def __repr__(self):
        return str(self.value)


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """

    def __init__(self, good_name, good_price):
        self.good = good_name
        self.stock = 0
        self.balance = 0
        self.price = good_price

    def deposit(self, n):
        if self.stock == 0:
            print("'Machine is out of stock. Here is your $" + str(n) + ".'")
        else:
            self.balance += n
            print("'Current balance: $" + str(self.balance) + "'")

    def restock(self, number):
        self.stock += number
        print("'Current %s stock: %x'" % (self.good, self.stock))

    def vend(self):
        if self.stock == 0:
            print("'Machine is out of stock.'")
        elif self.balance < self.price:
            print("'You must deposit $%d more.'" %
                  (self.price - self.balance))
        elif self.balance > self.price:
            self.stock -= 1
            print("'Here is your %s and $%i change.'" %
                  (self.good, (self.balance - self.price)))
            self.balance = 0
        elif self.balance == self.price:
            self.balance = 0
            self.stock -= 1
            print("'Here is your % s.'" % (self.good))
