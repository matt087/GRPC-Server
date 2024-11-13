import grpc
import user_service_pb2
import user_service_pb2_grpc
import course_service_pb2
import course_service_pb2_grpc
import os
import sys

#Credenciales de admin: admin@admin.com / 1234

def distincionMenu(isadmin, user_stub, course_stub, em):
    if isadmin == 2:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\tMenú de Usuario")
            print("1) Matricularse a un Curso")
            print("2) Mis Cursos")
            print("3) Eliminar Matrícula")
            print("4) Salir")
            while(True):
                opc = int(input("Seleccione una opción: "))
                if opc in [1,2,3,4]:
                    break
            if opc == 1:
                response = course_stub.ListCourses(course_service_pb2.ListCoursesRequest())
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n\tLista de Cursos")
                for course in response.courses:
                    print(f"ID: {course.id}, Nombre: {course.nombre}, Descripción: {course.descripcion}")
                response = course_stub.ListCourses(course_service_pb2.ListCoursesRequest())
                course_id = input("Ingrese el ID del curso al que desea matricularse: ")                
                matricula_response = course_stub.MatricularCurso(course_service_pb2.MatricularCursoRequest(email=em, course_id=course_id))
                print(matricula_response.message)
                input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
                os.system('cls' if os.name == 'nt' else 'clear')
            elif opc == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\tMis Cursos:")
                response = course_stub.ListUserCourses(course_service_pb2.ListUserCoursesRequest(email=em))
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
                os.system('cls' if os.name == 'nt' else 'clear')
            elif opc == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\tEliminación de Matrícula")
                course_id = input("Ingrese el ID del curso: ")
                request = user_service_pb2.EliminarMatriculaRequest(email=em, course_id=course_id)
                response = user_stub.EliminarMatricula(request)
                if response.success:
                    print("Matrícula eliminada exitosamente.")
                else:
                    print(f"Error: {response.message}")
                input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
                os.system('cls' if os.name == 'nt' else 'clear')
            elif opc == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
    elif isadmin == 1:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
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
                response = user_stub.ObtenerUsers(user_service_pb2.ObtenerUsersRequest())
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\tListado de Usuarios")
                for user in response.users:
                    print("-" * 30)
                    print(f"Email     : {user.email}")
                    print(f"Password  : {user.password}")
                    print(f"Nombre    : {user.name}")
                    print(f"Admin     : {'Sí' if user.admin == 1 else 'No'}")
                    if user.cursos:
                        cursos_nombres = [curso.nombre for curso in user.cursos]  
                        print(f"Cursos    : {', '.join(cursos_nombres)}")
                    else:
                        print(f"Cursos    : No inscrito")
                    
                    print("-" * 30)
                input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
                os.system('cls' if os.name == 'nt' else 'clear')
            if opc == 2:
                response = course_stub.ListCourses(course_service_pb2.ListCoursesRequest())
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n\tLista de Cursos")
                for curso in response.courses:
                    print("-" * 30)
                    print(f"ID          : {curso.id}")
                    print(f"Nombre      : {curso.nombre}")
                    print(f"Descripción : {curso.descripcion}")
                    print("-" * 30)
                input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
                os.system('cls' if os.name == 'nt' else 'clear')
            if opc == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                email = input("Ingrese el email del usuario a eliminar: ")
                request = user_service_pb2.EliminarUserRequest(email=email)
                response = user_stub.EliminarUser(request)
                if response.success:
                    print(response.message)
                else:
                    print(f"Error: {response.message}")
                input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
                os.system('cls' if os.name == 'nt' else 'clear')
            if opc == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\tRegistro de Cursos")
                curso_id = input("Ingrese el ID del curso: ")
                nombre = input("Ingrese el nombre del curso: ")
                descripcion = input("Ingrese la descripción del curso: ")

                curso = course_service_pb2.Curso(id=curso_id, nombre=nombre, descripcion=descripcion)
                request = course_service_pb2.CrearCursoRequest(curso=curso)

                response = course_stub.CrearCurso(request)
                
                if response.success:
                    print(response.message)
                else:
                    print("Error:", response.message)
                input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
                os.system('cls' if os.name == 'nt' else 'clear')
            if opc == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                break 




def run():
    channel = grpc.insecure_channel('localhost:50051')
    channel2 = grpc.insecure_channel('localhost:50052')
    user_stub = user_service_pb2_grpc.UserServiceStub(channel)
    course_stub = course_service_pb2_grpc.CourseServiceStub(channel2)

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
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\tInicio de Sesión")
            em = input("Ingrese su email: ")
            psw = input("Ingrese su contraseña: ")
            response = user_stub.Login(user_service_pb2.LoginRequest(email=em, password=psw))
            print(response.message)
            #print(response.content)
            input("PULSE CUALQUIER TECLA PARA CONTINUAR...")
            os.system('cls' if os.name == 'nt' else 'clear')
            distincionMenu(response.content.admin, user_stub, course_stub, em)
        elif opc == 2:
            #Register
            os.system('cls' if os.name == 'nt' else 'clear')
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
            os.system('cls' if os.name == 'nt' else 'clear')
        elif opc == 3:
            print("\n¡Gracias por usar la plataforma!")
            sys.exit(0)

if __name__ == '__main__':
    run()
