


# class Observable:

#     def __init__(self):
#         self.__observers = []

#     def notify(self, object: object):
#         for observer in self.__observers:
#             observer.notify(object)


#     def add_observer(self, observer: Observer):
#         self.__observers.append(observer)


#     def remove_observer(self, observer: Observer):
#         self.__observers.remove(observer)



# class Observer:

#     def notify(self, object: object):
#         pass
    
#     def subscribe(self, observable: Observable):
#         observable.add_observer(self)

#     def unsubscribe(self, observable: Observable):
#         observable.remove_observer(self)
