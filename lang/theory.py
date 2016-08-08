Normally, using a.b to get, set or delete an attribute looks up the object named b in the class dictionary for a, but if b is a descriptor, the respective descriptor method gets called.


An object is hashable if it has a hash value which never changes during its lifetime

All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries) are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal (except with themselves), and their hash value is their id().

iterator : an object representing a stream of data

metaclass: The class of a class. Class definitions create a class name, a class dictionary, and a list of base classes. The metaclass is responsible for taking those three arguments and creating the class. 

MRO: method resolution order 
module: An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects.

package: Technically, a package is a Python module with an __path__ attribute

reference count

object: type, value, identifier

views: objects returned from dict.keys(), dict.values(), and dict.items() are called dictionary views. They are lazy sequences that will see changes in the underlying dictionary. To force the dictionary view to become a full list use list(dictview).


python2.x do not have nonlocal keyword

'return' will break the loop

Packages support one more special attribute, __path__. This is initialized to be a list containing the name of the directory holding the package’s __init__.py before the code in that file is executed. This variable can be modified; doing so affects future searches for modules and subpackages contained in the package.



an object's type determines the operations that the object support
an object's mutability is determined by its type

It is not guaranteed that __del__() methods are called for objects that still exist when the interpreter exits.

print(object) execute object.__str__
repr(object) execute object.__repr__


__getattribute__ 

Specifically, any module that contains a __path__ attribute is considered a package.
