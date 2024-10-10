from multiprocessing import Process, Manager


class WarehouseManager:
    def __init__(self):
        man = Manager()
        self.data = man.dict()

    def run(self, request):
        p = [Process(target=self.process_request, args=a) for a in request]
        for a in p:
            a.start()
        for a in p:
            a.join()

    def process_request(self, *request):
        product_name, order, num = request
        if not isinstance(num, int) and num <= 0:
            raise Exception
        if order == 'receipt':
            if product_name in self.data:
                self.data[product_name] += num
            else:
                self.data[product_name] = num
        elif order == 'shipment':
            if product_name in self.data:
                self.data[product_name] -= num


if __name__ == '__main__':
    manager = WarehouseManager()
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    manager.run(requests)
    print(manager.data)
