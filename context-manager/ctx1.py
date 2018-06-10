class contextmanager:
    def __init__(self, gen):
        self.gen = gen

    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self

    def __enter__(self):
        print('__enter__')
        self.gen_inst = self.gen(**self.args, **self.kwargs)
        next(self.gen_inst)

    def __exit__(self, *args):
        print('__exit__')
        next(self.gen_inst, None)

def temptable(cur):
    cur.execute('create table points(x int, y int)')
    yield
    cur.execute('drop table points')

new_temptable = contextmanager(temptable)


with connect('test.db') as conn:
    cur = conn.cursor()
    with new_temptable(cur):
        cur.execute('insert into points (x, y) values(1, 1)')
        cur.execute('insert into points (x, y) values(1, 2)')
        cur.execute('insert into points (x, y) values(2, 1)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)

