class Persona():
    cui=0
    estadoCivil=''

    def __init__(self, cui, estadoCivil):
        self.cui=cui
        self.estadoCivil=estadoCivil

    def nacer(self,cui):
        self.cui=cui

class Registrador(Persona):
    numeEmpleado=0
    puesto='Normal'
    fechaAlta=0

    def __init__(self, cui, noEmpleado, position, fechaAlta):
        #super(cui,"soltero")
        self.cui=cui
        self.numeEmpleado=noEmpleado
        self.puesto=position
        self.fechaAlta=fechaAlta

    def registrar(self,cui):
        personaNueva=Persona(cui,"Soltero")
        return personaNueva

registrador1=Registrador("2503 45102 01011", 1 ,"Jefe","12-08-2017")
personaRegistrada=registrador1.registrar("2503 45102 0101")
print personaRegistrada.estadoCivil
print registrador1.cui
