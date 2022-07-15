parametros = input().split()
init = "self"
for parametro in parametros:
    init += ','+parametro
print(f'def __init__({init}):')
for parametro in parametros:
    print(f'    self.{parametro} = {parametro}')
print()
for parametro in parametros:
    print(f'def get{parametro.capitalize()}(self):')
    print(f'    return self.{parametro}')
    print()
    print(f'def set{parametro.capitalize()}(self,{parametro}):')
    print(f'    self.{parametro} = {parametro}')
    print()