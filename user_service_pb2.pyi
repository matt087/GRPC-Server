from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("email", "password", "name", "cursos", "admin")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURSOS_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    name: str
    cursos: _containers.RepeatedCompositeFieldContainer[Curso]
    admin: int
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ..., name: _Optional[str] = ..., cursos: _Optional[_Iterable[_Union[Curso, _Mapping]]] = ..., admin: _Optional[int] = ...) -> None: ...

class Curso(_message.Message):
    __slots__ = ("id", "nombre", "descripcion")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPCION_FIELD_NUMBER: _ClassVar[int]
    id: str
    nombre: str
    descripcion: str
    def __init__(self, id: _Optional[str] = ..., nombre: _Optional[str] = ..., descripcion: _Optional[str] = ...) -> None: ...

class RegisterRequest(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class EliminarMatriculaRequest(_message.Message):
    __slots__ = ("email", "course_id")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    course_id: str
    def __init__(self, email: _Optional[str] = ..., course_id: _Optional[str] = ...) -> None: ...

class EliminarMatriculaResponse(_message.Message):
    __slots__ = ("message", "success")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    message: str
    success: bool
    def __init__(self, message: _Optional[str] = ..., success: bool = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("success", "message", "content")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    content: User
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., content: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class EliminarUserRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class EliminarUserResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class ObtenerUserRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class ObtenerUserResponse(_message.Message):
    __slots__ = ("admin",)
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    admin: int
    def __init__(self, admin: _Optional[int] = ...) -> None: ...

class ObtenerUsersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ObtenerUsersResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...
