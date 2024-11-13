from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Curso(_message.Message):
    __slots__ = ("id", "nombre", "descripcion")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPCION_FIELD_NUMBER: _ClassVar[int]
    id: str
    nombre: str
    descripcion: str
    def __init__(self, id: _Optional[str] = ..., nombre: _Optional[str] = ..., descripcion: _Optional[str] = ...) -> None: ...

class CrearCursoRequest(_message.Message):
    __slots__ = ("curso",)
    CURSO_FIELD_NUMBER: _ClassVar[int]
    curso: Curso
    def __init__(self, curso: _Optional[_Union[Curso, _Mapping]] = ...) -> None: ...

class CrearCursoResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class EliminarCursoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EliminarCursoResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class ObtenerCursoRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ObtenerCursoResponse(_message.Message):
    __slots__ = ("curso",)
    CURSO_FIELD_NUMBER: _ClassVar[int]
    curso: Curso
    def __init__(self, curso: _Optional[_Union[Curso, _Mapping]] = ...) -> None: ...

class ObtenerCursoIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class ObtenerCursoIDResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[_Iterable[str]] = ...) -> None: ...

class ListCoursesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCoursesResponse(_message.Message):
    __slots__ = ("courses",)
    COURSES_FIELD_NUMBER: _ClassVar[int]
    courses: _containers.RepeatedCompositeFieldContainer[Curso]
    def __init__(self, courses: _Optional[_Iterable[_Union[Curso, _Mapping]]] = ...) -> None: ...

class ListUserCoursesRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class ListUserCoursesResponse(_message.Message):
    __slots__ = ("courses",)
    COURSES_FIELD_NUMBER: _ClassVar[int]
    courses: _containers.RepeatedCompositeFieldContainer[Curso]
    def __init__(self, courses: _Optional[_Iterable[_Union[Curso, _Mapping]]] = ...) -> None: ...

class MatricularCursoRequest(_message.Message):
    __slots__ = ("email", "course_id")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    course_id: str
    def __init__(self, email: _Optional[str] = ..., course_id: _Optional[str] = ...) -> None: ...

class MatricularCursoResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...
