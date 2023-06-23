class MyError(Exception): ...

class OtherError(Exception): ...

def up_raise():
    exception_ = MyError('erro tal tal')
    exception_.add_note('primeira nota sobre o erro')
    raise exception_

try: 
    up_raise()
except MyError as error:
    print(error.__class__.__name__)
    print(error)
    exception_ = OtherError('que gerou esse outro erro tal tal')
    exception_.add_note('um erro levou ao outro erro')
    print(exception_)
    raise exception_ from error

up_raise()
