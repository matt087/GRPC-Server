import grpc
from concurrent import futures
import user_service_pb2
import user_service_pb2_grpc
import sqlite3

class UserService(user_service_pb2_grpc.UserServiceServicer):
    def create_db_connection(self):
        con = sqlite3.connect("server_user.db", check_same_thread=False)
        return con

    def create_table_users(self):
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            password TEXT,
            nombre TEXT,
            cursos TEXT, 
            admin INTEGER
        )
        """)
        con.commit()
        con.close()

    def Register(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()

        if not self.validarNick(cur, request.user.email):
            con.close()
            return user_service_pb2.RegisterResponse(success=False, message="Email ya registrado")

        cursos_inscritos = ",".join(request.user.cursos)
        cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (request.user.email, request.user.password,
                                                                 request.user.name, cursos_inscritos, request.user.admin))
        con.commit()
        con.close()
        return user_service_pb2.RegisterResponse(success=True, message="Usuario registrado correctamente.")
    
    def Admin(self, request, context):
        #Para diferenciar entre admin 1 y user 2
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("Select * FROM users WHERE id = ",(request.id))
        row = cur.fetchone()
        con.close()
        if row:
            return user_service_pb2.ObtenerUserResponse(id=row[0])
        return user_service_pb2.ObtenerUserResponse()
    
    def ObtenerUsers(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall() 

        users = []

        for row in rows:
            cursos_inscritos = row[3].split(",") if row[3] else []
            cursos_detalle = []
            for curso_id in cursos_inscritos:
                cur.execute("SELECT id, nombre, descripcion FROM cursos WHERE id = ?", (curso_id,))
                curso_row = cur.fetchone()
                if curso_row:
                    curso = user_service_pb2.Curso(
                        id=curso_row[0],
                        nombre=curso_row[1],
                        descripcion=curso_row[2]
                    )
                    cursos_detalle.append(curso)

            users.append(user_service_pb2.User(
                email=row[0],
                password=row[1],
                name=row[2],
                cursos=cursos_detalle,  
                admin=row[4]
            ))
        con.close()

        return user_service_pb2.ObtenerUsersResponse(users=users)
    
    def EliminarUser(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE email = ?", (request.email,))
        if cur.fetchone() is None:
            con.close()
            return user_service_pb2.EliminarUserResponse(message="Usuario no encontrado.", success=False)
        cur.execute("DELETE FROM users WHERE email = ?", (request.email,))
        con.commit()
        con.close()
        return user_service_pb2.EliminarUserResponse(
            message="Usuario eliminado exitosamente.", success=True)

    def Login(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()
        
        cur.execute("SELECT email, password, nombre, admin FROM users WHERE email = ? AND password = ?", 
                    (request.email, request.password))
        response = cur.fetchone()
        
        if response is None:
            con.close()
            return user_service_pb2.LoginResponse(success=False, message="Credenciales Inválidas", content=None)
        
        cur.execute("SELECT nombre FROM cursos WHERE id IN (SELECT curso_id FROM user_courses WHERE user_email = ?)", 
                    (response[0],))
        courses = [row[0] for row in cur.fetchall()]
        
        user_info = user_service_pb2.User(
            email=response[0],
            password=response[1],  
            name=response[2], 
            cursos=courses, 
            admin=response[3]  # 1 si es admin, 2 si no lo es
        )

        con.close()
        return user_service_pb2.LoginResponse(success=True, message="Login successful.", content=user_info)

    def EliminarMatricula(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("SELECT cursos FROM users WHERE email = ?", (request.email,))
        row = cur.fetchone()
        cursos = row[0]
        if not cursos:
            con.close()
            return user_service_pb2.EliminarMatriculaResponse(message="El usuario no está inscrito en ningún curso.", success=False)
        cursos_lista = cursos.split(",")
        if str(request.course_id) not in cursos_lista:
            con.close()
            return user_service_pb2.EliminarMatriculaResponse(message="El usuario no está matriculado en este curso.", success=False)
        cursos_lista.remove(str(request.course_id))
        cursos_actualizados = ",".join(cursos_lista)
        cur.execute("UPDATE users SET cursos = ? WHERE email = ?", (cursos_actualizados, request.email))
        con.commit()
        con.close()
        return user_service_pb2.EliminarMatriculaResponse(message="Matrícula eliminada exitosamente.", success=True)

    def validarNick(self, cur, nick):
        nick_check = cur.execute("SELECT * FROM users WHERE email = ?", (nick,))
        return nick_check.fetchone() is None


def serve():
    user_service = UserService()
    user_service.create_table_users()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(user_service, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
