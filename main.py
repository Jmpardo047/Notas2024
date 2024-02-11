import modulos.menu as m
import modulos.gestoralumnos as st
if __name__=='__main__':
    alumnos = {
    }
    isActive = True
    while isActive:
        n=m.CreateMenu()
        if (n == 1):
            st.AddStudent(alumnos)
        elif(n == 2):
            st.SrchStudent(alumnos)
        elif(n == 3):
            st.DelStudent(alumnos)
        elif(n == 4):
            st.addGrades(alumnos)
        elif(n == 5):
            st.Listdata(alumnos)
        elif(n == 6):
            isActive = False
            m.os.system('cls')
            print("Hasta pronto")
            m.os.system("pause")
        else: 
            pass