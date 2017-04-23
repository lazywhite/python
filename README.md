## Introduction

This repo is a collection of Python2/3 practice code, mostly come from   
1. Oreilly Python 3 Cookbook  
2. Python standard library by example  


## Repo Structure
  
```
.
├── README.md
├── algorithm
│   ├── btree.py
│   ├── prime.py
│   ├── single_disptch.py
│   └── weight.py
├── aop
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
│   ├── node2.log
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
├── daemon
│   └── demo.py
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
│   ├── OpenERP
│   ├── bottle
│   ├── django
│   ├── flask
│   └── pyramid
├── func
│   ├── functools_t.py
│   ├── itertools_t.py
│   └── operator_t.py
├── get_text
│   ├── example.py
│   └── locale
├── inheriance
│   └── test.py
├── jinja2
│   ├── jinja2_test.py
│   └── templates
├── lang
│   ├── bytes-t.py
│   ├── note.txt
│   ├── pinject_t.py
│   └── theory.py
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
├── note.md
├── oauth
│   └── example.py
├── office
│   └── doc.py
├── oreilly
│   ├── annotation.py
│   ├── argparse_t.py
│   ├── atexit_t.py
│   ├── class_t.py
│   ├── config.ini
│   ├── config_parse.py
│   ├── context_manager_t.py
│   ├── context_proto.py
│   ├── couter_t.py
│   ├── data_processing.py
│   ├── datetime_t.py
│   ├── dateutil_t.py
│   ├── dedupe_t.py
│   ├── default_dict_t.py
│   ├── dequeue_t.py
│   ├── descriptor_t.py
│   ├── enum_t.py
│   ├── file.py
│   ├── filter_t.py
│   ├── fraction_t.py
│   ├── func.py
│   ├── getpass_t.py
│   ├── heapq_t.py
│   ├── iter_gene.py
│   ├── logging_t.py
│   ├── map_t.py
│   ├── math_t.py
│   ├── module_and_package.py
│   ├── multiprocess.py
│   ├── named_tuple_t.py
│   ├── operator_t.py
│   ├── ordered_dict_t.py
│   ├── partial_t.py
│   ├── priority_queue.py
│   ├── proxy_t.py
│   ├── random_t.py
│   ├── reduce_t.py
│   ├── signal_t.py
│   ├── slice_t.py
│   ├── special_attr.py
│   ├── stateMachine.py
│   ├── string_t.py
│   ├── subprocess_t.py
│   ├── unpack_item.py
│   ├── weakref_t.py
│   ├── web.py
│   └── wraps.py
├── orm
│   └── official.py
├── other
│   ├── beautifulsoup_t.py
│   ├── bianchenzhimei.py
│   ├── install_m2crypto.md
│   ├── jianzhioffer.py
│   ├── libvirt_t.py
│   ├── ms100.py
│   ├── oursql_t.py
│   └── parse_xlsx.py
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
│   ├── parse_access.py
│   └── re_test.py
├── restfull
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
├── sphinx
│   ├── note.md
│   └── sphinx_test
├── standard_module
│   ├── bisect_t.py
│   ├── codecs_t.py
│   ├── multiprocessing_t.py
│   ├── pathlib_t.py
│   ├── selectors_t.py
│   └── tracemalloc_t.py
├── super
│   ├── mro.py
│   ├── python3_super.py
│   └── super_mro.py
├── system
│   ├── os.txt
│   └── psutil_t.py
├── testTool
│   ├── doc_test.py
│   └── unit_test.py
├── tools
│   ├── cos_demo.py
│   ├── mock.md
│   ├── oss.md
│   ├── pg_bouncer.md
│   ├── pip.md
│   ├── pyenv.md
│   ├── pymssql.md
│   ├── send_slack.py
│   ├── sms.py
│   ├── smtp-t.py
│   ├── uwsgi.md
│   ├── virtualwrapper.md
│   └── wheel.md
├── with
│   ├── context_manager.py
│   └── protocol.py
├── yaml
│   ├── a.py
│   └── et.yml
├── yield
│   ├── fib.py
│   ├── gene_concurrent.py
│   ├── yield.py
│   └── yield_from.py
└── zabbix_to_word
    ├── config.yml
    ├── doc
    ├── graph
    ├── lib
    ├── new.py
    ├── requirements.txt
    ├── run.py
    └── template
```
