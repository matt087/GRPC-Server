import grpc
from concurrent import futures
import course_service_pb2
import course_service_pb2_grpc
import sqlite3

class CourseService(course_service_pb2_grpc.CourseServiceServicer):
    def create_db_connection(self):
        con = sqlite3.connect("server_user.db", check_same_thread=False)
        return con
    
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

    def ObtenerCurso(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()
        cursos = []
        for row in cur.execute("SELECT * FROM cursos"):
            cursos.append(course_service_pb2.Curso(id=row[0], nombre=row[1], descripcion=row[2]))
        con.close()
        return course_service_pb2.ObtenerCursoResponse(cursos=cursos)

    
    def ListCourses(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("SELECT id, nombre, descripcion FROM cursos")
        rows = cur.fetchall()
        con.close()

        courses = []
        for row in rows:
            courses.append(course_service_pb2.Curso(id=row[0], nombre=row[1], descripcion=row[2]))
        return course_service_pb2.ListCoursesResponse(courses=courses)
    
    def CrearCurso(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()    
        if not self.validarCurso(cur, request.curso.id):
            con.close()
            return course_service_pb2.CrearCursoResponse(success=False, message="Curso ya existe.")
        cur.execute("INSERT INTO cursos (id, nombre, descripcion) VALUES (?, ?, ?)",
                    (request.curso.id, request.curso.nombre, request.curso.descripcion))
        con.commit()
        con.close()
        return course_service_pb2.CrearCursoResponse(success=True, message="Curso registrado correctamente.")
    
    def ObtenerCursoID(self, request, context):
        #Para evitar que registren con la misma id
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("SELECT id FROM cursos")
        rows = cur.fetchall()
        con.close()
        
        ids = [row[0] for row in rows]
        return course_service_pb2.ObtenerCursoIDResponse(id=ids)
    
    def validarCurso(self, cur, nick):
        nick_check = cur.execute("SELECT * FROM cursos WHERE id = ?", (nick,))
        return nick_check.fetchone() is None
    
    def ListUserCourses(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("SELECT cursos FROM users WHERE email = ?", (request.email,))
        rows = cur.fetchone()
        
        if rows and rows[0]:
            elementos = rows[0].split(',')
            user_courses = []
            for i in elementos:
                cur.execute("SELECT * FROM cursos WHERE id = ?", (i,))
                res = cur.fetchone()
                if res:
                    user_courses.append(course_service_pb2.Curso(id=res[0], nombre=res[1], descripcion=res[2]))
        else:
            user_courses = []
        con.close()
        return course_service_pb2.ListUserCoursesResponse(courses=user_courses)

    def MatricularCurso(self, request, context):
        con = self.create_db_connection()
        cur = con.cursor()
        cur.execute("SELECT cursos FROM users WHERE email = ?", (request.email,))
        row = cur.fetchone()
        if row:
            cursos_inscritos = row[0].split(",") if row[0] else []
            if request.course_id in cursos_inscritos:
                con.close()
                return course_service_pb2.MatricularCursoResponse(success=False, message="Ya estás matriculado en este curso.")
            
            cursos_inscritos.append(request.course_id)
            nuevos_cursos = ",".join(cursos_inscritos)
            
            try:
                cur.execute("UPDATE users SET cursos = ? WHERE email = ?", (nuevos_cursos, request.email))
                con.commit()
                con.close()
                return course_service_pb2.MatricularCursoResponse(success=True, message="Curso matriculado exitosamente.")
            except Exception as e:
                con.close()
                return course_service_pb2.MatricularCursoResponse(success=False, message=f"Error al matricular curso: {str(e)}")
            
def serve():
    course_service = CourseService()
    course_service.create_table_cursos()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(course_service, server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Server started on port 50052...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()