import grpc
import user_service_pb2
import user_service_pb2_grpc
import os
import sys

def distincionMenu(isadmin, user_stub, course_stub, em):
    if isadmin == 2:
        while True:
            print("\tMenú de Usuario")
            print("1) Matricularse a un Curso")
            print("2) Mis Cursos")
            print("3) Salir")
            while(True):
                opc = int(input("Seleccione una opción: "))
                if opc in [1,2,3]:
                    break
            if opc == 1:
                response = user_stub.ListCourses(user_service_pb2.ListCoursesRequest())
                os.system("cls")
                #os.system("clear")     #Linux
                print("\n\tLista de Cursos")
                for course in response.courses:
                    print(f"ID: {course.id}, Nombre: {course.nombre}, Descripción: {course.descripcion}")
            elif opc == 2:
                print("\tMis Cursos:")
                response = user_stub.ListUserCourses(user_service_pb2.ListUserCoursesRequest(email=em))
                if response.courses:
                    for curso in response.courses:
                        print("-" * 30)
                        print(f"ID          : {curso.id}")
                        print(f"Nombre      : {curso.nombre}")
                        print(f"Descripción : {curso.descripcion}")
                        print("-" * 30)
                else:
                    print("No estás matriculado en ningún curso.")
                input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
                os.system("cls")
                #os.system("clear")     #Linux
            elif opc == 3:
                os.system("cls")
                #os.system("clear")     #Linux
                break

        

    elif isadmin == 1:
        while True:
            print("\tMenú de Administrador")
            print("1) Ver Usuarios")
            print("2) Ver Cursos")
            print("3) Eliminar Usuarios")
            print("4) Registrar Cursos")
            print("5) Salir")
            while(True):
                opc = int(input("Seleccione una opción: "))
                if opc in [1,2,3,4,5]:
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
            if opc == 2:
                response = course_stub.ListCourses(user_service_pb2.ListCoursesRequest())
                os.system("cls")
                #os.system("clear")     #Linux
                print("\n\tLista de Cursos")
                for curso in response.courses:
                    print("-" * 30)
                    print(f"ID          : {curso.id}")
                    print(f"Nombre      : {curso.nombre}")
                    print(f"Descripción : {curso.descripcion}")
                    print("-" * 30)
                input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
                os.system("cls")
                #os.system("clear")     #Linux
            if opc == 4:
                os.system("cls")
                #os.system("clear")     #Linux
                print("\tRegistro de Cursos")
                curso_id = input("Ingrese el ID del curso: ")
                nombre = input("Ingrese el nombre del curso: ")
                descripcion = input("Ingrese la descripción del curso: ")

                curso = user_service_pb2.Curso(id=curso_id, nombre=nombre, descripcion=descripcion)
                request = user_service_pb2.CrearCursoRequest(curso=curso)

                response = course_stub.CrearCurso(request)
                
                if response.success:
                    print(response.message)
                else:
                    print("Error:", response.message)
                input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
                os.system("cls")
                #os.system("clear")     #Linux
            if opc == 5:
                os.system("cls")
                #os.system("clear")     #Linux
                break 




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
            distincionMenu(response.content.admin, user_stub, course_stub, em)
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
