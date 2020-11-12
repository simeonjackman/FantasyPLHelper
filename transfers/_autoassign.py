

def autoassign(locals_):
    self_ = locals_['self']
    for key in locals_.keys():
        if key != 'self':
            self_.__dict__[key] = locals_[key]
