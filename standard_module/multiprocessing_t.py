'''
On Unix two new start methods, (spawn and forkserver, have been added for starting processes using multiprocessing. These make the mixing of processes with threads more robust

spawn
    The parent process starts a fresh python interpreter process. The child process will only inherit those resources necessary to run the process objects run() method. In particular, unnecessary file descriptors and handles from the parent process will not be inherited. Starting a process using this method is rather slow compared to using fork or forkserver.

    Available on Unix and Windows. The default on Windows.

fork
    The parent process uses os.fork() to fork the Python interpreter. The child process, when it begins, is effectively identical to the parent process. All resources of the parent are inherited by the child process. Note that safely forking a multithreaded process is problematic.

    Available on Unix only. The default on Unix.

forkserver
    When the program starts and selects the forkserver start method, a server process is started. From then on, whenever a new process is needed, the parent process connects to the server and requests that it fork a new process. The fork server process is single threaded so it is safe for it to use os.fork(). No unnecessary resources are inherited.

    Available on Unix platforms which support passing file descriptors over Unix pipes.
'''
import multiprocessing

print(multiprocessing.get_all_start_methods())
