__author__ = 'mark'


def observer(cls: type)->type:

    class Observer(cls):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__events = {}
            self.__once_events = {}

        def on(self, event_name: str, handler: callable)->None:
            try:
                self.__events[event_name].append(handler)
            except KeyError:
                self.__events[event_name] = [handler]

        def once(self, event_name: str, handler: callable)->None:
            try:
                self.__once_events[event_name].append(handler)
            except KeyError:
                self.__once_events[event_name] = [handler]

        def trigger(self, event_name: str, *args, **kwargs):
            try:
                for handler in self.__events[event_name]:
                    handler(*args, **kwargs)
            except KeyError:
                pass
            try:
                for handler in self.__once_events[event_name]:
                    handler(*args, **kwargs)
                self.__once_events[event_name].clear()
            except KeyError:
                pass

        def off(self, event_name: str, handler: callable=None):
            if not handler:
                try:
                    self.__events[event_name].clear()
                except KeyError:
                    pass
            else:
                try:
                    for key, value in enumerate(self.__events[event_name]):
                        if value == handler:
                            self.__events[event_name].pop(key)
                except KeyError:
                    pass

    return Observer


