import grpc
import service_pb2_grpc
from concurrent import futures
from handlers import *

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))  
    service_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)
    service_pb2_grpc.add_PlanServiceServicer_to_server(PlanService(),server)
    service_pb2_grpc.add_MethodServiceServicer_to_server(MethodService(),server)
    server.add_insecure_port('[::]:50052')  
    print("Servidor gRPC rodando na porta 50052...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
