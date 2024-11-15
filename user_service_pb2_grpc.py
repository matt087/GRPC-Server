# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import user_service_pb2 as user__service__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in user_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/user_service.UserService/Register',
                request_serializer=user__service__pb2.RegisterRequest.SerializeToString,
                response_deserializer=user__service__pb2.RegisterResponse.FromString,
                _registered_method=True)
        self.Login = channel.unary_unary(
                '/user_service.UserService/Login',
                request_serializer=user__service__pb2.LoginRequest.SerializeToString,
                response_deserializer=user__service__pb2.LoginResponse.FromString,
                _registered_method=True)
        self.EliminarUser = channel.unary_unary(
                '/user_service.UserService/EliminarUser',
                request_serializer=user__service__pb2.EliminarUserRequest.SerializeToString,
                response_deserializer=user__service__pb2.EliminarUserResponse.FromString,
                _registered_method=True)
        self.ObtenerUser = channel.unary_unary(
                '/user_service.UserService/ObtenerUser',
                request_serializer=user__service__pb2.ObtenerUserRequest.SerializeToString,
                response_deserializer=user__service__pb2.ObtenerUserResponse.FromString,
                _registered_method=True)
        self.ObtenerUsers = channel.unary_unary(
                '/user_service.UserService/ObtenerUsers',
                request_serializer=user__service__pb2.ObtenerUserRequest.SerializeToString,
                response_deserializer=user__service__pb2.ObtenerUsersResponse.FromString,
                _registered_method=True)
        self.EliminarMatricula = channel.unary_unary(
                '/user_service.UserService/EliminarMatricula',
                request_serializer=user__service__pb2.EliminarMatriculaRequest.SerializeToString,
                response_deserializer=user__service__pb2.EliminarMatriculaResponse.FromString,
                _registered_method=True)


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EliminarUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ObtenerUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ObtenerUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EliminarMatricula(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=user__service__pb2.RegisterRequest.FromString,
                    response_serializer=user__service__pb2.RegisterResponse.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=user__service__pb2.LoginRequest.FromString,
                    response_serializer=user__service__pb2.LoginResponse.SerializeToString,
            ),
            'EliminarUser': grpc.unary_unary_rpc_method_handler(
                    servicer.EliminarUser,
                    request_deserializer=user__service__pb2.EliminarUserRequest.FromString,
                    response_serializer=user__service__pb2.EliminarUserResponse.SerializeToString,
            ),
            'ObtenerUser': grpc.unary_unary_rpc_method_handler(
                    servicer.ObtenerUser,
                    request_deserializer=user__service__pb2.ObtenerUserRequest.FromString,
                    response_serializer=user__service__pb2.ObtenerUserResponse.SerializeToString,
            ),
            'ObtenerUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.ObtenerUsers,
                    request_deserializer=user__service__pb2.ObtenerUserRequest.FromString,
                    response_serializer=user__service__pb2.ObtenerUsersResponse.SerializeToString,
            ),
            'EliminarMatricula': grpc.unary_unary_rpc_method_handler(
                    servicer.EliminarMatricula,
                    request_deserializer=user__service__pb2.EliminarMatriculaRequest.FromString,
                    response_serializer=user__service__pb2.EliminarMatriculaResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user_service.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('user_service.UserService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user_service.UserService/Register',
            user__service__pb2.RegisterRequest.SerializeToString,
            user__service__pb2.RegisterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user_service.UserService/Login',
            user__service__pb2.LoginRequest.SerializeToString,
            user__service__pb2.LoginResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EliminarUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user_service.UserService/EliminarUser',
            user__service__pb2.EliminarUserRequest.SerializeToString,
            user__service__pb2.EliminarUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ObtenerUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user_service.UserService/ObtenerUser',
            user__service__pb2.ObtenerUserRequest.SerializeToString,
            user__service__pb2.ObtenerUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ObtenerUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user_service.UserService/ObtenerUsers',
            user__service__pb2.ObtenerUserRequest.SerializeToString,
            user__service__pb2.ObtenerUsersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EliminarMatricula(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/user_service.UserService/EliminarMatricula',
            user__service__pb2.EliminarMatriculaRequest.SerializeToString,
            user__service__pb2.EliminarMatriculaResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
