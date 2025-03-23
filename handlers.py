import service_pb2
import service_pb2_grpc
import sqlite3
import database

DATABASE = "./database.db"

class PaymentService(service_pb2_grpc.PaymentServiceServicer):

    def GetPaymentData(self, request, context):
        return super().GetPaymentData(request, context)

class PlanService(service_pb2_grpc.PlanServiceServicer):
    def GetPlanData(self, request, context):
        return super().GetPlanData(request, context)


