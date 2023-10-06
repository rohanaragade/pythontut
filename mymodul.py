import module        
                    #    rename the module using as keyword  ---->  import module as mx call using mx eg mx.list
 
module.info('rohan')
module.add(34,6)

a=module.list[2]
print(a)

b=module.dict['name']
print(b)

import platform

x=platform.system()
print(x)