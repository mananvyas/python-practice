class MyClass:
    variable  = "test"

    def function(self):
        print("this is message from class function")
    def another_func_with_arg(self, name):
        print("hello %s" % name)

myobject = MyClass()
myobject.function()
myobject.another_func_with_arg("Jabber")