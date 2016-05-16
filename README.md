## Introduction

This repo is a collection of Python2/3 practice code, mostly come from   
1. Oreilly Python 3 Cookbook  
2. Python standard library by example  


## Repo Structure
  
```
├── README.md
├── algorithm
│   ├── btree.py
│   └── weight.py
├── arg_clinic
│   ├── doc_opt.py
│   └── ls.py
├── asyncio
│   ├── aiohttp_t.py
│   ├── app-server.py
│   ├── app.py
│   ├── async_call.py
│   ├── async_note.md
│   ├── async_protocol.py
│   ├── async_redis.py
│   ├── async_sleep.py
│   ├── await.py
│   ├── sample
│   ├── start-server.py
│   ├── websockets_client.py
│   └── websockets_t.py
├── celery
│   ├── celery_config.py
│   ├── config_redis.py
│   ├── config_redis.pyc
│   ├── node1.log
│   ├── node1.pid
│   ├── node2.log
│   ├── node2.pid
│   ├── note.py
│   ├── redis_t.py
│   ├── single_task.py
│   ├── tasks.py
│   └── tasks.pyc
├── client
│   └── influxdb
├── cmd
│   └── prsh
├── concurrency
│   ├── future
│   ├── gevent
│   ├── multiprocessing
│   └── threading
├── curses
│   ├── newpad.py
│   └── wrap.py
├── datatype
│   ├── dict_with_default_value.py
│   ├── subdict.py
│   └── sublist.py
├── datetime
│   └── note.py
├── decorator
│   ├── deco_with_arg.py
│   ├── multi_deco.py
│   ├── note
│   └── tag.py
├── descriptor
│   ├── descriptor.py
│   └── property.py
├── devpi
│   └── note.md
├── extending
│   └── spam.c
├── framework
│   ├── django
│   ├── flask
│   ├── mysite
│   ├── pyramid
│   └── tornado
├── func
│   ├── functools_t.py
│   ├── itertools_t.py
│   └── operator_t.py
├── get_text
│   ├── example.py
│   └── locale
├── jinja2
│   ├── jinja2_test.py
│   └── templates
├── lxml
│   ├── a.py
│   └── example.xml
├── matplot
│   ├── a.py
│   ├── d.py
│   ├── e.py
│   ├── f.py
│   ├── m.py
│   ├── note
│   └── ss.py
├── metaclass
│   └── metaclass.py
├── note.txt
├── oauth
│   └── example.py
├── oreilly
│   ├── class_t.py
│   ├── config.ini
│   ├── data_processing.py
│   ├── dsaa.py
│   ├── enum_t.py
│   ├── file.py
│   ├── func.py
│   ├── getpass_t.py
│   ├── iter_gene.py
│   ├── logging_t.py
│   ├── math_t.py
│   ├── mc_Client.py
│   ├── mc_Listener.py
│   ├── module_and_package.py
│   ├── multiprocess.py
│   ├── puzzle.py
│   ├── sa.py
│   ├── sqlite3.db
│   ├── stock.csv
│   ├── stock.csv.bak
│   ├── string_t.py
│   ├── weakref_t.py
│   ├── web.py
│   └── wraps.py
├── orm
│   ├── __pycache__
│   └── official.py
├── other
│   ├── beautifulsoup_t.py
│   ├── bianchenzhimei.py
│   ├── jianzhioffer.py
│   ├── ms100.py
│   └── parse_xlsx.py
├── pinject_t.py
├── pip.md
├── prime.py
├── process
│   ├── daemon.py
│   └── test.py
├── project
│   ├── card
│   ├── plague
│   ├── pvp
│   └── websocket_app
├── protobuf
│   ├── addressbook.proto
│   ├── note.md
│   ├── pbreader.py
│   └── pbwriter.py
├── python-patterns
│   ├── 3-tier.py
│   ├── README.md
│   ├── abstract_factory.py
│   ├── adapter.py
│   ├── append_output.sh
│   ├── borg.py
│   ├── bridge.py
│   ├── builder.py
│   ├── catalog.py
│   ├── chain.py
│   ├── chaining_method.py
│   ├── command.py
│   ├── composite.py
│   ├── decorator.py
│   ├── di.py
│   ├── facade.py
│   ├── factory_method.py
│   ├── flyweight.py
│   ├── front_controller.py
│   ├── graph_search.py
│   ├── iterator.py
│   ├── lazy_evaluation.py
│   ├── mediator.py
│   ├── memento.py
│   ├── mvc.py
│   ├── observer.py
│   ├── pool.py
│   ├── prototype.py
│   ├── proxy.py
│   ├── publish_subscribe.py
│   ├── specification.py
│   ├── state.py
│   ├── strategy.py
│   ├── template.py
│   └── visitor.py
├── rabbit
│   ├── new_task.py
│   ├── new_worker.py
│   ├── rabbit_rpcclient.py
│   ├── rabbit_rpcserver.py
│   ├── receive.py
│   └── send.py
├── re
│   └── re_test.py
├── restfull
│   ├── __pycache__
│   ├── rest_t.py
│   ├── restless.py
│   └── resty.py
├── select
│   └── example.py
├── setuptools
│   └── helloworld
├── signal
│   ├── receiver.py
│   ├── receiver.pyc
│   ├── run.py
│   ├── run.pyc
│   ├── signalib.py
│   └── signalib.pyc
├── single_disptch.py
├── singleton
│   ├── same_obj_with_same_args.py
│   └── singleton.py
├── socket
│   ├── multicast_receiver.py
│   ├── multicast_sender.py
│   ├── select_sock_client.py
│   ├── select_sock_server.py
│   ├── selectors_echo.py
│   ├── socket_pair.py
│   ├── socket_server_t.py
│   ├── ssdp_client.py
│   ├── ssdp_server.py
│   ├── ssdp_server.pyc
│   ├── uds_server.py
│   ├── xmlrpc_client.py
│   └── xmlrpc_server.py
├── special_method
│   ├── del.py
│   └── prepare.py
├── standard_module
│   ├── bisect_t.py
│   ├── codecs_t.py
│   ├── multiprocessing_t.py
│   ├── pathlib_t.py
│   ├── selectors_t.py
│   └── tracemalloc_t.py
├── super
│   ├── mro.py
│   └── super_mro.py
├── system
│   └── psutil_t.py
├── testTool
│   ├── doc_test.py
│   └── unit_test.py
├── theory.py
├── tools
│   ├── mock.md
│   └── virtualwrapper.md
├── uwsgi.md
├── with
│   ├── context_manager.py
│   └── protocol.py
├── yaml
│   ├── a.py
│   └── et.yml
└── yield
```
