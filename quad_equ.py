from math import sqrt


def factor(coef):
    '''
    Factors using quadratic formula
    :param coef: Standard form coefficients
    :return: Result(s) of factoring in a tuple. Returns nothing if no solutions.
    '''
    #
    a, b, c = coef[0], coef[1], coef[2]
    dis = discriminant(a, b, c)
    if (dis < 0):
        return None
    elif (dis == 0):
        return tuple([-b / (2 * a)])
    else:
        x1 = (-b + sqrt(dis)) / (2 * a)
        x2 = (-b - sqrt(dis)) / (2 * a)
        return x1, x2


def discriminant(a, b, c):
    '''
    Finds the discriminant of an equation
    :param coef: Standard form coefficients
    :return: The discriminant
    '''
    return b ** 2 - 4 * a * c


class QuadForm:
    def __init__(self, a=1, b=0, c=0):
        assert (a != 0)
        self.a = a
        self.b = b
        self.c = c

    def solve_y(self, x):
        pass

    def solve_x(self, y):
        pass

    def to_std_form(self):
        return self

    def to_vert_form(self):
        return self

    def to_fac_form(self):
        return self


# standard form
class StdForm(QuadForm):
    def __init__(self, a=1, b=0, c=0):
        QuadForm.__init__(self, a, b, c)

    def __str__(self):
        '''
        Returns the equation in standard form as a string
        Standard form: y = ax^2 + bx + c
        :return: String of the equation in standard form
        '''
        s = 'y = '
        # a
        if (self.a == 0):
            None
        else:
            # add sign
            if (self.a < 0):
                s = s + '-'
            # add number
            if (abs(self.a) > 1):
                s = s + str(abs(self.a))
            s = s + 'x^2'

        # b
        if (self.b == 0):
            None
        else:
            # add sign
            if (self.b > 0):
                s = s + ' + '
            else:
                s = s + ' - '
            # add number
            if (abs(self.b) > 1):
                s = s + str(abs(self.b))
            s = s + 'x'

        # c
        if (self.c == 0):
            None
        else:
            # add sign
            if (self.c > 0):
                s = s + ' + '
            else:
                s = s + ' - '
            # add number
            s = s + str(abs(self.c))

        if (self.a == 0 and self.b == 0 and self.c == 0):
            s = s + str(0)
        return s

    def solve_y(self, x):
        '''
        Sovles for the value of y at a given x
        :param x: The value of x
        :return: The value of y
        '''
        return self.a * x ** 2 + self.b * x + self.c

    def solve_x(self, y):
        '''
        Sovles for the value(s) of y at a given x
        :param y: The value of y
        :return: The value(s) of x in a tuple. Returns nothing if no solution
        '''
        return factor((self.a, self.b, self.c - y))

    def to_vert_form(self):
        '''
        Converts from standard form to vertex form by completing the square. Returns coefficients of the equation as a tuple.
        Vertex form: a(x + b)^2 + c
        (-b, c) is the vertex
        :return: Vertex form equation object
        '''
        vert_b = (self.b / self.a) / 2
        vert_c = self.a * -(vert_b) ** 2 + self.c
        return VertForm(self.a, -vert_b, vert_c)

    def to_fac_form(self):
        '''
        Converts from standard form to factored form. Returns components of the equation as a tuple.
        Vertex form: y = a(x -b)(x-c)
        (-b, -c) are the roots
        :param coef: Standard form's coefficients as a tuple
        :return:  Factored form's coefficients as a tuple. Returns nothing if cannot be factored
        '''
        roots = factor((self.a, self.b, self.c))
        # no sol
        if (roots == None):
            return None
        elif (len(roots) == 1):
            return FacForm(self.a, roots[0], roots[0])
        else:
            return FacForm(self.a, roots[0], roots[1])

    def get_discriminant(self):
        return discriminant(self.a, self.b, self.c)


# vertex form
class VertForm(QuadForm):
    def __init__(self, a=1, b=0, c=0):
        QuadForm.__init__(self, a, b, c)

    def __str__(self):
        """
        Returns the equation in vertex form as a string
        Vertex form: y = a(x-b)^2+c
        :return: String of the equation in vertex form
        """
        s = 'y = '
        # a
        if (self.a == 0):
            None
        else:
            # add sign
            if (self.a < 0):
                s = s + '-'
            # add number
            if (abs(self.a) > 1):
                s = s + str(abs(self.a))

            # b
            if (self.b == 0):
                s = s + 'x'
            else:
                s = s + '(x'
                if (self.b == 0):
                    None
                else:
                    # add sign
                    if (-self.b > 0):
                        s = s + ' + '
                    else:
                        s = s + ' - '
                    # add number
                    s = s + str(abs(self.b))
                    s = s + ')'
            s = s + '^2'
        # c
        if (self.c == 0):
            None
        else:
            # add sign
            if (self.c > 0):
                s = s + ' + '
            else:
                s = s + ' - '
            # add number
            s = s + str(abs(self.c))
        return s

    def solve_y(self, x):
        '''
        Sovles for the value of y at a given x
        :param x: The value of x
        :return: The value of y
        '''
        return self.a * ((x - self.b) ** 2) + self.c

    def solve_x(self, y):
        d = (y - self.c) / self.a
        if (d < 0):
            return None
        elif (d == 0):
            return tuple([self.b])
        else:
            x1 = -sqrt(d) + self.b
            x2 = sqrt(d) + self.b
            return (x1, x2)

    def to_std_form(self):
        return StdForm(self.a, 2 * -self.b * self.a, self.a * self.b ** 2 + self.c)

    def to_fac_form(self):
        return self.to_std_form().to_fac_form()


# factored form
class FacForm(QuadForm):
    def __init__(self, a=1, b=0, c=0, ):
        if (b == c):
            self.num_roots = 1
        else:
            self.num_roots = 2
            if (c == 0):
                c = b
                b = 0
        if (self.num_roots == 1):
            QuadForm.__init__(self, a, b, b)
        else:
            QuadForm.__init__(self, a, b, c)

    def __str__(self):
        '''
        Returns the equation in factored form as a string
        Standard form: y = a(x-b)(x-c)
        :return: String of the equation in factored form
        '''
        s = 'y = '
        # a
        if (self.a == 0):
            None
        else:
            # add sign
            if (self.a < 0):
                s = s + '-'
            # add number
            if (abs(self.a) > 1):
                s = s + str(abs(self.a))

            # b
            if (self.b == 0):
                s = s + 'x'
            else:
                s = s + '(x'
                if (self.b == 0):
                    None
                else:
                    # add sign
                    if (-self.b > 0):
                        s = s + ' + '
                    else:
                        s = s + ' - '
                    # add number
                    s = s + str(abs(self.b))
                    s = s + ')'
            if (self.num_roots == 1):
                s = s + '^2'
            else:
                # c
                if (self.c == 0):
                    s = s + 'x'
                else:
                    s = s + '(x'
                    if (self.c == 0):
                        None
                    else:
                        # add sign
                        if (-self.c > 0):
                            s = s + ' + '
                        else:
                            s = s + ' - '
                        # add number
                        s = s + str(abs(self.c))
                    s = s + ')'

        return s

    def solve_y(self, x):
        '''
        Sovles for the value of y at a given x
        :param x: The value of x
        :return: The value of y
        '''
        return self.a * (x - self.b) * (x - self.c)

    def solve_x(self, y):
        return self.to_std_form().solve_x(y)

    def to_std_form(self):
        std_b = self.a * (-self.b - self.c)
        std_c = self.a * self.b * self.c
        return StdForm(self.a, std_b, std_c)

    def to_vert_form(self):
        vert_x = (self.b + self.c) / 2
        vert_y = self.solve_y(vert_x)
        return VertForm(self.a, vert_x, vert_y)


class QuadEqu:
    def __init__(self, a=1, b=0, c=0, form='std'):
        assert (a != 0)
        self.std_form = None
        self.vert_form = None
        self.fac_form = None

        # forms
        if (form == 'std'):
            self.std_form = StdForm(a, b, c)
            self.vert_form = self.std_form.to_vert_form()
            self.fac_form = self.std_form.to_fac_form()
        if (form == 'vert'):
            self.vert_form = VertForm(a, b, c)
            self.std_form = self.vert_form.to_std_form()
            self.fac_form = self.vert_form.to_fac_form()
        if (form == 'fac'):
            self.fac_form = FacForm(a, b, c)
            self.std_form = self.fac_form.to_std_form()
            self.vert_form = self.fac_form.to_vert_form()

        self.y_int = self.solve_y(0)
        self.x_int = self.solve_x(0, 'fac')
        self.vertex = (self.vert_form.b, self.vert_form.c)

    def solve_y(self, x, method='std'):
        '''
        Sovles for the value of y at a given x
        :param x: The value of x
        :param method: Method for solving. Defaults as standard form
        :return: The value of y
        '''
        if (method == 'std'):
            return self.std_form.solve_y(x)
        if (method == 'vert'):
            return self.vert_form.solve_y(x)
        if (method == 'fac'):
            if (self.fac_form == None):
                return None
            else:
                return self.fac_form.solve_y(x)

    def solve_x(self, y, method='std'):
        """
        Solves for value(s) of x at a given y
        :param y: The value of y
        :param method: Method for solving. Defaults as standard form
        :return: The value(s) of x in a tuple. Returns empty tuple if no solutions.
        """
        if (method == 'std'):
            return self.std_form.solve_x(y)
        if (method == 'vert'):
            return self.vert_form.solve_x(y)
        if (method == 'fac'):
            if (self.fac_form == None):
                return None
            else:
                return self.fac_form.solve_x(y)

    def get_discriminant(self):
        return (self.std_form.get_discriminant())

    def __str__(self):
        s = ''
        s = s + 'Standard form: ' + str(self.std_form) + '\n'
        s = s + 'Vertex form: ' + str(self.vert_form) + '\n'
        s = s + 'Factored form: ' + str(self.fac_form) + '\n'
        s = s + 'y intercept: y = ' + str(self.y_int) + '\n'
        s = s + 'x intercept: x = ' + str(self.x_int) + '\n'
        s = s + 'Vertex: ' + str(self.vertex)
        return s
