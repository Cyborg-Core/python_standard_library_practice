class BoolObjectTrue:
    ...


class BoolObjectFalse1:
    def __bool__(self):
        return False


class BoolObjectFalse2:
    def __len__(self):
        return 0


def boolean_value():
    # the value of bool, constants and None
    v1 = True
    print(f"the boolean value of True is {bool(v1)}")
    v1 = False
    print(f"the boolean value of False is {bool(v1)}")
    v1 = None
    print(f"the boolean value of None is {bool(v1)}")
    v1 = NotImplemented
    print(f"the boolean value of NotImplemented is {bool(v1)}")
    v1 = Ellipsis
    print(f"the boolean value of Ellipsis is {bool(v1)}")
    v1 = __debug__
    # If we add -O in interpreter options return is false
    print(f"the boolean value of __debug__ is {bool(v1)}")

    # Numeric type boolean
    v1 = 0
    print(f"the boolean value of integer 0 is {bool(v1)}")
    v1 = 1
    print(f"the boolean value of integer 1 is {bool(v1)}")

    # object boolean judgement
    v1 = BoolObjectFalse1
    print(f"the boolean value of class type {bool(v1)}")
    v1 = v1()
    print(f"the boolean value of BoolObjectFalse1 is {bool(v1)}")
    v1 = BoolObjectFalse2()
    print(f"the boolean value of BoolObjectFalse2 is {bool(v1)}")
    v1 = BoolObjectTrue()
    print(f"the boolean value of BoolObjectTrue is {bool(v1)}")



if __name__ == '__main__':
    boolean_value()
    print(BoolObjectTrue)
