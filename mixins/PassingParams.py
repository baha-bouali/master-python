# MROs have a problem with passing parameters to super() calls. 
# This is because the super() call does not know what parameters to pass to the next class in the MRO. 

from urllib3 import request


class PermissionMixin:
    def dispatch(self, *args, **kwargs):
        print("Checking permissions")
        return super().dispatch(*args, **kwargs)

class loggingMixin:
    def dispatch(self, *args, **kwargs):
        print("Logging request")
        return super().dispatch(*args, **kwargs)

class myView(PermissionMixin, loggingMixin):
    def dispatch(self, *args, **kwargs):
        print("Dispatching request")


myView().dispatch(request, project)

# The MRO is : 
# myView -> PermissionMixin -> loggingMixin -> object


# myView().dispatch(request, project) will call PermissionMixin.dispatch() first, which will print "Checking permissions"
# Then it will call loggingMixin.dispatch() next, which will print "Logging request"
# Finally, it will call myView.dispatch() last, which will print "Dispatching request"