from __future__ import print_function
import grpc
import foobar_pb2
import foobar_pb2_grpc

def run():
    channel = grpc.insecure_channel('127.0.0.1:1699')
    stub = foobar_pb2_grpc.FoobarStub(channel)
    response = stub.SayHello(foobar_pb2.HelloRequest(name='you'))
    print("Client received: " + response.message)

    channel2 = grpc.insecure_channel('127.0.0.1:1698')
    stub = foobar_pb2_grpc.FoobarStub(channel2)
    response = stub.SayHello(foobar_pb2.HelloRequest(name='you'))
    print("Client received: " + response.message)

if __name__ == '__main__':
    run()