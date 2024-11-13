# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import course_service_pb2 as course__service__pb2

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
        + f' but the generated code in course_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CourseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CrearCurso = channel.unary_unary(
                '/course_service.CourseService/CrearCurso',
                request_serializer=course__service__pb2.CrearCursoRequest.SerializeToString,
                response_deserializer=course__service__pb2.CrearCursoResponse.FromString,
                _registered_method=True)
        self.ObtenerCurso = channel.unary_unary(
                '/course_service.CourseService/ObtenerCurso',
                request_serializer=course__service__pb2.ObtenerCursoRequest.SerializeToString,
                response_deserializer=course__service__pb2.ObtenerCursoResponse.FromString,
                _registered_method=True)
        self.ObtenerCursoID = channel.unary_unary(
                '/course_service.CourseService/ObtenerCursoID',
                request_serializer=course__service__pb2.ObtenerCursoRequest.SerializeToString,
                response_deserializer=course__service__pb2.ObtenerCursoIDResponse.FromString,
                _registered_method=True)
        self.ListCourses = channel.unary_unary(
                '/course_service.CourseService/ListCourses',
                request_serializer=course__service__pb2.ListCoursesRequest.SerializeToString,
                response_deserializer=course__service__pb2.ListCoursesResponse.FromString,
                _registered_method=True)
        self.ListUserCourses = channel.unary_unary(
                '/course_service.CourseService/ListUserCourses',
                request_serializer=course__service__pb2.ListUserCoursesRequest.SerializeToString,
                response_deserializer=course__service__pb2.ListUserCoursesResponse.FromString,
                _registered_method=True)
        self.MatricularCurso = channel.unary_unary(
                '/course_service.CourseService/MatricularCurso',
                request_serializer=course__service__pb2.MatricularCursoRequest.SerializeToString,
                response_deserializer=course__service__pb2.MatricularCursoResponse.FromString,
                _registered_method=True)
        self.EliminarCurso = channel.unary_unary(
                '/course_service.CourseService/EliminarCurso',
                request_serializer=course__service__pb2.EliminarCursoRequest.SerializeToString,
                response_deserializer=course__service__pb2.EliminarCursoResponse.FromString,
                _registered_method=True)


class CourseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CrearCurso(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ObtenerCurso(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ObtenerCursoID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCourses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUserCourses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MatricularCurso(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EliminarCurso(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CourseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CrearCurso': grpc.unary_unary_rpc_method_handler(
                    servicer.CrearCurso,
                    request_deserializer=course__service__pb2.CrearCursoRequest.FromString,
                    response_serializer=course__service__pb2.CrearCursoResponse.SerializeToString,
            ),
            'ObtenerCurso': grpc.unary_unary_rpc_method_handler(
                    servicer.ObtenerCurso,
                    request_deserializer=course__service__pb2.ObtenerCursoRequest.FromString,
                    response_serializer=course__service__pb2.ObtenerCursoResponse.SerializeToString,
            ),
            'ObtenerCursoID': grpc.unary_unary_rpc_method_handler(
                    servicer.ObtenerCursoID,
                    request_deserializer=course__service__pb2.ObtenerCursoRequest.FromString,
                    response_serializer=course__service__pb2.ObtenerCursoIDResponse.SerializeToString,
            ),
            'ListCourses': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCourses,
                    request_deserializer=course__service__pb2.ListCoursesRequest.FromString,
                    response_serializer=course__service__pb2.ListCoursesResponse.SerializeToString,
            ),
            'ListUserCourses': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUserCourses,
                    request_deserializer=course__service__pb2.ListUserCoursesRequest.FromString,
                    response_serializer=course__service__pb2.ListUserCoursesResponse.SerializeToString,
            ),
            'MatricularCurso': grpc.unary_unary_rpc_method_handler(
                    servicer.MatricularCurso,
                    request_deserializer=course__service__pb2.MatricularCursoRequest.FromString,
                    response_serializer=course__service__pb2.MatricularCursoResponse.SerializeToString,
            ),
            'EliminarCurso': grpc.unary_unary_rpc_method_handler(
                    servicer.EliminarCurso,
                    request_deserializer=course__service__pb2.EliminarCursoRequest.FromString,
                    response_serializer=course__service__pb2.EliminarCursoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'course_service.CourseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('course_service.CourseService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CourseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CrearCurso(request,
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
            '/course_service.CourseService/CrearCurso',
            course__service__pb2.CrearCursoRequest.SerializeToString,
            course__service__pb2.CrearCursoResponse.FromString,
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
    def ObtenerCurso(request,
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
            '/course_service.CourseService/ObtenerCurso',
            course__service__pb2.ObtenerCursoRequest.SerializeToString,
            course__service__pb2.ObtenerCursoResponse.FromString,
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
    def ObtenerCursoID(request,
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
            '/course_service.CourseService/ObtenerCursoID',
            course__service__pb2.ObtenerCursoRequest.SerializeToString,
            course__service__pb2.ObtenerCursoIDResponse.FromString,
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
    def ListCourses(request,
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
            '/course_service.CourseService/ListCourses',
            course__service__pb2.ListCoursesRequest.SerializeToString,
            course__service__pb2.ListCoursesResponse.FromString,
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
    def ListUserCourses(request,
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
            '/course_service.CourseService/ListUserCourses',
            course__service__pb2.ListUserCoursesRequest.SerializeToString,
            course__service__pb2.ListUserCoursesResponse.FromString,
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
    def MatricularCurso(request,
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
            '/course_service.CourseService/MatricularCurso',
            course__service__pb2.MatricularCursoRequest.SerializeToString,
            course__service__pb2.MatricularCursoResponse.FromString,
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
    def EliminarCurso(request,
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
            '/course_service.CourseService/EliminarCurso',
            course__service__pb2.EliminarCursoRequest.SerializeToString,
            course__service__pb2.EliminarCursoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
