from concurrent import futures

import grpc
import foobar_pb2
import foobar_pb2_grpc

class Listener(foobar_pb2_grpc.FoobarServicer):
    def SayHello(self, request, context):
        return foobar_pb2.HelloReply(message='Foo, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    foobar_pb2_grpc.add_FoobarServicer_to_server(Listener(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    print("Server Running")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()