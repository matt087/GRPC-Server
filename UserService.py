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
    def create_table_cursos(self):
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS cursos (
            id TEXT PRIMARY KEY,
            nombre TEXT,
            descripcion TEXT
        )
        """)
        con.commit()
        con.close()

    def create_table_relation(self):
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS user_courses (
            user_email TEXT,
            curso_id TEXT,
            FOREIGN KEY (user_email) REFERENCES users(email),
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
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
        con.close()
        users = []

        for row in rows:
            cursos_inscritos = row[3].split(",") if row[3] else []
            users.append(user_service_pb2.User(
                email=row[0], password=row[1], name=row[2], cursos=cursos_inscritos, admin=row[4]
            ))
        return user_service_pb2.ObtenerUsersResponse(users=users)

    
    def EliminarUser(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("DELETE FROM users WHERE email = ?", (request.email,))
        con.commit()
        con.close()
        return user_service_pb2.EliminarUserResponse(success=True, message="Estudiante eliminado.")

    def Login(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()
        
        # Ejecuta la consulta para obtener los datos del usuario
        cur.execute("SELECT email, password, nombre, admin FROM users WHERE email = ? AND password = ?", 
                    (request.email, request.password))
        response = cur.fetchone()
        
        if response is None:
            con.close()
            return user_service_pb2.LoginResponse(success=False, message="Invalid credentials.", content=None)
        
        # Obtiene los cursos asociados con el usuario (suponiendo que tienes una tabla de relación)
        cur.execute("SELECT nombre FROM cursos WHERE id IN (SELECT curso_id FROM user_courses WHERE user_email = ?)", 
                    (response[0],))
        courses = [row[0] for row in cur.fetchall()]
        
        # Crea un objeto UserInfo con los datos del usuario y sus cursos
        user_info = user_service_pb2.User(
            email=response[0],
            password=response[1],  # Si necesitas devolver la contraseña, ten cuidado con la seguridad
            name=response[2],  # Aquí puedes usar 'nombre' si no tienes un campo 'username'
            cursos=courses,  # Esto será el arreglo de cursos
            admin=response[3]  # 1 si es admin, 0 si no lo es
        )

        con.close()
        return user_service_pb2.LoginResponse(success=True, message="Login successful.", content=user_info)

    
    ##CURSO
    def ObtenerCurso(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()
        cursos = []
        for row in cur.execute("SELECT * FROM cursos"):
            cursos.append(user_service_pb2.Curso(id=row[0], nombre=row[1], descripcion=row[2]))
        con.close()
        return user_service_pb2.ObtenerCursoResponse(cursos=cursos)
    
    def CrearCurso(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()    
        if not self.validarCurso(cur, request.curso.id):
            con.close()
            return user_service_pb2.CrearCursoResponse(success=False, message="Curso ya existe.")
        cur.execute("INSERT INTO cursos (id, nombre, descripcion) VALUES (?, ?, ?)",
                    (request.curso.id, request.curso.nombre, request.curso.descripcion))
        con.commit()
        con.close()
        return user_service_pb2.CrearCursoResponse(success=True, message="Curso registrado correctamente.")
    
    def ObtenerCursoID(self, request, context):
        #Para evitar que registren con la misma id
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("SELECT id FROM cursos")
        rows = cur.fetchall()
        con.close()
        
        ids = [row[0] for row in rows]
        return user_service_pb2.ObtenerCursoIDResponse(id=ids)
    
    def EliminarCurso(self, request, context):
        #Falta hacer
        return user_service_pb2.EliminarCursoResponse()

    def validarNick(self, cur, nick):
        nick_check = cur.execute("SELECT * FROM users WHERE email = ?", (nick,))
        return nick_check.fetchone() is None
    
    def validarCurso(self, cur, nick):
        nick_check = cur.execute("SELECT * FROM cursos WHERE id = ?", (nick,))
        return nick_check.fetchone() is None

def serve():
    user_service = UserService()
    user_service.create_table_users()
    user_service.create_table_cursos()
    user_service.create_table_relation()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(user_service, server)
    user_service_pb2_grpc.add_CourseServiceServicer_to_server(user_service, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
