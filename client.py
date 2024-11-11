import grpc
import user_service_pb2
import user_service_pb2_grpc
import os
import sys

def distincionMenu(isadmin, user_stub, course_stub):
    if isadmin == 2:
        print("\tMenú de Usuario")
        print("1) Matricularse a un Curso")
        print("2) Mis Cursos")
        print("3) Salir")
        while(True):
            opc = int(input("Seleccione una opción: "))
            if opc in [1,2,3,4]:
                break
        if opc == 1:
            response = user_stub.ListCourses(user_service_pb2.ListCoursesRequest())
            for course in response.courses:
                print(f"Course ID: {course.id}, Name: {course.nombre}, Description: {course.descripcion}")
        
        

    elif isadmin == 1:
        print("\tMenú de Administrador")
        print("1) Ver Usuarios")
        print("2) Eliminar Usuarios")
        print("3) Registrar Cursos")
        print("4) Salir")
        while(True):
            opc = int(input("Seleccione una opción: "))
            if opc in [1,2,3,4]:
                break
        if opc == 1:
            #Ver
            request = user_service_pb2.ObtenerUsersRequest(email="")
            response = user_stub.ObtenerUsers(request)
            os.system("cls")
            #os.system("clear")     #Linux
            print("\tListado de Usuarios")
            for user in response.users:
                print("-" * 30)
                print(f"Email     : {user.email}")
                print(f"Password  : {user.password}")
                print(f"Nombre    : {user.name}")
                print(f"Admin     : {'Sí' if user.admin == 1 else 'No'}")
                print(f"Cursos    : {', '.join(user.cursos) if user.cursos else 'No inscrito'}")
                print("-" * 30)
            input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
            os.system("cls")
            #os.system("clear")     #Linux



def run():
    channel = grpc.insecure_channel('localhost:50051')
    user_stub = user_service_pb2_grpc.UserServiceStub(channel)
    course_stub = user_service_pb2_grpc.CourseServiceStub(channel)

    while True:
        print("\tMenú")
        print("1) Iniciar Sesión")
        print("2) Registrarse")
        print("3) Salir")
        while(True):
            opc = int(input("Seleccione una opción: "))
            if opc in [1,2,3]:
                break
        if opc == 1:
            #Login
            os.system("cls")
            #os.system("clear")     #Linux
            print("\tInicio de Sesión")
            em = input("Ingrese su email: ")
            psw = input("Ingrese su contraseña: ")
            response = user_stub.Login(user_service_pb2.LoginRequest(email=em, password=psw))
            print(response.message)
            #print(response.content)
            input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
            os.system("cls")
            #os.system("clear")     #Linux
            distincionMenu(response.content.admin, user_stub, course_stub)
        elif opc == 2:
            #Register
            os.system("cls")
            #os.system("clear")     #Linux
            print("\tRegistro de Usuario")
            em = input("Ingrese su email: ")
            psw = input("Ingrese su contraseña: ")
            name = input("Ingrese su Nombre: ")
            user = user_service_pb2.User(
                email=em,
                password=psw,
                name=name,
                cursos=[],
                admin=2
            )
            response = user_stub.Register(user_service_pb2.RegisterRequest(user=user))
            print(response.message)
            input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
            os.system("cls")
            #os.system("clear")     #Linux
        elif opc == 3:
            print("\n¡Gracias por usar la plataforma!")
            sys.exit(0)
   
    #Register curso
    curso = user_service_pb2.Curso(
        id="curso_123",
        nombre="Curso de ejemplo",
        descripcion="Descripción del curso"
    )
    request = user_service_pb2.CrearCursoRequest(curso=curso)

    response = course_stub.CrearCurso(request)
    print("Respuesta:", response.message)

if __name__ == '__main__':
    run()
