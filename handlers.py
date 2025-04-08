import service_pb2
import service_pb2_grpc
import sqlite3
import database

DATABASE = "./database.db"

class PaymentService(service_pb2_grpc.PaymentServiceServicer):

    def GetPaymentData(self, request, context):

        conn = sqlite3.connect(DATABASE)

        data = database.get_all_payments(conn)

        conn.close()

        payments = []

        for row in data:
            payment = service_pb2.PaymentResponse(
                id=row[0],
                user_id=row[1],
                plan_id=row[2],
                method_id=row[3]
            )
            payments.append(payment)

        return service_pb2.PaymentListResponse(payment=payments)
    
    def GetPaymentDataById(self, request, context):

        conn = sqlite3.connect(DATABASE)

        payment_id = request.payment_id

        data = database.get_payment_by_id(conn, payment_id)

        return service_pb2.PaymentResponse(
            id=data[0],
            user_id=data[1],
            plan_id=data[2],
            method_id=data[3]
        )
    
    def UpdatePaymentData(self, request, context):

        conn = sqlite3.connect(DATABASE)

        id = request.id
        user_id = request.user_id
        plan_id = request.plan_id
        method_id = request.method_id

        data = database.update_payment_by_id(conn, id, user_id, plan_id, method_id)

        conn.close()

        return service_pb2.PaymentUpdateResponse(success=data)
    
    def CreatePaymentData(self, request, context):
        
        conn = sqlite3.connect(DATABASE)

        user_id = request.user_id
        plan_id = request.plan_id
        method_id = request.method_id

        id = database.create_payment(conn, user_id, plan_id, method_id)

        print(id)

        conn.close()

        return service_pb2.PaymentCreateResponse(id=id)

    def UpdatePaymentStudentId(self, request, context):

        conn = sqlite3.connect(DATABASE)

        student_id = request.student_id

        financial_id = request.financial_id

        status = database.update_student_id_by_financial_id(conn, student_id, financial_id)

        return service_pb2.PaymentUpdateResponse(success = status)
    
    def DeletePaymentById(self, request, context):

        conn = sqlite3.connect(DATABASE)

        payment_id = request.payment_id

        status = database.delete_payment_by_id(conn, payment_id)

        return service_pb2.PaymentUpdateResponse(success = status)

class PlanService(service_pb2_grpc.PlanServiceServicer):

    def GetPlanData(self, request, context):

        conn = sqlite3.connect(DATABASE)

        data = database.get_all_plans(conn)

        conn.close()

        plans = []

        for row in data:
            plan = service_pb2.PlanResponse(
                id=row[0],
                name=row[1],
                value=row[2]
            )
            plans.append(plan)

        return service_pb2.PlanListResponse(plan=plans)
    
    def GetPlanDataById(self, request, context):

        conn = sqlite3.connect(DATABASE)

        plan_id = request.plan_id

        data = database.get_plan_by_id(conn, plan_id)

        return service_pb2.PlanResponse(
            id=data[0],
            name=data[1],
            value=data[2]
        )

class MethodService(service_pb2_grpc.MethodServiceServicer):

    def GetMethodData(self, request, context):

        conn = sqlite3.connect(DATABASE)

        data = database.get_all_methods(conn)

        conn.close()

        methods = []

        for row in data:
            method = service_pb2.MethodResponse(
                id=row[0],
                name=row[1],
                discount=row[2]
            )
            methods.append(method)

        return service_pb2.MethodListResponse(method = methods)
    
    def GetMethodDataById(self, request, context):

        conn = sqlite3.connect(DATABASE)

        method_id = request.method_id

        data = database.get_method_by_id(conn, method_id)

        return service_pb2.MethodResponse(
            id=data[0],
            name=data[1],
            discount=data[2]
        )
    




