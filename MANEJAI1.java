package Repaso;
import java.util.Scanner;
public class MANEJAI1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		I1 i=new I1("Pedro",100);
        
		
		//https://www.discoduroderoer.es/ejercicios-propuestos-y-resueltos-basicos-java/
		
		//RECOGE NOMBRE
				Scanner sc = new Scanner(System.in);
		        System.out.println("Introduzca un nombre");
				String nombre=sc.nextLine();
				i.setNombre(nombre);
				System.out.println(i.getSaludo());
				
				
				///NUMERO DIVISIBLE
				//Nos aparece un cuadro de dialogo
		        Scanner sc = new Scanner(System.in);
		        System.out.println("Introduzca un numero");
		        int numero=sc.nextInt();
		        i.setNumero(numero);
		        System.out.println(i.esDiv());
		        
		      //PUNTERO
		        Scanner sc = new Scanner(System.in);
		        System.out.println("Introduce un caracter ASCII");
		        char caracter = sc.next().charAt(0);
		        //Pasamos el caracter a codigo
		        int codigo = (int) caracter;
		        System.out.println(codigo);
		     
		        int x=1;
				while(x<101) {
					System.out.println(x);
					x=x+1;
				}
				
				//&& AND 
				// ||OR
				// ! SIGNO CONTRARIO
				int x=1;
				while(x<101) {
					if(x%2==0||x%3==0) {
						System.out.println(x);
					}
					x=x+1;
				}
		//PRIMOS
			int x=1;
			int z=1;
			for(x=1;x<101;x++){
				int y=(int) Math.sqrt(x);
				int contador=0;
				for(z=y;z>1;z--) {
					if(x%z==0) {
						contador++;
					}
				}
				
				if(contador<1) {
					System.out.println(x);
				}
			}
			
			//CONTADOR DE LETRAS
			String cadena="La lluvia en Sevilla es una pura maravilla";
			int x;
			int contador=0;
			for(x=0;x<cadena.length();x++) {
				if(cadena.charAt(x)=='a') {
					contador++;
				}
			}
			
			//REEMPLAZADOR DE LETRAS
			System.out.println(cadena.replace('a', 'e'));
		
		
        
        
        
        
        
        
        
        
        
        
	}
}
