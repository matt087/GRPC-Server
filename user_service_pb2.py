# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'user_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12user_service.proto\x12\x0cuser_service\"i\n\x04User\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12#\n\x06\x63ursos\x18\x04 \x03(\x0b\x32\x13.user_service.Curso\x12\r\n\x05\x61\x64min\x18\x05 \x01(\x05\"3\n\x0fRegisterRequest\x12 \n\x04user\x18\x01 \x01(\x0b\x32\x12.user_service.User\"<\n\x18\x45liminarMatriculaRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x11\n\tcourse_id\x18\x02 \x01(\t\"=\n\x19\x45liminarMatriculaResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"4\n\x10RegisterResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"/\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"V\n\rLoginResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12#\n\x07\x63ontent\x18\x03 \x01(\x0b\x32\x12.user_service.User\"$\n\x13\x45liminarUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"8\n\x14\x45liminarUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"#\n\x12ObtenerUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"$\n\x13ObtenerUserResponse\x12\r\n\x05\x61\x64min\x18\x01 \x01(\x05\"\x15\n\x13ObtenerUsersRequest\"9\n\x14ObtenerUsersResponse\x12!\n\x05users\x18\x01 \x03(\x0b\x32\x12.user_service.User\"8\n\x05\x43urso\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06nombre\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scripcion\x18\x03 \x01(\t\"7\n\x11\x43rearCursoRequest\x12\"\n\x05\x63urso\x18\x01 \x01(\x0b\x32\x13.user_service.Curso\"6\n\x12\x43rearCursoResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\"\n\x14\x45liminarCursoRequest\x12\n\n\x02id\x18\x01 \x01(\t\"9\n\x15\x45liminarCursoResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x15\n\x13ObtenerCursoRequest\":\n\x14ObtenerCursoResponse\x12\"\n\x05\x63urso\x18\x01 \x01(\x0b\x32\x13.user_service.Curso\"$\n\x16ObtenerCursoIDResponse\x12\n\n\x02id\x18\x01 \x03(\t\"\x14\n\x12ListCoursesRequest\";\n\x13ListCoursesResponse\x12$\n\x07\x63ourses\x18\x01 \x03(\x0b\x32\x13.user_service.Curso\"\'\n\x16ListUserCoursesRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"?\n\x17ListUserCoursesResponse\x12$\n\x07\x63ourses\x18\x01 \x03(\x0b\x32\x13.user_service.Curso\":\n\x16MatricularCursoRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x11\n\tcourse_id\x18\x02 \x01(\t\";\n\x17MatricularCursoResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xc6\x03\n\rCourseService\x12O\n\nCrearCurso\x12\x1f.user_service.CrearCursoRequest\x1a .user_service.CrearCursoResponse\x12U\n\x0cObtenerCurso\x12!.user_service.ObtenerCursoRequest\x1a\".user_service.ObtenerCursoResponse\x12Y\n\x0eObtenerCursoID\x12!.user_service.ObtenerCursoRequest\x1a$.user_service.ObtenerCursoIDResponse\x12R\n\x0bListCourses\x12 .user_service.ListCoursesRequest\x1a!.user_service.ListCoursesResponse\x12^\n\x0fMatricularCurso\x12$.user_service.MatricularCursoRequest\x1a%.user_service.MatricularCursoResponse2\x8f\x06\n\x0bUserService\x12I\n\x08Register\x12\x1d.user_service.RegisterRequest\x1a\x1e.user_service.RegisterResponse\x12@\n\x05Login\x12\x1a.user_service.LoginRequest\x1a\x1b.user_service.LoginResponse\x12U\n\x0c\x45liminarUser\x12!.user_service.EliminarUserRequest\x1a\".user_service.EliminarUserResponse\x12R\n\x0bObtenerUser\x12 .user_service.ObtenerUserRequest\x1a!.user_service.ObtenerUserResponse\x12T\n\x0cObtenerUsers\x12 .user_service.ObtenerUserRequest\x1a\".user_service.ObtenerUsersResponse\x12R\n\x0bListCourses\x12 .user_service.ListCoursesRequest\x1a!.user_service.ListCoursesResponse\x12^\n\x0fListUserCourses\x12$.user_service.ListUserCoursesRequest\x1a%.user_service.ListUserCoursesResponse\x12\x64\n\x11\x45liminarMatricula\x12&.user_service.EliminarMatriculaRequest\x1a\'.user_service.EliminarMatriculaResponse\x12X\n\rEliminarCurso\x12\".user_service.EliminarCursoRequest\x1a#.user_service.EliminarCursoResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USER']._serialized_start=36
  _globals['_USER']._serialized_end=141
  _globals['_REGISTERREQUEST']._serialized_start=143
  _globals['_REGISTERREQUEST']._serialized_end=194
  _globals['_ELIMINARMATRICULAREQUEST']._serialized_start=196
  _globals['_ELIMINARMATRICULAREQUEST']._serialized_end=256
  _globals['_ELIMINARMATRICULARESPONSE']._serialized_start=258
  _globals['_ELIMINARMATRICULARESPONSE']._serialized_end=319
  _globals['_REGISTERRESPONSE']._serialized_start=321
  _globals['_REGISTERRESPONSE']._serialized_end=373
  _globals['_LOGINREQUEST']._serialized_start=375
  _globals['_LOGINREQUEST']._serialized_end=422
  _globals['_LOGINRESPONSE']._serialized_start=424
  _globals['_LOGINRESPONSE']._serialized_end=510
  _globals['_ELIMINARUSERREQUEST']._serialized_start=512
  _globals['_ELIMINARUSERREQUEST']._serialized_end=548
  _globals['_ELIMINARUSERRESPONSE']._serialized_start=550
  _globals['_ELIMINARUSERRESPONSE']._serialized_end=606
  _globals['_OBTENERUSERREQUEST']._serialized_start=608
  _globals['_OBTENERUSERREQUEST']._serialized_end=643
  _globals['_OBTENERUSERRESPONSE']._serialized_start=645
  _globals['_OBTENERUSERRESPONSE']._serialized_end=681
  _globals['_OBTENERUSERSREQUEST']._serialized_start=683
  _globals['_OBTENERUSERSREQUEST']._serialized_end=704
  _globals['_OBTENERUSERSRESPONSE']._serialized_start=706
  _globals['_OBTENERUSERSRESPONSE']._serialized_end=763
  _globals['_CURSO']._serialized_start=765
  _globals['_CURSO']._serialized_end=821
  _globals['_CREARCURSOREQUEST']._serialized_start=823
  _globals['_CREARCURSOREQUEST']._serialized_end=878
  _globals['_CREARCURSORESPONSE']._serialized_start=880
  _globals['_CREARCURSORESPONSE']._serialized_end=934
  _globals['_ELIMINARCURSOREQUEST']._serialized_start=936
  _globals['_ELIMINARCURSOREQUEST']._serialized_end=970
  _globals['_ELIMINARCURSORESPONSE']._serialized_start=972
  _globals['_ELIMINARCURSORESPONSE']._serialized_end=1029
  _globals['_OBTENERCURSOREQUEST']._serialized_start=1031
  _globals['_OBTENERCURSOREQUEST']._serialized_end=1052
  _globals['_OBTENERCURSORESPONSE']._serialized_start=1054
  _globals['_OBTENERCURSORESPONSE']._serialized_end=1112
  _globals['_OBTENERCURSOIDRESPONSE']._serialized_start=1114
  _globals['_OBTENERCURSOIDRESPONSE']._serialized_end=1150
  _globals['_LISTCOURSESREQUEST']._serialized_start=1152
  _globals['_LISTCOURSESREQUEST']._serialized_end=1172
  _globals['_LISTCOURSESRESPONSE']._serialized_start=1174
  _globals['_LISTCOURSESRESPONSE']._serialized_end=1233
  _globals['_LISTUSERCOURSESREQUEST']._serialized_start=1235
  _globals['_LISTUSERCOURSESREQUEST']._serialized_end=1274
  _globals['_LISTUSERCOURSESRESPONSE']._serialized_start=1276
  _globals['_LISTUSERCOURSESRESPONSE']._serialized_end=1339
  _globals['_MATRICULARCURSOREQUEST']._serialized_start=1341
  _globals['_MATRICULARCURSOREQUEST']._serialized_end=1399
  _globals['_MATRICULARCURSORESPONSE']._serialized_start=1401
  _globals['_MATRICULARCURSORESPONSE']._serialized_end=1460
  _globals['_COURSESERVICE']._serialized_start=1463
  _globals['_COURSESERVICE']._serialized_end=1917
  _globals['_USERSERVICE']._serialized_start=1920
  _globals['_USERSERVICE']._serialized_end=2703
# @@protoc_insertion_point(module_scope)
