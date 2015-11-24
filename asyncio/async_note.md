asyncio
    event loop
    coroutine and future, task
    transport and protocol
    streams
    subprocss
    sync primitives


pluggable event loop, transport, protocol

event loop method should always accept or return Future like coroutine

scheduler is provided for writing asyncio code replace for callback, just
like yield from in coroutine,
scheduler is not pluggable
scheduler offer operation to suspend a coroutine until a callback is called
 
a transport is an abstraction for socket (or similiar I/O endpoint) while
a protocol is an abstraciton for an application 
a view is simply that the transport and protocol interfaces  together define
an abstraction interface for using networking I/O, and interprocess I/O

There is almost always a 1:1 relationship between transport and protocol objects: the protocol calls transport methods to send data, while the transport calls protocol methods to pass it data that has been received. Neither transport not protocol methods "block" -- they set events into motion and then return.

The most common type of transport is a bidirectional stream transport. It represents a pair of buffered streams (one in each direction) that each transmit a sequence of bytes. The most common example of a bidirectional stream transport is probably a TCP connection. Another common example is an SSL/TLS connection. But there are some other things that can be viewed this way, for example an SSH session or a pair of UNIX pipes. Typically there aren't many different transport implementations, and most of them come with the event loop implementation. However, there is no requirement that all transports must be created by calling an event loop method: a third party module may well implement a new transport and provide a constructor or factory function for it that simply takes an event loop as an argument or calls get_event_loop().

Note that transports don't need to use sockets, not even if they use TCP -- sockets are a platform-specific implementation detail.
A bidirectional stream transport has two "ends": one end talks to the network (or another process, or whatever low-level interface it wraps), and the other end talks to the protocol. The former uses whatever API is necessary to implement the transport; but the interface between transport and protocol is standardized by this PEP.

default policy will create a new event loop only in the main thread
in other thread event loop should explicitly set

set_event_loop, set_event_loop_policy new_event_loop

all timeout, interval, delay are measured in seconds



event loop methods
=======================
start/stop: run_forever(), run_until_complete(), stop(), is_running()
basic/timed callback: call_soon(), call_later(), time()
thread interaction: call_soon_threadsafe(), run_in_executor(), set_default_executor()
internet name lookups: getaddrinfo(), getnameinfo()
internet connection: create_connection(), create_server(), create_datagram_endpoint()
wrapped socket methods: sock_recv(), sock_sendall(), sock_connect(), sock_accept()

## callback function return Handle type object
## even loop should never start a callback while another callback is still running
## create_server() return a Server object, has close() and wait_closed()(corotine)

asyncio.Future (not concurrent.future.Future)
============================
cancelled Future is considered done
a Future is associated with an event loop when it is created
result()
done()
exception()
add_done_callback(fn) , fn is called by call_soon()
remove_done_callback(fn)
set_result() Future should not be done already, make Future done and schedule
callback
set_exception()

asyncio.async(arg) if arg is a Future , it's returned unchanged, if it's a 
coroutine, it is wrapped into a Task(subclass of Future)

Transport
===========================
type: bidirectional stream transport, unbidirectional, datagram
bidirect: plain or SSL/TLS

A bidrectional stream transport is an abstraction on top of a socket or something similar (for example, a pair of UNIX pipes or an SSL/TLS connection).

interface between transport and protocol is asymmetric

From the protocol's point of view, writing data is done by calling the write() method on the transport object
whenever some data is read from the socket (or other data source), the transport calls the protocol's data_received() method

Protocol
============================
loop.create_server(protocol_factory, host, port)
Protocols are always used in conjunction with transports.
A (bidirectional) stream protocol must implement the following methods, which will be called by the transport.
connection_made()
data_received()
eof_received()
pause_writing()
resume_writing()
connection_lost()
these function will be called by transport under loop scheduling

Callback
===========================
style:  does not support keyword arguments.
If you have a callback that must be called with a keyword argument, you can use a lambda   <loop.call_soon(lambda: foo('abc', repeat=43))>

Coroutine
============================
usage of coroutine is optional, it is fine to write code using callback only

In the case of a coroutine object, there are two basic ways to start it running: call yield from coroutine from another coroutine (assuming the other coroutine is already running!), or convert it to a Task (see below).

to wait for multiple coroutine or Future, two apis are provided:
1. asyncio.wait() : 
2. asyncio.as_complete(): 
3. asyncio.wait_for()
4. asyncio.gather()
5. asyncio.shield()

sleep
=======================
asyncio.sleep(delay) is a coroutine, return None after delay

Tasks
========================
a task is an object that manage an independently running coroutine
Task is a subclass of Future, Task becomes done when its coroutine 
returns or raise an exception, all will be propageted
cancelling a Task not done yet throw an asyncio.CancelledError to coroutine

To convert a coroutine into a task, call the coroutine function and pass the resulting 
coroutine object to the asyncio.Task() constructor. You may also use asyncio.async() for this purpose.
also loop.create_task()

Scheduler
=======================
the scheduler has no public interface, you interact with it through "yield from " ,
there is no single object representing the scheduler, its behavior is implemented by Task or Future
using only the public interface of the event loop

Convenience Utilities
=======================
asyncio.open_connection()
asyncio.start_server()

