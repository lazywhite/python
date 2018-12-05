import jpype

jar_path = "/path/to/jar"
arg = "-Djava.class.path=%s" % jar_path

jvm_path = jpype.getDefaultJVMPath()

jpype.startJVM(jvm_path, arg)

jpype.JPackage("pkg").TestClass.TestMethod("arg1")
