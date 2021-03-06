# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: run.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='run.proto',
  package='protobuf',
  syntax='proto3',
  serialized_options=b'P\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\trun.proto\x12\x08protobuf\"v\n\x03Run\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x02id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\x03net\x18\x03 \x01(\x0b\x32\r.protobuf.Net\x12\x1f\n\x06traces\x18\x04 \x03(\x0b\x32\x0f.protobuf.TraceB\x07\n\x05_nameB\x05\n\x03_id\"x\n\x03Net\x12\x14\n\x07netName\x18\x01 \x01(\tH\x00\x88\x01\x01\x12&\n\tsystemNet\x18\x02 \x01(\x0b\x32\x13.protobuf.SystemNet\x12\'\n\nagentTypes\x18\x03 \x03(\x0b\x32\x13.protobuf.AgentTypeB\n\n\x08_netName\"\x90\x01\n\tSystemNet\x12%\n\x06places\x18\x01 \x03(\x0b\x32\x15.protobuf.SystemPlace\x12\x14\n\x0cstartPlaceId\x18\x02 \x01(\t\x12)\n\x0btransitions\x18\x03 \x03(\x0b\x32\x14.protobuf.Transition\x12\x1b\n\x04\x61rcs\x18\x04 \x03(\x0b\x32\r.protobuf.Arc\"\xad\x01\n\tAgentType\x12\x10\n\x08typeName\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x14\n\x0cstartPlaceId\x18\x03 \x01(\t\x12$\n\x06places\x18\x04 \x03(\x0b\x32\x14.protobuf.AgentPlace\x12)\n\x0btransitions\x18\x05 \x03(\x0b\x32\x14.protobuf.Transition\x12\x1b\n\x04\x61rcs\x18\x06 \x03(\x0b\x32\r.protobuf.Arc\"\'\n\nAgentPlace\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\"=\n\x0bSystemPlace\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x13\n\x0b\x61gentTypeId\x18\x03 \x01(\t\"U\n\nTransition\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x10\n\x08\x61\x63tivity\x18\x03 \x01(\t\x12\x11\n\x04sync\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_sync\"S\n\x03\x41rc\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\x05label\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x08sourceId\x18\x03 \x01(\t\x12\x10\n\x08targetId\x18\x04 \x01(\tB\x08\n\x06_label\"y\n\x05Trace\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12)\n\x0b\x61gentTraces\x18\x03 \x03(\x0b\x32\x14.protobuf.AgentTrace\x12*\n\x0bsystemTrace\x18\x04 \x01(\x0b\x32\x15.protobuf.SystemTrace\"u\n\nAgentTrace\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x61gentId\x18\x03 \x01(\t\x12\x1c\n\x04path\x18\x04 \x03(\x0b\x32\x0e.protobuf.Fire\x12,\n\x0flocalStatistics\x18\x05 \x03(\x0b\x32\x13.protobuf.Statistic\"\x94\x01\n\x0bSystemTrace\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\x05label\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x07\x61gentId\x18\x03 \x01(\t\x12\x1c\n\x04path\x18\x04 \x03(\x0b\x32\x0e.protobuf.Fire\x12,\n\x0flocalStatistics\x18\x05 \x03(\x0b\x32\x13.protobuf.StatisticB\x08\n\x06_label\"F\n\tStatistic\x12\r\n\x05label\x18\x01 \x01(\t\x12\t\n\x01\x63\x18\x02 \x01(\x05\x12\t\n\x01p\x18\x03 \x01(\x05\x12\t\n\x01m\x18\x04 \x01(\x05\x12\t\n\x01r\x18\x05 \x01(\x05\"D\n\x04\x46ire\x12\x13\n\x0bplaceIdFrom\x18\x01 \x01(\t\x12\x14\n\x0ctransitionId\x18\x02 \x01(\t\x12\x11\n\tplaceIdTo\x18\x03 \x01(\tB\x02P\x01\x62\x06proto3'
)




_RUN = _descriptor.Descriptor(
  name='Run',
  full_name='protobuf.Run',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protobuf.Run.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf.Run.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='net', full_name='protobuf.Run.net', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='traces', full_name='protobuf.Run.traces', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_name', full_name='protobuf.Run._name',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_id', full_name='protobuf.Run._id',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=23,
  serialized_end=141,
)


_NET = _descriptor.Descriptor(
  name='Net',
  full_name='protobuf.Net',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='netName', full_name='protobuf.Net.netName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemNet', full_name='protobuf.Net.systemNet', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agentTypes', full_name='protobuf.Net.agentTypes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_netName', full_name='protobuf.Net._netName',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=143,
  serialized_end=263,
)


_SYSTEMNET = _descriptor.Descriptor(
  name='SystemNet',
  full_name='protobuf.SystemNet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='places', full_name='protobuf.SystemNet.places', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startPlaceId', full_name='protobuf.SystemNet.startPlaceId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transitions', full_name='protobuf.SystemNet.transitions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arcs', full_name='protobuf.SystemNet.arcs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=410,
)


_AGENTTYPE = _descriptor.Descriptor(
  name='AgentType',
  full_name='protobuf.AgentType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='typeName', full_name='protobuf.AgentType.typeName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf.AgentType.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startPlaceId', full_name='protobuf.AgentType.startPlaceId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='places', full_name='protobuf.AgentType.places', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transitions', full_name='protobuf.AgentType.transitions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arcs', full_name='protobuf.AgentType.arcs', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=586,
)


_AGENTPLACE = _descriptor.Descriptor(
  name='AgentPlace',
  full_name='protobuf.AgentPlace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf.AgentPlace.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='protobuf.AgentPlace.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=627,
)


_SYSTEMPLACE = _descriptor.Descriptor(
  name='SystemPlace',
  full_name='protobuf.SystemPlace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf.SystemPlace.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='protobuf.SystemPlace.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agentTypeId', full_name='protobuf.SystemPlace.agentTypeId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=629,
  serialized_end=690,
)


_TRANSITION = _descriptor.Descriptor(
  name='Transition',
  full_name='protobuf.Transition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf.Transition.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='protobuf.Transition.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='activity', full_name='protobuf.Transition.activity', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sync', full_name='protobuf.Transition.sync', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_sync', full_name='protobuf.Transition._sync',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=692,
  serialized_end=777,
)


_ARC = _descriptor.Descriptor(
  name='Arc',
  full_name='protobuf.Arc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf.Arc.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='protobuf.Arc.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sourceId', full_name='protobuf.Arc.sourceId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetId', full_name='protobuf.Arc.targetId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_label', full_name='protobuf.Arc._label',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=779,
  serialized_end=862,
)


_TRACE = _descriptor.Descriptor(
  name='Trace',
  full_name='protobuf.Trace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf.Trace.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='protobuf.Trace.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agentTraces', full_name='protobuf.Trace.agentTraces', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='systemTrace', full_name='protobuf.Trace.systemTrace', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=864,
  serialized_end=985,
)


_AGENTTRACE = _descriptor.Descriptor(
  name='AgentTrace',
  full_name='protobuf.AgentTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf.AgentTrace.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agentId', full_name='protobuf.AgentTrace.agentId', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='protobuf.AgentTrace.path', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='localStatistics', full_name='protobuf.AgentTrace.localStatistics', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=987,
  serialized_end=1104,
)


_SYSTEMTRACE = _descriptor.Descriptor(
  name='SystemTrace',
  full_name='protobuf.SystemTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protobuf.SystemTrace.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='protobuf.SystemTrace.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agentId', full_name='protobuf.SystemTrace.agentId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='protobuf.SystemTrace.path', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='localStatistics', full_name='protobuf.SystemTrace.localStatistics', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_label', full_name='protobuf.SystemTrace._label',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1107,
  serialized_end=1255,
)


_STATISTIC = _descriptor.Descriptor(
  name='Statistic',
  full_name='protobuf.Statistic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='protobuf.Statistic.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c', full_name='protobuf.Statistic.c', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='p', full_name='protobuf.Statistic.p', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='m', full_name='protobuf.Statistic.m', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='r', full_name='protobuf.Statistic.r', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1257,
  serialized_end=1327,
)


_FIRE = _descriptor.Descriptor(
  name='Fire',
  full_name='protobuf.Fire',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='placeIdFrom', full_name='protobuf.Fire.placeIdFrom', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transitionId', full_name='protobuf.Fire.transitionId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='placeIdTo', full_name='protobuf.Fire.placeIdTo', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1329,
  serialized_end=1397,
)

_RUN.fields_by_name['net'].message_type = _NET
_RUN.fields_by_name['traces'].message_type = _TRACE
_RUN.oneofs_by_name['_name'].fields.append(
  _RUN.fields_by_name['name'])
_RUN.fields_by_name['name'].containing_oneof = _RUN.oneofs_by_name['_name']
_RUN.oneofs_by_name['_id'].fields.append(
  _RUN.fields_by_name['id'])
_RUN.fields_by_name['id'].containing_oneof = _RUN.oneofs_by_name['_id']
_NET.fields_by_name['systemNet'].message_type = _SYSTEMNET
_NET.fields_by_name['agentTypes'].message_type = _AGENTTYPE
_NET.oneofs_by_name['_netName'].fields.append(
  _NET.fields_by_name['netName'])
_NET.fields_by_name['netName'].containing_oneof = _NET.oneofs_by_name['_netName']
_SYSTEMNET.fields_by_name['places'].message_type = _SYSTEMPLACE
_SYSTEMNET.fields_by_name['transitions'].message_type = _TRANSITION
_SYSTEMNET.fields_by_name['arcs'].message_type = _ARC
_AGENTTYPE.fields_by_name['places'].message_type = _AGENTPLACE
_AGENTTYPE.fields_by_name['transitions'].message_type = _TRANSITION
_AGENTTYPE.fields_by_name['arcs'].message_type = _ARC
_TRANSITION.oneofs_by_name['_sync'].fields.append(
  _TRANSITION.fields_by_name['sync'])
_TRANSITION.fields_by_name['sync'].containing_oneof = _TRANSITION.oneofs_by_name['_sync']
_ARC.oneofs_by_name['_label'].fields.append(
  _ARC.fields_by_name['label'])
_ARC.fields_by_name['label'].containing_oneof = _ARC.oneofs_by_name['_label']
_TRACE.fields_by_name['agentTraces'].message_type = _AGENTTRACE
_TRACE.fields_by_name['systemTrace'].message_type = _SYSTEMTRACE
_AGENTTRACE.fields_by_name['path'].message_type = _FIRE
_AGENTTRACE.fields_by_name['localStatistics'].message_type = _STATISTIC
_SYSTEMTRACE.fields_by_name['path'].message_type = _FIRE
_SYSTEMTRACE.fields_by_name['localStatistics'].message_type = _STATISTIC
_SYSTEMTRACE.oneofs_by_name['_label'].fields.append(
  _SYSTEMTRACE.fields_by_name['label'])
_SYSTEMTRACE.fields_by_name['label'].containing_oneof = _SYSTEMTRACE.oneofs_by_name['_label']
DESCRIPTOR.message_types_by_name['Run'] = _RUN
DESCRIPTOR.message_types_by_name['Net'] = _NET
DESCRIPTOR.message_types_by_name['SystemNet'] = _SYSTEMNET
DESCRIPTOR.message_types_by_name['AgentType'] = _AGENTTYPE
DESCRIPTOR.message_types_by_name['AgentPlace'] = _AGENTPLACE
DESCRIPTOR.message_types_by_name['SystemPlace'] = _SYSTEMPLACE
DESCRIPTOR.message_types_by_name['Transition'] = _TRANSITION
DESCRIPTOR.message_types_by_name['Arc'] = _ARC
DESCRIPTOR.message_types_by_name['Trace'] = _TRACE
DESCRIPTOR.message_types_by_name['AgentTrace'] = _AGENTTRACE
DESCRIPTOR.message_types_by_name['SystemTrace'] = _SYSTEMTRACE
DESCRIPTOR.message_types_by_name['Statistic'] = _STATISTIC
DESCRIPTOR.message_types_by_name['Fire'] = _FIRE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Run = _reflection.GeneratedProtocolMessageType('Run', (_message.Message,), {
  'DESCRIPTOR' : _RUN,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Run)
  })
_sym_db.RegisterMessage(Run)

Net = _reflection.GeneratedProtocolMessageType('Net', (_message.Message,), {
  'DESCRIPTOR' : _NET,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Net)
  })
_sym_db.RegisterMessage(Net)

SystemNet = _reflection.GeneratedProtocolMessageType('SystemNet', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMNET,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.SystemNet)
  })
_sym_db.RegisterMessage(SystemNet)

AgentType = _reflection.GeneratedProtocolMessageType('AgentType', (_message.Message,), {
  'DESCRIPTOR' : _AGENTTYPE,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.AgentType)
  })
_sym_db.RegisterMessage(AgentType)

AgentPlace = _reflection.GeneratedProtocolMessageType('AgentPlace', (_message.Message,), {
  'DESCRIPTOR' : _AGENTPLACE,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.AgentPlace)
  })
_sym_db.RegisterMessage(AgentPlace)

SystemPlace = _reflection.GeneratedProtocolMessageType('SystemPlace', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMPLACE,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.SystemPlace)
  })
_sym_db.RegisterMessage(SystemPlace)

Transition = _reflection.GeneratedProtocolMessageType('Transition', (_message.Message,), {
  'DESCRIPTOR' : _TRANSITION,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Transition)
  })
_sym_db.RegisterMessage(Transition)

Arc = _reflection.GeneratedProtocolMessageType('Arc', (_message.Message,), {
  'DESCRIPTOR' : _ARC,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Arc)
  })
_sym_db.RegisterMessage(Arc)

Trace = _reflection.GeneratedProtocolMessageType('Trace', (_message.Message,), {
  'DESCRIPTOR' : _TRACE,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Trace)
  })
_sym_db.RegisterMessage(Trace)

AgentTrace = _reflection.GeneratedProtocolMessageType('AgentTrace', (_message.Message,), {
  'DESCRIPTOR' : _AGENTTRACE,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.AgentTrace)
  })
_sym_db.RegisterMessage(AgentTrace)

SystemTrace = _reflection.GeneratedProtocolMessageType('SystemTrace', (_message.Message,), {
  'DESCRIPTOR' : _SYSTEMTRACE,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.SystemTrace)
  })
_sym_db.RegisterMessage(SystemTrace)

Statistic = _reflection.GeneratedProtocolMessageType('Statistic', (_message.Message,), {
  'DESCRIPTOR' : _STATISTIC,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Statistic)
  })
_sym_db.RegisterMessage(Statistic)

Fire = _reflection.GeneratedProtocolMessageType('Fire', (_message.Message,), {
  'DESCRIPTOR' : _FIRE,
  '__module__' : 'run_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Fire)
  })
_sym_db.RegisterMessage(Fire)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
